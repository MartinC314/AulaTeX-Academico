# Bitacora AulaTeX

## 20260618-104500 - evaluar

```json
{
  "run_id": "20260618-104500",
  "target": "UnADM/licenciatura-en-derecho-unadm/historia-del-derecho-en-mexico-lde",
  "level": "materia",
  "action": "evaluar",
  "activity_number": 1,
  "engines": [
    "Codex"
  ],
  "llm_results": [
    {
      "engine": "Codex",
      "ok": true,
      "error": "",
      "chars": 4804
    }
  ],
  "compile_results": []
}
```

## 20260618-105534 - evaluar

```json
{
  "run_id": "20260618-105534",
  "target": "UnADM/licenciatura-en-derecho-unadm/historia-del-derecho-en-mexico-lde",
  "level": "materia",
  "action": "evaluar",
  "activity_number": 1,
  "engines": [
    "Codex"
  ],
  "llm_results": [
    {
      "engine": "Codex",
      "ok": true,
      "error": "",
      "chars": 4881
    }
  ],
  "compile_results": []
}
```

## 20260618-110215 - evaluar

```json
{
  "run_id": "20260618-110215",
  "target": "UnADM/licenciatura-en-derecho-unadm/historia-del-derecho-en-mexico-lde",
  "level": "materia",
  "action": "evaluar",
  "activity_number": 1,
  "engines": [
    "Codex"
  ],
  "agentic_patterns": [
    "planning-memory",
    "tool-using-workflow",
    "verification-validation",
    "collective-consensus"
  ],
  "tasks": [
    {
      "stage": "planificar",
      "role": "Planificador editorial",
      "mission": "descomponer el objetivo en plan ejecutable y criterios de aceptacion",
      "engine": "Codex"
    },
    {
      "stage": "investigar",
      "role": "Investigador documental",
      "mission": "detectar fuentes, contexto curricular y faltantes editoriales",
      "engine": "Codex"
    },
    {
      "stage": "generar",
      "role": "Arquitecto de plantillas",
      "mission": "proponer estructura de reporte/presentacion y actividad",
      "engine": "Codex"
    },
    {
      "stage": "validar",
      "role": "Verificador y validador",
      "mission": "verificar consistencia, compilacion y evidencias",
      "engine": "Codex"
    },
    {
      "stage": "criticar",
      "role": "Critico adversarial",
      "mission": "encontrar fallas antes de aplicar cambios",
      "engine": "Codex"
    }
  ],
  "llm_results": [
    {
      "engine": "Codex",
      "ok": true,
      "error": "",
      "chars": 3978
    },
    {
      "engine": "Codex",
      "ok": true,
      "error": "",
      "chars": 4877
    },
    {
      "engine": "Codex",
      "ok": true,
      "error": "",
      "chars": 4395
    },
    {
      "engine": "Codex",
      "ok": true,
      "error": "",
      "chars": 5261
    },
    {
      "engine": "Codex",
      "ok": true,
      "error": "",
      "chars": 4780
    }
  ],
  "compile_results": [],
  "consensus": {
    "consensus_score": 9.55,
    "passed": true,
    "criteria": {
      "identidad_institucional": true,
      "bibliografia": true,
      "trazabilidad": true,
      "compilacion": true,
      "riesgos": true
    },
    "role_scores": {
      "Planificador editorial": 8.6,
      "Investigador documental": 9.87,
      "Arquitecto de plantillas": 9.4,
      "Verificador y validador": 9.46,
      "Critico adversarial": 8.58
    },
    "risks": [],
    "recommendations": [
      "Usar el reporte como retroalimentacion editorial aplicable al objetivo."
    ]
  },
  "workflow_events": [
    {
      "timestamp": "2026-06-18 11:02:15",
      "state": "initialized",
      "action": "init",
      "status": "ok",
      "detail": "AulaTeX workflow initialized"
    },
    {
      "timestamp": "2026-06-18 11:02:15",
      "state": "initialized",
      "action": "llm-start",
      "status": "ok",
      "detail": "planificar: Planificador editorial via Codex"
    },
    {
      "timestamp": "2026-06-18 11:02:30",
      "state": "initialized",
      "action": "llm-end",
      "status": "ok",
      "detail": "planificar: 3978 chars"
    },
    {
      "timestamp": "2026-06-18 11:02:30",
      "state": "planned",
      "action": "initialized->planned",
      "status": "ok",
      "detail": "plan editorial producido"
    },
    {
      "timestamp": "2026-06-18 11:02:30",
      "state": "planned",
      "action": "llm-start",
      "status": "ok",
      "detail": "investigar: Investigador documental via Codex"
    },
    {
      "timestamp": "2026-06-18 11:02:43",
      "state": "planned",
      "action": "llm-end",
      "status": "ok",
      "detail": "investigar: 4877 chars"
    },
    {
      "timestamp": "2026-06-18 11:02:43",
      "state": "researched",
      "action": "planned->researched",
      "status": "ok",
      "detail": "diagnostico documental producido"
    },
    {
      "timestamp": "2026-06-18 11:02:43",
      "state": "researched",
      "action": "llm-start",
      "status": "ok",
      "detail": "generar: Arquitecto de plantillas via Codex"
    },
    {
      "timestamp": "2026-06-18 11:02:59",
      "state": "researched",
      "action": "llm-end",
      "status": "ok",
      "detail": "generar: 4395 chars"
    },
    {
      "timestamp": "2026-06-18 11:02:59",
      "state": "generated",
      "action": "researched->generated",
      "status": "ok",
      "detail": "propuesta editorial producida"
    },
    {
      "timestamp": "2026-06-18 11:02:59",
      "state": "generated",
      "action": "llm-start",
      "status": "ok",
      "detail": "validar: Verificador y validador via Codex"
    },
    {
      "timestamp": "2026-06-18 11:03:16",
      "state": "generated",
      "action": "llm-end",
      "status": "ok",
      "detail": "validar: 5261 chars"
    },
    {
      "timestamp": "2026-06-18 11:03:16",
      "state": "generated",
      "action": "llm-start",
      "status": "ok",
      "detail": "criticar: Critico adversarial via Codex"
    },
    {
      "timestamp": "2026-06-18 11:03:32",
      "state": "generated",
      "action": "llm-end",
      "status": "ok",
      "detail": "criticar: 4780 chars"
    },
    {
      "timestamp": "2026-06-18 11:03:32",
      "state": "generated",
      "action": "consensus",
      "status": "ok",
      "detail": "score=9.55"
    },
    {
      "timestamp": "2026-06-18 11:03:32",
      "state": "evaluated",
      "action": "generated->evaluated",
      "status": "ok",
      "detail": "validacion y consenso completados"
    },
    {
      "timestamp": "2026-06-18 11:03:32",
      "state": "finalized",
      "action": "evaluated->finalized",
      "status": "ok",
      "detail": "ciclo agentico cerrado"
    }
  ]
}
```

## 20260618-115618 - evaluar

```json
{
  "run_id": "20260618-115618",
  "target": "UnADM/licenciatura-en-derecho-unadm/historia-del-derecho-en-mexico-lde",
  "level": "materia",
  "action": "evaluar",
  "activity_number": 1,
  "engines": [
    "Codex",
    "Claude Foundry",
    "GPT-Pro",
    "Auto (model-router)"
  ],
  "agentic_patterns": [
    "planning-memory",
    "tool-using-workflow",
    "verification-validation",
    "collective-consensus"
  ],
  "tasks": [
    {
      "stage": "planificar",
      "role": "Planificador editorial",
      "mission": "descomponer el objetivo en plan ejecutable y criterios de aceptacion",
      "engine": "Codex"
    }
  ],
  "llm_results": [
    {
      "engine": "Codex",
      "ok": true,
      "error": "",
      "chars": 4477
    }
  ],
  "compile_results": [],
  "consensus": {
    "consensus_score": 9.23,
    "passed": true,
    "criteria": {
      "identidad_institucional": true,
      "bibliografia": true,
      "trazabilidad": true,
      "compilacion": true,
      "riesgos": true
    },
    "role_scores": {
      "Planificador editorial": 8.6
    },
    "risks": [],
    "recommendations": [
      "Usar el reporte como retroalimentacion editorial aplicable al objetivo."
    ]
  },
  "workflow_events": [
    {
      "timestamp": "2026-06-18 11:56:18",
      "state": "initialized",
      "action": "init",
      "status": "ok",
      "detail": "AulaTeX workflow initialized"
    },
    {
      "timestamp": "2026-06-18 11:56:18",
      "state": "initialized",
      "action": "llm-start",
      "status": "ok",
      "detail": "planificar: Planificador editorial via Codex"
    },
    {
      "timestamp": "2026-06-18 11:56:31",
      "state": "initialized",
      "action": "llm-end",
      "status": "ok",
      "detail": "planificar: 4477 chars"
    },
    {
      "timestamp": "2026-06-18 11:56:31",
      "state": "planned",
      "action": "initialized->planned",
      "status": "ok",
      "detail": "plan editorial producido"
    },
    {
      "timestamp": "2026-06-18 11:56:31",
      "state": "planned",
      "action": "consensus",
      "status": "ok",
      "detail": "score=9.23"
    },
    {
      "timestamp": "2026-06-18 11:56:31",
      "state": "evaluated",
      "action": "planned->evaluated",
      "status": "ok",
      "detail": "validacion y consenso completados"
    },
    {
      "timestamp": "2026-06-18 11:56:31",
      "state": "finalized",
      "action": "evaluated->finalized",
      "status": "ok",
      "detail": "ciclo agentico cerrado"
    }
  ]
}
```

## 20260618-115516 - generar-actividad

```json
{
  "run_id": "20260618-115516",
  "target": "UnADM/licenciatura-en-derecho-unadm/historia-del-derecho-en-mexico-lde",
  "level": "materia",
  "action": "generar-actividad",
  "activity_number": 1,
  "engines": [
    "Codex",
    "Claude Foundry",
    "GPT-Pro",
    "Auto (model-router)"
  ],
  "agentic_patterns": [
    "planning-memory",
    "tool-using-workflow",
    "verification-validation",
    "collective-consensus"
  ],
  "tasks": [
    {
      "stage": "planificar",
      "role": "Planificador editorial",
      "mission": "descomponer el objetivo en plan ejecutable y criterios de aceptacion",
      "engine": "Codex"
    },
    {
      "stage": "investigar",
      "role": "Investigador documental",
      "mission": "detectar fuentes, contexto curricular y faltantes editoriales",
      "engine": "Claude Foundry"
    },
    {
      "stage": "generar",
      "role": "Arquitecto de plantillas",
      "mission": "proponer estructura de reporte/presentacion y actividad",
      "engine": "GPT-Pro"
    },
    {
      "stage": "validar",
      "role": "Verificador y validador",
      "mission": "verificar consistencia, compilacion y evidencias",
      "engine": "Auto (model-router)"
    },
    {
      "stage": "criticar",
      "role": "Critico adversarial",
      "mission": "encontrar fallas antes de aplicar cambios",
      "engine": "Codex"
    }
  ],
  "llm_results": [
    {
      "engine": "Codex",
      "ok": true,
      "error": "",
      "chars": 4935
    },
    {
      "engine": "Claude Foundry",
      "ok": true,
      "error": "",
      "chars": 3570
    },
    {
      "engine": "GPT-Pro",
      "ok": true,
      "error": "",
      "chars": 0
    },
    {
      "engine": "Auto (model-router)",
      "ok": true,
      "error": "",
      "chars": 0
    },
    {
      "engine": "Codex",
      "ok": true,
      "error": "",
      "chars": 3672
    }
  ],
  "compile_results": [
    {
      "tex": "UnADM/licenciatura-en-derecho-unadm/historia-del-derecho-en-mexico-lde/reporte-historia-del-derecho-en-mexico.tex",
      "ok": false,
      "returncode": 1,
      "stdout_tail": "Informe/UCNL//;D:/Documentos/LaTEX/Template-Informe/UANL//;D:/Documentos/LaTEX/Template-Informe/IIIEPE//;D:/Documentos/LaTEX/Template-Informe/ITESCA//'\nLatexmk: Change directory to '.build/latex/aux/'.\nTo assist finding of files in document directory, I set\n  BIBINPUTS='D:/Documentos/LaTEX/Template-Informe;.build/latex/aux;D:\\Documentos\\LaTEX\\Template-Informe\\.build\\latex\\aux;D:/Documentos/LaTEX/Template-Informe;D:/Documentos/LaTEX/Template-Informe/base/Plantilla-Informe//;D:/Documentos/LaTEX/Template-Informe/UnADM//;D:/Documentos/LaTEX/Template-Informe/UCNL//;D:/Documentos/LaTEX/Template-Informe/UANL//;D:/Documentos/LaTEX/Template-Informe/IIIEPE//;D:/Documentos/LaTEX/Template-Informe/ITESCA//'\n  BSTINPUTS='D:/Documentos/LaTEX/Template-Informe;D:/Documentos/LaTEX/Template-Informe;D:/Documentos/LaTEX/Template-Informe/base/Plantilla-Informe/bibtex//;D:/Documentos/LaTEX/Template-Informe/base/Plantilla-Informe//'.\n------------\nRunning 'bibtex  \"reporte-historia-del-derecho-en-mexico\"'\n------------\nThis is BibTeX, Version 0.99d (MiKTeX 25.4)\nThe top-level auxiliary file: reporte-historia-del-derecho-en-mexico.aux\nThe style file: natnumurl.bst\nDatabase file #1: historia-del-derecho-en-mexico.bib\nLatexmk: Change directory back to 'D:/Documentos/LaTEX/Template-Informe'\nLatexmk: applying rule 'pdflatex'...\nRule 'pdflatex':  Reasons for rerun\nChanged files or newly in use/created:\n  .build/latex/aux/reporte-historia-del-derecho-en-mexico.aux\n  .build/latex/aux/reporte-historia-del-derecho-en-mexico.toc\n\n------------\nRun number 3 of rule 'pdflatex'\n------------\n------------\nRunning 'pdflatex  -interaction=nonstopmode -file-line-error -recorder -output-directory=\".build/latex/aux\"  -interaction=batchmode -file-line-error \"D:/Documentos/LaTEX/Template-Informe/UnADM/licenciatura-en-derecho-unadm/historia-del-derecho-en-mexico-lde/reporte-historia-del-derecho-en-mexico.tex\"'\n------------\nThis is pdfTeX, Version 3.141592653-2.6-1.40.27 (MiKTeX 25.4) (preloaded format=pdflatex.fmt)\n restricted \\write18 enabled.\nentering extended mode\nLatexmk: Moving '.build/latex/aux/reporte-historia-del-derecho-en-mexico.pdf' to '.build/latex/reporte-historia-del-derecho-en-mexico.pdf'\nLatexmk: Getting log file '.build/latex/aux/reporte-historia-del-derecho-en-mexico.log'\nLatexmk: Examining '.build/latex/aux/reporte-historia-del-derecho-en-mexico.fls'\nLatexmk: Examining '.build/latex/aux/reporte-historia-del-derecho-en-mexico.log'\nLatexmk: Found input bbl file '.build/latex/aux/reporte-historia-del-derecho-en-mexico.bbl'\nLatexmk: Log file says output to '.build/latex/aux/reporte-historia-del-derecho-en-mexico.pdf'\n  ===Source file '.build/latex/aux/reporte-historia-del-derecho-en-mexico.bbl' for 'pdflatex'\nLatexmk: Found bibliography file(s):\n  D:/Documentos/LaTEX/Template-Informe/UnADM/licenciatura-en-derecho-unadm/historia-del-derecho-en-mexico-lde/historia-del-derecho-en-mexico.bib\nLatexmk: All targets (.build/latex/reporte-historia-del-derecho-en-mexico.pdf) are up-to-date\n\n",
      "stderr_tail": "Latexmk: Using bibtex to make bibliography file(s).\nLatexmk: Missing input file 'reporte-historia-del-derecho-en-mexico.toc' message in .log file:\n  No file reporte-historia-del-derecho-en-mexico.toc.\nLatexmk: Missing bbl file '.build/latex/aux/reporte-historia-del-derecho-en-mexico.bbl' in following:\n No file reporte-historia-del-derecho-en-mexico.bbl.\nLatexmk: Using bibtex to make bibliography file(s).\nLatexmk: Using bibtex to make bibliography file(s).\nLatexmk: Using bibtex to make bibliography file(s).\nReverting Windows console CPs to (in,out) = (850,65001)\nCopy-Item : El proceso no puede obtener acceso al archivo 'D:\\Documentos\\LaTEX\\\nTemplate-Informe\\UnADM\\licenciatura-en-derecho-unadm\\historia-del-derecho-en-me\nxico-lde\\reporte-historia-del-derecho-en-mexico.pdf' porque est� siendo \nutilizado en otro proceso.\nEn D:\\Documentos\\LaTEX\\Template-Informe\\scripts\\latexmk-build.ps1: 119 \nCar�cter: 5\n+     Copy-Item -LiteralPath $GeneratedPdf -Destination $FinalPdf -Forc ...\n+     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n    + CategoryInfo          : NotSpecified: (:) [Copy-Item], IOException\n    + FullyQualifiedErrorId : System.IO.IOException,Microsoft.PowerShell.Comma \n   nds.CopyItemCommand\n \n"
    },
    {
      "tex": "UnADM/licenciatura-en-derecho-unadm/historia-del-derecho-en-mexico-lde/presentacion-historia-del-derecho-en-mexico.tex",
      "ok": false,
      "returncode": 1,
      "stdout_tail": "uild/latex/aux/presentacion-historia-del-derecho-en-mexico.log'\nLatexmk: Log file says output to '.build/latex/aux/presentacion-historia-del-derecho-en-mexico.pdf'\nNo existing .aux file, so I'll make a simple one, and require run of *latex.\nLatexmk: applying rule 'pdflatex'...\nRule 'pdflatex':  Reasons for rerun\nCategory 'other':\n  Rerun of 'pdflatex' forced or previously required:\n    Reason or flag: 'Initial setup'\n\n------------\nRun number 1 of rule 'pdflatex'\n------------\n------------\nRunning 'pdflatex  -interaction=nonstopmode -file-line-error -recorder -output-directory=\".build/latex/aux\"  -interaction=batchmode -file-line-error \"D:/Documentos/LaTEX/Template-Informe/UnADM/licenciatura-en-derecho-unadm/historia-del-derecho-en-mexico-lde/presentacion-historia-del-derecho-en-mexico.tex\"'\n------------\nThis is pdfTeX, Version 3.141592653-2.6-1.40.27 (MiKTeX 25.4) (preloaded format=pdflatex.fmt)\n restricted \\write18 enabled.\nentering extended mode\nLatexmk: Moving '.build/latex/aux/presentacion-historia-del-derecho-en-mexico.pdf' to '.build/latex/presentacion-historia-del-derecho-en-mexico.pdf'\nLatexmk: Getting log file '.build/latex/aux/presentacion-historia-del-derecho-en-mexico.log'\nLatexmk: Examining '.build/latex/aux/presentacion-historia-del-derecho-en-mexico.fls'\nLatexmk: Examining '.build/latex/aux/presentacion-historia-del-derecho-en-mexico.log'\nLatexmk: References changed.\nLatexmk: References changed.\nLatexmk: Log file says output to '.build/latex/aux/presentacion-historia-del-derecho-en-mexico.pdf'\nLatexmk: applying rule 'pdflatex'...\nRule 'pdflatex':  Reasons for rerun\nChanged files or newly in use/created:\n  .build/latex/aux/presentacion-historia-del-derecho-en-mexico.aux\n  .build/latex/aux/presentacion-historia-del-derecho-en-mexico.nav\n  .build/latex/aux/presentacion-historia-del-derecho-en-mexico.out\n\n------------\nRun number 2 of rule 'pdflatex'\n------------\n------------\nRunning 'pdflatex  -interaction=nonstopmode -file-line-error -recorder -output-directory=\".build/latex/aux\"  -interaction=batchmode -file-line-error \"D:/Documentos/LaTEX/Template-Informe/UnADM/licenciatura-en-derecho-unadm/historia-del-derecho-en-mexico-lde/presentacion-historia-del-derecho-en-mexico.tex\"'\n------------\nThis is pdfTeX, Version 3.141592653-2.6-1.40.27 (MiKTeX 25.4) (preloaded format=pdflatex.fmt)\n restricted \\write18 enabled.\nentering extended mode\nLatexmk: Moving '.build/latex/aux/presentacion-historia-del-derecho-en-mexico.pdf' to '.build/latex/presentacion-historia-del-derecho-en-mexico.pdf'\nLatexmk: Getting log file '.build/latex/aux/presentacion-historia-del-derecho-en-mexico.log'\nLatexmk: Examining '.build/latex/aux/presentacion-historia-del-derecho-en-mexico.fls'\nLatexmk: Examining '.build/latex/aux/presentacion-historia-del-derecho-en-mexico.log'\nLatexmk: Log file says output to '.build/latex/aux/presentacion-historia-del-derecho-en-mexico.pdf'\nLatexmk: All targets (.build/latex/presentacion-historia-del-derecho-en-mexico.pdf) are up-to-date\n\n",
      "stderr_tail": "Latexmk: Using bibtex to make bibliography file(s).\nLatexmk: Missing input file 'presentacion-historia-del-derecho-en-mexico.nav' message in .log file:\n  No file presentacion-historia-del-derecho-en-mexico.nav.\nLatexmk: Using bibtex to make bibliography file(s).\nLatexmk: Using bibtex to make bibliography file(s).\nReverting Windows console CPs to (in,out) = (850,65001)\nCopy-Item : El proceso no puede obtener acceso al archivo 'D:\\Documentos\\LaTEX\\\nTemplate-Informe\\UnADM\\licenciatura-en-derecho-unadm\\historia-del-derecho-en-me\nxico-lde\\presentacion-historia-del-derecho-en-mexico.pdf' porque est� siendo \nutilizado en otro proceso.\nEn D:\\Documentos\\LaTEX\\Template-Informe\\scripts\\latexmk-build.ps1: 119 \nCar�cter: 5\n+     Copy-Item -LiteralPath $GeneratedPdf -Destination $FinalPdf -Forc ...\n+     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n    + CategoryInfo          : NotSpecified: (:) [Copy-Item], IOException\n    + FullyQualifiedErrorId : System.IO.IOException,Microsoft.PowerShell.Comma \n   nds.CopyItemCommand\n \n"
    }
  ],
  "consensus": {
    "consensus_score": 7.3,
    "passed": true,
    "criteria": {
      "identidad_institucional": true,
      "bibliografia": true,
      "trazabilidad": true,
      "compilacion": true,
      "riesgos": true
    },
    "role_scores": {
      "Planificador editorial": 7.8,
      "Investigador documental": 9.03,
      "Arquitecto de plantillas": 0.0,
      "Verificador y validador": 0.0,
      "Critico adversarial": 8.58
    },
    "risks": [],
    "recommendations": [
      "Usar el reporte como retroalimentacion editorial aplicable al objetivo."
    ]
  },
  "workflow_events": [
    {
      "timestamp": "2026-06-18 11:55:16",
      "state": "initialized",
      "action": "init",
      "status": "ok",
      "detail": "AulaTeX workflow initialized"
    },
    {
      "timestamp": "2026-06-18 11:55:17",
      "state": "initialized",
      "action": "llm-start",
      "status": "ok",
      "detail": "planificar: Planificador editorial via Codex"
    },
    {
      "timestamp": "2026-06-18 11:55:30",
      "state": "initialized",
      "action": "llm-end",
      "status": "ok",
      "detail": "planificar: 4935 chars"
    },
    {
      "timestamp": "2026-06-18 11:55:30",
      "state": "planned",
      "action": "initialized->planned",
      "status": "ok",
      "detail": "plan editorial producido"
    },
    {
      "timestamp": "2026-06-18 11:55:30",
      "state": "planned",
      "action": "llm-start",
      "status": "ok",
      "detail": "investigar: Investigador documental via Claude Foundry"
    },
    {
      "timestamp": "2026-06-18 11:55:53",
      "state": "planned",
      "action": "llm-end",
      "status": "ok",
      "detail": "investigar: 3570 chars"
    },
    {
      "timestamp": "2026-06-18 11:55:53",
      "state": "researched",
      "action": "planned->researched",
      "status": "ok",
      "detail": "diagnostico documental producido"
    },
    {
      "timestamp": "2026-06-18 11:55:53",
      "state": "researched",
      "action": "llm-start",
      "status": "ok",
      "detail": "generar: Arquitecto de plantillas via GPT-Pro"
    },
    {
      "timestamp": "2026-06-18 11:56:29",
      "state": "researched",
      "action": "llm-end",
      "status": "ok",
      "detail": "generar: 0 chars"
    },
    {
      "timestamp": "2026-06-18 11:56:29",
      "state": "generated",
      "action": "researched->generated",
      "status": "ok",
      "detail": "propuesta editorial producida"
    },
    {
      "timestamp": "2026-06-18 11:56:29",
      "state": "generated",
      "action": "llm-start",
      "status": "ok",
      "detail": "validar: Verificador y validador via Auto (model-router)"
    },
    {
      "timestamp": "2026-06-18 11:56:53",
      "state": "generated",
      "action": "llm-end",
      "status": "ok",
      "detail": "validar: 0 chars"
    },
    {
      "timestamp": "2026-06-18 11:56:53",
      "state": "generated",
      "action": "llm-start",
      "status": "ok",
      "detail": "criticar: Critico adversarial via Codex"
    },
    {
      "timestamp": "2026-06-18 11:57:04",
      "state": "generated",
      "action": "llm-end",
      "status": "ok",
      "detail": "criticar: 3672 chars"
    },
    {
      "timestamp": "2026-06-18 11:57:04",
      "state": "generated",
      "action": "tool-select",
      "status": "ok",
      "detail": "latexmk-build.ps1 seleccionado para compilar objetivos canonicos"
    },
    {
      "timestamp": "2026-06-18 12:03:11",
      "state": "generated",
      "action": "tool-result",
      "status": "error",
      "detail": "UnADM/licenciatura-en-derecho-unadm/historia-del-derecho-en-mexico-lde/reporte-historia-del-derecho-en-mexico.tex rc=1"
    },
    {
      "timestamp": "2026-06-18 12:06:19",
      "state": "generated",
      "action": "tool-result",
      "status": "error",
      "detail": "UnADM/licenciatura-en-derecho-unadm/historia-del-derecho-en-mexico-lde/presentacion-historia-del-derecho-en-mexico.tex rc=1"
    },
    {
      "timestamp": "2026-06-18 12:06:19",
      "state": "compiled",
      "action": "generated->compiled",
      "status": "ok",
      "detail": "compilacion latexmk ejecutada"
    },
    {
      "timestamp": "2026-06-18 12:06:19",
      "state": "compiled",
      "action": "consensus",
      "status": "ok",
      "detail": "score=7.30"
    },
    {
      "timestamp": "2026-06-18 12:06:19",
      "state": "evaluated",
      "action": "compiled->evaluated",
      "status": "ok",
      "detail": "validacion y consenso completados"
    },
    {
      "timestamp": "2026-06-18 12:06:19",
      "state": "finalized",
      "action": "evaluated->finalized",
      "status": "ok",
      "detail": "ciclo agentico cerrado"
    }
  ]
}
```

## 20260618-122801 - generar-actividad

