from __future__ import annotations

import base64
import os
from pathlib import Path
from typing import Any

from openai import OpenAI
import requests

from .config import Settings
from .config import Settings, llm_max_output_tokens


_CONTINUATION_MARKERS = (
    "incomplete",
    "max_output_tokens",
    "length",
    "truncated",
)


def uses_openai_v1_endpoint(endpoint: str) -> bool:
    return "/openai/v1" in endpoint.rstrip("/")


def normalize_openai_v1_base_url(endpoint: str) -> str:
    endpoint = endpoint.strip().rstrip("/")
    marker = "/openai/v1"
    if marker in endpoint:
        return endpoint[: endpoint.index(marker) + len(marker)] + "/"
    return endpoint + "/openai/v1/"


def build_pdf_input_message(file_path: str | Path, prompt_text: str) -> list[dict[str, Any]]:
    path = Path(file_path)
    encoded = base64.b64encode(path.read_bytes()).decode("utf-8")
    return [
        {
            "role": "user",
            "content": [
                {
                    "type": "input_file",
                    "filename": path.name,
                    "file_data": f"data:application/pdf;base64,{encoded}",
                },
                {"type": "input_text", "text": prompt_text},
            ],
        }
    ]


def build_responses_payload(
    messages: list[dict[str, str]],
    max_tokens: int,
    temperature: float | None,
    input_override: Any | None = None,
    response_format_json: bool = False,
) -> dict[str, Any]:
    instructions = "\n\n".join(
        message["content"]
        for message in messages
        if message.get("role") == "system" and message.get("content")
    )
    input_text = "\n\n".join(
        f"{message.get('role', 'user')}: {message.get('content', '')}"
        for message in messages
        if message.get("role") != "system" and message.get("content")
    )
    payload: dict[str, Any] = {
        "input": input_override if input_override is not None else input_text,
        "max_output_tokens": max_tokens,
    }
    if instructions:
        payload["instructions"] = instructions
    if temperature is not None:
        payload["temperature"] = temperature

    reasoning_effort = os.getenv("AZURE_OPENAI_REASONING_EFFORT")
    if reasoning_effort:
        payload["reasoning"] = {"effort": reasoning_effort}

    text_config: dict[str, Any] = {}
    if response_format_json:
        text_config["format"] = {"type": "json_object"}

    text_verbosity = os.getenv("AZURE_OPENAI_TEXT_VERBOSITY")
    if text_verbosity:
        text_config["verbosity"] = text_verbosity
    if text_config:
        payload["text"] = text_config

    return payload


def _response_needs_continuation(response: Any) -> bool:
    status = str(response.get("status", "") if isinstance(response, dict) else getattr(response, "status", "")).casefold()
    if status == "incomplete":
        return True
    details = response.get("incomplete_details") if isinstance(response, dict) else getattr(response, "incomplete_details", None)
    return any(marker in str(details).casefold() for marker in _CONTINUATION_MARKERS)


def try_extract_response_text(response: Any) -> str | None:
    if isinstance(response, dict):
        try:
            content = response["choices"][0]["message"]["content"]
            if isinstance(content, str):
                return content
        except (KeyError, IndexError, TypeError):
            pass

        output_text = response.get("output_text")
        if isinstance(output_text, str) and output_text.strip():
            return output_text

        output = response.get("output")
        if isinstance(output, list):
            parts: list[str] = []
            for item in output:
                if not isinstance(item, dict):
                    continue
                content_items = item.get("content")
                if not isinstance(content_items, list):
                    continue
                for content_item in content_items:
                    if not isinstance(content_item, dict):
                        continue
                    text = content_item.get("text")
                    if isinstance(text, str) and text.strip():
                        parts.append(text)
            if parts:
                return "\n".join(parts)
        return None

    output_text = getattr(response, "output_text", None)
    if isinstance(output_text, str) and output_text.strip():
        return output_text

    parts: list[str] = []
    for item in getattr(response, "output", []) or []:
        for content_item in getattr(item, "content", []) or []:
            text = getattr(content_item, "text", None)
            if isinstance(text, str) and text.strip():
                parts.append(text)
            elif isinstance(content_item, dict):
                text = content_item.get("text")
                if isinstance(text, str) and text.strip():
                    parts.append(text)
    if parts:
        return "\n".join(parts)

    return None


def extract_response_text(response: Any) -> str:
    text = try_extract_response_text(response)
    if isinstance(text, str) and text.strip():
        return text

    raise RuntimeError(f"Respuesta inesperada de Azure OpenAI: {response}")


def format_azure_http_error(response: requests.Response) -> str:
    status = getattr(response, "status_code", "desconocido")
    error_code = ""
    error_message = ""
    try:
        body = response.json()
    except Exception:
        body = None

    if isinstance(body, dict):
        error = body.get("error")
        if isinstance(error, dict):
            error_code = str(error.get("code", "")).strip()
            error_message = str(error.get("message", "")).strip()

    details = f" ({error_code})" if error_code else ""
    if error_message:
        return f"Azure OpenAI fallo con HTTP {status}{details}: {error_message}"
    return f"Azure OpenAI fallo con HTTP {status}. Revisa endpoint, API key, deployment y version de API."


