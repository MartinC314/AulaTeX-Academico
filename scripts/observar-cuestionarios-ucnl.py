"""Observa el estado contractual de los cuestionarios UCNL.

Uso: python scripts/observar-cuestionarios-ucnl.py
Corre activity-observe (via subprocess al aulatex.ps1) sobre cada objetivo y
resume el score y los checks fallidos leyendo el ultimo run del observer.
"""
from __future__ import annotations

import glob
import json
import os
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.join(REPO, "UCNL", "licenciatura-en-administracion")

TARGETS = [
    ("administracion-i-lad", "reporte-administracion-I-Actividad-1.tex", 1),
    ("contabilidad-i-lad", "reporte-contabilidad-I-Actividad-1.tex", 1),
    ("contabilidad-i-lad", "reporte-contabilidad-I-Actividad-2.tex", 2),
    ("matematicas-i-lad", "reporte-matematicas-I-Actividad-1.tex", 1),
    ("ingles-i-lad", "reporte-ingles-I-Actividad-1.tex", 1),
    ("microeconomia-lad", "reporte-microeconomia-Actividad-1.tex", 1),
]


def latest_eval(activity: int) -> dict:
    pat = os.path.join(
        REPO,
        "retroalimentacion-editorial",
        "aulatex",
        "activity-observer",
        "runs",
        f"*activity-{activity:02d}-observer",
    )
    runs = sorted(glob.glob(pat))
    if not runs:
        return {}
    with open(os.path.join(runs[-1], "evaluacion.json"), encoding="utf-8") as fh:
        return json.load(fh)


def main() -> int:
    ps = os.path.join(REPO, "scripts", "aulatex.ps1")
    for folder, filename, activity in TARGETS:
        target = os.path.join(BASE, folder, filename)
        subprocess.run(
            [
                "powershell",
                "-NoProfile",
                "-File",
                ps,
                "activity-observe",
                "--target",
                target,
                "--activity",
                str(activity),
            ],
            cwd=REPO,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        ev = latest_eval(activity)
        contract = ev.get("contract", {})
        checks = contract.get("checks", {}) or {}
        failed = [k for k, v in checks.items() if not v]
        print(
            f"{folder} A{activity}: score {contract.get('score')} "
            f"| passed {contract.get('passed')} | fallidos: {failed}"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