```json
{
  "run_id": "20260618-122801",
  "target": "UnADM/licenciatura-en-derecho-unadm/historia-del-derecho-en-mexico-lde",
  "level": "materia",
  "action": "generar-actividad",
  "activity_number": 1,
  "engines": [
    "Codex",
    "Claude Foundry",
    "GPT-Pro",
    "Auto (model-router)"
  ],
  "agentic_patterns": [
    "planning-memory",
    "tool-using-workflow",
    "verification-validation",
    "collective-consensus"
  ],
  "tasks": [
    {
      "stage": "planificar",
      "role": "Planificador editorial",
      "mission": "descomponer el objetivo en plan ejecutable y criterios de aceptacion",
      "engine": "Codex"
    },
    {
      "stage": "investigar",
      "role": "Investigador documental",
      "mission": "detectar fuentes, contexto curricular y faltantes editoriales",
      "engine": "Claude Foundry"
    },
    {
      "stage": "generar",
      "role": "Arquitecto de plantillas",
      "mission": "proponer estructura de reporte/presentacion y actividad",
      "engine": "GPT-Pro"
    },
    {
      "stage": "validar",
      "role": "Verificador y validador",
      "mission": "verificar consistencia, compilacion y evidencias",
      "engine": "Auto (model-router)"
    },
    {
      "stage": "criticar",
      "role": "Critico adversarial",
      "mission": "encontrar fallas antes de aplicar cambios",
      "engine": "Codex"
    }
  ],
  "llm_results": [
    {
      "engine": "Codex",
      "ok": false,
      "error": "Error de red: ConnectionError.",
      "chars": 0
    },
    {
      "engine": "Claude Foundry",
      "ok": false,
      "error": "Error de red: ConnectionError.",
      "chars": 0
    },
    {
      "engine": "GPT-Pro",
      "ok": false,
      "error": "Error de red: ConnectionError.",
      "chars": 0
    },
    {
      "engine": "Auto (model-router)",
      "ok": false,
      "error": "Tiempo de espera agotado.",
      "chars": 0
    },
    {
      "engine": "Codex",
      "ok": false,
      "error": "Error de red: ConnectionError.",
      "chars": 0
    }
  ],
  "compile_results": [
    {
      "tex": "UnADM/licenciatura-en-derecho-unadm/historia-del-derecho-en-mexico-lde/reporte-historia-del-derecho-en-mexico.tex",
      "ok": false,
      "returncode": 1,
      "stdout_tail": "Initial Win CP for (console input, console output, system): (CP850, CP65001, CP1252)\nI changed them all to CP1252\nRc files read:\n  .latexmkrc\nLatexmk: This is Latexmk, John Collins, 15 June 2025. Version 4.87.\nLatexmk: Nothing to do for 'D:/Documentos/LaTEX/Template-Informe/UnADM/licenciatura-en-derecho-unadm/historia-del-derecho-en-mexico-lde/reporte-historia-del-derecho-en-mexico.tex'.\nLatexmk: All targets (.build/latex/reporte-historia-del-derecho-en-mexico.pdf) are up-to-date\n\n",
      "stderr_tail": "Reverting Windows console CPs to (in,out) = (850,65001)\nCopy-Item : El proceso no puede obtener acceso al archivo 'D:\\Documentos\\LaTEX\\\nTemplate-Informe\\UnADM\\licenciatura-en-derecho-unadm\\historia-del-derecho-en-me\nxico-lde\\reporte-historia-del-derecho-en-mexico.pdf' porque est� siendo \nutilizado en otro proceso.\nEn D:\\Documentos\\LaTEX\\Template-Informe\\scripts\\latexmk-build.ps1: 119 \nCar�cter: 5\n+     Copy-Item -LiteralPath $GeneratedPdf -Destination $FinalPdf -Forc ...\n+     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n    + CategoryInfo          : NotSpecified: (:) [Copy-Item], IOException\n    + FullyQualifiedErrorId : System.IO.IOException,Microsoft.PowerShell.Comma \n   nds.CopyItemCommand\n \n"
    },
    {
      "tex": "UnADM/licenciatura-en-derecho-unadm/historia-del-derecho-en-mexico-lde/presentacion-historia-del-derecho-en-mexico.tex",
      "ok": false,
      "returncode": 1,
      "stdout_tail": "Initial Win CP for (console input, console output, system): (CP850, CP65001, CP1252)\nI changed them all to CP1252\nRc files read:\n  .latexmkrc\nLatexmk: This is Latexmk, John Collins, 15 June 2025. Version 4.87.\nLatexmk: Nothing to do for 'D:/Documentos/LaTEX/Template-Informe/UnADM/licenciatura-en-derecho-unadm/historia-del-derecho-en-mexico-lde/presentacion-historia-del-derecho-en-mexico.tex'.\nLatexmk: All targets (.build/latex/presentacion-historia-del-derecho-en-mexico.pdf) are up-to-date\n\n",
      "stderr_tail": "Reverting Windows console CPs to (in,out) = (850,65001)\nCopy-Item : El proceso no puede obtener acceso al archivo 'D:\\Documentos\\LaTEX\\\nTemplate-Informe\\UnADM\\licenciatura-en-derecho-unadm\\historia-del-derecho-en-me\nxico-lde\\presentacion-historia-del-derecho-en-mexico.pdf' porque est� siendo \nutilizado en otro proceso.\nEn D:\\Documentos\\LaTEX\\Template-Informe\\scripts\\latexmk-build.ps1: 119 \nCar�cter: 5\n+     Copy-Item -LiteralPath $GeneratedPdf -Destination $FinalPdf -Forc ...\n+     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n    + CategoryInfo          : NotSpecified: (:) [Copy-Item], IOException\n    + FullyQualifiedErrorId : System.IO.IOException,Microsoft.PowerShell.Comma \n   nds.CopyItemCommand\n \n"
    }
  ],
  "consensus": {
    "consensus_score": 0.0,
    "passed": false,
    "criteria": {
      "identidad_institucional": false,
      "bibliografia": false,
      "trazabilidad": false,
      "compilacion": false,
      "riesgos": false
    },
    "role_scores": {
      "Planificador editorial": 0.0,
      "Investigador documental": 0.0,
      "Arquitecto de plantillas": 0.0,
      "Verificador y validador": 0.0,
      "Critico adversarial": 0.0
    },
    "risks": [
      "Criterio sin cobertura: identidad_institucional",
      "Criterio sin cobertura: bibliografia",
      "Criterio sin cobertura: trazabilidad",
      "Criterio sin cobertura: compilacion",
      "Criterio sin cobertura: riesgos",
      "LLM sin respuesta util: Codex, Claude Foundry, GPT-Pro, Auto (model-router), Codex"
    ],
    "recommendations": [
      "Ejecutar un ciclo de recuperacion documental antes de generar actividad final.",
      "Activar compilacion y anexar logs latexmk al siguiente ciclo.",
      "Repetir con al menos tres roles: investigador, arquitecto y critico."
    ]
  },
  "workflow_events": [
    {
      "timestamp": "2026-06-18 12:28:01",
      "state": "initialized",
      "action": "init",
      "status": "ok",
      "detail": "AulaTeX workflow initialized"
    },
    {
      "timestamp": "2026-06-18 12:28:01",
      "state": "initialized",
      "action": "llm-start",
      "status": "ok",
      "detail": "planificar: Planificador editorial via Codex"
    },
    {
      "timestamp": "2026-06-18 12:28:18",
      "state": "initialized",
      "action": "llm-end",
      "status": "error",
      "detail": "planificar: Error de red: ConnectionError."
    },
    {
      "timestamp": "2026-06-18 12:28:18",
      "state": "planned",
      "action": "initialized->planned",
      "status": "ok",
      "detail": "plan editorial producido"
    },
    {
      "timestamp": "2026-06-18 12:28:18",
      "state": "planned",
      "action": "llm-start",
      "status": "ok",
      "detail": "investigar: Investigador documental via Claude Foundry"
    },
    {
      "timestamp": "2026-06-18 12:29:17",
      "state": "planned",
      "action": "llm-end",
      "status": "error",
      "detail": "investigar: Error de red: ConnectionError."
    },
    {
      "timestamp": "2026-06-18 12:29:17",
      "state": "researched",
      "action": "planned->researched",
      "status": "ok",
      "detail": "diagnostico documental producido"
    },
    {
      "timestamp": "2026-06-18 12:29:17",
      "state": "researched",
      "action": "llm-start",
      "status": "ok",
      "detail": "generar: Arquitecto de plantillas via GPT-Pro"
    },
    {
      "timestamp": "2026-06-18 12:29:30",
      "state": "researched",
      "action": "llm-end",
      "status": "error",
      "detail": "generar: Error de red: ConnectionError."
    },
    {
      "timestamp": "2026-06-18 12:29:30",
      "state": "generated",
      "action": "researched->generated",
      "status": "ok",
      "detail": "propuesta editorial producida"
    },
    {
      "timestamp": "2026-06-18 12:29:30",
      "state": "generated",
      "action": "llm-start",
      "status": "ok",
      "detail": "validar: Verificador y validador via Auto (model-router)"
    },
    {
      "timestamp": "2026-06-18 12:30:44",
      "state": "generated",
      "action": "llm-end",
      "status": "error",
      "detail": "validar: Tiempo de espera agotado."
    },
    {
      "timestamp": "2026-06-18 12:30:44",
      "state": "generated",
      "action": "llm-start",
      "status": "ok",
      "detail": "criticar: Critico adversarial via Codex"
    },
    {
      "timestamp": "2026-06-18 12:31:01",
      "state": "generated",
      "action": "llm-end",
      "status": "error",
      "detail": "criticar: Error de red: ConnectionError."
    },
    {
      "timestamp": "2026-06-18 12:31:01",
      "state": "generated",
      "action": "tool-select",
      "status": "ok",
      "detail": "latexmk-build.ps1 seleccionado para compilar objetivos canonicos"
    },
    {
      "timestamp": "2026-06-18 12:31:02",
      "state": "generated",
      "action": "tool-result",
      "status": "error",
      "detail": "UnADM/licenciatura-en-derecho-unadm/historia-del-derecho-en-mexico-lde/reporte-historia-del-derecho-en-mexico.tex rc=1"
    },
    {
      "timestamp": "2026-06-18 12:31:04",
      "state": "generated",
      "action": "tool-result",
      "status": "error",
      "detail": "UnADM/licenciatura-en-derecho-unadm/historia-del-derecho-en-mexico-lde/presentacion-historia-del-derecho-en-mexico.tex rc=1"
    },
    {
      "timestamp": "2026-06-18 12:31:04",
      "state": "compiled",
      "action": "generated->compiled",
      "status": "ok",
      "detail": "compilacion latexmk ejecutada"
    },
    {
      "timestamp": "2026-06-18 12:31:04",
      "state": "compiled",
      "action": "consensus",
      "status": "warn",
      "detail": "score=0.00"
    },
    {
      "timestamp": "2026-06-18 12:31:04",
      "state": "evaluated",
      "action": "compiled->evaluated",
      "status": "ok",
      "detail": "validacion y consenso completados"
    },
    {
      "timestamp": "2026-06-18 12:31:04",
      "state": "finalized",
      "action": "evaluated->finalized",
      "status": "ok",
      "detail": "ciclo agentico cerrado"
    }
  ]
}
```

## 20260618-130622 - memoria-editorial

```json
{
  "run_id": "20260618-130622",
  "source_scope_key": "UnADM/licenciatura-en-derecho-unadm/historia-del-derecho-en-mexico-lde",
  "build_level": "materia",
  "propagation_mode": "local",
  "iterations": 1,
  "engines": [
    "Codex"
  ],
  "built_scopes": [
    "UnADM/licenciatura-en-derecho-unadm/historia-del-derecho-en-mexico-lde"
  ],
  "cycles": [
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/historia-del-derecho-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 1,
      "engine": "Codex",
      "ok": false,
      "chars": 30
    }
  ],
  "ok": false
}
```

## 20260618-134354 - memoria-editorial

```json
{
  "run_id": "20260618-134354",
  "source_scope_key": "ITESCA/ingenieria-en-sistemas-computacionales",
  "build_level": "institucion",
  "propagation_mode": "arriba-y-laterales",
  "iterations": 1,
  "engines": [
    "Codex"
  ],
  "built_scopes": [
    "ITESCA/ingenieria-en-sistemas-computacionales",
    "ITESCA/maestria-en-gestion-administrativa",
    "ITESCA",
    "IIIEPE",
    "UANL",
    "UCNL",
    "UnADM"
  ],
  "cycles": [
    {
      "scope_key": "ITESCA/ingenieria-en-sistemas-computacionales",
      "scope_level": "carrera",
      "cycle": 1,
      "engine": "Codex",
      "ok": true,
      "chars": 2265
    },
    {
      "scope_key": "ITESCA/maestria-en-gestion-administrativa",
      "scope_level": "carrera",
      "cycle": 1,
      "engine": "Codex",
      "ok": true,
      "chars": 2251
    },
    {
      "scope_key": "ITESCA",
      "scope_level": "institucion",
      "cycle": 1,
      "engine": "Codex",
      "ok": true,
      "chars": 2338
    },
    {
      "scope_key": "IIIEPE",
      "scope_level": "institucion",
      "cycle": 1,
      "engine": "Codex",
      "ok": true,
      "chars": 2271
    },
    {
      "scope_key": "UANL",
      "scope_level": "institucion",
      "cycle": 1,
      "engine": "Codex",
      "ok": true,
      "chars": 2296
    },
    {
      "scope_key": "UCNL",
      "scope_level": "institucion",
      "cycle": 1,
      "engine": "Codex",
      "ok": true,
      "chars": 2299
    },
    {
      "scope_key": "UnADM",
      "scope_level": "institucion",
      "cycle": 1,
      "engine": "Codex",
      "ok": true,
      "chars": 2241
    }
  ],
  "ok": true
}
```

## 20260618-142935 - memoria-editorial

```json
{
  "run_id": "20260618-142935",
  "source_scope_key": "ITESCA/ingenieria-en-sistemas-computacionales",
  "build_level": "institucion",
  "propagation_mode": "arriba-y-laterales",
  "iterations": 1,
  "engines": [
    "Codex"
  ],
  "built_scopes": [
    "ITESCA/ingenieria-en-sistemas-computacionales",
    "ITESCA/maestria-en-gestion-administrativa",
    "ITESCA",
    "IIIEPE",
    "UANL",
    "UCNL",
    "UnADM"
  ],
  "cycles": [],
  "ok": false,
  "cancelled": true
}
```

## 20260618-162942 - construccion-descendente

```json
{
  "run_id": "20260618-162942",
  "node_key": "UAS",
  "node_level": "institucion",
  "node_name": "UAS",
  "node_label": "UAS",
  "parent_scope_key": "interinstitucional",
  "activity_number": 0,
  "operation_mode": "crear",
  "destination_path": ".build/generation-smoke/UAS",
  "engines": [
    "Codex"
  ],
  "iterations": 1,
  "cancelled": false,
  "ok": true,
  "node_dir": ".build/generation-smoke/UAS",
  "artifacts": {
    "memory": ".build/generation-smoke/UAS/memoria-fundacional.json",
    "plan": ".build/generation-smoke/UAS/plan.md",
    "maqueta": ".build/generation-smoke/UAS/maqueta.tex"
  },
  "future_agent_contract": {
    "status": "ready-for-agent",
    "allowed_actions": [
      "investigar",
      "redactar",
      "evaluar",
      "compilar"
    ],
    "entrypoint": ".build/generation-smoke/UAS/maqueta.tex",
    "notes": "El Agente debe consumir esta maqueta sin recrear el nodo ni reconstruir memoria fundacional."
  },
  "cycle_logs": [
    {
      "cycle": 1,
      "engine": "Codex",
      "ok": true,
      "elapsed_ms": 0,
      "chars": 1125,
      "memory_items": 8,
      "sections_created": 23
    }
  ]
}
```

## 20260618-162950 - construccion-descendente

```json
{
  "run_id": "20260618-162950",
  "node_key": "UAS",
  "node_level": "institucion",
  "node_name": "UAS",
  "node_label": "UAS",
  "parent_scope_key": "interinstitucional",
  "activity_number": 0,
  "operation_mode": "reforzar",
  "destination_path": ".build/generation-smoke/UAS",
  "engines": [
    "Codex"
  ],
  "iterations": 1,
  "cancelled": false,
  "ok": true,
  "node_dir": ".build/generation-smoke/UAS",
  "artifacts": {
    "memory": ".build/generation-smoke/UAS/memoria-fundacional.json",
    "plan": ".build/generation-smoke/UAS/plan.md",
    "maqueta": ".build/generation-smoke/UAS/maqueta.tex"
  },
  "future_agent_contract": {
    "status": "ready-for-agent",
    "allowed_actions": [
      "investigar",
      "redactar",
      "evaluar",
      "compilar"
    ],
    "entrypoint": ".build/generation-smoke/UAS/maqueta.tex",
    "notes": "El Agente debe consumir esta maqueta sin recrear el nodo ni reconstruir memoria fundacional."
  },
  "cycle_logs": [
    {
      "cycle": 1,
      "engine": "Codex",
      "ok": true,
      "elapsed_ms": 0,
      "chars": 1178,
      "memory_items": 16,
      "sections_created": 23
    }
  ]
}
```

## 20260618-170258 - construccion-descendente

```json
{
  "run_id": "20260618-170258",
  "node_key": "UAS-INGESTA",
  "node_level": "institucion",
  "node_name": "UAS-INGESTA",
  "node_label": "UAS-INGESTA",
  "parent_scope_key": "interinstitucional",
  "activity_number": 0,
  "operation_mode": "crear",
  "destination_path": ".build/generation-smoke/UAS-INGESTA",
  "ingestion": {
    "has_text": true,
    "has_document": true,
    "document_path": ".build/generation-smoke/ingesta.txt"
  },
  "engines": [
    "Codex"
  ],
  "iterations": 1,
  "cancelled": false,
  "ok": true,
  "node_dir": ".build/generation-smoke/UAS-INGESTA",
  "artifacts": {
    "memory": ".build/generation-smoke/UAS-INGESTA/memoria-fundacional.json",
    "plan": ".build/generation-smoke/UAS-INGESTA/plan.md",
    "maqueta": ".build/generation-smoke/UAS-INGESTA/maqueta.tex"
  },
  "future_agent_contract": {
    "status": "ready-for-agent",
    "allowed_actions": [
      "investigar",
      "redactar",
      "evaluar",
      "compilar"
    ],
    "entrypoint": ".build/generation-smoke/UAS-INGESTA/maqueta.tex",
    "notes": "El Agente debe consumir esta maqueta sin recrear el nodo ni reconstruir memoria fundacional."
  },
  "cycle_logs": [
    {
      "cycle": 1,
      "engine": "Codex",
      "ok": true,
      "elapsed_ms": 0,
      "chars": 1327,
      "memory_items": 8,
      "sections_created": 27
    }
  ]
}
```

## 20260619-032116 - construccion-descendente

```json
{
  "run_id": "20260619-032116",
  "node_key": "UCNL",
  "node_level": "institucion",
  "node_name": "UCNL",
  "node_label": "UCNL",
  "parent_scope_key": "interinstitucional",
  "activity_number": 0,
  "operation_mode": "reforzar",
  "destination_path": "UCNL",
  "ingestion": {
    "has_text": false,
    "has_document": true,
    "document_path": "D:\\Descargas\\Modelo Educativo UC.pdf"
  },
  "engines": [
    "Codex",
    "Auto (model-router)",
    "Claude Foundry",
    "GPT-Pro"
  ],
  "iterations": 1,
  "cancelled": false,
  "ok": true,
  "node_dir": "UCNL",
  "artifacts": {
    "memory": "UCNL/memoria-fundacional.json",
    "plan": "UCNL/plan.md",
    "maqueta": "UCNL/maqueta.tex"
  },
  "future_agent_contract": {
    "status": "ready-for-agent",
    "allowed_actions": [
      "investigar",
      "redactar",
      "evaluar",
      "compilar"
    ],
    "entrypoint": "UCNL/maqueta.tex",
    "notes": "El Agente debe consumir esta maqueta sin recrear el nodo ni reconstruir memoria fundacional."
  },
  "cycle_logs": [
    {
      "cycle": 1,
      "engine": "Codex",
      "ok": true,
      "elapsed_ms": 18599,
      "chars": 7625,
      "memory_items": 26,
      "sections_created": 27
    },
    {
      "cycle": 1,
      "engine": "Auto (model-router)",
      "ok": true,
      "elapsed_ms": 13529,
      "chars": 5271,
      "memory_items": 51,
      "sections_created": 27
    },
    {
      "cycle": 1,
      "engine": "Claude Foundry",
      "ok": true,
      "elapsed_ms": 22283,
      "chars": 4448,
      "memory_items": 51,
      "sections_created": 27
    },
    {
      "cycle": 1,
      "engine": "GPT-Pro",
      "ok": true,
      "elapsed_ms": 42437,
      "chars": 0,
      "memory_items": 54,
      "sections_created": 27
    }
  ]
}
```

## 20260619-033859 - construccion-descendente

```json
{
  "run_id": "20260619-033859",
  "node_key": "IIIEPE",
  "node_level": "institucion",
  "node_name": "IIIEPE",
  "node_label": "IIIEPE",
  "parent_scope_key": "interinstitucional",
  "activity_number": 0,
  "operation_mode": "reforzar",
  "destination_path": "IIIEPE",
  "ingestion": {
    "has_text": false,
    "has_document": false,
    "document_path": ""
  },
  "engines": [
    "Codex",
    "Auto (model-router)",
    "Claude Foundry",
    "GPT-Pro"
  ],
  "iterations": 2,
  "cancelled": false,
  "ok": false,
  "node_dir": "IIIEPE",
  "artifacts": {
    "memory": "IIIEPE/memoria-fundacional.json",
    "plan": "IIIEPE/plan.md",
    "maqueta": "IIIEPE/maqueta.tex"
  },
  "future_agent_contract": {
    "status": "ready-for-agent",
    "allowed_actions": [
      "investigar",
      "redactar",
      "evaluar",
      "compilar"
    ],
    "entrypoint": "IIIEPE/maqueta.tex",
    "notes": "El Agente debe consumir esta maqueta sin recrear el nodo ni reconstruir memoria fundacional."
  },
  "cycle_logs": [
    {
      "cycle": 1,
      "engine": "Codex",
      "ok": true,
      "elapsed_ms": 18804,
      "chars": 7753,
      "memory_items": 28,
      "sections_created": 27
    },
    {
      "cycle": 1,
      "engine": "Auto (model-router)",
      "ok": true,
      "elapsed_ms": 43220,
      "chars": 15034,
      "memory_items": 77,
      "sections_created": 27
    },
    {
      "cycle": 1,
      "engine": "Claude Foundry",
      "ok": false,
      "elapsed_ms": 45821,
      "chars": 25,
      "memory_items": 80,
      "sections_created": 27
    },
    {
      "cycle": 1,
      "engine": "GPT-Pro",
      "ok": false,
      "elapsed_ms": 45842,
      "chars": 25,
      "memory_items": 81,
      "sections_created": 27
    },
    {
      "cycle": 2,
      "engine": "Codex",
      "ok": true,
      "elapsed_ms": 17259,
      "chars": 8682,
      "memory_items": 111,
      "sections_created": 27
    },
    {
      "cycle": 2,
      "engine": "Auto (model-router)",
      "ok": true,
      "elapsed_ms": 30773,
      "chars": 15733,
      "memory_items": 154,
      "sections_created": 27
    },
    {
      "cycle": 2,
      "engine": "Claude Foundry",
      "ok": false,
      "elapsed_ms": 45910,
      "chars": 25,
      "memory_items": 154,
      "sections_created": 27
    },
    {
      "cycle": 2,
      "engine": "GPT-Pro",
      "ok": false,
      "elapsed_ms": 45886,
      "chars": 25,
      "memory_items": 154,
      "sections_created": 27
    }
  ]
}
```

## 20260619-121930 - construccion-descendente

```json
{
  "run_id": "20260619-121930",
  "node_key": "UAS",
  "node_level": "institucion",
  "node_name": "UAS",
  "node_label": "UAS",
  "parent_scope_key": "interinstitucional",
  "activity_number": 0,
  "operation_mode": "reforzar",
  "destination_path": "UAS",
  "ingestion": {
    "has_text": true,
    "has_document": false,
    "document_path": ""
  },
  "engines": [
    "Codex",
    "Auto (model-router)",
    "Claude Foundry",
    "GPT-Pro"
  ],
  "iterations": 2,
  "cancelled": false,
  "ok": false,
  "node_dir": "UAS",
  "artifacts": {
    "memory": "UAS/memoria-fundacional.json",
    "plan": "UAS/plan.md",
    "maqueta": "UAS/maqueta.tex"
  },
  "future_agent_contract": {
    "status": "ready-for-agent",
    "allowed_actions": [
      "investigar",
      "redactar",
      "evaluar",
      "compilar"
    ],
    "entrypoint": "UAS/maqueta.tex",
    "notes": "El Agente debe consumir esta maqueta sin recrear el nodo ni reconstruir memoria fundacional."
  },
  "cycle_logs": [
    {
      "cycle": 1,
      "engine": "Codex",
      "ok": true,
      "elapsed_ms": 19673,
      "chars": 8135,
      "memory_items": 33,
      "sections_created": 27
    },
    {
      "cycle": 1,
      "engine": "Auto (model-router)",
      "ok": false,
      "elapsed_ms": 2200,
      "chars": 9,
      "memory_items": 36,
      "sections_created": 27
    },
    {
      "cycle": 1,
      "engine": "Claude Foundry",
      "ok": false,
      "elapsed_ms": 1727,
      "chars": 9,
      "memory_items": 37,
      "sections_created": 27
    },
    {
      "cycle": 1,
      "engine": "GPT-Pro",
      "ok": false,
      "elapsed_ms": 45756,
      "chars": 25,
      "memory_items": 38,
      "sections_created": 27
    },
    {
      "cycle": 2,
      "engine": "Codex",
      "ok": true,
      "elapsed_ms": 19671,
      "chars": 8924,
      "memory_items": 74,
      "sections_created": 27
    },
    {
      "cycle": 2,
      "engine": "Auto (model-router)",
      "ok": false,
      "elapsed_ms": 3693,
      "chars": 9,
      "memory_items": 74,
      "sections_created": 27
    },
    {
      "cycle": 2,
      "engine": "Claude Foundry",
      "ok": false,
      "elapsed_ms": 1471,
      "chars": 9,
      "memory_items": 74,
      "sections_created": 27
    },
    {
      "cycle": 2,
      "engine": "GPT-Pro",
      "ok": false,
      "elapsed_ms": 45822,
      "chars": 25,
      "memory_items": 74,
      "sections_created": 27
    }
  ]
}
```

## 20260619-180222 - construccion-descendente

