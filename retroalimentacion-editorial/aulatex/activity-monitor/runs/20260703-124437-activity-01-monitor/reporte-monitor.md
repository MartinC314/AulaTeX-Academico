# Monitor de actividad AulaTeX

- Objetivo: UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde
- Actividad: 1
- Ciclos máximos: 2
- Estado final: PASS

## Ciclos

### Ciclo 1

- Score: 71.43
- Passed: False
- Siguiente acción: run-extractor
- Acción ejecutada: run-extractor
- Hallazgos críticos:
  - No existe salida verificable del extractor para esta actividad.
  - El ciclo aún no puede cerrarse: siguiente acción requerida `run-extractor`.
- Resultado acción: {"ok": true, "selected_motor": "tfidf", "attempts": [{"motor": "anthropicfoundry", "ok": false, "run_dir": "retroalimentacion-editorial/aulatex/extractor/runs/20260703-124438-extractor", "manifest": "retroalimentacion-editorial/aulatex/extractor/runs/20260703-124438-extractor/manifest.json", "output_dir": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/extractor-aulatex", "stdout": "retroalimentacion-editorial/aulatex/extractor/runs/20260703-124438-extractor/stdout.txt", "stderr": "retroalimentacion-editorial/aulatex/extractor/runs/20260703-124438-extractor/stderr.txt"}, {"motor": "tfidf", "ok": true, "run_dir": "retroalimentacion-editorial/aulatex/extractor/runs/20260703-124444-extractor", "manifest": "retroalimentacion-editorial/aulatex/extractor/runs/20260703-124444-extractor/manifest.json", "output_dir": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/extractor-aulatex", "stdout": "retroalimentacion-editorial/aulatex/extractor/runs/20260703-124444-extractor/stdout.txt", "stderr": "retroalimentacion-editorial/aulatex/extractor/runs/20260703-124444-extractor/stderr.txt"}]}

### Ciclo 2

- Score: 85.71
- Passed: True
- Siguiente acción: finalize
- Acción ejecutada: ninguna
