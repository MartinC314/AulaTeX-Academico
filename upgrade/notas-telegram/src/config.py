from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlsplit

from dotenv import load_dotenv

load_dotenv(override=True)
load_dotenv("notas.env", override=True)
load_dotenv("credenciales.env", override=True)


@dataclass(frozen=True)
class Settings:
    telegram_bot_token: str
    notes_dir: Path
    audio_storage_dir: Path
    bot_mode: str
    azure_speech_key: str
    azure_speech_region: str
    azure_speech_language: str
    telegram_default_chat_id: str = ""
    research_max_tokens: int = 1800
    azure_openai_context_window_tokens: int = 1_050_000
    azure_openai_max_input_tokens: int = 922_000
    azure_openai_max_output_tokens: int = 128_000
    telegram_reply_audio_enabled: bool = False
    aws_access_key_id: str = ""
    aws_secret_access_key: str = ""
    aws_region: str = "us-east-1"
    aws_polly_voice_id: str = "Andres"
    aws_polly_engine: str = "generative"
    aws_polly_language_code: str = "es-MX"
    aws_polly_sample_rate: str = "24000"
    polly_max_chars: int = 2500
    azure_openai_endpoint: str = ""
    azure_openai_api_key: str = ""
    azure_openai_chat_deployment: str = ""
    azure_openai_api_version: str = "2024-10-21"
    transcription_provider: str = "speech"
    azure_openai_realtime_endpoint: str = ""
    azure_openai_realtime_deployment_name: str = ""
    azure_openai_realtime_api_key: str = ""
    azure_openai_realtime_transcription_model: str = "gpt-4o-mini-transcribe"


def _normalize_azure_endpoint(value: str) -> str:
    raw = value.strip()
    if not raw:
        return ""

    parts = urlsplit(raw)
    if parts.scheme and parts.netloc:
        path = parts.path.rstrip("/")
        if path.endswith("/openai/v1/responses"):
            return f"{parts.scheme}://{parts.netloc}{path}"
        if path.endswith("/openai/v1/chat/completions"):
            return f"{parts.scheme}://{parts.netloc}{path[: -len('/chat/completions')]}/"
        if path.endswith("/openai/v1"):
            return f"{parts.scheme}://{parts.netloc}{path}/"
        if parts.netloc.endswith(".services.ai.azure.com"):
            return f"{parts.scheme}://{parts.netloc}/openai/v1/"
        return f"{parts.scheme}://{parts.netloc}/"

    base = raw.rstrip("/")
    for suffix in ("/openai/v1", "/openai", "/openai/"):
        if base.endswith(suffix):
            base = base[: -len(suffix)]
            break
    return base + "/"


def _validated_llm_token_limits() -> tuple[int, int, int]:
    context_window_tokens = max(1, int(os.getenv("AZURE_OPENAI_CONTEXT_WINDOW_TOKENS", "1050000")))
    max_output_tokens = max(1, int(os.getenv("AZURE_OPENAI_MAX_OUTPUT_TOKENS", "128000")))
    default_input_tokens = max(1, context_window_tokens - max_output_tokens)
    max_input_tokens = max(1, int(os.getenv("AZURE_OPENAI_MAX_INPUT_TOKENS", str(default_input_tokens))))

    if max_output_tokens >= context_window_tokens:
        max_output_tokens = context_window_tokens
        max_input_tokens = 1
    elif max_input_tokens + max_output_tokens > context_window_tokens:
        max_input_tokens = context_window_tokens - max_output_tokens

    return context_window_tokens, max_input_tokens, max_output_tokens


def llm_max_output_tokens(settings: Settings, requested: int | None = None) -> int:
    limit = max(1, settings.azure_openai_max_output_tokens)
    if requested is None:
        return limit
    return max(1, min(int(requested), limit))