```json
{
  "run_id": "20260619-180222",
  "node_key": "UnADM/derecho-a-la-seguridad-social-lde",
  "node_level": "materia",
  "node_name": "derecho-a-la-seguridad-social-lde",
  "node_label": "derecho-a-la-seguridad-social-lde",
  "parent_scope_key": "UnADM",
  "activity_number": 0,
  "operation_mode": "reforzar",
  "destination_path": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
  "ingestion": {
    "has_text": false,
    "has_document": false,
    "document_path": ""
  },
  "engines": [
    "Codex",
    "Auto (model-router)",
    "Claude Foundry",
    "GPT-Pro"
  ],
  "iterations": 11,
  "cancelled": false,
  "ok": false,
  "node_dir": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
  "artifacts": {
    "memory": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/memoria-fundacional.json",
    "plan": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/plan.md",
    "maqueta": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/maqueta.tex"
  },
  "future_agent_contract": {
    "status": "ready-for-agent",
    "allowed_actions": [
      "investigar",
      "redactar",
      "evaluar",
      "compilar"
    ],
    "entrypoint": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/maqueta.tex",
    "notes": "El Agente debe consumir esta maqueta sin recrear el nodo ni reconstruir memoria fundacional."
  },
  "cycle_logs": [
    {
      "cycle": 1,
      "engine": "Codex",
      "ok": true,
      "elapsed_ms": 16216,
      "chars": 7829,
      "memory_items": 32,
      "sections_created": 27
    },
    {
      "cycle": 1,
      "engine": "Auto (model-router)",
      "ok": false,
      "elapsed_ms": 4069,
      "chars": 9,
      "memory_items": 35,
      "sections_created": 27
    },
    {
      "cycle": 1,
      "engine": "Claude Foundry",
      "ok": false,
      "elapsed_ms": 1533,
      "chars": 9,
      "memory_items": 36,
      "sections_created": 27
    },
    {
      "cycle": 1,
      "engine": "GPT-Pro",
      "ok": false,
      "elapsed_ms": 45905,
      "chars": 25,
      "memory_items": 37,
      "sections_created": 27
    },
    {
      "cycle": 2,
      "engine": "Codex",
      "ok": true,
      "elapsed_ms": 15324,
      "chars": 8786,
      "memory_items": 73,
      "sections_created": 27
    },
    {
      "cycle": 2,
      "engine": "Auto (model-router)",
      "ok": false,
      "elapsed_ms": 1308,
      "chars": 9,
      "memory_items": 73,
      "sections_created": 27
    },
    {
      "cycle": 2,
      "engine": "Claude Foundry",
      "ok": false,
      "elapsed_ms": 1613,
      "chars": 9,
      "memory_items": 73,
      "sections_created": 27
    },
    {
      "cycle": 2,
      "engine": "GPT-Pro",
      "ok": false,
      "elapsed_ms": 46033,
      "chars": 25,
      "memory_items": 73,
      "sections_created": 27
    },
    {
      "cycle": 3,
      "engine": "Codex",
      "ok": true,
      "elapsed_ms": 13372,
      "chars": 8697,
      "memory_items": 104,
      "sections_created": 27
    },
    {
      "cycle": 3,
      "engine": "Auto (model-router)",
      "ok": false,
      "elapsed_ms": 2401,
      "chars": 9,
      "memory_items": 104,
      "sections_created": 27
    },
    {
      "cycle": 3,
      "engine": "Claude Foundry",
      "ok": false,
      "elapsed_ms": 6179,
      "chars": 9,
      "memory_items": 104,
      "sections_created": 27
    },
    {
      "cycle": 3,
      "engine": "GPT-Pro",
      "ok": false,
      "elapsed_ms": 45833,
      "chars": 25,
      "memory_items": 104,
      "sections_created": 27
    },
    {
      "cycle": 4,
      "engine": "Codex",
      "ok": true,
      "elapsed_ms": 15034,
      "chars": 8979,
      "memory_items": 120,
      "sections_created": 27
    },
    {
      "cycle": 4,
      "engine": "Auto (model-router)",
      "ok": false,
      "elapsed_ms": 1797,
      "chars": 9,
      "memory_items": 120,
      "sections_created": 27
    },
    {
      "cycle": 4,
      "engine": "Claude Foundry",
      "ok": false,
      "elapsed_ms": 1421,
      "chars": 9,
      "memory_items": 120,
      "sections_created": 27
    },
    {
      "cycle": 4,
      "engine": "GPT-Pro",
      "ok": false,
      "elapsed_ms": 48511,
      "chars": 25,
      "memory_items": 120,
      "sections_created": 27
    },
    {
      "cycle": 5,
      "engine": "Codex",
      "ok": true,
      "elapsed_ms": 12550,
      "chars": 8856,
      "memory_items": 129,
      "sections_created": 27
    },
    {
      "cycle": 5,
      "engine": "Auto (model-router)",
      "ok": false,
      "elapsed_ms": 1856,
      "chars": 9,
      "memory_items": 129,
      "sections_created": 27
    },
    {
      "cycle": 5,
      "engine": "Claude Foundry",
      "ok": false,
      "elapsed_ms": 1622,
      "chars": 9,
      "memory_items": 129,
      "sections_created": 27
    },
    {
      "cycle": 5,
      "engine": "GPT-Pro",
      "ok": false,
      "elapsed_ms": 45896,
      "chars": 25,
      "memory_items": 129,
      "sections_created": 27
    },
    {
      "cycle": 6,
      "engine": "Codex",
      "ok": true,
      "elapsed_ms": 13762,
      "chars": 9332,
      "memory_items": 144,
      "sections_created": 27
    },
    {
      "cycle": 6,
      "engine": "Auto (model-router)",
      "ok": false,
      "elapsed_ms": 2797,
      "chars": 9,
      "memory_items": 144,
      "sections_created": 27
    },
    {
      "cycle": 6,
      "engine": "Claude Foundry",
      "ok": false,
      "elapsed_ms": 1505,
      "chars": 9,
      "memory_items": 144,
      "sections_created": 27
    },
    {
      "cycle": 6,
      "engine": "GPT-Pro",
      "ok": false,
      "elapsed_ms": 45732,
      "chars": 25,
      "memory_items": 144,
      "sections_created": 27
    },
    {
      "cycle": 7,
      "engine": "Codex",
      "ok": true,
      "elapsed_ms": 13808,
      "chars": 9317,
      "memory_items": 147,
      "sections_created": 27
    },
    {
      "cycle": 7,
      "engine": "Auto (model-router)",
      "ok": false,
      "elapsed_ms": 2157,
      "chars": 9,
      "memory_items": 147,
      "sections_created": 27
    },
    {
      "cycle": 7,
      "engine": "Claude Foundry",
      "ok": false,
      "elapsed_ms": 1825,
      "chars": 9,
      "memory_items": 147,
      "sections_created": 27
    },
    {
      "cycle": 7,
      "engine": "GPT-Pro",
      "ok": false,
      "elapsed_ms": 45735,
      "chars": 25,
      "memory_items": 147,
      "sections_created": 27
    },
    {
      "cycle": 8,
      "engine": "Codex",
      "ok": true,
      "elapsed_ms": 14183,
      "chars": 9420,
      "memory_items": 150,
      "sections_created": 27
    },
    {
      "cycle": 8,
      "engine": "Auto (model-router)",
      "ok": false,
      "elapsed_ms": 1800,
      "chars": 9,
      "memory_items": 150,
      "sections_created": 27
    },
    {
      "cycle": 8,
      "engine": "Claude Foundry",
      "ok": false,
      "elapsed_ms": 1905,
      "chars": 9,
      "memory_items": 150,
      "sections_created": 27
    },
    {
      "cycle": 8,
      "engine": "GPT-Pro",
      "ok": false,
      "elapsed_ms": 45731,
      "chars": 25,
      "memory_items": 150,
      "sections_created": 27
    },
    {
      "cycle": 9,
      "engine": "Codex",
      "ok": true,
      "elapsed_ms": 14796,
      "chars": 9586,
      "memory_items": 161,
      "sections_created": 27
    },
    {
      "cycle": 9,
      "engine": "Auto (model-router)",
      "ok": false,
      "elapsed_ms": 2158,
      "chars": 9,
      "memory_items": 161,
      "sections_created": 27
    },
    {
      "cycle": 9,
      "engine": "Claude Foundry",
      "ok": false,
      "elapsed_ms": 1539,
      "chars": 9,
      "memory_items": 161,
      "sections_created": 27
    },
    {
      "cycle": 9,
      "engine": "GPT-Pro",
      "ok": false,
      "elapsed_ms": 45774,
      "chars": 25,
      "memory_items": 161,
      "sections_created": 27
    },
    {
      "cycle": 10,
      "engine": "Codex",
      "ok": true,
      "elapsed_ms": 13459,
      "chars": 9557,
      "memory_items": 166,
      "sections_created": 27
    },
    {
      "cycle": 10,
      "engine": "Auto (model-router)",
      "ok": false,
      "elapsed_ms": 2248,
      "chars": 9,
      "memory_items": 166,
      "sections_created": 27
    },
    {
      "cycle": 10,
      "engine": "Claude Foundry",
      "ok": false,
      "elapsed_ms": 1930,
      "chars": 9,
      "memory_items": 166,
      "sections_created": 27
    },
    {
      "cycle": 10,
      "engine": "GPT-Pro",
      "ok": false,
      "elapsed_ms": 45874,
      "chars": 25,
      "memory_items": 166,
      "sections_created": 27
    },
    {
      "cycle": 11,
      "engine": "Codex",
      "ok": true,
      "elapsed_ms": 13764,
      "chars": 9561,
      "memory_items": 168,
      "sections_created": 27
    },
    {
      "cycle": 11,
      "engine": "Auto (model-router)",
      "ok": false,
      "elapsed_ms": 2094,
      "chars": 9,
      "memory_items": 168,
      "sections_created": 27
    },
    {
      "cycle": 11,
      "engine": "Claude Foundry",
      "ok": false,
      "elapsed_ms": 1469,
      "chars": 9,
      "memory_items": 168,
      "sections_created": 27
    },
    {
      "cycle": 11,
      "engine": "GPT-Pro",
      "ok": false,
      "elapsed_ms": 45757,
      "chars": 25,
      "memory_items": 168,
      "sections_created": 27
    }
  ]
}
```

## 20260620-073426 - generar-plantilla

```json
{
  "run_id": "20260620-073426",
  "target": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
  "display_target": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
  "level": "materia",
  "action": "generar-plantilla",
  "activity_number": 1,
  "generation_mode": "direct",
  "parent_scope_key": "",
  "child_level": "",
  "child_name": "",
  "child_preview": "",
  "engines": [
    "Codex"
  ],
  "agentic_patterns": [
    "planning-memory",
    "tool-using-workflow",
    "verification-validation",
    "collective-consensus"
  ],
  "tasks": [
    {
      "stage": "planificar",
      "role": "Planificador editorial",
      "mission": "descomponer el objetivo en plan ejecutable y criterios de aceptacion",
      "engine": "Codex"
    }
  ],
  "llm_results": [
    {
      "engine": "Codex",
      "ok": true,
      "error": "",
      "chars": 3994
    }
  ],
  "compile_results": [
    {
      "tex": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/reporte-derecho-a-la-seguridad-social-Actividad-1.tex",
      "ok": true,
      "returncode": 0,
      "stdout_tail": "Initial Win CP for (console input, console output, system): (CP1252, CP65001, CP1252)\nI changed them all to CP1252\nRc files read:\n  .latexmkrc\nLatexmk: This is Latexmk, John Collins, 15 June 2025. Version 4.87.\nLatexmk: Nothing to do for 'D:/Documentos/LaTEX/Template-Informe/UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/reporte-derecho-a-la-seguridad-social-Actividad-1.tex'.\nLatexmk: All targets (.build/latex/reporte-derecho-a-la-seguridad-social-Actividad-1.pdf) are up-to-date\n\nPDF final: D:\\Documentos\\LaTEX\\Template-Informe\\UnADM\\licenciatura-en-derecho-unadm\\derecho-a-la-seguridad-social-lde\\reporte-derecho-a-la-seguridad-social-Actividad-1.pdf\n",
      "stderr_tail": "Reverting Windows console CPs to (in,out) = (1252,65001)\n"
    },
    {
      "tex": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/presentacion-derecho-a-la-seguridad-social-Actividad-1.tex",
      "ok": false,
      "returncode": 124,
      "stdout_tail": "ex/latex/beamer\\beamerbasemodes.s\nty (C:\\Program Files\\MiKTeX\\tex/latex/etoolbox\\etoolbox.sty)\n(C:\\Users\\Asus TUF505\\AppData\\Roaming\\MiKTeX\\tex/latex/beamer\\beamerbasedecode.\nsty)) (C:\\Program Files\\MiKTeX\\tex/generic/iftex\\iftex.sty)\n(C:\\Users\\Asus TUF505\\AppData\\Roaming\\MiKTeX\\tex/latex/beamer\\beamerbaseoptions\n.sty (C:\\Program Files\\MiKTeX\\tex/latex/graphics\\keyval.sty))\n(C:\\Users\\Asus TUF505\\AppData\\Roaming\\MiKTeX\\tex/latex/geometry\\geometry.sty\n(C:\\Program Files\\MiKTeX\\tex/generic/iftex\\ifvtex.sty)\n(C:\\Users\\Asus TUF505\\AppData\\Roaming\\MiKTeX\\tex/latex/geometry\\geometry.cfg))\n(C:\\Program Files\\MiKTeX\\tex/latex/pgf/math\\pgfmath.sty\n(C:\\Program Files\\MiKTeX\\tex/latex/pgf/utilities\\pgfrcs.sty\n(C:\\Program Files\\MiKTeX\\tex/generic/pgf/utilities\\pgfutil-common.tex)\n(C:\\Program Files\\MiKTeX\\tex/generic/pgf/utilities\\pgfutil-latex.def)\n(C:\\Program Files\\MiKTeX\\tex/generic/pgf/utilities\\pgfrcs.code.tex\n(C:\\Program Files\\MiKTeX\\tex/generic/pgf\\pgf.revision.tex)))\n(C:\\Program Files\\MiKTeX\\tex/latex/pgf/utilities\\pgfkeys.sty\n(C:\\Program Files\\MiKTeX\\tex/generic/pgf/utilities\\pgfkeys.code.tex\n(C:\\Program Files\\MiKTeX\\tex/generic/pgf/utilities\\pgfkeyslibraryfiltered.code.\ntex))) (C:\\Program Files\\MiKTeX\\tex/generic/pgf/math\\pgfmath.code.tex\n(C:\\Program Files\\MiKTeX\\tex/generic/pgf/math\\pgfmathutil.code.tex)\n(C:\\Program Files\\MiKTeX\\tex/generic/pgf/math\\pgfmathparser.code.tex)\n(C:\\Program Files\\MiKTeX\\tex/generic/pgf/math\\pgfmathfunctions.code.tex)\n(C:\\Program Files\\MiKTeX\\tex/generic/pgf/math\\pgfmathfunctions.basic.code.tex)\n(C:\\Program Files\\MiKTeX\\tex/generic/pgf/math\\pgfmathfunctions.trigonometric.co\nde.tex)\n(C:\\Program Files\\MiKTeX\\tex/generic/pgf/math\\pgfmathfunctions.random.code.tex)\n\n(C:\\Program Files\\MiKTeX\\tex/generic/pgf/math\\pgfmathfunctions.comparison.code.\ntex)\n(C:\\Program Files\\MiKTeX\\tex/generic/pgf/math\\pgfmathfunctions.base.code.tex)\n(C:\\Program Files\\MiKTeX\\tex/generic/pgf/math\\pgfmathfunctions.round.code.tex)\n(C:\\Program Files\\MiKTeX\\tex/generic/pgf/math\\pgfmathfunctions.misc.code.tex)\n(C:\\Program Files\\MiKTeX\\tex/generic/pgf/math\\pgfmathfunctions.integerarithmeti\ncs.code.tex) (C:\\Program Files\\MiKTeX\\tex/generic/pgf/math\\pgfmathcalc.code.tex\n) (C:\\Program Files\\MiKTeX\\tex/generic/pgf/math\\pgfmathfloat.code.tex)))\n(C:\\Program Files\\MiKTeX\\tex/latex/base\\size11.clo)\n(C:\\Program Files\\MiKTeX\\tex/latex/pgf/basiclayer\\pgfcore.sty\n(C:\\Program Files\\MiKTeX\\tex/latex/graphics\\graphicx.sty\n(C:\\Program Files\\MiKTeX\\tex/latex/graphics\\graphics.sty\n(C:\\Program Files\\MiKTeX\\tex/latex/graphics\\trig.sty)\n(C:\\Program Files\\MiKTeX\\tex/latex/graphics-cfg\\graphics.cfg)\n(C:\\Program Files\\MiKTeX\\tex/latex/graphics-def\\pdftex.def)))\n(C:\\Program Files\\MiKTeX\\tex/latex/pgf/systemlayer\\pgfsys.sty\n(C:\\Program Files\\MiKTeX\\tex/generic/pgf/systemlayer\\pgfsys.code.tex\nTiempo de espera agotado tras 180s al compilar UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/presentacion-derecho-a-la-seguridad-social-Actividad-1.tex con latexmk-build.ps1.\n",
      "stderr_tail": "Latexmk: Missing input file 'presentacion-derecho-a-la-seguridad-social-Actividad-1.nav' message in .log file:\n  No file presentacion-derecho-a-la-seguridad-social-Actividad-1.nav.\nLatexmk: Using bibtex to make bibliography file(s).\n"
    }
  ],
  "materialization": {
    "enabled": true,
    "ok": true,
    "target_dir": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
    "artifacts": [
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/referencias-derecho-a-la-seguridad-social",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/planeaciones-derecho-a-la-seguridad-social",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/assets-derecho-a-la-seguridad-social",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/README.md",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/COMPILACION-derecho-a-la-seguridad-social.md",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/programa-analitico-derecho-a-la-seguridad-social.md",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/derecho-a-la-seguridad-social.bib",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/reporte-derecho-a-la-seguridad-social.tex",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/reporte-derecho-a-la-seguridad-social-Actividad-1.tex",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/informe-derecho-a-la-seguridad-social.tex",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/presentacion-derecho-a-la-seguridad-social.tex",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/presentacion-derecho-a-la-seguridad-social-Actividad-1.tex",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/estructura-aulatex.json"
    ],
    "notes": [
      "Materializado: UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/README.md",
      "Materializado: UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/COMPILACION-derecho-a-la-seguridad-social.md",
      "Materializado: UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/programa-analitico-derecho-a-la-seguridad-social.md",
      "Materializado: UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/derecho-a-la-seguridad-social.bib",
      "Materializado: UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/reporte-derecho-a-la-seguridad-social.tex",
      "Materializado: UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/reporte-derecho-a-la-seguridad-social-Actividad-1.tex",
      "Materializado: UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/informe-derecho-a-la-seguridad-social.tex",
      "Materializado: UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/presentacion-derecho-a-la-seguridad-social.tex",
      "Materializado: UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/presentacion-derecho-a-la-seguridad-social-Actividad-1.tex",
      "Materializado: UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/estructura-aulatex.json"
    ]
  },
  "consensus": {
    "consensus_score": 9.23,
    "passed": true,
    "criteria": {
      "identidad_institucional": true,
      "bibliografia": true,
      "trazabilidad": true,
      "compilacion": true,
      "riesgos": true
    },
    "role_scores": {
      "Planificador editorial": 8.6
    },
    "risks": [],
    "recommendations": [
      "Usar el reporte como retroalimentacion editorial aplicable al objetivo."
    ]
  },
  "workflow_events": [
    {
      "timestamp": "2026-06-20 07:34:26",
      "state": "initialized",
      "action": "init",
      "status": "ok",
      "detail": "AulaTeX workflow initialized"
    },
    {
      "timestamp": "2026-06-20 07:34:28",
      "state": "initialized",
      "action": "llm-start",
      "status": "ok",
      "detail": "planificar: Planificador editorial via Codex"
    },
    {
      "timestamp": "2026-06-20 07:34:38",
      "state": "initialized",
      "action": "llm-end",
      "status": "ok",
      "detail": "planificar: 3994 chars"
    },
    {
      "timestamp": "2026-06-20 07:34:38",
      "state": "planned",
      "action": "initialized->planned",
      "status": "ok",
      "detail": "plan editorial producido"
    },
    {
      "timestamp": "2026-06-20 07:34:38",
      "state": "planned",
      "action": "materialize-start",
      "status": "ok",
      "detail": "generar-plantilla materializara estructura canonica de archivos"
    },
    {
      "timestamp": "2026-06-20 07:34:38",
      "state": "planned",
      "action": "materialize-end",
      "status": "ok",
      "detail": "13 artefactos procesados"
    },
    {
      "timestamp": "2026-06-20 07:34:38",
      "state": "planned",
      "action": "tool-select",
      "status": "ok",
      "detail": "latexmk-build.ps1 seleccionado para compilar objetivos canonicos"
    },
    {
      "timestamp": "2026-06-20 07:34:40",
      "state": "planned",
      "action": "tool-result",
      "status": "ok",
      "detail": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/reporte-derecho-a-la-seguridad-social-Actividad-1.tex rc=0"
    },
    {
      "timestamp": "2026-06-20 07:37:40",
      "state": "planned",
      "action": "tool-result",
      "status": "error",
      "detail": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/presentacion-derecho-a-la-seguridad-social-Actividad-1.tex rc=124"
    },
    {
      "timestamp": "2026-06-20 07:37:40",
      "state": "planned",
      "action": "consensus",
      "status": "ok",
      "detail": "score=9.23"
    },
    {
      "timestamp": "2026-06-20 07:37:40",
      "state": "evaluated",
      "action": "planned->evaluated",
      "status": "ok",
      "detail": "validacion y consenso completados"
    },
    {
      "timestamp": "2026-06-20 07:37:40",
      "state": "finalized",
      "action": "evaluated->finalized",
      "status": "ok",
      "detail": "ciclo agentico cerrado"
    }
  ]
}
```

## 20260620-074947 - generar-plantilla

```json
{
  "run_id": "20260620-074947",
  "target": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
  "display_target": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
  "level": "materia",
  "action": "generar-plantilla",
  "activity_number": 1,
  "generation_mode": "direct",
  "parent_scope_key": "",
  "child_level": "",
  "child_name": "",
  "child_preview": "",
  "engines": [
    "Codex"
  ],
  "agentic_patterns": [
    "planning-memory",
    "tool-using-workflow",
    "verification-validation",
    "collective-consensus"
  ],
  "tasks": [
    {
      "stage": "planificar",
      "role": "Planificador editorial",
      "mission": "descomponer el objetivo en plan ejecutable y criterios de aceptacion",
      "engine": "Codex"
    }
  ],
  "llm_results": [
    {
      "engine": "Codex",
      "ok": true,
      "error": "",
      "chars": 3801
    }
  ],
  "compile_results": [
    {
      "tex": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/reporte-derecho-a-la-seguridad-social-Actividad-1.tex",
      "ok": false,
      "returncode": 124,
      "stdout_tail": "n 3.141592653-2.6-1.40.27 (MiKTeX 25.4) (preloaded format=pdflatex.fmt)\n restricted \\write18 enabled.\nentering extended mode\n\n(D:/Documentos/LaTEX/Template-Informe/UnADM/licenciatura-en-derecho-unadm/derec\nho-a-la-seguridad-social-lde/reporte-derecho-a-la-seguridad-social-Actividad-1.\ntex\nLaTeX2e <2025-06-01> patch level 1\nL3 programming layer <2025-07-20>\n(C:\\Program Files\\MiKTeX\\tex/latex/base\\article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(C:\\Program Files\\MiKTeX\\tex/latex/base\\size10.clo))\n(D:/Documentos/LaTEX/Template-Informe/base/Plantilla-Informe\\template.tex\n(D:/Documentos/LaTEX/Template-Informe/base/Plantilla-Informe\\src/defs.tex\n(C:\\Program Files\\MiKTeX\\tex/latex/xcolor\\xcolor.sty\n(C:\\Program Files\\MiKTeX\\tex/latex/graphics-cfg\\color.cfg)\n(C:\\Program Files\\MiKTeX\\tex/latex/graphics-def\\pdftex.def)\n(C:\\Program Files\\MiKTeX\\tex/latex/graphics\\mathcolor.ltx))\n(C:\\Program Files\\MiKTeX\\tex/latex/graphics\\dvipsnam.def)\n(C:\\Users\\Asus TUF505\\AppData\\Roaming\\MiKTeX\\tex/latex/colortbl\\colortbl.sty\n(C:\\Program Files\\MiKTeX\\tex/latex/tools\\array.sty)))\n(D:/Documentos/LaTEX/Template-Informe/base/Plantilla-Informe\\src/config.tex)\n(D:/Documentos/LaTEX/Template-Informe/base/Plantilla-Informe\\src/env/imports.te\nx (C:\\Program Files\\MiKTeX\\tex/generic/iftex\\iftex.sty)\n(C:\\Program Files\\MiKTeX\\tex/latex/base\\ifthen.sty)\n(C:\\Users\\Asus TUF505\\AppData\\Roaming\\MiKTeX\\tex/latex/tracklang\\tracklang.sty\n(C:\\Users\\Asus TUF505\\AppData\\Roaming\\MiKTeX\\tex/generic/tracklang\\tracklang.te\nx))\n(C:\\Users\\Asus TUF505\\AppData\\Roaming\\MiKTeX\\tex/latex/tocbibind\\tocbibind.sty\n\nPackage tocbibind Note: Using section or other style headings.\n\n) (C:\\Users\\Asus TUF505\\AppData\\Roaming\\MiKTeX\\tex/latex/natbib\\natbib.sty)\n(C:\\Program Files\\MiKTeX\\tex/generic/babel\\babel.sty\n(C:\\Program Files\\MiKTeX\\tex/generic/babel\\txtbabel.def)\n(C:\\Users\\Asus TUF505\\AppData\\Roaming\\MiKTeX\\tex/latex/babel-spanish\\spanish.ld\nf (C:\\Program Files\\MiKTeX\\tex/generic/babel/locale/es\\babel-spanish.tex)))\n(C:\\Users\\Asus TUF505\\AppData\\Roaming\\MiKTeX\\tex/latex/sectsty\\sectsty.sty)\n(C:\\Program Files\\MiKTeX\\tex/latex/base\\inputenc.sty)\n(C:\\Program Files\\MiKTeX\\tex/latex/amsmath\\amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(C:\\Program Files\\MiKTeX\\tex/latex/amsmath\\amstext.sty\n(C:\\Program Files\\MiKTeX\\tex/latex/amsmath\\amsgen.sty))\n(C:\\Program Files\\MiKTeX\\tex/latex/amsmath\\amsbsy.sty)\n(C:\\Program Files\\MiKTeX\\tex/latex/amsmath\\amsopn.sty))\n(C:\\Users\\Asus TUF505\\AppData\\Roaming\\MiKTeX\\tex/latex/koma-script\\scrextend.st\ny\n(C:\\Users\\Asus TUF505\\AppData\\Roaming\\MiKTeX\\tex/latex/koma-script\\scrkbase.sty\n(C:\\Users\\Asus TUF505\\AppData\\Roaming\\MiKTeX\\tex/latex/koma-script\\scrbase.sty\n(C:\\Users\\Asus TUF505\\AppData\\Roaming\\MiKTeX\\tex/latex/koma-script\\scrlfile.sty\n\nTiempo de espera agotado tras 180s al compilar UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/reporte-derecho-a-la-seguridad-social-Actividad-1.tex con latexmk-build.ps1.\n",
      "stderr_tail": "Latexmk: Using bibtex to make bibliography file(s).\nLatexmk: Missing input file 'reporte-derecho-a-la-seguridad-social-Actividad-1.toc' message in .log file:\n  No file reporte-derecho-a-la-seguridad-social-Actividad-1.toc.\nLatexmk: Missing bbl file '.build/latex/aux/reporte-derecho-a-la-seguridad-social-Actividad-1.bbl' in following:\n No file reporte-derecho-a-la-seguridad-social-Actividad-1.bbl.\nLatexmk: Using bibtex to make bibliography file(s).\n"
    },
    {
      "tex": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/presentacion-derecho-a-la-seguridad-social-Actividad-1.tex",
      "ok": false,
      "returncode": 4294967295,
      "stdout_tail": "d:\n  .build/latex/aux/presentacion-derecho-a-la-seguridad-social-Actividad-1.aux\n  .build/latex/aux/presentacion-derecho-a-la-seguridad-social-Actividad-1.out\n\n------------\nRun number 2 of rule 'pdflatex'\n------------\n------------\nRunning 'pdflatex -halt-on-error -interaction=nonstopmode -file-line-error  -interaction=nonstopmode -file-line-error -recorder -output-directory=\".build/latex/aux\"  \"D:/Documentos/LaTEX/Template-Informe/UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/presentacion-derecho-a-la-seguridad-social-Actividad-1.tex\"'\n------------\nThis is pdfTeX, Version 3.141592653-2.6-1.40.27 (MiKTeX 25.4) (preloaded format=pdflatex.fmt)\n restricted \\write18 enabled.\nentering extended mode\n\n(D:/Documentos/LaTEX/Template-Informe/UnADM/licenciatura-en-derecho-unadm/derec\nho-a-la-seguridad-social-lde/presentacion-derecho-a-la-seguridad-social-Activid\nad-1.tex\nLaTeX2e <2025-06-01> patch level 1\nL3 programming layer <2025-07-20>\n(C:\\Program Files\\MiKTeX\\tex/latex/base\\article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(C:\\Program Files\\MiKTeX\\tex/latex/base\\size10.clo))\n(C:\\Users\\Asus TUF505\\AppData\\Roaming\\MiKTeX\\tex/latex/geometry\\geometry.sty\n(C:\\Program Files\\MiKTeX\\tex/latex/graphics\\keyval.sty)\n(C:\\Program Files\\MiKTeX\\tex/generic/iftex\\ifvtex.sty\n(C:\\Program Files\\MiKTeX\\tex/generic/iftex\\iftex.sty))\n(C:\\Users\\Asus TUF505\\AppData\\Roaming\\MiKTeX\\tex/latex/geometry\\geometry.cfg))\n(C:\\Program Files\\MiKTeX\\tex/latex/base\\inputenc.sty)\n(C:\\Program Files\\MiKTeX\\tex/latex/base\\fontenc.sty)\n(C:\\Program Files\\MiKTeX\\tex/generic/babel\\babel.sty\n(C:\\Program Files\\MiKTeX\\tex/generic/babel\\txtbabel.def)\n*************************************\n* Local config file bblopts.cfg used\n*\n(C:\\Program Files\\MiKTeX\\tex/latex/arabi\\bblopts.cfg)\n(C:\\Users\\Asus TUF505\\AppData\\Roaming\\MiKTeX\\tex/latex/babel-spanish\\spanish.ld\nf (C:\\Program Files\\MiKTeX\\tex/generic/babel/locale/es\\babel-spanish.tex)))\n(C:\\Users\\Asus TUF505\\AppData\\Roaming\\MiKTeX\\tex/latex/psnfss\\helvet.sty)\n(C:\\Program Files\\MiKTeX\\tex/latex/xcolor\\xcolor.sty\n(C:\\Program Files\\MiKTeX\\tex/latex/graphics-cfg\\color.cfg)\n(C:\\Program Files\\MiKTeX\\tex/latex/graphics-def\\pdftex.def)\n(C:\\Program Files\\MiKTeX\\tex/latex/graphics\\mathcolor.ltx))\n(C:\\Users\\Asus TUF505\\AppData\\Roaming\\MiKTeX\\tex/latex/colortbl\\colortbl.sty\n(C:\\Program Files\\MiKTeX\\tex/latex/tools\\array.sty))\n(C:\\Program Files\\MiKTeX\\tex/latex/graphics\\graphicx.sty\n(C:\\Program Files\\MiKTeX\\tex/latex/graphics\\graphics.sty\n(C:\\Program Files\\MiKTeX\\tex/latex/graphics\\trig.sty)\n(C:\\Program Files\\MiKTeX\\tex/latex/graphics-cfg\\graphics.cfg)))\n(C:\\Program Files\\MiKTeX\\tex/latex/ragged2e\\ragged2e.sty)\n(C:\\Program Files\\MiKTeX\\tex/latex/hyperref\\hyperref.sty\n(C:\\Users\\Asus TUF505\\AppData\\Roaming\\MiKTeX\\tex/latex/kvsetkeys\\kvsetkeys.sty)\n\n(C:\\Users\\Asus TUF505\\AppData\\Roaming\\MiKTeX\\tex/generic/kvdefinekeys\\kvdefinek\neys.sty)\n(C:\\Users\\Asus TUF505\\AppData\\Roaming\\MiKTeX\\tex/generic/pdfescape\\pdfescape.st\ny",
      "stderr_tail": "Latexmk: Using bibtex to make bibliography file(s).\nLatexmk: Using bibtex to make bibliography file(s).\n"
    }
  ],
  "materialization": {
    "enabled": true,
    "ok": true,
    "target_dir": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
    "artifacts": [
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/referencias-derecho-a-la-seguridad-social",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/planeaciones-derecho-a-la-seguridad-social",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/assets-derecho-a-la-seguridad-social",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/README.md",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/COMPILACION-derecho-a-la-seguridad-social.md",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/programa-analitico-derecho-a-la-seguridad-social.md",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/derecho-a-la-seguridad-social.bib",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/reporte-derecho-a-la-seguridad-social.tex",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/reporte-derecho-a-la-seguridad-social-Actividad-1.tex",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/informe-derecho-a-la-seguridad-social.tex",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/presentacion-derecho-a-la-seguridad-social.tex",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/presentacion-derecho-a-la-seguridad-social-Actividad-1.tex",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/estructura-aulatex.json"
    ],
    "notes": [
      "Materializado: UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/README.md",
      "Materializado: UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/COMPILACION-derecho-a-la-seguridad-social.md",
      "Materializado: UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/programa-analitico-derecho-a-la-seguridad-social.md",
      "Materializado: UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/derecho-a-la-seguridad-social.bib",
      "Materializado: UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/reporte-derecho-a-la-seguridad-social.tex",
      "Materializado: UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/reporte-derecho-a-la-seguridad-social-Actividad-1.tex",
      "Materializado: UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/informe-derecho-a-la-seguridad-social.tex",
      "Materializado: UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/presentacion-derecho-a-la-seguridad-social.tex",
      "Materializado: UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/presentacion-derecho-a-la-seguridad-social-Actividad-1.tex",
      "Materializado: UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/estructura-aulatex.json"
    ]
  },
  "consensus": {
    "consensus_score": 8.33,
    "passed": false,
    "criteria": {
      "identidad_institucional": true,
      "bibliografia": true,
      "trazabilidad": true,
      "compilacion": true,
      "riesgos": false
    },
    "role_scores": {
      "Planificador editorial": 8.6
    },
    "risks": [
      "Criterio sin cobertura: riesgos"
    ],
    "recommendations": [
      "Usar el reporte como retroalimentacion editorial aplicable al objetivo."
    ]
  },
  "workflow_events": [
    {
      "timestamp": "2026-06-20 07:49:47",
      "state": "initialized",
      "action": "init",
      "status": "ok",
      "detail": "AulaTeX workflow initialized"
    },
    {
      "timestamp": "2026-06-20 07:49:48",
      "state": "initialized",
      "action": "llm-start",
      "status": "ok",
      "detail": "planificar: Planificador editorial via Codex"
    },
    {
      "timestamp": "2026-06-20 07:49:57",
      "state": "initialized",
      "action": "llm-end",
      "status": "ok",
      "detail": "planificar: 3801 chars"
    },
    {
      "timestamp": "2026-06-20 07:49:57",
      "state": "planned",
      "action": "initialized->planned",
      "status": "ok",
      "detail": "plan editorial producido"
    },
    {
      "timestamp": "2026-06-20 07:49:57",
      "state": "planned",
      "action": "materialize-start",
      "status": "ok",
      "detail": "generar-plantilla materializara estructura canonica de archivos"
    },
    {
      "timestamp": "2026-06-20 07:49:57",
      "state": "planned",
      "action": "materialize-end",
      "status": "ok",
      "detail": "13 artefactos procesados"
    },
    {
      "timestamp": "2026-06-20 07:49:57",
      "state": "planned",
      "action": "tool-select",
      "status": "ok",
      "detail": "latexmk-build.ps1 seleccionado para compilar objetivos canonicos"
    },
    {
      "timestamp": "2026-06-20 07:52:58",
      "state": "planned",
      "action": "tool-result",
      "status": "error",
      "detail": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/reporte-derecho-a-la-seguridad-social-Actividad-1.tex rc=124"
    },
    {
      "timestamp": "2026-06-20 07:54:00",
      "state": "planned",
      "action": "tool-result",
      "status": "error",
      "detail": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/presentacion-derecho-a-la-seguridad-social-Actividad-1.tex rc=4294967295"
    },
    {
      "timestamp": "2026-06-20 07:54:00",
      "state": "planned",
      "action": "consensus",
      "status": "warn",
      "detail": "score=8.33"
    },
    {
      "timestamp": "2026-06-20 07:54:00",
      "state": "evaluated",
      "action": "planned->evaluated",
      "status": "ok",
      "detail": "validacion y consenso completados"
    },
    {
      "timestamp": "2026-06-20 07:54:00",
      "state": "finalized",
      "action": "evaluated->finalized",
      "status": "ok",
      "detail": "ciclo agentico cerrado"
    }
  ]
}
```

