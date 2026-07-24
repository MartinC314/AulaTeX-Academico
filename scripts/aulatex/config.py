from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path


LLM_ENGINES = (
    "Auto (model-router)",
    "Claude Foundry",
    "Claude Sonnet",
    "Claude Haiku",
    "GPT-5.6-SOL",
    "GPT-5.6-Luna",
    "GPT-5.6-Terra",
    "GPT-Pro",
    "Codex",
    "Mistral-Large-3",
    "DeepSeek-V4-Pro",
    "GPT-Chat-Latest",
)

ENGINE_ENV_PREFIX = {
    "Auto (model-router)": "MODEL_ROUTER",
    "Claude Foundry": "ANTHROPIC_FOUNDRY",
    "GPT-5.6-SOL": "AZURE_OPENAI_GPT_5_6_SOL",
    "GPT-5.6-Luna": "AZURE_OPENAI_GPT_5_6_LUNA",
    "GPT-5.6-Terra": "AZURE_OPENAI_GPT_5_6_TERRA",
    "GPT-Pro": "GPT_PRO",
    "Codex": "CODEX",
    # LLMs adicionales presentes en aulatex.env (protocolo chat/completions).
    "Mistral-Large-3": "MISTRAL_LARGE_3",
    "DeepSeek-V4-Pro": "DEEPSEEK_V4_PRO",
    "GPT-Chat-Latest": "GPT_CHAT_LATEST",
    # Anthropic Sonnet/Haiku (mismo endpoint que Claude Foundry, otro deployment).
    "Claude Sonnet": "ANTHROPIC_SONNET",
    "Claude Haiku": "ANTHROPIC_HAIKU",
}

REQUIRED_LLM_SUFFIXES = ("BASE_URL", "API_KEY", "CHAT_DEPLOYMENT")
_TRUE_VALUES = {"1", "true", "yes", "on", "si", "sí"}


@dataclass(frozen=True)
class EnvLoadResult:
    path: Path
    exists: bool
    loaded: int
    skipped: int


@dataclass(frozen=True)
class CredentialStatus:
    engine: str
    prefix: str
    ok: bool
    present: tuple[str, ...]
    missing: tuple[str, ...]


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def default_env_path() -> Path:
    return repo_root() / "scripts" / "aulatex.env"


