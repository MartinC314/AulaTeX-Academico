{
  "summary": [
    "ITESCA define un nivel institucional sobre carrera y materia.",
    "La uniformidad visual y editorial se centraliza en ITESCA/_shared/.",
    "Los wrappers por carrera y materia declaran solo metadatos del documento.",
    "Existe control editorial comun con evidencia, pertinencia y transferencia profesional.",
    "La compilacion se ejecuta desde la raiz del proyecto con scripts latexmk."
  ],
  "identity_rules": [
    "Usar ITESCA/_shared/ como fuente unica de identidad visual institucional.",
    "Centralizar metadatos institucionales y criterio editorial en perfiles compartidos.",
    "Mantener coherencia institucional en argumentacion, no solo en formato.",
    "Alinear documentos con claridad tecnica, pertinencia academica y aplicacion profesional."
  ],
  "structure_rules": [
    "Respetar jerarquia institucion -> carrera -> materia.",
    "Mantener en cada carrera: bibliografia compartida, reporte canonico, presentacion canonica, referencias de apoyo y carpetas por materia.",
    "Conservar _shared/ como nucleo comun para evitar duplicacion de wrappers y reglas.",
    "Ubicar activos institucionales en rutas centralizadas de ITESCA."
  ],
  "activity_rules": [
    "Incluir ficha editorial de actividad en cada entrega.",
    "Declarar nivel cognitivo minimo de la actividad.",
    "Incluir matriz de cumplimiento de criterios.",
    "Presentar producto visible y evidencia interpretada.",
    "Vincular actividad con carrera, materia y contexto profesional.",
    "Cerrar con postura, aprendizaje y consecuencia transferible."
  ],
  "quality_gates": [
    "Verificar que el documento herede de templates y perfiles compartidos de ITESCA.",
    "Verificar que el wrapper solo declare datos especificos del documento.",
    "Comprobar presencia de evidencia verificable y conclusion transferible.",
    "Compilar desde la raiz del proyecto con scripts oficiales.",
    "Evitar metadatos repetidos fuera de _shared/."
  ],
  "latex_rules": [
    "Heredar desde itesca-report-template.tex para reportes.",
    "Heredar desde itesca-presentation-template.tex para presentaciones.",
    "Usar perfiles editoriales compartidos por programa cuando aplique.",
    "Mantener rutas institucionales de logos y activos en assets-itesca.",
    "Ejecutar compilacion con scripts/latexmk-build.ps1 desde