## 20260620-080525 - generar-plantilla

```json
{
  "run_id": "20260620-080525",
  "target": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
  "display_target": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
  "level": "materia",
  "action": "generar-plantilla",
  "activity_number": 1,
  "generation_mode": "direct",
  "parent_scope_key": "",
  "child_level": "",
  "child_name": "",
  "child_preview": "",
  "engines": [
    "Codex"
  ],
  "agentic_patterns": [
    "planning-memory",
    "tool-using-workflow",
    "verification-validation",
    "collective-consensus"
  ],
  "tasks": [
    {
      "stage": "planificar",
      "role": "Planificador editorial",
      "mission": "descomponer el objetivo en plan ejecutable y criterios de aceptacion",
      "engine": "Codex"
    }
  ],
  "llm_results": [
    {
      "engine": "Codex",
      "ok": true,
      "error": "",
      "chars": 4413
    }
  ],
  "compile_results": [
    {
      "tex": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/reporte-derecho-a-la-seguridad-social-Actividad-1.tex",
      "ok": false,
      "returncode": 124,
      "stdout_tail": "s\\MiKTeX\\tex/latex/tools\\array.sty))\n(C:\\Users\\Asus TUF505\\AppData\\Roaming\\MiKTeX\\tex/latex/booktabs\\booktabs.sty)\n(C:\\Program Files\\MiKTeX\\tex/latex/tools\\longtable.sty)\n(C:\\Program Files\\MiKTeX\\tex/latex/hyperref\\hyperref.sty\n(C:\\Users\\Asus TUF505\\AppData\\Roaming\\MiKTeX\\tex/latex/kvsetkeys\\kvsetkeys.sty)\n\n(C:\\Users\\Asus TUF505\\AppData\\Roaming\\MiKTeX\\tex/generic/kvdefinekeys\\kvdefinek\neys.sty)\n(C:\\Users\\Asus TUF505\\AppData\\Roaming\\MiKTeX\\tex/generic/pdfescape\\pdfescape.st\ny (C:\\Users\\Asus TUF505\\AppData\\Roaming\\MiKTeX\\tex/generic/ltxcmds\\ltxcmds.sty)\n (C:\\Program Files\\MiKTeX\\tex/generic/pdftexcmds\\pdftexcmds.sty\n(C:\\Users\\Asus TUF505\\AppData\\Roaming\\MiKTeX\\tex/generic/infwarerr\\infwarerr.st\ny))) (C:\\Users\\Asus TUF505\\AppData\\Roaming\\MiKTeX\\tex/latex/hycolor\\hycolor.sty\n) (C:\\Program Files\\MiKTeX\\tex/latex/hyperref\\nameref.sty\n(C:\\Users\\Asus TUF505\\AppData\\Roaming\\MiKTeX\\tex/latex/refcount\\refcount.sty)\n(C:\\Users\\Asus TUF505\\AppData\\Roaming\\MiKTeX\\tex/generic/gettitlestring\\gettitl\nestring.sty\n(C:\\Users\\Asus TUF505\\AppData\\Roaming\\MiKTeX\\tex/latex/kvoptions\\kvoptions.sty)\n)) (C:\\Program Files\\MiKTeX\\tex/latex/etoolbox\\etoolbox.sty)\n(C:\\Users\\Asus TUF505\\AppData\\Roaming\\MiKTeX\\tex/generic/stringenc\\stringenc.st\ny) (C:\\Program Files\\MiKTeX\\tex/latex/hyperref\\pd1enc.def)\n(C:\\Users\\Asus TUF505\\AppData\\Roaming\\MiKTeX\\tex/generic/intcalc\\intcalc.sty)\n(C:\\Program Files\\MiKTeX\\tex/latex/hyperref\\puenc.def)\n(C:\\Program Files\\MiKTeX\\tex/latex/url\\url.sty)\n(C:\\Users\\Asus TUF505\\AppData\\Roaming\\MiKTeX\\tex/generic/bitset\\bitset.sty\n(C:\\Users\\Asus TUF505\\AppData\\Roaming\\MiKTeX\\tex/generic/bigintcalc\\bigintcalc.\nsty))) (C:\\Program Files\\MiKTeX\\tex/latex/hyperref\\hpdftex.def\n(C:\\Users\\Asus TUF505\\AppData\\Roaming\\MiKTeX\\tex/latex/rerunfilecheck\\rerunfile\ncheck.sty\n(C:\\Users\\Asus TUF505\\AppData\\Roaming\\MiKTeX\\tex/generic/uniquecounter\\uniqueco\nunter.sty)))\n(C:\\Users\\Asus TUF505\\AppData\\Roaming\\MiKTeX\\tex/latex/natbib\\natbib.sty)\n(C:\\Users\\Asus TUF505\\AppData\\Roaming\\MiKTeX\\tex/latex/psnfss\\t1phv.fd)\n(C:\\Program Files\\MiKTeX\\tex/latex/l3backend\\l3backend-pdftex.def)\n(D:\\Documentos\\LaTEX\\Template-Informe\\.build\\latex\\aux\\reporte-derecho-a-la-seg\nuridad-social-Actividad-1.aux)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(C:\\Program Files\\MiKTeX\\tex/context/base/mkii\\supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (C:\\Program Files\\MiKTeX\\tex/latex/epstopdf-pkg\\epstopdf-base.sty\n(C:\\Users\\Asus TUF505\\AppData\\Roaming\\MiKTeX\\tex/latex/grfext\\grfext.sty)\n(C:\\Program Files\\MiKTeX\\tex/latex/00miktex\\epstopdf-sys.cfg))\n(D:\\Documentos\\LaTEX\\Template-Informe\\.build\\latex\\aux\\reporte-derecho-a-la-seg\nuridad-social-Actividad-1.out)\n(D:\\Documentos\\LaTEX\\Template-Informe\\.build\\latex\\aux\\reporte-derecho-a-la-seg\nuridad-social-Actividad-1.out)\nTiempo de espera agotado tras 180s al compilar UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/reporte-derecho-a-la-seguridad-social-Actividad-1.tex con latexmk-build.ps1.\n",
      "stderr_tail": "Latexmk: Using bibtex to make bibliography file(s).\nLatexmk: Missing input file 'reporte-derecho-a-la-seguridad-social-Actividad-1.toc' message in .log file:\n  No file reporte-derecho-a-la-seguridad-social-Actividad-1.toc.\nLatexmk: Missing bbl file '.build/latex/aux/reporte-derecho-a-la-seguridad-social-Actividad-1.bbl' in following:\n No file reporte-derecho-a-la-seguridad-social-Actividad-1.bbl.\nLatexmk: Using bibtex to make bibliography file(s).\nLatexmk: Using bibtex to make bibliography file(s).\nLatexmk: Using bibtex to make bibliography file(s).\n"
    },
    {
      "tex": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/presentacion-derecho-a-la-seguridad-social-Actividad-1.tex",
      "ok": true,
      "returncode": 0,
      "stdout_tail": "ackend\\l3backend-pdftex.def)\n(D:\\Documentos\\LaTEX\\Template-Informe\\.build\\latex\\aux\\presentacion-derecho-a-l\na-seguridad-social-Actividad-1.aux)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(C:\\Program Files\\MiKTeX\\tex/context/base/mkii\\supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (C:\\Program Files\\MiKTeX\\tex/latex/epstopdf-pkg\\epstopdf-base.sty\n(C:\\Program Files\\MiKTeX\\tex/latex/00miktex\\epstopdf-sys.cfg))\n(D:\\Documentos\\LaTEX\\Template-Informe\\.build\\latex\\aux\\presentacion-derecho-a-l\na-seguridad-social-Actividad-1.out)\n(D:\\Documentos\\LaTEX\\Template-Informe\\.build\\latex\\aux\\presentacion-derecho-a-l\na-seguridad-social-Actividad-1.out)\n\npdfTeX warning: pdflatex (file D:/Documentos/LaTEX/Template-Informe/base/Planti\nlla-Informe/img/departamentos/UnADM.pdf): PDF inclusion: found PDF version <1.7\n>, but at most version <1.5> allowed\n\n[1{C:/Users/Asus TUF505/AppData/Local/MiKTeX/fonts/map/pdftex/pdftex.map}{C:/Pr\nogram Files/MiKTeX/fonts/enc/dvips/base/8r.enc} <D:/Documentos/LaTEX/Template-I\nnforme/base/Plantilla-Informe/img/departamentos/UnADM.pdf>]\nUnderfull \\hbox (badness 10000) in paragraph at lines 90--91\n\n\n[2]\nUnderfull \\hbox (badness 10000) in paragraph at lines 99--100\n\n\n[3]\nUnderfull \\hbox (badness 10000) in paragraph at lines 109--110\n\n\n[4]\nUnderfull \\hbox (badness 10000) in paragraph at lines 118--119\n\n\n[5]\nUnderfull \\hbox (badness 10000) in paragraph at lines 124--125\n\n\n[6]\n(D:\\Documentos\\LaTEX\\Template-Informe\\.build\\latex\\aux\\presentacion-derecho-a-l\na-seguridad-social-Actividad-1.aux) )\n(see the transcript file for additional information) <C:\\Users\\Asus TUF505\\AppD\nata\\Local\\MiKTeX\\fonts/pk/ljfour/jknappen/ec/dpi600\\ectt1440.pk><C:/Program Fil\nes/MiKTeX/fonts/type1/urw/helvetic/uhvb8a.pfb><C:/Program Files/MiKTeX/fonts/ty\npe1/urw/helvetic/uhvr8a.pfb>\nOutput written on D:\\Documentos\\LaTEX\\Template-Informe\\.build\\latex\\aux\\present\nacion-derecho-a-la-seguridad-social-Actividad-1.pdf (6 pages, 59722 bytes).\nTranscript written on D:\\Documentos\\LaTEX\\Template-Informe\\.build\\latex\\aux\\pre\nsentacion-derecho-a-la-seguridad-social-Actividad-1.log.\nLatexmk: Moving '.build/latex/aux/presentacion-derecho-a-la-seguridad-social-Actividad-1.pdf' to '.build/latex/presentacion-derecho-a-la-seguridad-social-Actividad-1.pdf'\nLatexmk: Getting log file '.build/latex/aux/presentacion-derecho-a-la-seguridad-social-Actividad-1.log'\nLatexmk: Examining '.build/latex/aux/presentacion-derecho-a-la-seguridad-social-Actividad-1.fls'\nLatexmk: Examining '.build/latex/aux/presentacion-derecho-a-la-seguridad-social-Actividad-1.log'\nLatexmk: Log file says output to '.build/latex/aux/presentacion-derecho-a-la-seguridad-social-Actividad-1.pdf'\nLatexmk: All targets (.build/latex/presentacion-derecho-a-la-seguridad-social-Actividad-1.pdf) are up-to-date\n\nPDF final: D:\\Documentos\\LaTEX\\Template-Informe\\UnADM\\licenciatura-en-derecho-unadm\\derecho-a-la-seguridad-social-lde\\presentacion-derecho-a-la-seguridad-social-Actividad-1.pdf\n",
      "stderr_tail": "Latexmk: Using bibtex to make bibliography file(s).\nLatexmk: Using bibtex to make bibliography file(s).\nLatexmk: Using bibtex to make bibliography file(s).\nReverting Windows console CPs to (in,out) = (1252,65001)\n"
    }
  ],
  "materialization": {
    "enabled": true,
    "ok": true,
    "target_dir": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
    "artifacts": [
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/referencias-derecho-a-la-seguridad-social",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/planeaciones-derecho-a-la-seguridad-social",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/assets-derecho-a-la-seguridad-social",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/README.md",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/COMPILACION-derecho-a-la-seguridad-social.md",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/programa-analitico-derecho-a-la-seguridad-social.md",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/derecho-a-la-seguridad-social.bib",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/reporte-derecho-a-la-seguridad-social.tex",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/reporte-derecho-a-la-seguridad-social-Actividad-1.tex",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/informe-derecho-a-la-seguridad-social.tex",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/presentacion-derecho-a-la-seguridad-social.tex",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/presentacion-derecho-a-la-seguridad-social-Actividad-1.tex",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/estructura-aulatex.json"
    ],
    "notes": [
      "Materializado: UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/README.md",
      "Materializado: UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/COMPILACION-derecho-a-la-seguridad-social.md",
      "Materializado: UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/programa-analitico-derecho-a-la-seguridad-social.md",
      "Materializado: UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/derecho-a-la-seguridad-social.bib",
      "Materializado: UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/reporte-derecho-a-la-seguridad-social.tex",
      "Materializado: UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/reporte-derecho-a-la-seguridad-social-Actividad-1.tex",
      "Materializado: UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/informe-derecho-a-la-seguridad-social.tex",
      "Materializado: UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/presentacion-derecho-a-la-seguridad-social.tex",
      "Materializado: UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/presentacion-derecho-a-la-seguridad-social-Actividad-1.tex",
      "Materializado: UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/estructura-aulatex.json"
    ]
  },
  "consensus": {
    "consensus_score": 8.79,
    "passed": true,
    "criteria": {
      "identidad_institucional": true,
      "bibliografia": true,
      "trazabilidad": true,
      "compilacion": true,
      "riesgos": true
    },
    "role_scores": {
      "Planificador editorial": 7.8
    },
    "risks": [],
    "recommendations": [
      "Usar el reporte como retroalimentacion editorial aplicable al objetivo."
    ]
  },
  "workflow_events": [
    {
      "timestamp": "2026-06-20 08:05:25",
      "state": "initialized",
      "action": "init",
      "status": "ok",
      "detail": "AulaTeX workflow initialized"
    },
    {
      "timestamp": "2026-06-20 08:05:26",
      "state": "initialized",
      "action": "llm-start",
      "status": "ok",
      "detail": "planificar: Planificador editorial via Codex"
    },
    {
      "timestamp": "2026-06-20 08:05:37",
      "state": "initialized",
      "action": "llm-end",
      "status": "ok",
      "detail": "planificar: 4413 chars"
    },
    {
      "timestamp": "2026-06-20 08:05:37",
      "state": "planned",
      "action": "initialized->planned",
      "status": "ok",
      "detail": "plan editorial producido"
    },
    {
      "timestamp": "2026-06-20 08:05:37",
      "state": "planned",
      "action": "materialize-start",
      "status": "ok",
      "detail": "generar-plantilla materializara estructura canonica de archivos"
    },
    {
      "timestamp": "2026-06-20 08:05:37",
      "state": "planned",
      "action": "materialize-end",
      "status": "ok",
      "detail": "13 artefactos procesados"
    },
    {
      "timestamp": "2026-06-20 08:05:37",
      "state": "planned",
      "action": "tool-select",
      "status": "ok",
      "detail": "latexmk-build.ps1 seleccionado para compilar objetivos canonicos"
    },
    {
      "timestamp": "2026-06-20 08:08:38",
      "state": "planned",
      "action": "tool-result",
      "status": "error",
      "detail": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/reporte-derecho-a-la-seguridad-social-Actividad-1.tex rc=124"
    },
    {
      "timestamp": "2026-06-20 08:10:00",
      "state": "planned",
      "action": "tool-result",
      "status": "ok",
      "detail": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/presentacion-derecho-a-la-seguridad-social-Actividad-1.tex rc=0"
    },
    {
      "timestamp": "2026-06-20 08:10:00",
      "state": "planned",
      "action": "consensus",
      "status": "ok",
      "detail": "score=8.79"
    },
    {
      "timestamp": "2026-06-20 08:10:00",
      "state": "evaluated",
      "action": "planned->evaluated",
      "status": "ok",
      "detail": "validacion y consenso completados"
    },
    {
      "timestamp": "2026-06-20 08:10:00",
      "state": "finalized",
      "action": "evaluated->finalized",
      "status": "ok",
      "detail": "ciclo agentico cerrado"
    }
  ]
}
```

## 20260620-081350 - generar-plantilla

```json
{
  "run_id": "20260620-081350",
  "target": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
  "display_target": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
  "level": "materia",
  "action": "generar-plantilla",
  "activity_number": 1,
  "generation_mode": "direct",
  "parent_scope_key": "",
  "child_level": "",
  "child_name": "",
  "child_preview": "",
  "engines": [
    "Codex"
  ],
  "agentic_patterns": [
    "planning-memory",
    "tool-using-workflow",
    "verification-validation",
    "collective-consensus"
  ],
  "tasks": [
    {
      "stage": "planificar",
      "role": "Planificador editorial",
      "mission": "descomponer el objetivo en plan ejecutable y criterios de aceptacion",
      "engine": "Codex"
    }
  ],
  "llm_results": [
    {
      "engine": "Codex",
      "ok": true,
      "error": "",
      "chars": 4678
    }
  ],
  "compile_results": [
    {
      "tex": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/reporte-derecho-a-la-seguridad-social-Actividad-1.tex",
      "ok": true,
      "returncode": 0,
      "stdout_tail": "plate-Informe\\.build\\latex\\aux\\reporte-derecho-a-la-seg\nuridad-social-Actividad-1.out)\n(D:\\Documentos\\LaTEX\\Template-Informe\\.build\\latex\\aux\\reporte-derecho-a-la-seg\nuridad-social-Actividad-1.out)\n\npdfTeX warning: pdflatex (file D:/Documentos/LaTEX/Template-Informe/base/Planti\nlla-Informe/img/departamentos/UnADM.pdf): PDF inclusion: found PDF version <1.7\n>, but at most version <1.5> allowed\n\n[1{C:/Users/Asus TUF505/AppData/Local/MiKTeX/fonts/map/pdftex/pdftex.map}{C:/Pr\nogram Files/MiKTeX/fonts/enc/dvips/base/8r.enc} <D:/Documentos/LaTEX/Template-I\nnforme/base/Plantilla-Informe/img/departamentos/UnADM.pdf>]\n(D:\\Documentos\\LaTEX\\Template-Informe\\.build\\latex\\aux\\reporte-derecho-a-la-seg\nuridad-social-Actividad-1.toc)\n\npdfTeX warning (ext4): destination with the same identifier (name{page.1}) has \nbeen already used, duplicate ignored\n<to be read again> \n                   \\relax \nl.63 \\clearpage\n                [1]\n[2]\n[3]\n[4]\n(D:\\Documentos\\LaTEX\\Template-Informe\\.build\\latex\\aux\\reporte-derecho-a-la-seg\nuridad-social-Actividad-1.bbl)\n[5]\n(D:\\Documentos\\LaTEX\\Template-Informe\\.build\\latex\\aux\\reporte-derecho-a-la-seg\nuridad-social-Actividad-1.aux) )\n(see the transcript file for additional information) <C:\\Users\\Asus TUF505\\AppD\nata\\Local\\MiKTeX\\fonts/pk/ljfour/jknappen/ec/dpi600\\ectt1200.pk><C:/Program Fil\nes/MiKTeX/fonts/type1/urw/helvetic/uhvb8a.pfb><C:/Program Files/MiKTeX/fonts/ty\npe1/urw/helvetic/uhvr8a.pfb><C:/Program Files/MiKTeX/fonts/type1/urw/helvetic/u\nhvro8a.pfb>\nOutput written on D:\\Documentos\\LaTEX\\Template-Informe\\.build\\latex\\aux\\reporte\n-derecho-a-la-seguridad-social-Actividad-1.pdf (6 pages, 84823 bytes).\nTranscript written on D:\\Documentos\\LaTEX\\Template-Informe\\.build\\latex\\aux\\rep\norte-derecho-a-la-seguridad-social-Actividad-1.log.\nLatexmk: Moving '.build/latex/aux/reporte-derecho-a-la-seguridad-social-Actividad-1.pdf' to '.build/latex/reporte-derecho-a-la-seguridad-social-Actividad-1.pdf'\nLatexmk: Getting log file '.build/latex/aux/reporte-derecho-a-la-seguridad-social-Actividad-1.log'\nLatexmk: Examining '.build/latex/aux/reporte-derecho-a-la-seguridad-social-Actividad-1.fls'\nLatexmk: Examining '.build/latex/aux/reporte-derecho-a-la-seguridad-social-Actividad-1.log'\nLatexmk: Found input bbl file '.build/latex/aux/reporte-derecho-a-la-seguridad-social-Actividad-1.bbl'\nLatexmk: Log file says output to '.build/latex/aux/reporte-derecho-a-la-seguridad-social-Actividad-1.pdf'\n  ===Source file '.build/latex/aux/reporte-derecho-a-la-seguridad-social-Actividad-1.bbl' for 'pdflatex'\nLatexmk: Found bibliography file(s):\n  D:/Documentos/LaTEX/Template-Informe/UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/derecho-a-la-seguridad-social.bib\nLatexmk: All targets (.build/latex/reporte-derecho-a-la-seguridad-social-Actividad-1.pdf) are up-to-date\n\nPDF final: D:\\Documentos\\LaTEX\\Template-Informe\\UnADM\\licenciatura-en-derecho-unadm\\derecho-a-la-seguridad-social-lde\\reporte-derecho-a-la-seguridad-social-Actividad-1.pdf\n",
      "stderr_tail": "Latexmk: Using bibtex to make bibliography file(s).\nLatexmk: Missing input file 'reporte-derecho-a-la-seguridad-social-Actividad-1.toc' message in .log file:\n  No file reporte-derecho-a-la-seguridad-social-Actividad-1.toc.\nLatexmk: Missing bbl file '.build/latex/aux/reporte-derecho-a-la-seguridad-social-Actividad-1.bbl' in following:\n No file reporte-derecho-a-la-seguridad-social-Actividad-1.bbl.\nLatexmk: Using bibtex to make bibliography file(s).\nLatexmk: Using bibtex to make bibliography file(s).\nLatexmk: Using bibtex to make bibliography file(s).\nLatexmk: Using bibtex to make bibliography file(s).\nReverting Windows console CPs to (in,out) = (1252,65001)\n"
    },
    {
      "tex": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/presentacion-derecho-a-la-seguridad-social-Actividad-1.tex",
      "ok": true,
      "returncode": 0,
      "stdout_tail": "ackend\\l3backend-pdftex.def)\n(D:\\Documentos\\LaTEX\\Template-Informe\\.build\\latex\\aux\\presentacion-derecho-a-l\na-seguridad-social-Actividad-1.aux)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(C:\\Program Files\\MiKTeX\\tex/context/base/mkii\\supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (C:\\Program Files\\MiKTeX\\tex/latex/epstopdf-pkg\\epstopdf-base.sty\n(C:\\Program Files\\MiKTeX\\tex/latex/00miktex\\epstopdf-sys.cfg))\n(D:\\Documentos\\LaTEX\\Template-Informe\\.build\\latex\\aux\\presentacion-derecho-a-l\na-seguridad-social-Actividad-1.out)\n(D:\\Documentos\\LaTEX\\Template-Informe\\.build\\latex\\aux\\presentacion-derecho-a-l\na-seguridad-social-Actividad-1.out)\n\npdfTeX warning: pdflatex (file D:/Documentos/LaTEX/Template-Informe/base/Planti\nlla-Informe/img/departamentos/UnADM.pdf): PDF inclusion: found PDF version <1.7\n>, but at most version <1.5> allowed\n\n[1{C:/Users/Asus TUF505/AppData/Local/MiKTeX/fonts/map/pdftex/pdftex.map}{C:/Pr\nogram Files/MiKTeX/fonts/enc/dvips/base/8r.enc} <D:/Documentos/LaTEX/Template-I\nnforme/base/Plantilla-Informe/img/departamentos/UnADM.pdf>]\nUnderfull \\hbox (badness 10000) in paragraph at lines 90--91\n\n\n[2]\nUnderfull \\hbox (badness 10000) in paragraph at lines 99--100\n\n\n[3]\nUnderfull \\hbox (badness 10000) in paragraph at lines 109--110\n\n\n[4]\nUnderfull \\hbox (badness 10000) in paragraph at lines 118--119\n\n\n[5]\nUnderfull \\hbox (badness 10000) in paragraph at lines 124--125\n\n\n[6]\n(D:\\Documentos\\LaTEX\\Template-Informe\\.build\\latex\\aux\\presentacion-derecho-a-l\na-seguridad-social-Actividad-1.aux) )\n(see the transcript file for additional information) <C:\\Users\\Asus TUF505\\AppD\nata\\Local\\MiKTeX\\fonts/pk/ljfour/jknappen/ec/dpi600\\ectt1440.pk><C:/Program Fil\nes/MiKTeX/fonts/type1/urw/helvetic/uhvb8a.pfb><C:/Program Files/MiKTeX/fonts/ty\npe1/urw/helvetic/uhvr8a.pfb>\nOutput written on D:\\Documentos\\LaTEX\\Template-Informe\\.build\\latex\\aux\\present\nacion-derecho-a-la-seguridad-social-Actividad-1.pdf (6 pages, 59722 bytes).\nTranscript written on D:\\Documentos\\LaTEX\\Template-Informe\\.build\\latex\\aux\\pre\nsentacion-derecho-a-la-seguridad-social-Actividad-1.log.\nLatexmk: Moving '.build/latex/aux/presentacion-derecho-a-la-seguridad-social-Actividad-1.pdf' to '.build/latex/presentacion-derecho-a-la-seguridad-social-Actividad-1.pdf'\nLatexmk: Getting log file '.build/latex/aux/presentacion-derecho-a-la-seguridad-social-Actividad-1.log'\nLatexmk: Examining '.build/latex/aux/presentacion-derecho-a-la-seguridad-social-Actividad-1.fls'\nLatexmk: Examining '.build/latex/aux/presentacion-derecho-a-la-seguridad-social-Actividad-1.log'\nLatexmk: Log file says output to '.build/latex/aux/presentacion-derecho-a-la-seguridad-social-Actividad-1.pdf'\nLatexmk: All targets (.build/latex/presentacion-derecho-a-la-seguridad-social-Actividad-1.pdf) are up-to-date\n\nPDF final: D:\\Documentos\\LaTEX\\Template-Informe\\UnADM\\licenciatura-en-derecho-unadm\\derecho-a-la-seguridad-social-lde\\presentacion-derecho-a-la-seguridad-social-Actividad-1.pdf\n",
      "stderr_tail": "Latexmk: Using bibtex to make bibliography file(s).\nLatexmk: Using bibtex to make bibliography file(s).\nLatexmk: Using bibtex to make bibliography file(s).\nReverting Windows console CPs to (in,out) = (1252,65001)\n"
    }
  ],
  "materialization": {
    "enabled": true,
    "ok": true,
    "target_dir": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
    "artifacts": [
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/referencias-derecho-a-la-seguridad-social",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/planeaciones-derecho-a-la-seguridad-social",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/assets-derecho-a-la-seguridad-social",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/README.md",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/COMPILACION-derecho-a-la-seguridad-social.md",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/programa-analitico-derecho-a-la-seguridad-social.md",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/derecho-a-la-seguridad-social.bib",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/reporte-derecho-a-la-seguridad-social.tex",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/reporte-derecho-a-la-seguridad-social-Actividad-1.tex",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/informe-derecho-a-la-seguridad-social.tex",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/presentacion-derecho-a-la-seguridad-social.tex",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/presentacion-derecho-a-la-seguridad-social-Actividad-1.tex",
      "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/estructura-aulatex.json"
    ],
    "notes": [
      "Materializado: UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/README.md",
      "Materializado: UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/COMPILACION-derecho-a-la-seguridad-social.md",
      "Materializado: UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/programa-analitico-derecho-a-la-seguridad-social.md",
      "Materializado: UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/derecho-a-la-seguridad-social.bib",
      "Materializado: UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/reporte-derecho-a-la-seguridad-social.tex",
      "Materializado: UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/reporte-derecho-a-la-seguridad-social-Actividad-1.tex",
      "Materializado: UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/informe-derecho-a-la-seguridad-social.tex",
      "Materializado: UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/presentacion-derecho-a-la-seguridad-social.tex",
      "Materializado: UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/presentacion-derecho-a-la-seguridad-social-Actividad-1.tex",
      "Materializado: UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/estructura-aulatex.json"
    ]
  },
  "consensus": {
    "consensus_score": 9.23,
    "passed": true,
    "criteria": {
      "identidad_institucional": true,
      "bibliografia": true,
      "trazabilidad": true,
      "compilacion": true,
      "riesgos": true
    },
    "role_scores": {
      "Planificador editorial": 8.6
    },
    "risks": [],
    "recommendations": [
      "Usar el reporte como retroalimentacion editorial aplicable al objetivo."
    ]
  },
  "workflow_events": [
    {
      "timestamp": "2026-06-20 08:13:50",
      "state": "initialized",
      "action": "init",
      "status": "ok",
      "detail": "AulaTeX workflow initialized"
    },
    {
      "timestamp": "2026-06-20 08:13:51",
      "state": "initialized",
      "action": "llm-start",
      "status": "ok",
      "detail": "planificar: Planificador editorial via Codex"
    },
    {
      "timestamp": "2026-06-20 08:14:02",
      "state": "initialized",
      "action": "llm-end",
      "status": "ok",
      "detail": "planificar: 4678 chars"
    },
    {
      "timestamp": "2026-06-20 08:14:02",
      "state": "planned",
      "action": "initialized->planned",
      "status": "ok",
      "detail": "plan editorial producido"
    },
    {
      "timestamp": "2026-06-20 08:14:02",
      "state": "planned",
      "action": "materialize-start",
      "status": "ok",
      "detail": "generar-plantilla materializara estructura canonica de archivos"
    },
    {
      "timestamp": "2026-06-20 08:14:02",
      "state": "planned",
      "action": "materialize-end",
      "status": "ok",
      "detail": "13 artefactos procesados"
    },
    {
      "timestamp": "2026-06-20 08:14:02",
      "state": "planned",
      "action": "tool-select",
      "status": "ok",
      "detail": "latexmk-build.ps1 seleccionado para compilar objetivos canonicos"
    },
    {
      "timestamp": "2026-06-20 08:16:54",
      "state": "planned",
      "action": "tool-result",
      "status": "ok",
      "detail": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/reporte-derecho-a-la-seguridad-social-Actividad-1.tex rc=0"
    },
    {
      "timestamp": "2026-06-20 08:18:08",
      "state": "planned",
      "action": "tool-result",
      "status": "ok",
      "detail": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/presentacion-derecho-a-la-seguridad-social-Actividad-1.tex rc=0"
    },
    {
      "timestamp": "2026-06-20 08:18:08",
      "state": "planned",
      "action": "consensus",
      "status": "ok",
      "detail": "score=9.23"
    },
    {
      "timestamp": "2026-06-20 08:18:08",
      "state": "evaluated",
      "action": "planned->evaluated",
      "status": "ok",
      "detail": "validacion y consenso completados"
    },
    {
      "timestamp": "2026-06-20 08:18:08",
      "state": "finalized",
      "action": "evaluated->finalized",
      "status": "ok",
      "detail": "ciclo agentico cerrado"
    }
  ]
}
```