def _strip_env_value(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def load_aulatex_env(path: str | Path | None = None, *, override: bool = True) -> EnvLoadResult:
    env_path = Path(path or os.getenv("AULATEX_ENV_PATH") or default_env_path()).expanduser().resolve()
    if not env_path.exists():
        return EnvLoadResult(env_path, False, 0, 0)

    loaded = 0
    skipped = 0
    for raw_line in env_path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        if line.lower().startswith("export "):
            line = line[7:].strip()
        name, value = line.split("=", 1)
        name = name.strip()
        if not name:
            skipped += 1
            continue
        if not override and name in os.environ:
            skipped += 1
            continue
        os.environ[name] = _strip_env_value(value)
        loaded += 1
    # Descifrado autónomo de los valores enc: con la clave local del proyecto.
    _decrypt_local_secrets()
    return EnvLoadResult(env_path, True, loaded, skipped)


def _decrypt_local_secrets() -> None:
    """Descifra en os.environ los valores con prefijo ``enc:`` usando la clave
    local del proyecto (scripts/secret.key). Silencioso si no hay clave/módulo."""
    if not any(str(v).startswith("enc:") for v in os.environ.values()):
        return
    try:
        import importlib.util

        module_path = repo_root() / "scripts" / "secrets_local.py"
        if not module_path.exists():
            return
        spec = importlib.util.spec_from_file_location("aulatex_secrets_local", module_path)
        if spec is None or spec.loader is None:
            return
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        fernet = mod.resolve_fernet(create=False)
        if fernet is None:
            return
        from cryptography.fernet import InvalidToken

        for key, value in list(os.environ.items()):
            if isinstance(value, str) and value.startswith("enc:"):
                try:
                    os.environ[key] = fernet.decrypt(value[4:].encode("ascii")).decode("utf-8")
                except InvalidToken:
                    pass
    except Exception:
        # El descifrado es best-effort; si falla, se dejan los valores tal cual.
        pass


def credential_status() -> list[CredentialStatus]:
    load_aulatex_env()
    statuses: list[CredentialStatus] = []
    for engine, prefix in ENGINE_ENV_PREFIX.items():
        present: list[str] = []
        missing: list[str] = []
        # Sonnet/Haiku comparten endpoint/clave con Claude Foundry: solo aportan
        # su *_DEPLOYMENT y heredan BASE_URL/API_KEY de ANTHROPIC_FOUNDRY.
        inherits_anthropic = prefix in ("ANTHROPIC_SONNET", "ANTHROPIC_HAIKU")
        for suffix in REQUIRED_LLM_SUFFIXES:
            key = f"{prefix}_{suffix}"
            value = os.getenv(key, "").strip().strip('"').strip("'")
            if not value and inherits_anthropic and suffix in ("BASE_URL", "API_KEY"):
                value = os.getenv(f"ANTHROPIC_FOUNDRY_{suffix}", "").strip().strip('"').strip("'")
            if not value and inherits_anthropic and suffix == "CHAT_DEPLOYMENT":
                value = os.getenv(f"{prefix}_DEPLOYMENT", "").strip().strip('"').strip("'")
            if value:
                present.append(key)
            else:
                missing.append(key)
        statuses.append(
            CredentialStatus(
                engine=engine,
                prefix=prefix,
                ok=not missing,
                present=tuple(present),
                missing=tuple(missing),
            )
        )
    return statuses


def diagnostic_metrics_enabled() -> bool:
    load_aulatex_env(override=False)
    value = os.getenv("AULATEX_ENABLE_DIAGNOSTIC_METRICS", "").strip().lower()
    return value in _TRUE_VALUES


# ---------------------------------------------------------------------------
# Catálogo de credenciales para la interfaz de configuración embebida.
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class CredentialField:
    """Descripción de una clave individual del archivo .env."""

    key: str
    label: str
    secret: bool = False
    required: bool = True
    placeholder: str = ""
    help: str = ""


@dataclass(frozen=True)
class CredentialGroup:
    """Agrupación lógica de claves relacionadas (un motor o servicio)."""

    group_id: str
    title: str
    description: str = ""
    fields: tuple[CredentialField, ...] = field(default_factory=tuple)


def _llm_group(group_id: str, title: str, prefix: str, *, description: str = "") -> CredentialGroup:
    return CredentialGroup(
        group_id=group_id,
        title=title,
        description=description,
        fields=(
            CredentialField(f"{prefix}_BASE_URL", "Base URL", secret=False, help="Endpoint del despliegue."),
            CredentialField(f"{prefix}_API_KEY", "API Key", secret=True, help="Clave secreta de acceso."),
            CredentialField(f"{prefix}_CHAT_DEPLOYMENT", "Deployment", secret=False, help="Nombre del despliegue de chat."),
        ),
    )


CREDENTIAL_GROUPS: tuple[CredentialGroup, ...] = (
    _llm_group("model_router", "Auto (model-router)", "MODEL_ROUTER", description="Enrutador automático de modelos."),
    CredentialGroup(
        group_id="claude_foundry",
        title="Claude Foundry",
        description="Anthropic Messages API en Foundry.",
        fields=(
            CredentialField("ANTHROPIC_FOUNDRY_BASE_URL", "Base URL", help="Endpoint de mensajes de Anthropic."),
            CredentialField("ANTHROPIC_FOUNDRY_API_KEY", "API Key", secret=True),
            CredentialField("ANTHROPIC_FOUNDRY_CHAT_DEPLOYMENT", "Deployment"),
            CredentialField("ANTHROPIC_FOUNDRY_API_VERSION", "API Version", required=False),
        ),
    ),
    _llm_group("gpt_5_6_sol", "GPT-5.6-SOL", "AZURE_OPENAI_GPT_5_6_SOL"),
    _llm_group("gpt_5_6_luna", "GPT-5.6-Luna", "AZURE_OPENAI_GPT_5_6_LUNA"),
    _llm_group("gpt_5_6_terra", "GPT-5.6-Terra", "AZURE_OPENAI_GPT_5_6_TERRA"),
    _llm_group("gpt_pro", "GPT-Pro", "GPT_PRO"),
    _llm_group("codex", "Codex", "CODEX"),
    CredentialGroup(
        group_id="azure_speech",
        title="Azure Speech",
        description="Síntesis de voz para audio (M4A).",
        fields=(
            CredentialField("AZURE_SPEECH_KEY", "Speech Key", secret=True),
            CredentialField("AZURE_SPEECH_REGION", "Región", required=False, placeholder="eastus"),
            CredentialField("AZURE_SPEECH_LANGUAGE", "Idioma", required=False, placeholder="es-MX"),
            CredentialField("AZURE_SPEECH_VOICE", "Voz", required=False, placeholder="es-MX-JorgeNeural"),
        ),
    ),
    CredentialGroup(
        group_id="azure_translator",
        title="Azure Translator",
        description="Traducción de libros y textos.",
        fields=(
            CredentialField("AZURE_TRANSLATOR_KEY", "Translator Key", secret=True),
            CredentialField("AZURE_TRANSLATOR_REGION", "Región", required=False, placeholder="eastus"),
            CredentialField("AZURE_TRANSLATOR_ENDPOINT", "Endpoint", required=False),
        ),
    ),
    CredentialGroup(
        group_id="amazon_polly",
        title="Amazon Polly / AWS",
        description="Síntesis de voz generativa y almacenamiento.",
        fields=(
            CredentialField("AWS_ACCESS_KEY_ID", "Access Key ID", secret=True),
            CredentialField("AWS_SECRET_ACCESS_KEY", "Secret Access Key", secret=True),
            CredentialField("AWS_REGION", "Región", required=False, placeholder="us-east-1"),
            CredentialField("POLLY_VOICE_ID", "Voz Polly", required=False, placeholder="Andres"),
        ),
    ),
    CredentialGroup(
        group_id="azure_sora",
        title="Azure Sora / Video",
        description="Generación de video y audio TTS.",
        fields=(
            CredentialField("AZURE_ENDPOINT", "Endpoint", required=False),
            CredentialField("AZURE_API_KEY", "API Key", secret=True, required=False),
            CredentialField("AZURE_OPENAI_DEPLOYMENT_NAME", "Deployment", required=False, placeholder="sora-2"),
        ),
    ),
)


def credential_catalog() -> tuple[CredentialGroup, ...]:
    """Devuelve el catálogo de grupos de credenciales para la interfaz."""

    return CREDENTIAL_GROUPS


def read_env_values(keys: "list[str] | tuple[str, ...]", path: str | Path | None = None) -> dict[str, str]:
    """Lee valores actuales del archivo .env sin tocar os.environ."""

    env_path = Path(path or os.getenv("AULATEX_ENV_PATH") or default_env_path()).expanduser()
    result: dict[str, str] = {key: "" for key in keys}
    if not env_path.exists():
        return result
    wanted = set(keys)
    for raw_line in env_path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        if line.lower().startswith("export "):
            line = line[7:].strip()
        name, value = line.split("=", 1)
        name = name.strip()
        if name in wanted:
            result[name] = _strip_env_value(value)
    return result


def write_env_values(
    values: dict[str, str],
    path: str | Path | None = None,
    *,
    reload: bool = True,
) -> Path:
    """Actualiza o inserta claves en el archivo .env preservando comentarios y orden.

    - Sólo se escriben claves con valor no vacío tras strip; las claves con valor
      vacío se dejan intactas (no se borran del archivo).
    - Los valores que contienen espacios o caracteres especiales se entrecomillan.
    - Las claves nuevas se agregan al final bajo una sección gestionada.
    """

    env_path = Path(path or os.getenv("AULATEX_ENV_PATH") or default_env_path()).expanduser().resolve()
    env_path.parent.mkdir(parents=True, exist_ok=True)

    to_write = {name: value for name, value in values.items() if value is not None and str(value).strip() != ""}
    if not to_write:
        return env_path

    lines: list[str] = []
    if env_path.exists():
        lines = env_path.read_text(encoding="utf-8", errors="replace").splitlines()

    remaining = dict(to_write)
    updated_lines: list[str] = []
    for raw_line in lines:
        stripped = raw_line.strip()
        matched_name = None
        if stripped and not stripped.startswith("#") and "=" in stripped:
            candidate = stripped[7:].strip() if stripped.lower().startswith("export ") else stripped
            name = candidate.split("=", 1)[0].strip()
            if name in remaining:
                matched_name = name
        if matched_name is not None:
            updated_lines.append(f"{matched_name}={_quote_env_value(remaining.pop(matched_name))}")
        else:
            updated_lines.append(raw_line)

    if remaining:
        if updated_lines and updated_lines[-1].strip():
            updated_lines.append("")
        updated_lines.append("# --- Claves agregadas desde la interfaz de credenciales ---")
        for name, value in remaining.items():
            updated_lines.append(f"{name}={_quote_env_value(value)}")

    env_path.write_text("\n".join(updated_lines) + "\n", encoding="utf-8")

    if reload:
        load_aulatex_env(env_path)
    return env_path


def _quote_env_value(value: str) -> str:
    value = str(value)
    if value == "":
        return value
    needs_quotes = any(ch.isspace() for ch in value) or value[0] in {'"', "'"}
    if needs_quotes:
        escaped = value.replace('"', '\\"')
        return f'"{escaped}"'
    return value