def _invoke_openai_v1_responses(
    settings: Settings,
    messages: list[dict[str, str]],
    max_tokens: int,
    temperature: float | None,
    input_override: Any | None = None,
    response_format_json: bool = False,
) -> str:
    max_tokens = llm_max_output_tokens(settings, max_tokens)
    client = OpenAI(
        api_key=settings.azure_openai_api_key,
        base_url=normalize_openai_v1_base_url(settings.azure_openai_endpoint),
    )
    payload = build_responses_payload(
        messages,
        max_tokens=max_tokens,
        temperature=temperature,
        input_override=input_override,
        response_format_json=response_format_json,
    )
    payload["model"] = settings.azure_openai_chat_deployment

    removable_fields = ["temperature", "reasoning", "text"]
    parts: list[str] = []
    continuation_round = 0
    while True:
        try:
            response = client.responses.create(**payload)
            response_text = try_extract_response_text(response)
            if response_text:
                parts.append(response_text)

            if not _response_needs_continuation(response):
                if parts:
                    return "\n\n".join(part.strip() for part in parts if part.strip())
                raise RuntimeError("Azure OpenAI devolvio una respuesta sin texto util.")

            if continuation_round >= 3:
                if parts:
                    return "\n\n".join(part.strip() for part in parts if part.strip())
                raise RuntimeError(
                    "Azure OpenAI devolvio varias respuestas incompletas sin texto util. "
                    "Reduce el esfuerzo de razonamiento o aumenta max_output_tokens."
                )

            continuation_round += 1
            if response_text:
                continuation_input: Any = (
                    "Continua exactamente desde donde se corto la respuesta anterior. "
                    "No repitas lo ya dicho y no agregues introduccion.\n\n"
                    f"Respuesta anterior parcial:\n{response_text}"
                )
            else:
                continuation_input = input_override if input_override is not None else "\n\n".join(
                    f"{message.get('role', 'user')}: {message.get('content', '')}"
                    for message in messages
                    if message.get("role") != "system" and message.get("content")
                )
            payload = build_responses_payload(
                messages,
                max_tokens=max(max_tokens, 2200) if not response_text else max_tokens,
                temperature=temperature if response_text else None,
                input_override=continuation_input,
                response_format_json=response_format_json,
            )
            payload["model"] = settings.azure_openai_chat_deployment
            if not response_text and "reasoning" not in payload:
                payload["reasoning"] = {"effort": "low"}
        except Exception as exc:
            message = str(exc).lower()
            removed = False
            for field in removable_fields:
                if field in payload and field in message:
                    payload.pop(field, None)
                    removed = True
                    break
            if removed:
                continue
            raise RuntimeError(f"Azure OpenAI fallo: {exc}") from exc


def _invoke_classic_chat_completions(
    settings: Settings,
    messages: list[dict[str, str]],
    max_tokens: int,
    temperature: float | None,
    response_format_json: bool,
) -> str:
    max_tokens = llm_max_output_tokens(settings, max_tokens)
    payload: dict[str, Any] = {
        "messages": messages,
        "max_tokens": max_tokens,
    }
    if temperature is not None:
        payload["temperature"] = temperature
    if response_format_json:
        payload["response_format"] = {"type": "json_object"}

    url = (
        f"{settings.azure_openai_endpoint}openai/deployments/"
        f"{settings.azure_openai_chat_deployment}/chat/completions"
        f"?api-version={settings.azure_openai_api_version}"
    )
    response = requests.post(
        url,
        headers={
            "Content-Type": "application/json",
            "api-key": settings.azure_openai_api_key,
        },
        json=payload,
        timeout=120,
    )
    try:
        response.raise_for_status()
    except Exception as exc:
        raise RuntimeError(format_azure_http_error(response)) from exc

    return extract_response_text(response.json())


def invoke_chat(
    settings: Settings,
    messages: list[dict[str, str]],
    max_tokens: int | None = None,
    temperature: float | None = 0.7,
    response_format_json: bool = False,
    input_override: Any | None = None,
) -> str:
    if not settings.azure_openai_endpoint or not settings.azure_openai_api_key or not settings.azure_openai_chat_deployment:
        raise RuntimeError("Falta configurar Azure OpenAI.")

    normalized_max_tokens = llm_max_output_tokens(settings, max_tokens)

    if uses_openai_v1_endpoint(settings.azure_openai_endpoint):
        return _invoke_openai_v1_responses(
            settings,
            messages,
            normalized_max_tokens,
            temperature,
            input_override,
            response_format_json,
        )

    return _invoke_classic_chat_completions(
        settings,
        messages,
        normalized_max_tokens,
        temperature,
        response_format_json,
    )