## 20260620-090520 - construccion-descendente

```json
{
  "run_id": "20260620-090520",
  "node_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
  "node_level": "materia",
  "node_name": "Derecho a la Seguridad Social",
  "node_label": "Derecho a la Seguridad Social",
  "parent_scope_key": "UnADM/licenciatura-en-derecho-unadm",
  "activity_number": 0,
  "operation_mode": "reforzar",
  "destination_path": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
  "ingestion": {
    "has_text": false,
    "has_document": false,
    "document_path": ""
  },
  "engines": [
    "Auto (model-router)"
  ],
  "iterations": 1,
  "cancelled": false,
  "ok": true,
  "node_dir": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
  "artifacts": {
    "memory": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/memoria-fundacional-derecho-a-la-seguridad-social.json",
    "plan": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/plan.md",
    "maqueta": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/maqueta-derecho-a-la-seguridad-social.tex"
  },
  "future_agent_contract": {
    "status": "ready-for-agent",
    "allowed_actions": [
      "investigar",
      "redactar",
      "evaluar",
      "compilar"
    ],
    "entrypoint": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/maqueta-derecho-a-la-seguridad-social.tex",
    "notes": "El Agente debe consumir esta maqueta sin recrear el nodo ni reconstruir memoria fundacional."
  },
  "cycle_logs": [
    {
      "cycle": 1,
      "engine": "Auto (model-router)",
      "ok": true,
      "elapsed_ms": 27934,
      "chars": 0,
      "memory_items": 170,
      "sections_created": 27
    }
  ]
}
```

## 20260620-093435 - construccion-descendente

```json
{
  "run_id": "20260620-093435",
  "node_key": "derecho-a-la-seguridad-social-lde",
  "node_level": "institucion",
  "node_name": "derecho-a-la-seguridad-social-lde",
  "node_label": "derecho-a-la-seguridad-social-lde",
  "parent_scope_key": "interinstitucional",
  "activity_number": 0,
  "operation_mode": "reforzar",
  "destination_path": "UnADM",
  "ingestion": {
    "has_text": false,
    "has_document": false,
    "document_path": ""
  },
  "engines": [
    "Codex",
    "Auto (model-router)",
    "Claude Foundry",
    "GPT-Pro"
  ],
  "iterations": 11,
  "cancelled": false,
  "ok": false,
  "node_dir": "UnADM",
  "artifacts": {
    "memory": "UnADM/memoria-fundacional.json",
    "plan": "UnADM/plan.md",
    "maqueta": "UnADM/maqueta.tex"
  },
  "future_agent_contract": {
    "status": "ready-for-agent",
    "allowed_actions": [
      "investigar",
      "redactar",
      "evaluar",
      "compilar"
    ],
    "entrypoint": "UnADM/maqueta.tex",
    "notes": "El Agente debe consumir esta maqueta sin recrear el nodo ni reconstruir memoria fundacional."
  },
  "cycle_logs": [
    {
      "cycle": 1,
      "engine": "Codex",
      "ok": true,
      "elapsed_ms": 18094,
      "chars": 8049,
      "memory_items": 31,
      "sections_created": 27
    },
    {
      "cycle": 1,
      "engine": "Auto (model-router)",
      "ok": false,
      "elapsed_ms": 1827,
      "chars": 9,
      "memory_items": 34,
      "sections_created": 27
    },
    {
      "cycle": 1,
      "engine": "Claude Foundry",
      "ok": false,
      "elapsed_ms": 2020,
      "chars": 9,
      "memory_items": 35,
      "sections_created": 27
    },
    {
      "cycle": 1,
      "engine": "GPT-Pro",
      "ok": false,
      "elapsed_ms": 45846,
      "chars": 25,
      "memory_items": 36,
      "sections_created": 27
    },
    {
      "cycle": 2,
      "engine": "Codex",
      "ok": true,
      "elapsed_ms": 17504,
      "chars": 9063,
      "memory_items": 67,
      "sections_created": 27
    },
    {
      "cycle": 2,
      "engine": "Auto (model-router)",
      "ok": false,
      "elapsed_ms": 2708,
      "chars": 9,
      "memory_items": 67,
      "sections_created": 27
    },
    {
      "cycle": 2,
      "engine": "Claude Foundry",
      "ok": false,
      "elapsed_ms": 1721,
      "chars": 9,
      "memory_items": 67,
      "sections_created": 27
    },
    {
      "cycle": 2,
      "engine": "GPT-Pro",
      "ok": false,
      "elapsed_ms": 45915,
      "chars": 25,
      "memory_items": 67,
      "sections_created": 27
    },
    {
      "cycle": 3,
      "engine": "Codex",
      "ok": true,
      "elapsed_ms": 13548,
      "chars": 8722,
      "memory_items": 96,
      "sections_created": 27
    },
    {
      "cycle": 3,
      "engine": "Auto (model-router)",
      "ok": false,
      "elapsed_ms": 2627,
      "chars": 9,
      "memory_items": 96,
      "sections_created": 27
    },
    {
      "cycle": 3,
      "engine": "Claude Foundry",
      "ok": false,
      "elapsed_ms": 2536,
      "chars": 9,
      "memory_items": 96,
      "sections_created": 27
    },
    {
      "cycle": 3,
      "engine": "GPT-Pro",
      "ok": false,
      "elapsed_ms": 45928,
      "chars": 25,
      "memory_items": 96,
      "sections_created": 27
    },
    {
      "cycle": 4,
      "engine": "Codex",
      "ok": true,
      "elapsed_ms": 14105,
      "chars": 8735,
      "memory_items": 106,
      "sections_created": 27
    },
    {
      "cycle": 4,
      "engine": "Auto (model-router)",
      "ok": false,
      "elapsed_ms": 1918,
      "chars": 9,
      "memory_items": 106,
      "sections_created": 27
    },
    {
      "cycle": 4,
      "engine": "Claude Foundry",
      "ok": false,
      "elapsed_ms": 2193,
      "chars": 9,
      "memory_items": 106,
      "sections_created": 27
    },
    {
      "cycle": 4,
      "engine": "GPT-Pro",
      "ok": false,
      "elapsed_ms": 45754,
      "chars": 25,
      "memory_items": 106,
      "sections_created": 27
    },
    {
      "cycle": 5,
      "engine": "Codex",
      "ok": true,
      "elapsed_ms": 12892,
      "chars": 8670,
      "memory_items": 109,
      "sections_created": 27
    },
    {
      "cycle": 5,
      "engine": "Auto (model-router)",
      "ok": false,
      "elapsed_ms": 1869,
      "chars": 9,
      "memory_items": 109,
      "sections_created": 27
    },
    {
      "cycle": 5,
      "engine": "Claude Foundry",
      "ok": false,
      "elapsed_ms": 1893,
      "chars": 9,
      "memory_items": 109,
      "sections_created": 27
    },
    {
      "cycle": 5,
      "engine": "GPT-Pro",
      "ok": false,
      "elapsed_ms": 46300,
      "chars": 25,
      "memory_items": 109,
      "sections_created": 27
    },
    {
      "cycle": 6,
      "engine": "Codex",
      "ok": true,
      "elapsed_ms": 15258,
      "chars": 8715,
      "memory_items": 112,
      "sections_created": 27
    },
    {
      "cycle": 6,
      "engine": "Auto (model-router)",
      "ok": false,
      "elapsed_ms": 1962,
      "chars": 9,
      "memory_items": 112,
      "sections_created": 27
    },
    {
      "cycle": 6,
      "engine": "Claude Foundry",
      "ok": false,
      "elapsed_ms": 1470,
      "chars": 9,
      "memory_items": 112,
      "sections_created": 27
    },
    {
      "cycle": 6,
      "engine": "GPT-Pro",
      "ok": false,
      "elapsed_ms": 46086,
      "chars": 25,
      "memory_items": 112,
      "sections_created": 27
    },
    {
      "cycle": 7,
      "engine": "Codex",
      "ok": true,
      "elapsed_ms": 12956,
      "chars": 8786,
      "memory_items": 113,
      "sections_created": 27
    },
    {
      "cycle": 7,
      "engine": "Auto (model-router)",
      "ok": false,
      "elapsed_ms": 1966,
      "chars": 9,
      "memory_items": 113,
      "sections_created": 27
    },
    {
      "cycle": 7,
      "engine": "Claude Foundry",
      "ok": false,
      "elapsed_ms": 2400,
      "chars": 9,
      "memory_items": 113,
      "sections_created": 27
    },
    {
      "cycle": 7,
      "engine": "GPT-Pro",
      "ok": false,
      "elapsed_ms": 46312,
      "chars": 25,
      "memory_items": 113,
      "sections_created": 27
    },
    {
      "cycle": 8,
      "engine": "Codex",
      "ok": true,
      "elapsed_ms": 13736,
      "chars": 8786,
      "memory_items": 113,
      "sections_created": 27
    },
    {
      "cycle": 8,
      "engine": "Auto (model-router)",
      "ok": false,
      "elapsed_ms": 1980,
      "chars": 9,
      "memory_items": 113,
      "sections_created": 27
    },
    {
      "cycle": 8,
      "engine": "Claude Foundry",
      "ok": false,
      "elapsed_ms": 1801,
      "chars": 9,
      "memory_items": 113,
      "sections_created": 27
    },
    {
      "cycle": 8,
      "engine": "GPT-Pro",
      "ok": false,
      "elapsed_ms": 45938,
      "chars": 25,
      "memory_items": 113,
      "sections_created": 27
    },
    {
      "cycle": 9,
      "engine": "Codex",
      "ok": true,
      "elapsed_ms": 13909,
      "chars": 8812,
      "memory_items": 115,
      "sections_created": 27
    },
    {
      "cycle": 9,
      "engine": "Auto (model-router)",
      "ok": false,
      "elapsed_ms": 1383,
      "chars": 9,
      "memory_items": 115,
      "sections_created": 27
    },
    {
      "cycle": 9,
      "engine": "Claude Foundry",
      "ok": false,
      "elapsed_ms": 1628,
      "chars": 9,
      "memory_items": 115,
      "sections_created": 27
    },
    {
      "cycle": 9,
      "engine": "GPT-Pro",
      "ok": false,
      "elapsed_ms": 45799,
      "chars": 25,
      "memory_items": 115,
      "sections_created": 27
    },
    {
      "cycle": 10,
      "engine": "Codex",
      "ok": true,
      "elapsed_ms": 13418,
      "chars": 8828,
      "memory_items": 116,
      "sections_created": 27
    },
    {
      "cycle": 10,
      "engine": "Auto (model-router)",
      "ok": false,
      "elapsed_ms": 2261,
      "chars": 9,
      "memory_items": 116,
      "sections_created": 27
    },
    {
      "cycle": 10,
      "engine": "Claude Foundry",
      "ok": false,
      "elapsed_ms": 1475,
      "chars": 9,
      "memory_items": 116,
      "sections_created": 27
    },
    {
      "cycle": 10,
      "engine": "GPT-Pro",
      "ok": false,
      "elapsed_ms": 46218,
      "chars": 25,
      "memory_items": 116,
      "sections_created": 27
    },
    {
      "cycle": 11,
      "engine": "Codex",
      "ok": true,
      "elapsed_ms": 13268,
      "chars": 8786,
      "memory_items": 120,
      "sections_created": 27
    },
    {
      "cycle": 11,
      "engine": "Auto (model-router)",
      "ok": false,
      "elapsed_ms": 2038,
      "chars": 9,
      "memory_items": 120,
      "sections_created": 27
    },
    {
      "cycle": 11,
      "engine": "Claude Foundry",
      "ok": false,
      "elapsed_ms": 2338,
      "chars": 9,
      "memory_items": 120,
      "sections_created": 27
    },
    {
      "cycle": 11,
      "engine": "GPT-Pro",
      "ok": false,
      "elapsed_ms": 45767,
      "chars": 25,
      "memory_items": 120,
      "sections_created": 27
    }
  ]
}
```

## 20260620-100744 - memoria-editorial

```json
{
  "run_id": "20260620-100744",
  "source_scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
  "build_level": "materia",
  "propagation_mode": "ascendente",
  "iterations": 1,
  "engines": [
    "Codex"
  ],
  "built_scopes": [
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde"
  ],
  "cycles": [
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 1,
      "engine": "Codex",
      "ok": true,
      "chars": 5429
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 1,
      "engine": "Codex",
      "ok": true,
      "chars": 5873
    }
  ],
  "ok": true,
  "cancelled": false
}
```

## 20260620-105026 - memoria-editorial

```json
{
  "run_id": "20260620-105026",
  "source_scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
  "build_level": "actividad",
  "propagation_mode": "local",
  "iterations": 1,
  "engines": [
    "Codex"
  ],
  "built_scopes": [
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1"
  ],
  "cycles": [
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 1,
      "engine": "Codex",
      "ok": true,
      "chars": 5400
    }
  ],
  "ok": true,
  "cancelled": false
}
```

## 20260620-105757 - memoria-editorial

```json
{
  "run_id": "20260620-105757",
  "source_scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
  "build_level": "actividad",
  "propagation_mode": "local",
  "iterations": 1,
  "engines": [
    "Codex"
  ],
  "built_scopes": [
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1"
  ],
  "cycles": [
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 1,
      "engine": "Codex",
      "ok": true,
      "chars": 5076
    }
  ],
  "ok": true,
  "cancelled": false
}
```

## 20260620-110328 - memoria-editorial

```json
{
  "run_id": "20260620-110328",
  "source_scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
  "build_level": "actividad",
  "propagation_mode": "local",
  "iterations": 100,
  "engines": [
    "Codex"
  ],
  "built_scopes": [
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1"
  ],
  "cycles": [
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 1,
      "engine": "Codex",
      "ok": true,
      "chars": 5294
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 2,
      "engine": "Codex",
      "ok": true,
      "chars": 5052
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 3,
      "engine": "Codex",
      "ok": true,
      "chars": 5000
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 4,
      "engine": "Codex",
      "ok": true,
      "chars": 5046
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 5,
      "engine": "Codex",
      "ok": true,
      "chars": 5394
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 6,
      "engine": "Codex",
      "ok": true,
      "chars": 5011
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 7,
      "engine": "Codex",
      "ok": true,
      "chars": 5048
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 8,
      "engine": "Codex",
      "ok": true,
      "chars": 4893
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 9,
      "engine": "Codex",
      "ok": true,
      "chars": 4961
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 10,
      "engine": "Codex",
      "ok": true,
      "chars": 4785
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 11,
      "engine": "Codex",
      "ok": true,
      "chars": 5368
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 12,
      "engine": "Codex",
      "ok": true,
      "chars": 5376
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 13,
      "engine": "Codex",
      "ok": true,
      "chars": 4974
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 14,
      "engine": "Codex",
      "ok": true,
      "chars": 5185
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 15,
      "engine": "Codex",
      "ok": true,
      "chars": 5193
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 16,
      "engine": "Codex",
      "ok": true,
      "chars": 5153
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 17,
      "engine": "Codex",
      "ok": true,
      "chars": 5504
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 18,
      "engine": "Codex",
      "ok": true,
      "chars": 5398
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 19,
      "engine": "Codex",
      "ok": true,
      "chars": 5201
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 20,
      "engine": "Codex",
      "ok": true,
      "chars": 5271
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 21,
      "engine": "Codex",
      "ok": true,
      "chars": 5280
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 22,
      "engine": "Codex",
      "ok": true,
      "chars": 5249
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 23,
      "engine": "Codex",
      "ok": true,
      "chars": 5160
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 24,
      "engine": "Codex",
      "ok": true,
      "chars": 5167
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 25,
      "engine": "Codex",
      "ok": true,
      "chars": 5347
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 26,
      "engine": "Codex",
      "ok": true,
      "chars": 5191
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 27,
      "engine": "Codex",
      "ok": true,
      "chars": 5407
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 28,
      "engine": "Codex",
      "ok": true,
      "chars": 5213
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 29,
      "engine": "Codex",
      "ok": true,
      "chars": 5278
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 30,
      "engine": "Codex",
      "ok": true,
      "chars": 5424
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 31,
      "engine": "Codex",
      "ok": true,
      "chars": 5239
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 32,
      "engine": "Codex",
      "ok": true,
      "chars": 5251
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 33,
      "engine": "Codex",
      "ok": true,
      "chars": 5111
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 34,
      "engine": "Codex",
      "ok": true,
      "chars": 5290
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 35,
      "engine": "Codex",
      "ok": true,
      "chars": 5147
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 36,
      "engine": "Codex",
      "ok": true,
      "chars": 5382
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 37,
      "engine": "Codex",
      "ok": true,
      "chars": 5311
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 38,
      "engine": "Codex",
      "ok": true,
      "chars": 5365
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 39,
      "engine": "Codex",
      "ok": true,
      "chars": 5190
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 40,
      "engine": "Codex",
      "ok": true,
      "chars": 5297
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 41,
      "engine": "Codex",
      "ok": true,
      "chars": 5411
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 42,
      "engine": "Codex",
      "ok": true,
      "chars": 5310
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 43,
      "engine": "Codex",
      "ok": true,
      "chars": 5462
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 44,
      "engine": "Codex",
      "ok": true,
      "chars": 5330
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 45,
      "engine": "Codex",
      "ok": true,
      "chars": 5416
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 46,
      "engine": "Codex",
      "ok": true,
      "chars": 5186
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 47,
      "engine": "Codex",
      "ok": true,
      "chars": 5331
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 48,
      "engine": "Codex",
      "ok": true,
      "chars": 5378
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 49,
      "engine": "Codex",
      "ok": true,
      "chars": 5337
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 50,
      "engine": "Codex",
      "ok": true,
      "chars": 5463
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 51,
      "engine": "Codex",
      "ok": true,
      "chars": 5331
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 52,
      "engine": "Codex",
      "ok": true,
      "chars": 5439
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 53,
      "engine": "Codex",
      "ok": true,
      "chars": 5326
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 54,
      "engine": "Codex",
      "ok": true,
      "chars": 5237
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 55,
      "engine": "Codex",
      "ok": true,
      "chars": 5252
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 56,
      "engine": "Codex",
      "ok": true,
      "chars": 5397
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 57,
      "engine": "Codex",
      "ok": true,
      "chars": 5350
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 58,
      "engine": "Codex",
      "ok": true,
      "chars": 5327
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 59,
      "engine": "Codex",
      "ok": true,
      "chars": 5328
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 60,
      "engine": "Codex",
      "ok": true,
      "chars": 5395
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 61,
      "engine": "Codex",
      "ok": true,
      "chars": 5376
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 62,
      "engine": "Codex",
      "ok": true,
      "chars": 5323
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 63,
      "engine": "Codex",
      "ok": true,
      "chars": 5198
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 64,
      "engine": "Codex",
      "ok": true,
      "chars": 5369
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 65,
      "engine": "Codex",
      "ok": true,
      "chars": 5266
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 66,
      "engine": "Codex",
      "ok": true,
      "chars": 5331
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 67,
      "engine": "Codex",
      "ok": true,
      "chars": 5336
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 68,
      "engine": "Codex",
      "ok": true,
      "chars": 5373
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 69,
      "engine": "Codex",
      "ok": true,
      "chars": 5255
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 70,
      "engine": "Codex",
      "ok": true,
      "chars": 5317
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 71,
      "engine": "Codex",
      "ok": true,
      "chars": 5407
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 72,
      "engine": "Codex",
      "ok": true,
      "chars": 5341
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 73,
      "engine": "Codex",
      "ok": true,
      "chars": 5331
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 74,
      "engine": "Codex",
      "ok": true,
      "chars": 5405
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 75,
      "engine": "Codex",
      "ok": true,
      "chars": 5378
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 76,
      "engine": "Codex",
      "ok": true,
      "chars": 5479
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 77,
      "engine": "Codex",
      "ok": true,
      "chars": 5246
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 78,
      "engine": "Codex",
      "ok": true,
      "chars": 5272
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 79,
      "engine": "Codex",
      "ok": true,
      "chars": 5344
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 80,
      "engine": "Codex",
      "ok": true,
      "chars": 5329
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 81,
      "engine": "Codex",
      "ok": true,
      "chars": 5291
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 82,
      "engine": "Codex",
      "ok": true,
      "chars": 5340
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 83,
      "engine": "Codex",
      "ok": true,
      "chars": 5426
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 84,
      "engine": "Codex",
      "ok": true,
      "chars": 5121
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 85,
      "engine": "Codex",
      "ok": true,
      "chars": 5326
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 86,
      "engine": "Codex",
      "ok": true,
      "chars": 5143
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 87,
      "engine": "Codex",
      "ok": true,
      "chars": 5429
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 88,
      "engine": "Codex",
      "ok": true,
      "chars": 5343
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 89,
      "engine": "Codex",
      "ok": true,
      "chars": 5338
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 90,
      "engine": "Codex",
      "ok": true,
      "chars": 5375
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 91,
      "engine": "Codex",
      "ok": true,
      "chars": 5344
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 92,
      "engine": "Codex",
      "ok": true,
      "chars": 5353
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 93,
      "engine": "Codex",
      "ok": true,
      "chars": 5356
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 94,
      "engine": "Codex",
      "ok": true,
      "chars": 5414
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 95,
      "engine": "Codex",
      "ok": true,
      "chars": 5389
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 96,
      "engine": "Codex",
      "ok": true,
      "chars": 5370
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 97,
      "engine": "Codex",
      "ok": true,
      "chars": 5512
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 98,
      "engine": "Codex",
      "ok": true,
      "chars": 5393
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 99,
      "engine": "Codex",
      "ok": true,
      "chars": 5397
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 100,
      "engine": "Codex",
      "ok": true,
      "chars": 5369
    }
  ],
  "ok": true,
  "cancelled": false
}
```

## 20260621-030126 - memoria-editorial

```json
{
  "run_id": "20260621-030126",
  "source_scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
  "build_level": "actividad",
  "propagation_mode": "recursivo",
  "iterations": 1,
  "engines": [
    "Codex",
    "GPT-Pro"
  ],
  "built_scopes": [
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1"
  ],
  "cycles": [
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 1,
      "engine": "Codex",
      "ok": true,
      "chars": 8158
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 1,
      "engine": "GPT-Pro",
      "ok": false,
      "chars": 25
    }
  ],
  "ok": false,
  "cancelled": false
}
```

## 20260621-031317 - memoria-editorial

```json
{
  "run_id": "20260621-031317",
  "source_scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
  "build_level": "actividad",
  "propagation_mode": "recursivo",
  "iterations": 1,
  "engines": [
    "Codex",
    "GPT-Pro"
  ],
  "built_scopes": [
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1"
  ],
  "cycles": [
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 1,
      "engine": "Codex",
      "ok": true,
      "chars": 8761
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 1,
      "engine": "GPT-Pro",
      "ok": false,
      "chars": 25
    }
  ],
  "ok": false,
  "cancelled": false
}
```

## 20260621-033515 - memoria-editorial

```json
{
  "run_id": "20260621-033515",
  "source_scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
  "build_level": "actividad",
  "propagation_mode": "recursivo",
  "iterations": 1,
  "engines": [
    "Codex"
  ],
  "timeout_seconds": 300,
  "built_scopes": [
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1"
  ],
  "cycles": [
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 1,
      "engine": "Codex",
      "ok": true,
      "chars": 8720
    }
  ],
  "ok": true,
  "cancelled": false
}
```

## 20260621-034012 - memoria-editorial

```json
{
  "run_id": "20260621-034012",
  "source_scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
  "build_level": "actividad",
  "propagation_mode": "recursivo",
  "iterations": 1,
  "engines": [
    "GPT-Pro"
  ],
  "timeout_seconds": 900,
  "built_scopes": [
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1"
  ],
  "cycles": [
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 1,
      "engine": "GPT-Pro",
      "ok": false,
      "chars": 25
    }
  ],
  "ok": false,
  "cancelled": false
}
```

## 20260621-040821 - memoria-editorial

