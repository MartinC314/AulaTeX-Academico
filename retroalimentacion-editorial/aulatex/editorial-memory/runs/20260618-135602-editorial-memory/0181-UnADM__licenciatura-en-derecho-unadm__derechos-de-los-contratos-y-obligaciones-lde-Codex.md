{
  "summary": [
    "Base institucional UnADM reutilizable en la materia.",
    "Normalizar toda herencia no estructurada antes de propagar.",
    "La materia exige identidad UnADM, citas verificables y cierre juridico propio.",
    "La carpeta de materia es el punto canonico para reportes, presentaciones y bibliografia.",
    "Salida sin JSON parseable desde Codex para UnADM requiere normalizacion.",
    "Salida sin JSON parseable desde Codex para derechos-de-los-contratos-y-obligaciones-lde.",
    "Salida sin JSON parseable desde GPT-Pro para derechos-de-los-contratos-y-obligaciones-lde."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada y redaccion.",
    "Usar datos de la materia: Derechos de los contratos y obligaciones, semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Conservar enfoque juridico aplicado a contratos y obligaciones.",
    "Usar el codigo de curso LDE-S4B1 cuando la plantilla lo requiera.",
    "Tratar la herencia Codex desde ingenieria-en-sistemas-computacionales como provisional.",
    "Marcar como [supuesto] cualquier dato institucional no confirmado.",
    "Mantener autor por defecto Martin Jonathan de la Cruz salvo indicacion contraria.",
    "Usar ubicacion institucional Roma Norte, Ciudad de Mexico en metadatos.",
    "Fuente provisional: GPT-Pro desde Actividad 1.",
    "Fuente provisional: Codex desde ingenieria-en-sistemas-computacionales."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Alinear cada entrega a los cinco ejes del programa analitico.",
    "Incluir problema juridico o social, conceptos pertinentes, producto solicitado, analisis propio y conclusion transferible.",
    "Transformar la planeacion semanal en reportes, presentaciones o productos visuales segun corresponda.",
    "Conservar trazabilidad entre objetivo, evidencia, argumento y cierre."
  ],
  "activity_rules": [
    "Adaptar cada actividad al producto solicitado por la planeacion semanal.",
    "Explicitar postura academica propia con fundamento juridico.",
    "Cerrar con conclusion juridica util para la practica profesional.",
    "Marcar supuestos cuando falte instruccion especifica de la actividad.",
    "Distinguir problema, norma o doctrina, analisis y criterio propio.",
    "Evitar trasladar contenido de Filosofia del Derecho sin adecuacion contractual."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de persistir memoria propagada.",
    "Revisar y normalizar herencia proveniente de salidas no estructuradas.",
    "Verificar coherencia entre objetivo de actividad y evidencia incluida.",
    "Comprobar trazabilidad de citas y referencias en el .bib local.",
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Validar compatibilidad disciplinar antes de propagacion lateral.",
    "Corregir placeholders o caracteres de control en rutas antes de compilar.",
    "Confirmar que los metadatos LaTeX coincidan con la materia.",
    "No degradar reglas utiles previas durante union-dedupe.",
    "Resolver placeholders PowerShell tipo $(@{...}.Slug) en nombres de .bib antes de compilar."
  ],
  "latex_rules": [
    "Conservar plantilla LaTeX base de la materia y sus metadatos institucionales.",
    "Mantener campos de curso, autor, universidad y ubicacion completos antes de compilar.",
    "Usar espanol academico claro y terminologia juridica precisa.",
    "Evitar cambios de estilo no justificados por la pauta editorial.",
    "Usar reporte-derechos-de-los-contratos-y-obligaciones.tex como base de reporte.",
    "Usar presentacion-derechos-de-los-contratos-y-obligaciones.tex como base de presentacion si existe.",
    "Verificar que el archivo .bib referenciado sea derechos-de-los-contratos-y-obligaciones.bib.",
    "Actualizar documentsubtitle por numero de actividad antes de compilar."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas de cada actividad en derechos-de-los-contratos-y-obligaciones.bib.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales verificables.",
    "No inventar fuentes.",
    "Declarar [supuesto] si una referencia no esta disponible.",
    "Mantener notas de consulta y origen documental cuando aplique.",
    "Conservar la malla curricular de Derecho como fuente institucional local.",
    "Agregar doctrina, normas o jurisprudencia solo cuando sean verificables.",
    "Separar bibliografia base de fuentes especificas de actividad.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar estas reglas a actividades hijas de la materia en ciclo 2.",
    "Aplicar lateralmente a materias LDE solo tras validar compatibilidad disciplinar.",
    "Mantener compresion union-dedupe sin eliminar reglas utiles previas.",
    "Etiquetar elementos heredados de calidad como control transversal.",
    "Propagar hacia arriba solo reglas institucionales y transversales.",
    "Normalizar manualmente la herencia del ciclo 1 si se reutiliza.",
    "Evitar propagar detalles contractuales a materias no juridicas.",
    "Ciclo 1 necesita normalizacion manual si se reutiliza."
  ],
  "open_questions": [
    "Confirmar si existe guia formal de citacion juridica obligatoria para LDE.",
    "Definir formato minimo de conclusion juridica esperado por actividad.",
    "Precisar si la plantilla de presentacion comparte los mismos metadatos que el reporte.",
    "Confirmar la planeacion semanal especifica de cada actividad.",
    "Confirmar si se requiere formato APA, juridico mexicano u otro estilo institucional.",
    "Confirmar si deben usarse leyes federales, codigos civiles locales o ambos segun actividad."
  ]
}