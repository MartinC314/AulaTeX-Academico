{
  "summary": [
    "Base institucional UnADM reutilizable en la materia.",
    "La materia exige identidad UnADM, citas verificables y cierre juridico propio.",
    "Normalizar toda herencia no estructurada antes de propagar.",
    "Existe herencia institucional provisional desde Codex que requiere validacion.",
    "La carpeta de materia es el punto canonico para reportes, presentaciones y bibliografia."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada y redaccion.",
    "Usar datos de la materia: Derechos de los contratos y obligaciones, semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Conservar enfoque juridico aplicado a contratos y obligaciones.",
    "Usar el codigo de curso LDE-S4B1 cuando la plantilla lo requiera.",
    "Tratar la herencia Codex desde ingenieria-en-sistemas-computacionales como provisional.",
    "Marcar como [supuesto] cualquier dato institucional no confirmado."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Alinear cada entrega a los cinco ejes del programa analitico.",
    "Incluir problema juridico o social, conceptos pertinentes, producto solicitado, analisis propio y conclusion transferible.",
    "Mantener consistencia entre reporte, presentacion y bibliografia local.",
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
    "Revisar respuesta no estructurada antes de aplicarla aguas abajo.",
    "Verificar coherencia entre objetivo de actividad y evidencia incluida.",
    "Comprobar trazabilidad de citas y referencias en el .bib local.",
    "Validar compatibilidad disciplinar antes de propagacion lateral.",
    "Corregir placeholders o caracteres de control en rutas antes de compilar.",
    "Confirmar que los metadatos LaTeX coincidan con la materia.",
    "No degradar reglas utiles previas durante union-dedupe."
  ],
  "latex_rules": [
    "Conservar plantilla LaTeX base de la materia y sus metadatos institucionales.",
    "Mantener campos de curso, autor, universidad y ubicacion completos antes de compilar.",
    "Usar espanol academico claro y terminologia juridica precisa.",
    "Evitar cambios de estilo no justificados por la pauta editorial.",
    "Usar reporte-derechos-de-los-contratos-y-obligaciones.tex como base de reporte.",
    "Usar presentacion-derechos-de-los-contratos-y-obligaciones.tex como base de presentacion si existe.",
    "Verificar que el archivo .bib referenciado sea derechos-de-los-contratos-y-obligaciones.bib."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas de cada actividad en derechos-de-los-contratos-y-obligaciones.bib.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales verificables.",
    "No inventar fuentes.",
    "Declarar [supuesto] si una referencia no esta disponible.",
    "Mantener notas de consulta y origen documental cuando aplique.",
    "Conservar la malla curricular de Derecho como fuente institucional local.",
    "Agregar doctrina, normas o jurisprudencia solo cuando sean verificables.",
    "Separar bibliografia base de fuentes especificas de actividad."
  ],
  "propagation_hints": [
    "Propagar estas reglas a actividades hijas de la materia en ciclo 1.",
    "Aplicar lateralmente a materias LDE solo tras validar compatibilidad disciplinar.",
    "Propagar hacia arriba solo reglas institucionales y transversales.",
    "Mantener compresion union-dedupe sin eliminar reglas utiles previas.",
    "Etiquetar elementos heredados de calidad como control transversal.",
    "Normalizar manualmente la herencia del ciclo 1 si se reutiliza.",
    "Evitar propagar detalles contractuales a materias no juridicas."
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