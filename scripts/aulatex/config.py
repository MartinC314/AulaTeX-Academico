from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


LLM_ENGINES = (
    "Auto (model-router)",
    "Claude Foundry",
    "GPT-Pro",
    "Codex",
)

ENGINE_ENV_PREFIX = {
    "Auto (model-router)": "MODEL_ROUTER",
    "Claude Foundry": "ANTHROPIC_FOUNDRY",
    "GPT-Pro": "GPT_PRO",
    "Codex": "CODEX",
}

REQUIRED_LLM_SUFFIXES = ("BASE_URL", "API_KEY", "CHAT_DEPLOYMENT")


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
    return EnvLoadResult(env_path, True, loaded, skipped)


def credential_status() -> list[CredentialStatus]:
    load_aulatex_env()
    statuses: list[CredentialStatus] = []
    for engine, prefix in ENGINE_ENV_PREFIX.items():
        present: list[str] = []
        missing: list[str] = []
        for suffix in REQUIRED_LLM_SUFFIXES:
            key = f"{prefix}_{suffix}"
            if os.getenv(key, "").strip().strip('"').strip("'"):
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