def load_settings() -> Settings:
    notes_dir = os.getenv("NOTES_DIR") or os.getenv("NOTES_OUTPUT_DIR") or "data/notes"
    context_window_tokens, max_input_tokens, max_output_tokens = _validated_llm_token_limits()
    research_max_tokens = max(
        400,
        min(max_output_tokens, int(os.getenv("RESEARCH_MAX_TOKENS", str(max_output_tokens)))),
    )

    return Settings(
        telegram_bot_token=os.getenv("TELEGRAM_BOT_TOKEN", "").strip(),
        telegram_default_chat_id=os.getenv("TELEGRAM_DEFAULT_CHAT_ID", "").strip(),
        notes_dir=Path(notes_dir).resolve(),
        audio_storage_dir=Path(os.getenv("AUDIO_STORAGE_DIR", "data/audio")).resolve(),
        bot_mode=os.getenv("BOT_MODE", "polling").strip().lower() or "polling",
        azure_speech_key=os.getenv("AZURE_SPEECH_KEY", "").strip(),
        azure_speech_region=os.getenv("AZURE_SPEECH_REGION", "").strip(),
        azure_speech_language=os.getenv("AZURE_SPEECH_LANGUAGE", "es-MX").strip() or "es-MX",
        research_max_tokens=research_max_tokens,
        azure_openai_context_window_tokens=context_window_tokens,
        azure_openai_max_input_tokens=max_input_tokens,
        azure_openai_max_output_tokens=max_output_tokens,
        telegram_reply_audio_enabled=os.getenv("TELEGRAM_REPLY_AUDIO_ENABLED", "").strip().lower() in {"1", "true", "yes", "on"},
        aws_access_key_id=(
            os.getenv("AWS_ACCESS_KEY_ID")
            or os.getenv("POLLY_AWS_ACCESS_KEY_ID")
            or ""
        ).strip(),
        aws_secret_access_key=(
            os.getenv("AWS_SECRET_ACCESS_KEY")
            or os.getenv("POLLY_AWS_SECRET_ACCESS_KEY")
            or ""
        ).strip(),
        aws_region=(
            os.getenv("AWS_REGION")
            or os.getenv("POLLY_AWS_REGION")
            or "us-east-1"
        ).strip() or "us-east-1",
        aws_polly_voice_id=os.getenv("POLLY_VOICE_ID", "Andres").strip() or "Andres",
        aws_polly_engine=os.getenv("POLLY_ENGINE", "generative").strip() or "generative",
        aws_polly_language_code=os.getenv("POLLY_LANGUAGE_CODE", "es-MX").strip() or "es-MX",
        aws_polly_sample_rate=os.getenv("POLLY_SAMPLE_RATE", "24000").strip() or "24000",
        polly_max_chars=max(300, int(os.getenv("POLLY_MAX_CHARS", os.getenv("MAX_CHARS", "2500")))),
        azure_openai_endpoint=_normalize_azure_endpoint(os.getenv("AZURE_OPENAI_ENDPOINT", "")),
        azure_openai_api_key=os.getenv("AZURE_OPENAI_API_KEY", "").strip(),
        azure_openai_chat_deployment=(
            os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT")
            or os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
            or ""
        ).strip(),
        azure_openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-10-21").strip() or "2024-10-21",
        transcription_provider=os.getenv("TRANSCRIPTION_PROVIDER", "speech").strip().lower() or "speech",
        azure_openai_realtime_endpoint=_normalize_azure_endpoint(os.getenv("AZURE_OPENAI_REALTIME_ENDPOINT", "")),
        azure_openai_realtime_deployment_name=os.getenv("AZURE_OPENAI_REALTIME_DEPLOYMENT_NAME", "").strip(),
        azure_openai_realtime_api_key=(
            os.getenv("AZURE_OPENAI_REALTIME_API_KEY")
            or os.getenv("AZURE_OPENAI_API_KEY")
            or ""
        ).strip(),
        azure_openai_realtime_transcription_model=os.getenv(
            "AZURE_OPENAI_REALTIME_TRANSCRIPTION_MODEL",
            "gpt-4o-mini-transcribe",
        ).strip() or "gpt-4o-mini-transcribe",
    )


def validate_settings(settings: Settings) -> list[str]:
    missing: list[str] = []
    if not settings.telegram_bot_token:
        missing.append("TELEGRAM_BOT_TOKEN")

    provider = settings.transcription_provider
    if provider not in {"speech", "realtime", "auto"}:
        missing.append("TRANSCRIPTION_PROVIDER debe ser speech, realtime o auto")

    if provider in {"speech", "auto"}:
        if not settings.azure_speech_key:
            missing.append("AZURE_SPEECH_KEY")
        if not settings.azure_speech_region:
            missing.append("AZURE_SPEECH_REGION")

    if provider in {"realtime", "auto"}:
        if not settings.azure_openai_realtime_endpoint:
            missing.append("AZURE_OPENAI_REALTIME_ENDPOINT")
        if not settings.azure_openai_realtime_deployment_name:
            missing.append("AZURE_OPENAI_REALTIME_DEPLOYMENT_NAME")
        if not settings.azure_openai_realtime_api_key:
            missing.append("AZURE_OPENAI_REALTIME_API_KEY")

    if not settings.azure_openai_endpoint:
        missing.append("AZURE_OPENAI_ENDPOINT")
    if not settings.azure_openai_api_key:
        missing.append("AZURE_OPENAI_API_KEY")
    if not settings.azure_openai_chat_deployment:
        missing.append("AZURE_OPENAI_CHAT_DEPLOYMENT")
    return missing