```json
{
  "run_id": "20260621-040821",
  "source_scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
  "build_level": "actividad",
  "propagation_mode": "recursivo",
  "iterations": 1,
  "engines": [
    "Codex"
  ],
  "timeout_seconds": 300,
  "scope_offset": 0,
  "scope_limit": 1,
  "full_plan_scope_count": 1,
  "batch_scope_count": 1,
  "built_scopes": [
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1"
  ],
  "cycles": [
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 1,
      "engine": "Codex",
      "ok": true,
      "chars": 8385
    }
  ],
  "ok": true,
  "cancelled": false
}
```

## 20260621-041432 - memoria-editorial

```json
{
  "run_id": "20260621-041432",
  "source_scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
  "build_level": "materia",
  "propagation_mode": "recursivo",
  "iterations": 1,
  "engines": [
    "Codex"
  ],
  "timeout_seconds": 300,
  "scope_offset": 0,
  "scope_limit": 1,
  "full_plan_scope_count": 7,
  "batch_scope_count": 1,
  "built_scopes": [
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1"
  ],
  "cycles": [
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 1,
      "engine": "Codex",
      "ok": true,
      "chars": 8816
    }
  ],
  "ok": true,
  "cancelled": false
}
```

## 20260621-041914 - memoria-editorial

```json
{
  "run_id": "20260621-041914",
  "source_scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
  "build_level": "materia",
  "propagation_mode": "recursivo",
  "iterations": 1,
  "engines": [
    "Codex"
  ],
  "timeout_seconds": 300,
  "scope_offset": 1,
  "scope_limit": 1,
  "full_plan_scope_count": 7,
  "batch_scope_count": 1,
  "built_scopes": [
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2"
  ],
  "cycles": [
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 1,
      "engine": "Codex",
      "ok": true,
      "chars": 8065
    }
  ],
  "ok": true,
  "cancelled": false
}
```

## 20260621-045109 - memoria-editorial

```json
{
  "run_id": "20260621-045109",
  "source_scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
  "build_level": "interinstitucional",
  "propagation_mode": "recursivo",
  "iterations": 100,
  "engines": [
    "Codex"
  ],
  "timeout_seconds": 900,
  "scope_offset": 1,
  "scope_limit": 1,
  "full_plan_scope_count": 461,
  "batch_scope_count": 1,
  "built_scopes": [
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2"
  ],
  "cycles": [
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 1,
      "engine": "Codex",
      "ok": true,
      "chars": 7672
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 2,
      "engine": "Codex",
      "ok": true,
      "chars": 7672
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 3,
      "engine": "Codex",
      "ok": true,
      "chars": 7909
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 4,
      "engine": "Codex",
      "ok": true,
      "chars": 8155
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 5,
      "engine": "Codex",
      "ok": true,
      "chars": 8069
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 6,
      "engine": "Codex",
      "ok": true,
      "chars": 8042
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 7,
      "engine": "Codex",
      "ok": true,
      "chars": 7093
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 8,
      "engine": "Codex",
      "ok": true,
      "chars": 7687
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 9,
      "engine": "Codex",
      "ok": true,
      "chars": 7617
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 10,
      "engine": "Codex",
      "ok": true,
      "chars": 7763
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 11,
      "engine": "Codex",
      "ok": true,
      "chars": 7858
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 12,
      "engine": "Codex",
      "ok": true,
      "chars": 7916
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 13,
      "engine": "Codex",
      "ok": true,
      "chars": 7913
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 14,
      "engine": "Codex",
      "ok": true,
      "chars": 7671
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 15,
      "engine": "Codex",
      "ok": true,
      "chars": 7601
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 16,
      "engine": "Codex",
      "ok": true,
      "chars": 8151
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 17,
      "engine": "Codex",
      "ok": true,
      "chars": 7022
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 18,
      "engine": "Codex",
      "ok": true,
      "chars": 7880
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 19,
      "engine": "Codex",
      "ok": true,
      "chars": 7857
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 20,
      "engine": "Codex",
      "ok": true,
      "chars": 7751
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 21,
      "engine": "Codex",
      "ok": true,
      "chars": 8487
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 22,
      "engine": "Codex",
      "ok": true,
      "chars": 7592
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 23,
      "engine": "Codex",
      "ok": true,
      "chars": 7373
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 24,
      "engine": "Codex",
      "ok": true,
      "chars": 7707
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 25,
      "engine": "Codex",
      "ok": true,
      "chars": 7882
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 26,
      "engine": "Codex",
      "ok": true,
      "chars": 7710
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 27,
      "engine": "Codex",
      "ok": true,
      "chars": 7912
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 28,
      "engine": "Codex",
      "ok": true,
      "chars": 8083
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 29,
      "engine": "Codex",
      "ok": true,
      "chars": 7744
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 30,
      "engine": "Codex",
      "ok": true,
      "chars": 7851
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 31,
      "engine": "Codex",
      "ok": true,
      "chars": 7635
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 32,
      "engine": "Codex",
      "ok": true,
      "chars": 7929
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 33,
      "engine": "Codex",
      "ok": true,
      "chars": 8102
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 34,
      "engine": "Codex",
      "ok": true,
      "chars": 8653
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 35,
      "engine": "Codex",
      "ok": true,
      "chars": 7908
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 36,
      "engine": "Codex",
      "ok": true,
      "chars": 7910
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 37,
      "engine": "Codex",
      "ok": true,
      "chars": 7430
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 38,
      "engine": "Codex",
      "ok": true,
      "chars": 7372
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 39,
      "engine": "Codex",
      "ok": true,
      "chars": 7487
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 40,
      "engine": "Codex",
      "ok": true,
      "chars": 8222
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 41,
      "engine": "Codex",
      "ok": true,
      "chars": 7271
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 42,
      "engine": "Codex",
      "ok": true,
      "chars": 7118
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 43,
      "engine": "Codex",
      "ok": true,
      "chars": 7572
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 44,
      "engine": "Codex",
      "ok": true,
      "chars": 7542
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 45,
      "engine": "Codex",
      "ok": true,
      "chars": 7889
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 46,
      "engine": "Codex",
      "ok": true,
      "chars": 7854
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 47,
      "engine": "Codex",
      "ok": true,
      "chars": 7516
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 48,
      "engine": "Codex",
      "ok": true,
      "chars": 8296
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 49,
      "engine": "Codex",
      "ok": true,
      "chars": 7118
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 50,
      "engine": "Codex",
      "ok": true,
      "chars": 8117
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 51,
      "engine": "Codex",
      "ok": true,
      "chars": 7367
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 52,
      "engine": "Codex",
      "ok": true,
      "chars": 7880
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 53,
      "engine": "Codex",
      "ok": true,
      "chars": 7554
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 54,
      "engine": "Codex",
      "ok": true,
      "chars": 8281
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 55,
      "engine": "Codex",
      "ok": true,
      "chars": 7827
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 56,
      "engine": "Codex",
      "ok": true,
      "chars": 7737
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 57,
      "engine": "Codex",
      "ok": true,
      "chars": 7217
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 58,
      "engine": "Codex",
      "ok": true,
      "chars": 7349
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 59,
      "engine": "Codex",
      "ok": true,
      "chars": 8062
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 60,
      "engine": "Codex",
      "ok": true,
      "chars": 7414
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 61,
      "engine": "Codex",
      "ok": true,
      "chars": 7568
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 62,
      "engine": "Codex",
      "ok": true,
      "chars": 7481
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 63,
      "engine": "Codex",
      "ok": true,
      "chars": 7570
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 64,
      "engine": "Codex",
      "ok": true,
      "chars": 7362
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 65,
      "engine": "Codex",
      "ok": true,
      "chars": 7381
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 66,
      "engine": "Codex",
      "ok": true,
      "chars": 7684
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 67,
      "engine": "Codex",
      "ok": true,
      "chars": 7957
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 68,
      "engine": "Codex",
      "ok": true,
      "chars": 7434
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 69,
      "engine": "Codex",
      "ok": true,
      "chars": 8095
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 70,
      "engine": "Codex",
      "ok": true,
      "chars": 7884
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 71,
      "engine": "Codex",
      "ok": true,
      "chars": 7990
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 72,
      "engine": "Codex",
      "ok": true,
      "chars": 7343
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 73,
      "engine": "Codex",
      "ok": true,
      "chars": 8280
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 74,
      "engine": "Codex",
      "ok": true,
      "chars": 7277
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 75,
      "engine": "Codex",
      "ok": true,
      "chars": 7885
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 76,
      "engine": "Codex",
      "ok": true,
      "chars": 7643
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 77,
      "engine": "Codex",
      "ok": true,
      "chars": 7931
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 78,
      "engine": "Codex",
      "ok": true,
      "chars": 7655
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 79,
      "engine": "Codex",
      "ok": true,
      "chars": 7402
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 80,
      "engine": "Codex",
      "ok": true,
      "chars": 7515
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 81,
      "engine": "Codex",
      "ok": true,
      "chars": 7342
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 82,
      "engine": "Codex",
      "ok": true,
      "chars": 7540
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 83,
      "engine": "Codex",
      "ok": true,
      "chars": 7104
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 84,
      "engine": "Codex",
      "ok": true,
      "chars": 7899
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 85,
      "engine": "Codex",
      "ok": true,
      "chars": 7893
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 86,
      "engine": "Codex",
      "ok": true,
      "chars": 8092
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 87,
      "engine": "Codex",
      "ok": true,
      "chars": 7905
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 88,
      "engine": "Codex",
      "ok": true,
      "chars": 7401
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 89,
      "engine": "Codex",
      "ok": true,
      "chars": 7923
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 90,
      "engine": "Codex",
      "ok": true,
      "chars": 8028
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 91,
      "engine": "Codex",
      "ok": true,
      "chars": 7701
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 92,
      "engine": "Codex",
      "ok": true,
      "chars": 8129
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 93,
      "engine": "Codex",
      "ok": true,
      "chars": 7831
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 94,
      "engine": "Codex",
      "ok": true,
      "chars": 7851
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 95,
      "engine": "Codex",
      "ok": true,
      "chars": 7365
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 96,
      "engine": "Codex",
      "ok": true,
      "chars": 8003
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 97,
      "engine": "Codex",
      "ok": true,
      "chars": 8881
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 98,
      "engine": "Codex",
      "ok": true,
      "chars": 7394
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 99,
      "engine": "Codex",
      "ok": true,
      "chars": 8013
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2",
      "scope_level": "actividad",
      "cycle": 100,
      "engine": "Codex",
      "ok": true,
      "chars": 7276
    }
  ],
  "ok": true,
  "cancelled": false
}
```

## 20260621-052341 - memoria-editorial

```json
{
  "run_id": "20260621-052341",
  "source_scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
  "build_level": "interinstitucional",
  "propagation_mode": "recursivo",
  "iterations": 100,
  "engines": [
    "Codex"
  ],
  "timeout_seconds": 900,
  "scope_offset": 2,
  "scope_limit": 1,
  "full_plan_scope_count": 461,
  "batch_scope_count": 1,
  "built_scopes": [
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3"
  ],
  "cycles": [
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 1,
      "engine": "Codex",
      "ok": true,
      "chars": 8193
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 2,
      "engine": "Codex",
      "ok": true,
      "chars": 8250
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 3,
      "engine": "Codex",
      "ok": true,
      "chars": 7984
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 4,
      "engine": "Codex",
      "ok": true,
      "chars": 8176
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 5,
      "engine": "Codex",
      "ok": true,
      "chars": 8324
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 6,
      "engine": "Codex",
      "ok": true,
      "chars": 7879
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 7,
      "engine": "Codex",
      "ok": true,
      "chars": 8620
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 8,
      "engine": "Codex",
      "ok": true,
      "chars": 8800
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 9,
      "engine": "Codex",
      "ok": true,
      "chars": 8015
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 10,
      "engine": "Codex",
      "ok": true,
      "chars": 8381
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 11,
      "engine": "Codex",
      "ok": true,
      "chars": 8267
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 12,
      "engine": "Codex",
      "ok": true,
      "chars": 8725
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 13,
      "engine": "Codex",
      "ok": true,
      "chars": 8611
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 14,
      "engine": "Codex",
      "ok": true,
      "chars": 8573
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 15,
      "engine": "Codex",
      "ok": true,
      "chars": 8932
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 16,
      "engine": "Codex",
      "ok": true,
      "chars": 8413
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 17,
      "engine": "Codex",
      "ok": true,
      "chars": 8647
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 18,
      "engine": "Codex",
      "ok": true,
      "chars": 8365
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 19,
      "engine": "Codex",
      "ok": true,
      "chars": 7933
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 20,
      "engine": "Codex",
      "ok": true,
      "chars": 8617
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 21,
      "engine": "Codex",
      "ok": true,
      "chars": 8181
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 22,
      "engine": "Codex",
      "ok": true,
      "chars": 8175
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 23,
      "engine": "Codex",
      "ok": true,
      "chars": 8348
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 24,
      "engine": "Codex",
      "ok": true,
      "chars": 8760
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 25,
      "engine": "Codex",
      "ok": true,
      "chars": 8733
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 26,
      "engine": "Codex",
      "ok": true,
      "chars": 7660
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 27,
      "engine": "Codex",
      "ok": true,
      "chars": 8841
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 28,
      "engine": "Codex",
      "ok": true,
      "chars": 8370
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 29,
      "engine": "Codex",
      "ok": true,
      "chars": 8241
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 30,
      "engine": "Codex",
      "ok": true,
      "chars": 8315
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 31,
      "engine": "Codex",
      "ok": true,
      "chars": 8194
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 32,
      "engine": "Codex",
      "ok": true,
      "chars": 8339
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 33,
      "engine": "Codex",
      "ok": true,
      "chars": 8074
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 34,
      "engine": "Codex",
      "ok": true,
      "chars": 8209
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 35,
      "engine": "Codex",
      "ok": true,
      "chars": 8403
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 36,
      "engine": "Codex",
      "ok": true,
      "chars": 7995
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 37,
      "engine": "Codex",
      "ok": true,
      "chars": 8427
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 38,
      "engine": "Codex",
      "ok": true,
      "chars": 7789
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 39,
      "engine": "Codex",
      "ok": true,
      "chars": 8204
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 40,
      "engine": "Codex",
      "ok": true,
      "chars": 8209
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 41,
      "engine": "Codex",
      "ok": true,
      "chars": 8170
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 42,
      "engine": "Codex",
      "ok": true,
      "chars": 8109
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 43,
      "engine": "Codex",
      "ok": true,
      "chars": 8448
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 44,
      "engine": "Codex",
      "ok": true,
      "chars": 8687
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 45,
      "engine": "Codex",
      "ok": true,
      "chars": 8716
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 46,
      "engine": "Codex",
      "ok": true,
      "chars": 8840
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 47,
      "engine": "Codex",
      "ok": true,
      "chars": 8094
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 48,
      "engine": "Codex",
      "ok": true,
      "chars": 8776
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 49,
      "engine": "Codex",
      "ok": true,
      "chars": 9027
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 50,
      "engine": "Codex",
      "ok": true,
      "chars": 8457
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 51,
      "engine": "Codex",
      "ok": true,
      "chars": 8347
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 52,
      "engine": "Codex",
      "ok": true,
      "chars": 7986
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 53,
      "engine": "Codex",
      "ok": true,
      "chars": 7627
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 54,
      "engine": "Codex",
      "ok": true,
      "chars": 8236
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 55,
      "engine": "Codex",
      "ok": true,
      "chars": 8696
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 56,
      "engine": "Codex",
      "ok": true,
      "chars": 8527
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 57,
      "engine": "Codex",
      "ok": true,
      "chars": 8397
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 58,
      "engine": "Codex",
      "ok": true,
      "chars": 7909
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 59,
      "engine": "Codex",
      "ok": true,
      "chars": 8714
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 60,
      "engine": "Codex",
      "ok": true,
      "chars": 8566
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 61,
      "engine": "Codex",
      "ok": true,
      "chars": 7917
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 62,
      "engine": "Codex",
      "ok": true,
      "chars": 8608
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 63,
      "engine": "Codex",
      "ok": true,
      "chars": 8086
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 64,
      "engine": "Codex",
      "ok": true,
      "chars": 8465
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 65,
      "engine": "Codex",
      "ok": true,
      "chars": 8572
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 66,
      "engine": "Codex",
      "ok": true,
      "chars": 8830
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 67,
      "engine": "Codex",
      "ok": true,
      "chars": 8270
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 68,
      "engine": "Codex",
      "ok": true,
      "chars": 8148
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 69,
      "engine": "Codex",
      "ok": true,
      "chars": 8147
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 70,
      "engine": "Codex",
      "ok": true,
      "chars": 8635
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 71,
      "engine": "Codex",
      "ok": true,
      "chars": 8483
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 72,
      "engine": "Codex",
      "ok": true,
      "chars": 8320
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 73,
      "engine": "Codex",
      "ok": true,
      "chars": 7712
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 74,
      "engine": "Codex",
      "ok": true,
      "chars": 8587
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 75,
      "engine": "Codex",
      "ok": true,
      "chars": 8444
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 76,
      "engine": "Codex",
      "ok": true,
      "chars": 8254
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 77,
      "engine": "Codex",
      "ok": true,
      "chars": 8504
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 78,
      "engine": "Codex",
      "ok": true,
      "chars": 8324
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 79,
      "engine": "Codex",
      "ok": true,
      "chars": 8358
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 80,
      "engine": "Codex",
      "ok": true,
      "chars": 8320
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 81,
      "engine": "Codex",
      "ok": true,
      "chars": 8447
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 82,
      "engine": "Codex",
      "ok": true,
      "chars": 8786
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 83,
      "engine": "Codex",
      "ok": true,
      "chars": 8979
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 84,
      "engine": "Codex",
      "ok": true,
      "chars": 8492
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 85,
      "engine": "Codex",
      "ok": true,
      "chars": 8288
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 86,
      "engine": "Codex",
      "ok": true,
      "chars": 8297
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 87,
      "engine": "Codex",
      "ok": true,
      "chars": 8227
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 88,
      "engine": "Codex",
      "ok": true,
      "chars": 8397
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 89,
      "engine": "Codex",
      "ok": true,
      "chars": 8115
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 90,
      "engine": "Codex",
      "ok": true,
      "chars": 7934
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 91,
      "engine": "Codex",
      "ok": true,
      "chars": 8348
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 92,
      "engine": "Codex",
      "ok": true,
      "chars": 8328
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 93,
      "engine": "Codex",
      "ok": true,
      "chars": 8205
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 94,
      "engine": "Codex",
      "ok": true,
      "chars": 8408
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 95,
      "engine": "Codex",
      "ok": true,
      "chars": 8248
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 96,
      "engine": "Codex",
      "ok": true,
      "chars": 8078
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 97,
      "engine": "Codex",
      "ok": true,
      "chars": 8324
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 98,
      "engine": "Codex",
      "ok": true,
      "chars": 9214
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 99,
      "engine": "Codex",
      "ok": true,
      "chars": 8445
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
      "scope_level": "actividad",
      "cycle": 100,
      "engine": "Codex",
      "ok": true,
      "chars": 8318
    }
  ],
  "ok": true,
  "cancelled": false
}
```

## 20260621-055618 - memoria-editorial

```json
{
  "run_id": "20260621-055618",
  "source_scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
  "build_level": "interinstitucional",
  "propagation_mode": "recursivo",
  "iterations": 100,
  "engines": [
    "Codex"
  ],
  "timeout_seconds": 900,
  "scope_offset": 3,
  "scope_limit": 1,
  "full_plan_scope_count": 461,
  "batch_scope_count": 1,
  "built_scopes": [
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4"
  ],
  "cycles": [
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 1,
      "engine": "Codex",
      "ok": true,
      "chars": 8103
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 2,
      "engine": "Codex",
      "ok": true,
      "chars": 7189
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 3,
      "engine": "Codex",
      "ok": true,
      "chars": 7277
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 4,
      "engine": "Codex",
      "ok": true,
      "chars": 7843
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 5,
      "engine": "Codex",
      "ok": true,
      "chars": 8286
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 6,
      "engine": "Codex",
      "ok": true,
      "chars": 7918
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 7,
      "engine": "Codex",
      "ok": true,
      "chars": 7981
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 8,
      "engine": "Codex",
      "ok": true,
      "chars": 7779
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 9,
      "engine": "Codex",
      "ok": true,
      "chars": 7474
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 10,
      "engine": "Codex",
      "ok": true,
      "chars": 7208
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 11,
      "engine": "Codex",
      "ok": true,
      "chars": 8041
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 12,
      "engine": "Codex",
      "ok": true,
      "chars": 7967
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 13,
      "engine": "Codex",
      "ok": true,
      "chars": 7727
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 14,
      "engine": "Codex",
      "ok": true,
      "chars": 8560
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 15,
      "engine": "Codex",
      "ok": true,
      "chars": 7826
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 16,
      "engine": "Codex",
      "ok": true,
      "chars": 8108
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 17,
      "engine": "Codex",
      "ok": true,
      "chars": 7908
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 18,
      "engine": "Codex",
      "ok": true,
      "chars": 8815
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 19,
      "engine": "Codex",
      "ok": true,
      "chars": 7993
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 20,
      "engine": "Codex",
      "ok": true,
      "chars": 8008
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 21,
      "engine": "Codex",
      "ok": true,
      "chars": 7578
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 22,
      "engine": "Codex",
      "ok": true,
      "chars": 8307
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 23,
      "engine": "Codex",
      "ok": true,
      "chars": 7255
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 24,
      "engine": "Codex",
      "ok": true,
      "chars": 7808
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 25,
      "engine": "Codex",
      "ok": true,
      "chars": 7510
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 26,
      "engine": "Codex",
      "ok": true,
      "chars": 8031
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 27,
      "engine": "Codex",
      "ok": true,
      "chars": 8539
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 28,
      "engine": "Codex",
      "ok": true,
      "chars": 8093
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 29,
      "engine": "Codex",
      "ok": true,
      "chars": 7917
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 30,
      "engine": "Codex",
      "ok": true,
      "chars": 7762
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 31,
      "engine": "Codex",
      "ok": true,
      "chars": 8288
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 32,
      "engine": "Codex",
      "ok": true,
      "chars": 8232
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 33,
      "engine": "Codex",
      "ok": true,
      "chars": 7701
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 34,
      "engine": "Codex",
      "ok": true,
      "chars": 8133
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 35,
      "engine": "Codex",
      "ok": true,
      "chars": 7861
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 36,
      "engine": "Codex",
      "ok": true,
      "chars": 7656
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 37,
      "engine": "Codex",
      "ok": true,
      "chars": 7970
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 38,
      "engine": "Codex",
      "ok": true,
      "chars": 7583
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 39,
      "engine": "Codex",
      "ok": true,
      "chars": 8047
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 40,
      "engine": "Codex",
      "ok": true,
      "chars": 8284
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 41,
      "engine": "Codex",
      "ok": true,
      "chars": 8051
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 42,
      "engine": "Codex",
      "ok": true,
      "chars": 7673
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 43,
      "engine": "Codex",
      "ok": true,
      "chars": 7501
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 44,
      "engine": "Codex",
      "ok": true,
      "chars": 8200
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 45,
      "engine": "Codex",
      "ok": true,
      "chars": 7765
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 46,
      "engine": "Codex",
      "ok": true,
      "chars": 8022
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 47,
      "engine": "Codex",
      "ok": true,
      "chars": 8098
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 48,
      "engine": "Codex",
      "ok": true,
      "chars": 8482
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 49,
      "engine": "Codex",
      "ok": true,
      "chars": 7842
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 50,
      "engine": "Codex",
      "ok": true,
      "chars": 7959
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 51,
      "engine": "Codex",
      "ok": true,
      "chars": 7819
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 52,
      "engine": "Codex",
      "ok": true,
      "chars": 8183
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 53,
      "engine": "Codex",
      "ok": true,
      "chars": 8048
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 54,
      "engine": "Codex",
      "ok": true,
      "chars": 8204
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 55,
      "engine": "Codex",
      "ok": true,
      "chars": 8107
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 56,
      "engine": "Codex",
      "ok": true,
      "chars": 8172
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 57,
      "engine": "Codex",
      "ok": true,
      "chars": 7848
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 58,
      "engine": "Codex",
      "ok": true,
      "chars": 8203
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 59,
      "engine": "Codex",
      "ok": true,
      "chars": 7595
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 60,
      "engine": "Codex",
      "ok": true,
      "chars": 7382
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 61,
      "engine": "Codex",
      "ok": true,
      "chars": 7596
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 62,
      "engine": "Codex",
      "ok": true,
      "chars": 7939
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 63,
      "engine": "Codex",
      "ok": true,
      "chars": 7522
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 64,
      "engine": "Codex",
      "ok": true,
      "chars": 7855
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 65,
      "engine": "Codex",
      "ok": true,
      "chars": 8001
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 66,
      "engine": "Codex",
      "ok": true,
      "chars": 8814
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 67,
      "engine": "Codex",
      "ok": true,
      "chars": 7898
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 68,
      "engine": "Codex",
      "ok": true,
      "chars": 7990
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 69,
      "engine": "Codex",
      "ok": true,
      "chars": 8087
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 70,
      "engine": "Codex",
      "ok": true,
      "chars": 7499
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 71,
      "engine": "Codex",
      "ok": true,
      "chars": 8071
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 72,
      "engine": "Codex",
      "ok": true,
      "chars": 7423
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 73,
      "engine": "Codex",
      "ok": true,
      "chars": 8378
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 74,
      "engine": "Codex",
      "ok": true,
      "chars": 7760
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 75,
      "engine": "Codex",
      "ok": true,
      "chars": 7846
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 76,
      "engine": "Codex",
      "ok": true,
      "chars": 7801
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 77,
      "engine": "Codex",
      "ok": true,
      "chars": 7995
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 78,
      "engine": "Codex",
      "ok": true,
      "chars": 8588
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 79,
      "engine": "Codex",
      "ok": true,
      "chars": 8147
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 80,
      "engine": "Codex",
      "ok": true,
      "chars": 8031
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 81,
      "engine": "Codex",
      "ok": true,
      "chars": 7938
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 82,
      "engine": "Codex",
      "ok": true,
      "chars": 8052
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 83,
      "engine": "Codex",
      "ok": true,
      "chars": 7254
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 84,
      "engine": "Codex",
      "ok": true,
      "chars": 8297
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 85,
      "engine": "Codex",
      "ok": true,
      "chars": 7983
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 86,
      "engine": "Codex",
      "ok": true,
      "chars": 8162
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 87,
      "engine": "Codex",
      "ok": true,
      "chars": 8044
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 88,
      "engine": "Codex",
      "ok": true,
      "chars": 8138
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 89,
      "engine": "Codex",
      "ok": true,
      "chars": 8303
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 90,
      "engine": "Codex",
      "ok": true,
      "chars": 8557
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 91,
      "engine": "Codex",
      "ok": true,
      "chars": 7622
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 92,
      "engine": "Codex",
      "ok": true,
      "chars": 8205
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 93,
      "engine": "Codex",
      "ok": true,
      "chars": 8153
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 94,
      "engine": "Codex",
      "ok": true,
      "chars": 8755
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 95,
      "engine": "Codex",
      "ok": true,
      "chars": 8158
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 96,
      "engine": "Codex",
      "ok": true,
      "chars": 7842
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 97,
      "engine": "Codex",
      "ok": true,
      "chars": 7777
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 98,
      "engine": "Codex",
      "ok": true,
      "chars": 8126
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 99,
      "engine": "Codex",
      "ok": true,
      "chars": 8156
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4",
      "scope_level": "actividad",
      "cycle": 100,
      "engine": "Codex",
      "ok": true,
      "chars": 8439
    }
  ],
  "ok": true,
  "cancelled": false
}
```

## 20260621-062828 - memoria-editorial

