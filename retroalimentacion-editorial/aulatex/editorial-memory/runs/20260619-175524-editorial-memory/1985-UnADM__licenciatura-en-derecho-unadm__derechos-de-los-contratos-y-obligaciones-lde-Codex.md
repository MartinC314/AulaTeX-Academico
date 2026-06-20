{
  "summary": [
    "Base institucional UnADM reutilizable y activa en la materia.",
    "La carpeta de materia es el punto canonico para reportes, presentaciones y bibliografia local.",
    "La materia corresponde a Derechos de los contratos y obligaciones, semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Las salidas sin JSON parseable requieren normalizacion antes de propagar.",
    "Existe herencia institucional provisional desde Codex, GPT-Pro, Auto y Claude Foundry que requiere validacion.",
    "El contexto local confirma README, programa analitico, reporte base y archivo .bib local.",
    "El contexto local contiene placeholders PowerShell y caracteres de control en rutas que deben corregirse."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada y redaccion.",
    "Usar datos de la materia: Derechos de los contratos y obligaciones, semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Conservar enfoque juridico aplicado a contratos y obligaciones.",
    "Usar el codigo de curso LDE-S4B1 cuando la plantilla lo requiera.",
    "Mantener autor por defecto Martin Jonathan de la Cruz salvo indicacion contraria.",
    "Usar ubicacion institucional Roma Norte, Ciudad de Mexico en metadatos.",
    "Tratar herencias de Codex, GPT-Pro, Auto y Claude Foundry como provisionales.",
    "Marcar como [supuesto] cualquier dato institucional no confirmado.",
    "Fuente provisional: Codex desde ingenieria-en-sistemas-computacionales.",
    "Fuente provisional: Codex desde Actividad 1.",
    "Fuente provisional: GPT-Pro desde Actividad 1.",
    "Fuente provisional: Auto (model-router) desde Actividad 1.",
    "Fuente provisional: Claude Foundry desde Actividad 1."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Alinear cada entrega a los cinco ejes del programa analitico.",
    "Incluir problema juridico o social, conceptos pertinentes, producto solicitado, analisis propio y conclusion transferible.",
    "Transformar la planeacion semanal en reportes, presentaciones o productos visuales segun corresponda.",
    "Conservar trazabilidad entre objetivo, evidencia, argumento y cierre.",
    "Distinguir bibliografia base y fuentes especificas de actividad.",
    "Mantener consistencia entre reporte, presentacion y bibliografia local."
  ],
  "activity_rules": [
    "Adaptar cada actividad al producto solicitado por la planeacion semanal.",
    "Explicitar postura academica propia con fundamento juridico.",
    "Distinguir problema, norma o doctrina, analisis y criterio propio.",
    "Cerrar con conclusion juridica util para la practica profesional.",
    "Marcar supuestos cuando falte instruccion especifica de la actividad.",
    "Evitar trasladar contenido de Filosofia del Derecho sin adecuacion contractual."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de persistir memoria propagada.",
    "Revisar toda respuesta no estructurada antes de aplicarla aguas abajo.",
    "Normalizar herencia proveniente de salidas no estructuradas.",
    "No degradar reglas utiles previas durante union-dedupe.",
    "Validar compatibilidad disciplinar antes de propagacion lateral.",
    "Verificar coherencia entre objetivo de actividad y evidencia incluida.",
    "Comprobar trazabilidad de citas y referencias en el .bib local.",
    "Corregir placeholders o caracteres de control en rutas antes de compilar.",
    "Resolver placeholders PowerShell tipo $(@{...}.Slug) en nombres de .bib antes de compilar.",
    "Confirmar que los metadatos LaTeX coincidan con la materia."
  ],
  "latex_rules": [
    "Conservar plantilla LaTeX base de la materia y sus metadatos institucionales.",
    "Usar reporte-derechos-de-los-contratos-y-obligaciones.tex como base de reporte.",
    "Usar presentacion-derechos-de-los-contratos-y-obligaciones.tex como base de presentacion si existe.",
    "Mantener campos de curso, autor, universidad y ubicacion completos antes de compilar.",
    "Verificar que el archivo .bib referenciado sea derechos-de-los-contratos-y-obligaciones.bib.",
    "Actualizar documentsubtitle por numero de actividad antes de compilar.",
    "Ajustar documenttitle al producto final cuando deje de ser plantilla base.",
    "Usar espanol academico claro y terminologia juridica precisa.",
    "Evitar cambios de estilo no justificados por la pauta editorial."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas de cada actividad en derechos-de-los-contratos-y-obligaciones.bib.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales verificables.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Conservar la malla curricular de Derecho como fuente institucional local.",
    "Separar bibliografia base de fuentes especificas de actividad.",
    "Agregar doctrina, normas o jurisprudencia solo cuando sean verificables.",
    "Mantener notas de consulta y origen documental cuando aplique.",
    "No inventar fuentes.",
    "Declarar [supuesto] si una referencia no esta disponible."
  ],
  "propagation_hints": [
    "Propagar estas reglas a actividades hijas de la materia en ciclo 13.",
    "Normalizar manualmente la herencia de ciclos previos si se reutiliza.",
    "Ciclo 13 necesita normalizacion manual si se reutiliza.",
    "Propagar hacia arriba solo reglas institucionales y transversales.",
    "Aplicar lateralmente a materias LDE solo tras validar compatibilidad disciplinar.",
    "Excluir metadatos especificos de la materia cuando no coincidan con el destino lateral.",
    "Evitar propagar detalles contractuales a materias no juridicas.",
    "Reutilizar controles de placeholders en carpetas con rutas generadas por PowerShell.",
    "Mantener compresion union-dedupe sin eliminar reglas utiles previas.",
    "Etiquetar elementos heredados de calidad como control transversal."
  ],
  "open_questions": [
    "Confirmar si existe guia formal de citacion juridica obligatoria para LDE.",
    "Confirmar si se requiere formato APA, juridico mexicano u otro estilo institucional.",
    "Definir formato minimo de conclusion juridica esperado por actividad.",
    "Confirmar la planeacion semanal especifica de cada actividad.",
    "Confirmar si la plantilla de presentacion comparte los mismos metadatos que el reporte.",
    "Confirmar si deben usarse leyes federales, codigos civiles locales o ambos segun actividad.",
    "Confirmar la correccion canonica del nombre .bib en README y programa analitico."
  ]
}