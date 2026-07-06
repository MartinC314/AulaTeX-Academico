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
.\scripts\aulatex.ps1 investigation --target .\UnADM\licenciatura-en-derecho-unadm\historia-del-derecho-en-mexico-lde --query "historia del derecho en mexico unadm programa analitico" --query "historia del derecho en mexico bibliografia recomendada"
.\scripts\aulatex.ps1 extractor --preview --target .\UnADM\licenciatura-en-derecho-unadm\historia-del-derecho-en-mexico-lde
.\scripts\aulatex.ps1 extractor --target .\UnADM\licenciatura-en-derecho-unadm\historia-del-derecho-en-mexico-lde --fuentes .\UnADM\licenciatura-en-derecho-unadm\historia-del-derecho-en-mexico-lde\referencias --planeacion .\UnADM\licenciatura-en-derecho-unadm\historia-del-derecho-en-mexico-lde\planeacion.txt --salida .\UnADM\licenciatura-en-derecho-unadm\historia-del-derecho-en-mexico-lde\extractor-aulatex --motor anthropicfoundry
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

## Fase Investigación

La pestaña Investigación y el comando `investigation` consolidan la base de
conocimiento previa al extractor. La corrida combina contexto local del scope,
consultas web y memoria editorial heredada para producir:

- `investigacion-aulatex/base-conocimiento.json`
- `investigacion-aulatex/base-conocimiento.md`
- `investigacion-aulatex/fuentes-web.md`
- el `.bib` canónico del scope o uno sugerido si aún no existe
- `referencias-*/` cuando aplica
- `assets-*/` para institución o carrera cuando aplica
- `programa-analitico-*.md` para materia si aún no existe

El orden recomendado del flujo es:

1. construir memoria editorial;
2. consolidar investigación;
3. ejecutar el extractor;
4. generar, redactar y compilar.

## Adaptador del extractor

El subcomando `extractor` encapsula la ejecucion de
`scripts/extractor-conceptos-ideas/run.py` y deja una corrida trazable en:

```text
retroalimentacion-editorial/aulatex/extractor/runs/
```

La ejecucion queda normalizada con:

- `manifest.json`;
- `stdout.txt`;
- `stderr.txt`;
- verificacion de artefactos nucleares como `fichas_conceptos.json`,
  `conceptos_detectados.json`, `ideas_detectadas.json` y
  `trazabilidad_fuentes.json`.

La opcion `--preview` permite resolver scope, salida por defecto y comando
previsto sin lanzar el extractor.

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

El agente soporta dos modos de iteracion:

- `--cycle-mode stages`: modo corto. `--iterations` selecciona de 1 a 5 etapas del ciclo base.
- `--cycle-mode full`: modo intensivo. `--iterations N` ejecuta N ciclos completos de todos los roles. Por ejemplo, `--iterations 2 --cycle-mode full` ejecuta 10 llamadas LLM; `--iterations 100 --cycle-mode full` ejecuta 500 llamadas LLM si hay cinco roles activos.

Uso recomendado:

```powershell
# Prueba corta
.\scripts\aulatex.ps1 agent --target .\UnADM\licenciatura-en-derecho-unadm\filosofia-del-derecho-lde --action evaluar --iterations 2 --cycle-mode full --no-compile --no-extractor

# Corrida intensiva controlada
.\scripts\aulatex.ps1 agent --target .\UnADM\licenciatura-en-derecho-unadm\filosofia-del-derecho-lde --action realizar-actividad --activity 5 --iterations 100 --cycle-mode full --no-compile
```

Para corridas intensivas conviene usar primero `--no-compile` y `--extractor-probe` o `--no-extractor`, validar el estado, y luego activar herramientas costosas por lote.

La capa agentica vive en `scripts/aulatex/agentic_patterns.py` e incorpora:

- planificacion + memoria aumentada;
- registro de herramientas con invocacion segura;
- flujo con maquina de estados y auditoria;
- verificacion/validacion editorial;
- consenso multiagente con critico adversarial.

## Siguiente capa: agente con bucle real

La arquitectura actual ya cubre memoria editorial, investigacion, generacion y
evaluacion. El siguiente paso es cerrar el bucle operativo por actividad con un
estado persistido, decisiones explicitas y reevaluacion por artefactos.

El contrato propuesto para esa capa vive en:

```text
retroalimentacion-editorial/aulatex/agente-verdadero-contrato-operativo.md
```

La bitacora acumulada vive en:

```text
retroalimentacion-editorial/aulatex/bitacora.md
```