```json
{
  "run_id": "20260621-062828",
  "source_scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
  "build_level": "interinstitucional",
  "propagation_mode": "recursivo",
  "iterations": 100,
  "engines": [
    "Codex"
  ],
  "timeout_seconds": 900,
  "scope_offset": 4,
  "scope_limit": 1,
  "full_plan_scope_count": 461,
  "batch_scope_count": 1,
  "built_scopes": [
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5"
  ],
  "cycles": [
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 1,
      "engine": "Codex",
      "ok": true,
      "chars": 8176
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 2,
      "engine": "Codex",
      "ok": true,
      "chars": 8294
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 3,
      "engine": "Codex",
      "ok": true,
      "chars": 7974
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 4,
      "engine": "Codex",
      "ok": true,
      "chars": 8181
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 5,
      "engine": "Codex",
      "ok": true,
      "chars": 8260
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 6,
      "engine": "Codex",
      "ok": true,
      "chars": 7921
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 7,
      "engine": "Codex",
      "ok": true,
      "chars": 8219
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 8,
      "engine": "Codex",
      "ok": true,
      "chars": 7607
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 9,
      "engine": "Codex",
      "ok": true,
      "chars": 8036
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 10,
      "engine": "Codex",
      "ok": true,
      "chars": 8106
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 11,
      "engine": "Codex",
      "ok": true,
      "chars": 8562
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 12,
      "engine": "Codex",
      "ok": true,
      "chars": 7790
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 13,
      "engine": "Codex",
      "ok": true,
      "chars": 8171
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 14,
      "engine": "Codex",
      "ok": true,
      "chars": 8271
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 15,
      "engine": "Codex",
      "ok": true,
      "chars": 8488
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 16,
      "engine": "Codex",
      "ok": true,
      "chars": 8163
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 17,
      "engine": "Codex",
      "ok": true,
      "chars": 8233
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 18,
      "engine": "Codex",
      "ok": true,
      "chars": 8404
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 19,
      "engine": "Codex",
      "ok": true,
      "chars": 8985
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 20,
      "engine": "Codex",
      "ok": true,
      "chars": 8243
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 21,
      "engine": "Codex",
      "ok": true,
      "chars": 8559
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 22,
      "engine": "Codex",
      "ok": true,
      "chars": 8664
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 23,
      "engine": "Codex",
      "ok": true,
      "chars": 8101
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 24,
      "engine": "Codex",
      "ok": true,
      "chars": 8261
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 25,
      "engine": "Codex",
      "ok": true,
      "chars": 8931
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 26,
      "engine": "Codex",
      "ok": true,
      "chars": 8485
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 27,
      "engine": "Codex",
      "ok": true,
      "chars": 8698
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 28,
      "engine": "Codex",
      "ok": true,
      "chars": 8500
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 29,
      "engine": "Codex",
      "ok": true,
      "chars": 8145
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 30,
      "engine": "Codex",
      "ok": true,
      "chars": 8378
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 31,
      "engine": "Codex",
      "ok": true,
      "chars": 8321
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 32,
      "engine": "Codex",
      "ok": true,
      "chars": 8757
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 33,
      "engine": "Codex",
      "ok": true,
      "chars": 8018
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 34,
      "engine": "Codex",
      "ok": true,
      "chars": 8347
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 35,
      "engine": "Codex",
      "ok": true,
      "chars": 8318
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 36,
      "engine": "Codex",
      "ok": true,
      "chars": 8018
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 37,
      "engine": "Codex",
      "ok": true,
      "chars": 8615
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 38,
      "engine": "Codex",
      "ok": true,
      "chars": 8459
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 39,
      "engine": "Codex",
      "ok": true,
      "chars": 8285
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 40,
      "engine": "Codex",
      "ok": true,
      "chars": 8296
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 41,
      "engine": "Codex",
      "ok": true,
      "chars": 8737
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 42,
      "engine": "Codex",
      "ok": true,
      "chars": 8632
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 43,
      "engine": "Codex",
      "ok": true,
      "chars": 8750
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 44,
      "engine": "Codex",
      "ok": true,
      "chars": 8293
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 45,
      "engine": "Codex",
      "ok": true,
      "chars": 8405
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 46,
      "engine": "Codex",
      "ok": true,
      "chars": 8932
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 47,
      "engine": "Codex",
      "ok": true,
      "chars": 8103
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 48,
      "engine": "Codex",
      "ok": true,
      "chars": 8634
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 49,
      "engine": "Codex",
      "ok": true,
      "chars": 8693
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 50,
      "engine": "Codex",
      "ok": true,
      "chars": 8627
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 51,
      "engine": "Codex",
      "ok": true,
      "chars": 8258
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 52,
      "engine": "Codex",
      "ok": true,
      "chars": 8188
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 53,
      "engine": "Codex",
      "ok": true,
      "chars": 9371
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 54,
      "engine": "Codex",
      "ok": true,
      "chars": 7817
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 55,
      "engine": "Codex",
      "ok": true,
      "chars": 8802
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 56,
      "engine": "Codex",
      "ok": true,
      "chars": 8660
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 57,
      "engine": "Codex",
      "ok": true,
      "chars": 8437
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 58,
      "engine": "Codex",
      "ok": true,
      "chars": 8538
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 59,
      "engine": "Codex",
      "ok": true,
      "chars": 8631
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 60,
      "engine": "Codex",
      "ok": true,
      "chars": 8137
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 61,
      "engine": "Codex",
      "ok": true,
      "chars": 8495
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 62,
      "engine": "Codex",
      "ok": true,
      "chars": 8817
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 63,
      "engine": "Codex",
      "ok": true,
      "chars": 8606
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 64,
      "engine": "Codex",
      "ok": true,
      "chars": 8662
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 65,
      "engine": "Codex",
      "ok": true,
      "chars": 8212
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 66,
      "engine": "Codex",
      "ok": true,
      "chars": 9134
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 67,
      "engine": "Codex",
      "ok": true,
      "chars": 7432
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 68,
      "engine": "Codex",
      "ok": true,
      "chars": 8163
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 69,
      "engine": "Codex",
      "ok": true,
      "chars": 8453
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 70,
      "engine": "Codex",
      "ok": true,
      "chars": 8734
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 71,
      "engine": "Codex",
      "ok": true,
      "chars": 8007
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 72,
      "engine": "Codex",
      "ok": true,
      "chars": 8606
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 73,
      "engine": "Codex",
      "ok": true,
      "chars": 8645
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 74,
      "engine": "Codex",
      "ok": true,
      "chars": 8199
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 75,
      "engine": "Codex",
      "ok": true,
      "chars": 8381
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 76,
      "engine": "Codex",
      "ok": true,
      "chars": 8081
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 77,
      "engine": "Codex",
      "ok": true,
      "chars": 8704
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 78,
      "engine": "Codex",
      "ok": true,
      "chars": 8152
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 79,
      "engine": "Codex",
      "ok": true,
      "chars": 8343
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 80,
      "engine": "Codex",
      "ok": true,
      "chars": 8824
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 81,
      "engine": "Codex",
      "ok": true,
      "chars": 7886
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 82,
      "engine": "Codex",
      "ok": true,
      "chars": 8702
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 83,
      "engine": "Codex",
      "ok": true,
      "chars": 8274
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 84,
      "engine": "Codex",
      "ok": true,
      "chars": 8308
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 85,
      "engine": "Codex",
      "ok": true,
      "chars": 8121
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 86,
      "engine": "Codex",
      "ok": true,
      "chars": 9336
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 87,
      "engine": "Codex",
      "ok": true,
      "chars": 7821
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 88,
      "engine": "Codex",
      "ok": true,
      "chars": 8646
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 89,
      "engine": "Codex",
      "ok": true,
      "chars": 8621
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 90,
      "engine": "Codex",
      "ok": true,
      "chars": 8222
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 91,
      "engine": "Codex",
      "ok": true,
      "chars": 9003
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 92,
      "engine": "Codex",
      "ok": true,
      "chars": 8622
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 93,
      "engine": "Codex",
      "ok": true,
      "chars": 8531
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 94,
      "engine": "Codex",
      "ok": true,
      "chars": 8910
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 95,
      "engine": "Codex",
      "ok": true,
      "chars": 8555
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 96,
      "engine": "Codex",
      "ok": true,
      "chars": 8613
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 97,
      "engine": "Codex",
      "ok": true,
      "chars": 8668
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 98,
      "engine": "Codex",
      "ok": true,
      "chars": 8250
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 99,
      "engine": "Codex",
      "ok": true,
      "chars": 8035
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
      "scope_level": "actividad",
      "cycle": 100,
      "engine": "Codex",
      "ok": true,
      "chars": 8604
    }
  ],
  "ok": true,
  "cancelled": false
}
```

## 20260621-070004 - memoria-editorial

```json
{
  "run_id": "20260621-070004",
  "source_scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
  "build_level": "interinstitucional",
  "propagation_mode": "recursivo",
  "iterations": 100,
  "engines": [
    "Codex"
  ],
  "timeout_seconds": 900,
  "scope_offset": 5,
  "scope_limit": 1,
  "full_plan_scope_count": 461,
  "batch_scope_count": 1,
  "built_scopes": [
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6"
  ],
  "cycles": [
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 1,
      "engine": "Codex",
      "ok": true,
      "chars": 8338
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 2,
      "engine": "Codex",
      "ok": true,
      "chars": 8761
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 3,
      "engine": "Codex",
      "ok": true,
      "chars": 9340
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 4,
      "engine": "Codex",
      "ok": true,
      "chars": 8490
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 5,
      "engine": "Codex",
      "ok": true,
      "chars": 9338
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 6,
      "engine": "Codex",
      "ok": true,
      "chars": 8795
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 7,
      "engine": "Codex",
      "ok": true,
      "chars": 8769
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 8,
      "engine": "Codex",
      "ok": true,
      "chars": 9477
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 9,
      "engine": "Codex",
      "ok": true,
      "chars": 8378
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 10,
      "engine": "Codex",
      "ok": true,
      "chars": 8826
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 11,
      "engine": "Codex",
      "ok": true,
      "chars": 8787
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 12,
      "engine": "Codex",
      "ok": true,
      "chars": 8664
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 13,
      "engine": "Codex",
      "ok": true,
      "chars": 9712
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 14,
      "engine": "Codex",
      "ok": true,
      "chars": 9188
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 15,
      "engine": "Codex",
      "ok": true,
      "chars": 8977
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 16,
      "engine": "Codex",
      "ok": true,
      "chars": 8785
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 17,
      "engine": "Codex",
      "ok": true,
      "chars": 8752
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 18,
      "engine": "Codex",
      "ok": true,
      "chars": 8617
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 19,
      "engine": "Codex",
      "ok": true,
      "chars": 9669
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 20,
      "engine": "Codex",
      "ok": true,
      "chars": 8346
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 21,
      "engine": "Codex",
      "ok": true,
      "chars": 8865
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 22,
      "engine": "Codex",
      "ok": true,
      "chars": 9167
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 23,
      "engine": "Codex",
      "ok": true,
      "chars": 8854
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 24,
      "engine": "Codex",
      "ok": true,
      "chars": 8891
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 25,
      "engine": "Codex",
      "ok": true,
      "chars": 9228
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 26,
      "engine": "Codex",
      "ok": true,
      "chars": 8236
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 27,
      "engine": "Codex",
      "ok": true,
      "chars": 8691
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 28,
      "engine": "Codex",
      "ok": true,
      "chars": 9049
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 29,
      "engine": "Codex",
      "ok": true,
      "chars": 8847
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 30,
      "engine": "Codex",
      "ok": true,
      "chars": 8592
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 31,
      "engine": "Codex",
      "ok": true,
      "chars": 8462
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 32,
      "engine": "Codex",
      "ok": true,
      "chars": 8648
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 33,
      "engine": "Codex",
      "ok": true,
      "chars": 9084
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 34,
      "engine": "Codex",
      "ok": true,
      "chars": 9154
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 35,
      "engine": "Codex",
      "ok": true,
      "chars": 8908
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 36,
      "engine": "Codex",
      "ok": true,
      "chars": 7828
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 37,
      "engine": "Codex",
      "ok": true,
      "chars": 8056
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 38,
      "engine": "Codex",
      "ok": true,
      "chars": 8977
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 39,
      "engine": "Codex",
      "ok": true,
      "chars": 8869
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 40,
      "engine": "Codex",
      "ok": true,
      "chars": 8219
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 41,
      "engine": "Codex",
      "ok": true,
      "chars": 8984
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 42,
      "engine": "Codex",
      "ok": true,
      "chars": 8188
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 43,
      "engine": "Codex",
      "ok": true,
      "chars": 8702
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 44,
      "engine": "Codex",
      "ok": true,
      "chars": 9155
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 45,
      "engine": "Codex",
      "ok": true,
      "chars": 8623
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 46,
      "engine": "Codex",
      "ok": true,
      "chars": 9194
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 47,
      "engine": "Codex",
      "ok": true,
      "chars": 8099
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 48,
      "engine": "Codex",
      "ok": true,
      "chars": 9116
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 49,
      "engine": "Codex",
      "ok": true,
      "chars": 8978
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 50,
      "engine": "Codex",
      "ok": true,
      "chars": 8777
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 51,
      "engine": "Codex",
      "ok": true,
      "chars": 9218
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 52,
      "engine": "Codex",
      "ok": true,
      "chars": 9840
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 53,
      "engine": "Codex",
      "ok": true,
      "chars": 8051
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 54,
      "engine": "Codex",
      "ok": true,
      "chars": 8933
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 55,
      "engine": "Codex",
      "ok": true,
      "chars": 8910
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 56,
      "engine": "Codex",
      "ok": true,
      "chars": 8266
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 57,
      "engine": "Codex",
      "ok": true,
      "chars": 8824
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 58,
      "engine": "Codex",
      "ok": true,
      "chars": 9499
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 59,
      "engine": "Codex",
      "ok": true,
      "chars": 8662
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 60,
      "engine": "Codex",
      "ok": true,
      "chars": 8762
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 61,
      "engine": "Codex",
      "ok": true,
      "chars": 8536
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 62,
      "engine": "Codex",
      "ok": true,
      "chars": 8984
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 63,
      "engine": "Codex",
      "ok": true,
      "chars": 8967
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 64,
      "engine": "Codex",
      "ok": true,
      "chars": 9253
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 65,
      "engine": "Codex",
      "ok": true,
      "chars": 8891
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 66,
      "engine": "Codex",
      "ok": true,
      "chars": 9070
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 67,
      "engine": "Codex",
      "ok": true,
      "chars": 9363
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 68,
      "engine": "Codex",
      "ok": true,
      "chars": 8949
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 69,
      "engine": "Codex",
      "ok": true,
      "chars": 8238
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 70,
      "engine": "Codex",
      "ok": true,
      "chars": 8811
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 71,
      "engine": "Codex",
      "ok": true,
      "chars": 8656
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 72,
      "engine": "Codex",
      "ok": true,
      "chars": 8971
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 73,
      "engine": "Codex",
      "ok": true,
      "chars": 9232
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 74,
      "engine": "Codex",
      "ok": true,
      "chars": 8160
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 75,
      "engine": "Codex",
      "ok": true,
      "chars": 8838
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 76,
      "engine": "Codex",
      "ok": true,
      "chars": 9055
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 77,
      "engine": "Codex",
      "ok": true,
      "chars": 8524
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 78,
      "engine": "Codex",
      "ok": true,
      "chars": 9306
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 79,
      "engine": "Codex",
      "ok": true,
      "chars": 9368
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 80,
      "engine": "Codex",
      "ok": true,
      "chars": 8144
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 81,
      "engine": "Codex",
      "ok": true,
      "chars": 8585
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 82,
      "engine": "Codex",
      "ok": true,
      "chars": 8188
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 83,
      "engine": "Codex",
      "ok": true,
      "chars": 9227
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 84,
      "engine": "Codex",
      "ok": true,
      "chars": 8795
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 85,
      "engine": "Codex",
      "ok": true,
      "chars": 8798
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 86,
      "engine": "Codex",
      "ok": true,
      "chars": 8693
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 87,
      "engine": "Codex",
      "ok": true,
      "chars": 8731
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 88,
      "engine": "Codex",
      "ok": true,
      "chars": 8989
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 89,
      "engine": "Codex",
      "ok": true,
      "chars": 8052
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 90,
      "engine": "Codex",
      "ok": true,
      "chars": 8962
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 91,
      "engine": "Codex",
      "ok": true,
      "chars": 8458
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 92,
      "engine": "Codex",
      "ok": true,
      "chars": 8624
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 93,
      "engine": "Codex",
      "ok": true,
      "chars": 7694
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 94,
      "engine": "Codex",
      "ok": true,
      "chars": 8934
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 95,
      "engine": "Codex",
      "ok": true,
      "chars": 8599
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 96,
      "engine": "Codex",
      "ok": true,
      "chars": 8328
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 97,
      "engine": "Codex",
      "ok": true,
      "chars": 9128
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 98,
      "engine": "Codex",
      "ok": true,
      "chars": 9106
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 99,
      "engine": "Codex",
      "ok": true,
      "chars": 9169
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
      "scope_level": "actividad",
      "cycle": 100,
      "engine": "Codex",
      "ok": true,
      "chars": 8197
    }
  ],
  "ok": true,
  "cancelled": false
}
```

## 20260621-073412 - memoria-editorial

```json
{
  "run_id": "20260621-073412",
  "source_scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
  "build_level": "interinstitucional",
  "propagation_mode": "recursivo",
  "iterations": 100,
  "engines": [
    "Codex"
  ],
  "timeout_seconds": 900,
  "scope_offset": 6,
  "scope_limit": 1,
  "full_plan_scope_count": 461,
  "batch_scope_count": 1,
  "built_scopes": [
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde"
  ],
  "cycles": [
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 1,
      "engine": "Codex",
      "ok": true,
      "chars": 8171
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 2,
      "engine": "Codex",
      "ok": true,
      "chars": 8032
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 3,
      "engine": "Codex",
      "ok": true,
      "chars": 8264
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 4,
      "engine": "Codex",
      "ok": true,
      "chars": 8211
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 5,
      "engine": "Codex",
      "ok": true,
      "chars": 8540
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 6,
      "engine": "Codex",
      "ok": true,
      "chars": 9028
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 7,
      "engine": "Codex",
      "ok": true,
      "chars": 9715
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 8,
      "engine": "Codex",
      "ok": true,
      "chars": 8384
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 9,
      "engine": "Codex",
      "ok": true,
      "chars": 8561
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 10,
      "engine": "Codex",
      "ok": true,
      "chars": 7707
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 11,
      "engine": "Codex",
      "ok": true,
      "chars": 8123
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 12,
      "engine": "Codex",
      "ok": true,
      "chars": 7834
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 13,
      "engine": "Codex",
      "ok": true,
      "chars": 8358
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 14,
      "engine": "Codex",
      "ok": true,
      "chars": 8548
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 15,
      "engine": "Codex",
      "ok": true,
      "chars": 8335
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 16,
      "engine": "Codex",
      "ok": true,
      "chars": 8092
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 17,
      "engine": "Codex",
      "ok": true,
      "chars": 8373
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 18,
      "engine": "Codex",
      "ok": true,
      "chars": 8510
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 19,
      "engine": "Codex",
      "ok": true,
      "chars": 8143
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 20,
      "engine": "Codex",
      "ok": true,
      "chars": 8578
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 21,
      "engine": "Codex",
      "ok": true,
      "chars": 8651
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 22,
      "engine": "Codex",
      "ok": true,
      "chars": 8375
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 23,
      "engine": "Codex",
      "ok": true,
      "chars": 8473
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 24,
      "engine": "Codex",
      "ok": true,
      "chars": 8086
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 25,
      "engine": "Codex",
      "ok": true,
      "chars": 8319
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 26,
      "engine": "Codex",
      "ok": true,
      "chars": 8055
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 27,
      "engine": "Codex",
      "ok": true,
      "chars": 8316
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 28,
      "engine": "Codex",
      "ok": true,
      "chars": 8001
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 29,
      "engine": "Codex",
      "ok": true,
      "chars": 7936
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 30,
      "engine": "Codex",
      "ok": true,
      "chars": 7869
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 31,
      "engine": "Codex",
      "ok": true,
      "chars": 7908
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 32,
      "engine": "Codex",
      "ok": true,
      "chars": 8631
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 33,
      "engine": "Codex",
      "ok": true,
      "chars": 8500
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 34,
      "engine": "Codex",
      "ok": true,
      "chars": 8530
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 35,
      "engine": "Codex",
      "ok": true,
      "chars": 8503
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 36,
      "engine": "Codex",
      "ok": true,
      "chars": 8686
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 37,
      "engine": "Codex",
      "ok": true,
      "chars": 7956
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 38,
      "engine": "Codex",
      "ok": true,
      "chars": 8117
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 39,
      "engine": "Codex",
      "ok": true,
      "chars": 8435
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 40,
      "engine": "Codex",
      "ok": true,
      "chars": 8525
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 41,
      "engine": "Codex",
      "ok": true,
      "chars": 8446
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 42,
      "engine": "Codex",
      "ok": true,
      "chars": 8355
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 43,
      "engine": "Codex",
      "ok": true,
      "chars": 8071
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 44,
      "engine": "Codex",
      "ok": true,
      "chars": 8556
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 45,
      "engine": "Codex",
      "ok": true,
      "chars": 8443
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 46,
      "engine": "Codex",
      "ok": true,
      "chars": 7666
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 47,
      "engine": "Codex",
      "ok": true,
      "chars": 8370
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 48,
      "engine": "Codex",
      "ok": true,
      "chars": 8549
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 49,
      "engine": "Codex",
      "ok": true,
      "chars": 8501
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 50,
      "engine": "Codex",
      "ok": true,
      "chars": 8386
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 51,
      "engine": "Codex",
      "ok": true,
      "chars": 8062
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 52,
      "engine": "Codex",
      "ok": true,
      "chars": 8276
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 53,
      "engine": "Codex",
      "ok": true,
      "chars": 7856
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 54,
      "engine": "Codex",
      "ok": true,
      "chars": 8085
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 55,
      "engine": "Codex",
      "ok": true,
      "chars": 8434
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 56,
      "engine": "Codex",
      "ok": true,
      "chars": 7861
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 57,
      "engine": "Codex",
      "ok": true,
      "chars": 8387
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 58,
      "engine": "Codex",
      "ok": true,
      "chars": 8597
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 59,
      "engine": "Codex",
      "ok": true,
      "chars": 8272
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 60,
      "engine": "Codex",
      "ok": true,
      "chars": 8385
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 61,
      "engine": "Codex",
      "ok": true,
      "chars": 7659
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 62,
      "engine": "Codex",
      "ok": true,
      "chars": 8271
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 63,
      "engine": "Codex",
      "ok": true,
      "chars": 8191
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 64,
      "engine": "Codex",
      "ok": true,
      "chars": 8128
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 65,
      "engine": "Codex",
      "ok": true,
      "chars": 8408
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 66,
      "engine": "Codex",
      "ok": true,
      "chars": 8260
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 67,
      "engine": "Codex",
      "ok": true,
      "chars": 8234
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 68,
      "engine": "Codex",
      "ok": true,
      "chars": 9063
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 69,
      "engine": "Codex",
      "ok": true,
      "chars": 8946
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 70,
      "engine": "Codex",
      "ok": true,
      "chars": 8541
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 71,
      "engine": "Codex",
      "ok": true,
      "chars": 8341
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 72,
      "engine": "Codex",
      "ok": true,
      "chars": 8359
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 73,
      "engine": "Codex",
      "ok": true,
      "chars": 8486
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 74,
      "engine": "Codex",
      "ok": true,
      "chars": 8526
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 75,
      "engine": "Codex",
      "ok": true,
      "chars": 8582
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 76,
      "engine": "Codex",
      "ok": true,
      "chars": 8400
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 77,
      "engine": "Codex",
      "ok": true,
      "chars": 8950
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 78,
      "engine": "Codex",
      "ok": true,
      "chars": 8631
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 79,
      "engine": "Codex",
      "ok": true,
      "chars": 8406
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 80,
      "engine": "Codex",
      "ok": true,
      "chars": 8667
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 81,
      "engine": "Codex",
      "ok": true,
      "chars": 8769
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 82,
      "engine": "Codex",
      "ok": true,
      "chars": 8167
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 83,
      "engine": "Codex",
      "ok": true,
      "chars": 8262
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 84,
      "engine": "Codex",
      "ok": true,
      "chars": 8671
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 85,
      "engine": "Codex",
      "ok": true,
      "chars": 8229
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 86,
      "engine": "Codex",
      "ok": true,
      "chars": 8250
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 87,
      "engine": "Codex",
      "ok": true,
      "chars": 8469
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 88,
      "engine": "Codex",
      "ok": true,
      "chars": 8466
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 89,
      "engine": "Codex",
      "ok": true,
      "chars": 7880
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 90,
      "engine": "Codex",
      "ok": true,
      "chars": 7969
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 91,
      "engine": "Codex",
      "ok": true,
      "chars": 8749
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 92,
      "engine": "Codex",
      "ok": true,
      "chars": 8088
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 93,
      "engine": "Codex",
      "ok": true,
      "chars": 8994
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 94,
      "engine": "Codex",
      "ok": true,
      "chars": 8145
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 95,
      "engine": "Codex",
      "ok": true,
      "chars": 8569
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 96,
      "engine": "Codex",
      "ok": true,
      "chars": 8545
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 97,
      "engine": "Codex",
      "ok": true,
      "chars": 7909
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 98,
      "engine": "Codex",
      "ok": true,
      "chars": 8028
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 99,
      "engine": "Codex",
      "ok": true,
      "chars": 8093
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
      "scope_level": "materia",
      "cycle": 100,
      "engine": "Codex",
      "ok": true,
      "chars": 8242
    }
  ],
  "ok": true,
  "cancelled": false
}
```

## 20260621-080646 - memoria-editorial

```json
{
  "run_id": "20260621-080646",
  "source_scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
  "build_level": "interinstitucional",
  "propagation_mode": "recursivo",
  "iterations": 100,
  "engines": [
    "Codex"
  ],
  "timeout_seconds": 900,
  "scope_offset": 7,
  "scope_limit": 1,
  "full_plan_scope_count": 461,
  "batch_scope_count": 1,
  "built_scopes": [
    "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde"
  ],
  "cycles": [
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 1,
      "engine": "Codex",
      "ok": true,
      "chars": 8173
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 2,
      "engine": "Codex",
      "ok": true,
      "chars": 7815
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 3,
      "engine": "Codex",
      "ok": true,
      "chars": 8383
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 4,
      "engine": "Codex",
      "ok": true,
      "chars": 8334
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 5,
      "engine": "Codex",
      "ok": true,
      "chars": 8043
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 6,
      "engine": "Codex",
      "ok": true,
      "chars": 8717
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 7,
      "engine": "Codex",
      "ok": true,
      "chars": 7940
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 8,
      "engine": "Codex",
      "ok": true,
      "chars": 7603
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 9,
      "engine": "Codex",
      "ok": true,
      "chars": 8158
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 10,
      "engine": "Codex",
      "ok": true,
      "chars": 7828
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 11,
      "engine": "Codex",
      "ok": true,
      "chars": 8167
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 12,
      "engine": "Codex",
      "ok": true,
      "chars": 8827
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 13,
      "engine": "Codex",
      "ok": true,
      "chars": 8260
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 14,
      "engine": "Codex",
      "ok": true,
      "chars": 8975
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 15,
      "engine": "Codex",
      "ok": true,
      "chars": 8399
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 16,
      "engine": "Codex",
      "ok": true,
      "chars": 7854
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 17,
      "engine": "Codex",
      "ok": true,
      "chars": 7819
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 18,
      "engine": "Codex",
      "ok": true,
      "chars": 7795
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 19,
      "engine": "Codex",
      "ok": true,
      "chars": 8575
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 20,
      "engine": "Codex",
      "ok": true,
      "chars": 8436
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 21,
      "engine": "Codex",
      "ok": true,
      "chars": 8435
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 22,
      "engine": "Codex",
      "ok": true,
      "chars": 8047
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 23,
      "engine": "Codex",
      "ok": true,
      "chars": 8116
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 24,
      "engine": "Codex",
      "ok": true,
      "chars": 8452
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 25,
      "engine": "Codex",
      "ok": true,
      "chars": 7910
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 26,
      "engine": "Codex",
      "ok": true,
      "chars": 7816
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 27,
      "engine": "Codex",
      "ok": true,
      "chars": 8278
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 28,
      "engine": "Codex",
      "ok": true,
      "chars": 7894
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 29,
      "engine": "Codex",
      "ok": true,
      "chars": 8321
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 30,
      "engine": "Codex",
      "ok": true,
      "chars": 7782
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 31,
      "engine": "Codex",
      "ok": true,
      "chars": 7719
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 32,
      "engine": "Codex",
      "ok": true,
      "chars": 8392
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 33,
      "engine": "Codex",
      "ok": true,
      "chars": 8481
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 34,
      "engine": "Codex",
      "ok": true,
      "chars": 8847
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 35,
      "engine": "Codex",
      "ok": true,
      "chars": 7229
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 36,
      "engine": "Codex",
      "ok": true,
      "chars": 8262
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 37,
      "engine": "Codex",
      "ok": true,
      "chars": 7949
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 38,
      "engine": "Codex",
      "ok": true,
      "chars": 8394
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 39,
      "engine": "Codex",
      "ok": true,
      "chars": 7664
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 40,
      "engine": "Codex",
      "ok": true,
      "chars": 8611
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 41,
      "engine": "Codex",
      "ok": true,
      "chars": 8448
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 42,
      "engine": "Codex",
      "ok": true,
      "chars": 8064
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 43,
      "engine": "Codex",
      "ok": true,
      "chars": 8137
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 44,
      "engine": "Codex",
      "ok": true,
      "chars": 8174
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 45,
      "engine": "Codex",
      "ok": true,
      "chars": 8169
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 46,
      "engine": "Codex",
      "ok": true,
      "chars": 8390
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 47,
      "engine": "Codex",
      "ok": true,
      "chars": 8509
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 48,
      "engine": "Codex",
      "ok": true,
      "chars": 7643
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 49,
      "engine": "Codex",
      "ok": true,
      "chars": 8570
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 50,
      "engine": "Codex",
      "ok": true,
      "chars": 8658
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 51,
      "engine": "Codex",
      "ok": true,
      "chars": 8127
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 52,
      "engine": "Codex",
      "ok": true,
      "chars": 7994
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 53,
      "engine": "Codex",
      "ok": true,
      "chars": 7978
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 54,
      "engine": "Codex",
      "ok": true,
      "chars": 8706
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 55,
      "engine": "Codex",
      "ok": true,
      "chars": 8247
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 56,
      "engine": "Codex",
      "ok": true,
      "chars": 8610
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 57,
      "engine": "Codex",
      "ok": true,
      "chars": 7982
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 58,
      "engine": "Codex",
      "ok": true,
      "chars": 7797
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 59,
      "engine": "Codex",
      "ok": true,
      "chars": 8067
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 60,
      "engine": "Codex",
      "ok": true,
      "chars": 8090
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 61,
      "engine": "Codex",
      "ok": true,
      "chars": 8038
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 62,
      "engine": "Codex",
      "ok": true,
      "chars": 7764
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 63,
      "engine": "Codex",
      "ok": true,
      "chars": 8393
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 64,
      "engine": "Codex",
      "ok": true,
      "chars": 7887
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 65,
      "engine": "Codex",
      "ok": true,
      "chars": 8373
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 66,
      "engine": "Codex",
      "ok": true,
      "chars": 8044
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 67,
      "engine": "Codex",
      "ok": true,
      "chars": 8395
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 68,
      "engine": "Codex",
      "ok": true,
      "chars": 7813
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 69,
      "engine": "Codex",
      "ok": true,
      "chars": 7802
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 70,
      "engine": "Codex",
      "ok": true,
      "chars": 8179
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 71,
      "engine": "Codex",
      "ok": true,
      "chars": 8297
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 72,
      "engine": "Codex",
      "ok": true,
      "chars": 8627
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 73,
      "engine": "Codex",
      "ok": true,
      "chars": 7814
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 74,
      "engine": "Codex",
      "ok": true,
      "chars": 8239
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 75,
      "engine": "Codex",
      "ok": true,
      "chars": 8358
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 76,
      "engine": "Codex",
      "ok": true,
      "chars": 7685
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 77,
      "engine": "Codex",
      "ok": true,
      "chars": 8253
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 78,
      "engine": "Codex",
      "ok": true,
      "chars": 8172
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 79,
      "engine": "Codex",
      "ok": true,
      "chars": 7317
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 80,
      "engine": "Codex",
      "ok": true,
      "chars": 7934
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 81,
      "engine": "Codex",
      "ok": true,
      "chars": 8597
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 82,
      "engine": "Codex",
      "ok": true,
      "chars": 7852
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 83,
      "engine": "Codex",
      "ok": true,
      "chars": 7572
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 84,
      "engine": "Codex",
      "ok": true,
      "chars": 8247
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 85,
      "engine": "Codex",
      "ok": true,
      "chars": 8149
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 86,
      "engine": "Codex",
      "ok": true,
      "chars": 8288
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 87,
      "engine": "Codex",
      "ok": true,
      "chars": 7698
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 88,
      "engine": "Codex",
      "ok": true,
      "chars": 8208
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 89,
      "engine": "Codex",
      "ok": true,
      "chars": 8058
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 90,
      "engine": "Codex",
      "ok": true,
      "chars": 8113
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 91,
      "engine": "Codex",
      "ok": true,
      "chars": 7866
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 92,
      "engine": "Codex",
      "ok": true,
      "chars": 8125
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 93,
      "engine": "Codex",
      "ok": true,
      "chars": 7805
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 94,
      "engine": "Codex",
      "ok": true,
      "chars": 8083
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 95,
      "engine": "Codex",
      "ok": true,
      "chars": 8008
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 96,
      "engine": "Codex",
      "ok": true,
      "chars": 8594
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 97,
      "engine": "Codex",
      "ok": true,
      "chars": 7851
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 98,
      "engine": "Codex",
      "ok": true,
      "chars": 8354
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 99,
      "engine": "Codex",
      "ok": true,
      "chars": 8420
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
      "scope_level": "materia",
      "cycle": 100,
      "engine": "Codex",
      "ok": true,
      "chars": 7680
    }
  ],
  "ok": true,
  "cancelled": false
}
```

