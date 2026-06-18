{
  "summary": [
    "Base editorial inicial creada para ITESCA/maestria-en-gestion-administrativa.",
    "Se detecta estructura por tronco comun y dos LGAC con materias 2026.",
    "Existe plantilla LaTeX canonica de carrera con metadatos por \\providecommand.",
    "Existe bibliografia base local en archivo .bib institucional."
  ],
  "identity_rules": [
    "Usar nombre institucional: Instituto Tecnologico Superior de Cajeme.",
    "Usar programa destino: Maestria en Gestion Administrativa.",
    "Usar nivel academico: Maestria.",
    "Conservar codigo corto de carrera: MGA.",
    "Mantener contexto de gestion administrativa basado en diagnostico, evidencia y mejora.",
    "Marcar como supuesto cualquier dato no definido de periodo, modalidad o figura docente."
  ],
  "structure_rules": [
    "Conservar organizacion por tronco comun y LGAC.",
    "Mantener las dos LGAC declaradas en README sin renombrar.",
    "Conservar carpeta semilla primer-ingreso-mga como no curricular.",
    "Mantener por carpeta de materia: reporte, presentacion, bibliografia local y guia de compilacion.",
    "Usar reporte-itesca-mga.tex como punto de entrada canonico de carrera."
  ],
  "activity_rules": [
    "Iniciar cada actividad con problema, diagnostico, evidencia, decision, consecuencia y mejora.",
    "Aplicar redaccion critica y argumentacion ejecutiva en productos escritos.",
    "Priorizar tecnicas didacticas declaradas: caso, matriz, comparativo, ensayo, debate, portafolio y proyecto integrador.",
    "Alinear evidencias con toma de decisiones administrativas y pertinencia institucional."
  ],
  "quality_gates": [
    "Verificar consistencia entre metadatos de portada y carrera MGA.",
    "Verificar que toda afirmacion clave tenga evidencia o referencia trazable.",
    "Verificar que campos por definir se mantengan explicitamente marcados y no simulados.",
    "Verificar compilacion sin errores del archivo contenedor de cada materia.",
    "Verificar que cada materia conserve bibliografia local y ruta de compilacion."
  ],
  "latex_rules": [
    "Definir metadatos editables con \\providecommand para permitir sobreescritura segura.",
    "Mantener \\def para titulos de documento solo en archivo canonico de entrada.",
    "