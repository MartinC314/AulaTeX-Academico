"""Cifrado local y autónomo de secretos para AulaTeX-Académico.

Gestiona sus propias credenciales de forma INDEPENDIENTE de otros repos, con
una clave Fernet propia (``secret.key``) junto al ``.env`` correspondiente.
La aplicación accede a sus claves por sí misma sin depender de otro proyecto.

Comandos:
    python secrets_local.py init-key                 # genera secret.key local
    python secrets_local.py encrypt aulatex.env      # cifra los secretos del .env
    python secrets_local.py decrypt-env aulatex.env  # imprime NAME<TAB>plano (PowerShell)
    python secrets_local.py hydrate aulatex.env      # descifra en os.environ (Python)

Resolución de la clave:
    1. Variable de entorno ``AULATEX_SECRET_KEY`` (clave Fernet directa).
    2. Archivo ``secret.key`` junto a este script.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

from cryptography.fernet import Fernet, InvalidToken

HERE = Path(__file__).resolve().parent
SECRET_KEY_PATH = HERE / "secret.key"
ENC_PREFIX = "enc:"

# Claves que se consideran secretas (se cifran). El resto queda en claro.
_SECRET_HINTS = ("API_KEY", "TOKEN", "SECRET", "PASSWORD", "_KEY", "ACCESS_KEY_ID")

# Nombres que contienen una pista de secreto pero NO lo son (limites, flags...).
_SECRET_EXCLUDES = ("MAX_TOKENS", "TOKENS_LIMIT", "TOKEN_LIMIT", "KEY_VAULT_NAME")


def _is_secret_name(name: str) -> bool:
    up = name.upper()
    if any(x in up for x in _SECRET_EXCLUDES):
        return False
    return any(h in up for h in _SECRET_HINTS)


def resolve_fernet(create: bool = False) -> Fernet | None:
    env_key = os.getenv("AULATEX_SECRET_KEY", "").strip()
    if env_key:
        return Fernet(env_key.encode("utf-8"))
    if SECRET_KEY_PATH.exists():
        return Fernet(SECRET_KEY_PATH.read_bytes().strip())
    if create:
        key = Fernet.generate_key()
        SECRET_KEY_PATH.write_bytes(key)
        try:
            os.chmod(SECRET_KEY_PATH, 0o600)
        except OSError:
            pass
        return Fernet(key)
    return None


def _parse_line(line: str):
    stripped = line.strip()
    if not stripped or stripped.startswith("#") or "=" not in stripped:
        return None, None
    name, _, value = stripped.partition("=")
    name = name.strip()
    value = value.strip()
    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
        value = value[1:-1]
    return name, value


def cmd_init_key() -> int:
    if SECRET_KEY_PATH.exists():
        print(f"Ya existe: {SECRET_KEY_PATH}")
        return 0
    resolve_fernet(create=True)
    print(f"Clave local generada: {SECRET_KEY_PATH}")
    print("IMPORTANTE: añade 'secret.key' a .gitignore; NO la subas al repo.")
    return 0


def cmd_encrypt(env_file: str) -> int:
    path = HERE / env_file if not Path(env_file).is_absolute() else Path(env_file)
    if not path.exists():
        print(f"No existe: {path}")
        return 1
    f = resolve_fernet(create=True)
    if f is None:
        print("No hay clave disponible.")
        return 1

    out_lines: list[str] = []
    cifrados = 0
    for line in path.read_text(encoding="utf-8").splitlines():
        name, value = _parse_line(line)
        if name and value and _is_secret_name(name) and not value.startswith(ENC_PREFIX):
            token = f.encrypt(value.encode("utf-8")).decode("ascii")
            out_lines.append(f"{name}={ENC_PREFIX}{token}")
            cifrados += 1
        else:
            out_lines.append(line)
    path.write_text("\n".join(out_lines) + "\n", encoding="utf-8")
    print(f"Cifrados {cifrados} secretos en {path.name}")
    return 0


def cmd_decrypt_env(env_file: str) -> int:
    path = HERE / env_file if not Path(env_file).is_absolute() else Path(env_file)
    f = resolve_fernet(create=False)
    if f is None or not path.exists():
        return 0
    for line in path.read_text(encoding="utf-8").splitlines():
        name, value = _parse_line(line)
        if name and value and value.startswith(ENC_PREFIX):
            try:
                plain = f.decrypt(value[len(ENC_PREFIX):].encode("ascii")).decode("utf-8")
            except InvalidToken:
                continue
            sys.stdout.write(f"{name}\t{plain}\n")
    return 0


def hydrate(env_file: str) -> None:
    """Descifra los valores enc: del .env directamente en os.environ."""
    path = HERE / env_file if not Path(env_file).is_absolute() else Path(env_file)
    f = resolve_fernet(create=False)
    if f is None or not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        name, value = _parse_line(line)
        if not name:
            continue
        if value.startswith(ENC_PREFIX):
            try:
                value = f.decrypt(value[len(ENC_PREFIX):].encode("ascii")).decode("utf-8")
            except InvalidToken:
                continue
        os.environ[name] = value


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    cmd = sys.argv[1]
    if cmd == "init-key":
        return cmd_init_key()
    if cmd == "encrypt" and len(sys.argv) >= 3:
        return cmd_encrypt(sys.argv[2])
    if cmd == "decrypt-env" and len(sys.argv) >= 3:
        return cmd_decrypt_env(sys.argv[2])
    if cmd == "hydrate" and len(sys.argv) >= 3:
        hydrate(sys.argv[2])
        return 0
    print(f"Comando no reconocido: {cmd}")
    print(__doc__)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
