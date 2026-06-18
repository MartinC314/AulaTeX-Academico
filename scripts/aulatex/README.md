# AulaTeX

Suite local para coordinar edicion, investigacion, compilacion y evaluacion
editorial de plantillas academicas LaTeX.

## Lanzamiento

Desde la raiz del repositorio:

```powershell
.\scripts\aulatex.ps1
```

Modo CLI:

```powershell
.\scripts\aulatex.ps1 llm-env
.\scripts\aulatex.ps1 llm-check
.\scripts\aulatex.ps1 agent-patterns
.\scripts\aulatex.ps1 agent --target UnADM/licenciatura-en-derecho-unadm/historia-del-derecho-en-mexico-lde --action generar-actividad --activity 1
.\scripts\aulatex.ps1 compile .\UnADM\licenciatura-en-derecho-unadm\historia-del-derecho-en-mexico-lde\reporte-historia-del-derecho-en-mexico.tex
```

## Integracion LLM

AulaTeX usa un cliente HTTP propio en `scripts/aulatex/llm_bridge.py`.
Las credenciales se cargan desde `scripts/aulatex.env` antes de cada llamada.
Los motores disponibles son:

- `Auto (model-router)`
- `Claude Foundry`
- `GPT-Pro`
- `Codex`

`llm-env` muestra variables presentes/faltantes sin revelar secretos.
`llm-check` realiza una llamada HTTP real de verificacion por motor.

## Ciclo agente

Cada ejecucion del agente crea una carpeta en:

```text
retroalimentacion-editorial/aulatex/runs/
```

El ciclo base es:

1. planificar con memoria compartida;
2. investigar el estado editorial del objetivo;
3. generar plantilla, actividad o propuesta;
4. validar criterios, riesgos y siguiente iteracion;
5. criticar adversarialmente antes de aplicar cambios;
6. compilar hasta dos `.tex` canonicos del objetivo cuando se solicita.

La capa agentica vive en `scripts/aulatex/agentic_patterns.py` e incorpora:

- planificacion + memoria aumentada;
- registro de herramientas con invocacion segura;
- flujo con maquina de estados y auditoria;
- verificacion/validacion editorial;
- consenso multiagente con critico adversarial.

La bitacora acumulada vive en:

```text
retroalimentacion-editorial/aulatex/bitacora.md
```