## 20260621-083802 - memoria-editorial

```json
{
  "run_id": "20260621-083802",
  "source_scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
  "build_level": "interinstitucional",
  "propagation_mode": "recursivo",
  "iterations": 100,
  "engines": [
    "Codex"
  ],
  "timeout_seconds": 900,
  "scope_offset": 8,
  "scope_limit": 1,
  "full_plan_scope_count": 461,
  "batch_scope_count": 1,
  "built_scopes": [
    "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde"
  ],
  "cycles": [
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 1,
      "engine": "Codex",
      "ok": true,
      "chars": 7809
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 2,
      "engine": "Codex",
      "ok": true,
      "chars": 8781
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 3,
      "engine": "Codex",
      "ok": true,
      "chars": 8366
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 4,
      "engine": "Codex",
      "ok": true,
      "chars": 9158
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 5,
      "engine": "Codex",
      "ok": true,
      "chars": 8648
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 6,
      "engine": "Codex",
      "ok": true,
      "chars": 8331
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 7,
      "engine": "Codex",
      "ok": true,
      "chars": 7791
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 8,
      "engine": "Codex",
      "ok": true,
      "chars": 8608
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 9,
      "engine": "Codex",
      "ok": true,
      "chars": 7966
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 10,
      "engine": "Codex",
      "ok": true,
      "chars": 8867
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 11,
      "engine": "Codex",
      "ok": true,
      "chars": 8604
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 12,
      "engine": "Codex",
      "ok": true,
      "chars": 7701
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 13,
      "engine": "Codex",
      "ok": true,
      "chars": 8623
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 14,
      "engine": "Codex",
      "ok": true,
      "chars": 9151
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 15,
      "engine": "Codex",
      "ok": true,
      "chars": 7881
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 16,
      "engine": "Codex",
      "ok": true,
      "chars": 9206
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 17,
      "engine": "Codex",
      "ok": true,
      "chars": 9216
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 18,
      "engine": "Codex",
      "ok": true,
      "chars": 8719
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 19,
      "engine": "Codex",
      "ok": true,
      "chars": 7937
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 20,
      "engine": "Codex",
      "ok": true,
      "chars": 7587
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 21,
      "engine": "Codex",
      "ok": true,
      "chars": 8633
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 22,
      "engine": "Codex",
      "ok": true,
      "chars": 8457
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 23,
      "engine": "Codex",
      "ok": true,
      "chars": 9266
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 24,
      "engine": "Codex",
      "ok": true,
      "chars": 8673
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 25,
      "engine": "Codex",
      "ok": true,
      "chars": 8590
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 26,
      "engine": "Codex",
      "ok": true,
      "chars": 8734
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 27,
      "engine": "Codex",
      "ok": true,
      "chars": 8048
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 28,
      "engine": "Codex",
      "ok": true,
      "chars": 7949
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 29,
      "engine": "Codex",
      "ok": true,
      "chars": 8431
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 30,
      "engine": "Codex",
      "ok": true,
      "chars": 8093
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 31,
      "engine": "Codex",
      "ok": true,
      "chars": 8334
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 32,
      "engine": "Codex",
      "ok": true,
      "chars": 8233
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 33,
      "engine": "Codex",
      "ok": true,
      "chars": 8845
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 34,
      "engine": "Codex",
      "ok": true,
      "chars": 8398
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 35,
      "engine": "Codex",
      "ok": true,
      "chars": 8944
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 36,
      "engine": "Codex",
      "ok": true,
      "chars": 8593
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 37,
      "engine": "Codex",
      "ok": true,
      "chars": 8803
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 38,
      "engine": "Codex",
      "ok": true,
      "chars": 8055
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 39,
      "engine": "Codex",
      "ok": true,
      "chars": 8773
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 40,
      "engine": "Codex",
      "ok": true,
      "chars": 8743
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 41,
      "engine": "Codex",
      "ok": true,
      "chars": 8109
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 42,
      "engine": "Codex",
      "ok": true,
      "chars": 8021
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 43,
      "engine": "Codex",
      "ok": true,
      "chars": 7734
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 44,
      "engine": "Codex",
      "ok": true,
      "chars": 8232
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 45,
      "engine": "Codex",
      "ok": true,
      "chars": 8330
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 46,
      "engine": "Codex",
      "ok": true,
      "chars": 8086
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 47,
      "engine": "Codex",
      "ok": true,
      "chars": 7973
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 48,
      "engine": "Codex",
      "ok": true,
      "chars": 8627
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 49,
      "engine": "Codex",
      "ok": true,
      "chars": 8161
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 50,
      "engine": "Codex",
      "ok": true,
      "chars": 8256
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 51,
      "engine": "Codex",
      "ok": true,
      "chars": 8157
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 52,
      "engine": "Codex",
      "ok": true,
      "chars": 8619
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 53,
      "engine": "Codex",
      "ok": true,
      "chars": 8217
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 54,
      "engine": "Codex",
      "ok": true,
      "chars": 8005
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 55,
      "engine": "Codex",
      "ok": true,
      "chars": 8360
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 56,
      "engine": "Codex",
      "ok": true,
      "chars": 8272
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 57,
      "engine": "Codex",
      "ok": true,
      "chars": 8296
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 58,
      "engine": "Codex",
      "ok": true,
      "chars": 8038
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 59,
      "engine": "Codex",
      "ok": true,
      "chars": 8568
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 60,
      "engine": "Codex",
      "ok": true,
      "chars": 7975
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 61,
      "engine": "Codex",
      "ok": true,
      "chars": 8419
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 62,
      "engine": "Codex",
      "ok": true,
      "chars": 8094
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 63,
      "engine": "Codex",
      "ok": true,
      "chars": 8222
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 64,
      "engine": "Codex",
      "ok": true,
      "chars": 8250
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 65,
      "engine": "Codex",
      "ok": true,
      "chars": 8816
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 66,
      "engine": "Codex",
      "ok": true,
      "chars": 8434
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 67,
      "engine": "Codex",
      "ok": true,
      "chars": 8148
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 68,
      "engine": "Codex",
      "ok": true,
      "chars": 8149
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 69,
      "engine": "Codex",
      "ok": true,
      "chars": 8560
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 70,
      "engine": "Codex",
      "ok": true,
      "chars": 8256
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 71,
      "engine": "Codex",
      "ok": true,
      "chars": 8297
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 72,
      "engine": "Codex",
      "ok": true,
      "chars": 8167
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 73,
      "engine": "Codex",
      "ok": true,
      "chars": 9331
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 74,
      "engine": "Codex",
      "ok": true,
      "chars": 7257
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 75,
      "engine": "Codex",
      "ok": true,
      "chars": 8645
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 76,
      "engine": "Codex",
      "ok": true,
      "chars": 7967
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 77,
      "engine": "Codex",
      "ok": true,
      "chars": 8322
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 78,
      "engine": "Codex",
      "ok": true,
      "chars": 8149
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 79,
      "engine": "Codex",
      "ok": true,
      "chars": 9093
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 80,
      "engine": "Codex",
      "ok": true,
      "chars": 8384
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 81,
      "engine": "Codex",
      "ok": true,
      "chars": 8829
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 82,
      "engine": "Codex",
      "ok": true,
      "chars": 7963
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 83,
      "engine": "Codex",
      "ok": true,
      "chars": 8557
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 84,
      "engine": "Codex",
      "ok": true,
      "chars": 8386
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 85,
      "engine": "Codex",
      "ok": true,
      "chars": 8809
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 86,
      "engine": "Codex",
      "ok": true,
      "chars": 8416
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 87,
      "engine": "Codex",
      "ok": true,
      "chars": 8135
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 88,
      "engine": "Codex",
      "ok": true,
      "chars": 7869
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 89,
      "engine": "Codex",
      "ok": true,
      "chars": 8493
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 90,
      "engine": "Codex",
      "ok": true,
      "chars": 8817
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 91,
      "engine": "Codex",
      "ok": true,
      "chars": 8205
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 92,
      "engine": "Codex",
      "ok": true,
      "chars": 8307
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 93,
      "engine": "Codex",
      "ok": true,
      "chars": 8124
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 94,
      "engine": "Codex",
      "ok": true,
      "chars": 8778
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 95,
      "engine": "Codex",
      "ok": true,
      "chars": 8343
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 96,
      "engine": "Codex",
      "ok": true,
      "chars": 7960
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 97,
      "engine": "Codex",
      "ok": true,
      "chars": 8839
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 98,
      "engine": "Codex",
      "ok": true,
      "chars": 8684
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 99,
      "engine": "Codex",
      "ok": true,
      "chars": 8089
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
      "scope_level": "materia",
      "cycle": 100,
      "engine": "Codex",
      "ok": true,
      "chars": 8486
    }
  ],
  "ok": true,
  "cancelled": false
}
```

## 20260621-090923 - memoria-editorial

```json
{
  "run_id": "20260621-090923",
  "source_scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
  "build_level": "interinstitucional",
  "propagation_mode": "recursivo",
  "iterations": 100,
  "engines": [
    "Codex"
  ],
  "timeout_seconds": 900,
  "scope_offset": 9,
  "scope_limit": 1,
  "full_plan_scope_count": 461,
  "batch_scope_count": 1,
  "built_scopes": [
    "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1"
  ],
  "cycles": [
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 1,
      "engine": "Codex",
      "ok": true,
      "chars": 8860
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 2,
      "engine": "Codex",
      "ok": true,
      "chars": 8303
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 3,
      "engine": "Codex",
      "ok": true,
      "chars": 7691
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 4,
      "engine": "Codex",
      "ok": true,
      "chars": 8112
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 5,
      "engine": "Codex",
      "ok": true,
      "chars": 8519
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 6,
      "engine": "Codex",
      "ok": true,
      "chars": 8547
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 7,
      "engine": "Codex",
      "ok": true,
      "chars": 8147
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 8,
      "engine": "Codex",
      "ok": true,
      "chars": 8494
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 9,
      "engine": "Codex",
      "ok": true,
      "chars": 8687
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 10,
      "engine": "Codex",
      "ok": true,
      "chars": 8400
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 11,
      "engine": "Codex",
      "ok": true,
      "chars": 8545
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 12,
      "engine": "Codex",
      "ok": true,
      "chars": 8699
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 13,
      "engine": "Codex",
      "ok": true,
      "chars": 8066
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 14,
      "engine": "Codex",
      "ok": true,
      "chars": 8406
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 15,
      "engine": "Codex",
      "ok": true,
      "chars": 8506
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 16,
      "engine": "Codex",
      "ok": true,
      "chars": 8726
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 17,
      "engine": "Codex",
      "ok": true,
      "chars": 8228
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 18,
      "engine": "Codex",
      "ok": true,
      "chars": 7930
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 19,
      "engine": "Codex",
      "ok": true,
      "chars": 7880
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 20,
      "engine": "Codex",
      "ok": true,
      "chars": 8576
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 21,
      "engine": "Codex",
      "ok": true,
      "chars": 8605
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 22,
      "engine": "Codex",
      "ok": true,
      "chars": 8489
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 23,
      "engine": "Codex",
      "ok": true,
      "chars": 8729
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 24,
      "engine": "Codex",
      "ok": true,
      "chars": 8473
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 25,
      "engine": "Codex",
      "ok": true,
      "chars": 8253
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 26,
      "engine": "Codex",
      "ok": true,
      "chars": 8199
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 27,
      "engine": "Codex",
      "ok": true,
      "chars": 8676
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 28,
      "engine": "Codex",
      "ok": true,
      "chars": 7985
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 29,
      "engine": "Codex",
      "ok": true,
      "chars": 8099
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 30,
      "engine": "Codex",
      "ok": true,
      "chars": 8578
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 31,
      "engine": "Codex",
      "ok": true,
      "chars": 8860
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 32,
      "engine": "Codex",
      "ok": true,
      "chars": 8123
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 33,
      "engine": "Codex",
      "ok": true,
      "chars": 8376
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 34,
      "engine": "Codex",
      "ok": true,
      "chars": 8300
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 35,
      "engine": "Codex",
      "ok": true,
      "chars": 8448
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 36,
      "engine": "Codex",
      "ok": true,
      "chars": 8394
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 37,
      "engine": "Codex",
      "ok": true,
      "chars": 8660
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 38,
      "engine": "Codex",
      "ok": true,
      "chars": 8054
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 39,
      "engine": "Codex",
      "ok": true,
      "chars": 7863
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 40,
      "engine": "Codex",
      "ok": true,
      "chars": 8500
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 41,
      "engine": "Codex",
      "ok": true,
      "chars": 8322
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 42,
      "engine": "Codex",
      "ok": true,
      "chars": 8548
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 43,
      "engine": "Codex",
      "ok": true,
      "chars": 8438
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 44,
      "engine": "Codex",
      "ok": true,
      "chars": 8416
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 45,
      "engine": "Codex",
      "ok": true,
      "chars": 7999
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 46,
      "engine": "Codex",
      "ok": true,
      "chars": 8522
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 47,
      "engine": "Codex",
      "ok": true,
      "chars": 8285
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 48,
      "engine": "Codex",
      "ok": true,
      "chars": 7916
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 49,
      "engine": "Codex",
      "ok": true,
      "chars": 8295
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 50,
      "engine": "Codex",
      "ok": true,
      "chars": 8307
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 51,
      "engine": "Codex",
      "ok": true,
      "chars": 8422
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 52,
      "engine": "Codex",
      "ok": true,
      "chars": 8146
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 53,
      "engine": "Codex",
      "ok": true,
      "chars": 8386
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 54,
      "engine": "Codex",
      "ok": true,
      "chars": 8117
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 55,
      "engine": "Codex",
      "ok": true,
      "chars": 8738
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 56,
      "engine": "Codex",
      "ok": true,
      "chars": 8214
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 57,
      "engine": "Codex",
      "ok": true,
      "chars": 8213
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 58,
      "engine": "Codex",
      "ok": true,
      "chars": 8393
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 59,
      "engine": "Codex",
      "ok": true,
      "chars": 8169
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 60,
      "engine": "Codex",
      "ok": true,
      "chars": 8381
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 61,
      "engine": "Codex",
      "ok": true,
      "chars": 8534
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 62,
      "engine": "Codex",
      "ok": true,
      "chars": 8227
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 63,
      "engine": "Codex",
      "ok": true,
      "chars": 8543
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 64,
      "engine": "Codex",
      "ok": true,
      "chars": 8676
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 65,
      "engine": "Codex",
      "ok": true,
      "chars": 8916
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 66,
      "engine": "Codex",
      "ok": true,
      "chars": 8104
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 67,
      "engine": "Codex",
      "ok": true,
      "chars": 8341
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 68,
      "engine": "Codex",
      "ok": true,
      "chars": 8359
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 69,
      "engine": "Codex",
      "ok": true,
      "chars": 7896
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 70,
      "engine": "Codex",
      "ok": true,
      "chars": 8576
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 71,
      "engine": "Codex",
      "ok": true,
      "chars": 8276
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 72,
      "engine": "Codex",
      "ok": true,
      "chars": 8302
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 73,
      "engine": "Codex",
      "ok": true,
      "chars": 8479
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 74,
      "engine": "Codex",
      "ok": true,
      "chars": 7543
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 75,
      "engine": "Codex",
      "ok": true,
      "chars": 8300
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 76,
      "engine": "Codex",
      "ok": true,
      "chars": 8394
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 77,
      "engine": "Codex",
      "ok": true,
      "chars": 8617
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 78,
      "engine": "Codex",
      "ok": true,
      "chars": 8576
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 79,
      "engine": "Codex",
      "ok": true,
      "chars": 8378
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 80,
      "engine": "Codex",
      "ok": true,
      "chars": 8225
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 81,
      "engine": "Codex",
      "ok": true,
      "chars": 8474
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 82,
      "engine": "Codex",
      "ok": true,
      "chars": 8681
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 83,
      "engine": "Codex",
      "ok": true,
      "chars": 8510
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 84,
      "engine": "Codex",
      "ok": true,
      "chars": 8224
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 85,
      "engine": "Codex",
      "ok": true,
      "chars": 8578
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 86,
      "engine": "Codex",
      "ok": true,
      "chars": 8558
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 87,
      "engine": "Codex",
      "ok": true,
      "chars": 8173
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 88,
      "engine": "Codex",
      "ok": true,
      "chars": 8063
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 89,
      "engine": "Codex",
      "ok": true,
      "chars": 8019
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 90,
      "engine": "Codex",
      "ok": true,
      "chars": 8436
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 91,
      "engine": "Codex",
      "ok": true,
      "chars": 8536
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 92,
      "engine": "Codex",
      "ok": true,
      "chars": 8714
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 93,
      "engine": "Codex",
      "ok": true,
      "chars": 8241
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 94,
      "engine": "Codex",
      "ok": true,
      "chars": 8588
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 95,
      "engine": "Codex",
      "ok": true,
      "chars": 8063
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 96,
      "engine": "Codex",
      "ok": true,
      "chars": 8343
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 97,
      "engine": "Codex",
      "ok": true,
      "chars": 7905
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 98,
      "engine": "Codex",
      "ok": true,
      "chars": 8489
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 99,
      "engine": "Codex",
      "ok": true,
      "chars": 8460
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-1",
      "scope_level": "actividad",
      "cycle": 100,
      "engine": "Codex",
      "ok": true,
      "chars": 8176
    }
  ],
  "ok": true,
  "cancelled": false
}
```

## 20260621-093902 - memoria-editorial

```json
{
  "run_id": "20260621-093902",
  "source_scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
  "build_level": "interinstitucional",
  "propagation_mode": "recursivo",
  "iterations": 100,
  "engines": [
    "Codex"
  ],
  "timeout_seconds": 900,
  "scope_offset": 10,
  "scope_limit": 1,
  "full_plan_scope_count": 461,
  "batch_scope_count": 1,
  "built_scopes": [
    "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde"
  ],
  "cycles": [
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 1,
      "engine": "Codex",
      "ok": true,
      "chars": 8474
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 2,
      "engine": "Codex",
      "ok": true,
      "chars": 8175
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 3,
      "engine": "Codex",
      "ok": true,
      "chars": 8012
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 4,
      "engine": "Codex",
      "ok": true,
      "chars": 7715
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 5,
      "engine": "Codex",
      "ok": true,
      "chars": 8159
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 6,
      "engine": "Codex",
      "ok": true,
      "chars": 8914
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 7,
      "engine": "Codex",
      "ok": true,
      "chars": 8082
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 8,
      "engine": "Codex",
      "ok": true,
      "chars": 8717
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 9,
      "engine": "Codex",
      "ok": true,
      "chars": 7722
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 10,
      "engine": "Codex",
      "ok": true,
      "chars": 8429
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 11,
      "engine": "Codex",
      "ok": true,
      "chars": 8160
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 12,
      "engine": "Codex",
      "ok": true,
      "chars": 8505
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 13,
      "engine": "Codex",
      "ok": true,
      "chars": 7909
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 14,
      "engine": "Codex",
      "ok": true,
      "chars": 8043
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 15,
      "engine": "Codex",
      "ok": true,
      "chars": 8457
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 16,
      "engine": "Codex",
      "ok": true,
      "chars": 7793
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 17,
      "engine": "Codex",
      "ok": true,
      "chars": 9026
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 18,
      "engine": "Codex",
      "ok": true,
      "chars": 8851
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 19,
      "engine": "Codex",
      "ok": true,
      "chars": 8269
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 20,
      "engine": "Codex",
      "ok": true,
      "chars": 8210
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 21,
      "engine": "Codex",
      "ok": true,
      "chars": 8284
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 22,
      "engine": "Codex",
      "ok": true,
      "chars": 7475
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 23,
      "engine": "Codex",
      "ok": true,
      "chars": 7620
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 24,
      "engine": "Codex",
      "ok": true,
      "chars": 8695
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 25,
      "engine": "Codex",
      "ok": true,
      "chars": 7846
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 26,
      "engine": "Codex",
      "ok": true,
      "chars": 8392
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 27,
      "engine": "Codex",
      "ok": true,
      "chars": 7489
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 28,
      "engine": "Codex",
      "ok": true,
      "chars": 8702
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 29,
      "engine": "Codex",
      "ok": true,
      "chars": 7740
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 30,
      "engine": "Codex",
      "ok": true,
      "chars": 8419
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 31,
      "engine": "Codex",
      "ok": true,
      "chars": 8544
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 32,
      "engine": "Codex",
      "ok": true,
      "chars": 8147
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 33,
      "engine": "Codex",
      "ok": true,
      "chars": 7885
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 34,
      "engine": "Codex",
      "ok": true,
      "chars": 8051
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 35,
      "engine": "Codex",
      "ok": true,
      "chars": 8040
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 36,
      "engine": "Codex",
      "ok": true,
      "chars": 7928
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 37,
      "engine": "Codex",
      "ok": true,
      "chars": 7824
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 38,
      "engine": "Codex",
      "ok": true,
      "chars": 8320
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 39,
      "engine": "Codex",
      "ok": true,
      "chars": 7793
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 40,
      "engine": "Codex",
      "ok": true,
      "chars": 8454
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 41,
      "engine": "Codex",
      "ok": true,
      "chars": 7932
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 42,
      "engine": "Codex",
      "ok": true,
      "chars": 8400
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 43,
      "engine": "Codex",
      "ok": true,
      "chars": 7553
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 44,
      "engine": "Codex",
      "ok": true,
      "chars": 7623
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 45,
      "engine": "Codex",
      "ok": true,
      "chars": 7964
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 46,
      "engine": "Codex",
      "ok": true,
      "chars": 8017
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 47,
      "engine": "Codex",
      "ok": true,
      "chars": 7829
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 48,
      "engine": "Codex",
      "ok": true,
      "chars": 7470
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 49,
      "engine": "Codex",
      "ok": true,
      "chars": 8959
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 50,
      "engine": "Codex",
      "ok": true,
      "chars": 7626
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 51,
      "engine": "Codex",
      "ok": true,
      "chars": 7496
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 52,
      "engine": "Codex",
      "ok": true,
      "chars": 8127
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 53,
      "engine": "Codex",
      "ok": true,
      "chars": 7935
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 54,
      "engine": "Codex",
      "ok": true,
      "chars": 8388
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 55,
      "engine": "Codex",
      "ok": true,
      "chars": 9549
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 56,
      "engine": "Codex",
      "ok": true,
      "chars": 9108
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 57,
      "engine": "Codex",
      "ok": true,
      "chars": 7948
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 58,
      "engine": "Codex",
      "ok": true,
      "chars": 8324
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 59,
      "engine": "Codex",
      "ok": true,
      "chars": 8094
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 60,
      "engine": "Codex",
      "ok": true,
      "chars": 8286
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 61,
      "engine": "Codex",
      "ok": true,
      "chars": 7918
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 62,
      "engine": "Codex",
      "ok": true,
      "chars": 8226
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 63,
      "engine": "Codex",
      "ok": true,
      "chars": 7892
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 64,
      "engine": "Codex",
      "ok": true,
      "chars": 8206
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 65,
      "engine": "Codex",
      "ok": true,
      "chars": 8064
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 66,
      "engine": "Codex",
      "ok": true,
      "chars": 8089
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 67,
      "engine": "Codex",
      "ok": true,
      "chars": 8122
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 68,
      "engine": "Codex",
      "ok": true,
      "chars": 8521
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 69,
      "engine": "Codex",
      "ok": true,
      "chars": 8432
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 70,
      "engine": "Codex",
      "ok": true,
      "chars": 8373
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 71,
      "engine": "Codex",
      "ok": true,
      "chars": 8222
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 72,
      "engine": "Codex",
      "ok": true,
      "chars": 8335
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 73,
      "engine": "Codex",
      "ok": true,
      "chars": 7970
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 74,
      "engine": "Codex",
      "ok": true,
      "chars": 8680
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 75,
      "engine": "Codex",
      "ok": true,
      "chars": 8378
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 76,
      "engine": "Codex",
      "ok": true,
      "chars": 7848
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 77,
      "engine": "Codex",
      "ok": true,
      "chars": 8397
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 78,
      "engine": "Codex",
      "ok": true,
      "chars": 9174
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 79,
      "engine": "Codex",
      "ok": true,
      "chars": 8988
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 80,
      "engine": "Codex",
      "ok": true,
      "chars": 8029
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 81,
      "engine": "Codex",
      "ok": true,
      "chars": 8278
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 82,
      "engine": "Codex",
      "ok": true,
      "chars": 8565
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 83,
      "engine": "Codex",
      "ok": true,
      "chars": 7727
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 84,
      "engine": "Codex",
      "ok": true,
      "chars": 8714
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 85,
      "engine": "Codex",
      "ok": true,
      "chars": 8426
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 86,
      "engine": "Codex",
      "ok": true,
      "chars": 8298
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 87,
      "engine": "Codex",
      "ok": true,
      "chars": 8068
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 88,
      "engine": "Codex",
      "ok": true,
      "chars": 8111
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 89,
      "engine": "Codex",
      "ok": true,
      "chars": 7633
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 90,
      "engine": "Codex",
      "ok": true,
      "chars": 8363
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 91,
      "engine": "Codex",
      "ok": true,
      "chars": 8216
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 92,
      "engine": "Codex",
      "ok": true,
      "chars": 7981
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 93,
      "engine": "Codex",
      "ok": true,
      "chars": 8071
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 94,
      "engine": "Codex",
      "ok": true,
      "chars": 8452
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 95,
      "engine": "Codex",
      "ok": true,
      "chars": 8010
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 96,
      "engine": "Codex",
      "ok": false,
      "chars": 30
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 97,
      "engine": "Codex",
      "ok": false,
      "chars": 25
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 98,
      "engine": "Codex",
      "ok": false,
      "chars": 9
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 99,
      "engine": "Codex",
      "ok": true,
      "chars": 8115
    },
    {
      "scope_key": "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
      "scope_level": "materia",
      "cycle": 100,
      "engine": "Codex",
      "ok": true,
      "chars": 8781
    }
  ],
  "ok": false,
  "cancelled": false
}
```
