{
  "summary": [
    "Materia destino UnADM Derecho: semestre 6, bloque 2, obligatoria, 8 creditos.",
    "La carpeta de materia es punto de entrada canonico para plantilla, programa y bibliografia local.",
    "La pauta exige identidad UnADM, integridad academica, citas verificables y conclusion juridica propia.",
    "Existe bibliografia local en derechos-de-contratos-mercantiles-y-titulos-valores.bib.",
    "Supuesto heredado: persiste alerta institucional por salida no JSON parseable hasta nueva evidencia.",
    "Supuesto heredado: fuente provisional Codex desde ingenieria-en-sistemas-computacionales."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, metadatos y redaccion academica.",
    "Alinear entregables a Licenciatura en Derecho.",
    "Alinear contenidos a Derechos de contratos mercantiles y titulos valores.",
    "Conservar tono juridico-formal.",
    "Cerrar con postura academica propia."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como nodo canonico.",
    "Mantener consistencia entre README, programa analitico, .tex y .bib.",
    "Estructurar cada actividad con problema, conceptos o normas, producto, analisis propio y conclusion.",
    "Incluir transferencia profesional en el cierre.",
    "Corregir en README nombres truncados de reporte y referencias.",
    "Sustituir placeholders de slug por nombres reales de archivo."
  ],
  "activity_rules": [
    "Contextualizar cada actividad con un problema juridico o social concreto.",
    "Vincular argumentos con normas, doctrina o datos verificables.",
    "Desarrollar el producto solicitado por la planeacion.",
    "Distinguir evidencia citada de analisis propio.",
    "Cerrar cada entrega con conclusion juridica aplicable a practica profesional."
  ],
  "quality_gates": [
    "Validar que la salida sea JSON parseable antes de propagar memoria.",
    "Revisar respuestas no estructuradas antes de aplicarlas aguas abajo.",
    "Revisar que no haya regresion de reglas utiles heredadas.",
    "Comprobar trazabilidad entre afirmaciones y fuentes citadas.",
    "Verificar que no se agreguen fuentes inventadas.",
    "Confirmar que README y programa apunten al .bib local real."
  ],
  "latex_rules": [
    "Conservar plantilla base de reporte de la materia.",
    "Completar metadatos del curso en cada entrega.",
    "Mantener nomenclatura consistente para reporte y presentacion.",
    "Corregir macros incompletas o truncadas antes de compilar.",
    "Revisar macro truncada \\def\\universitydepartmen en la plantilla.",
    "Validar compilacion despues de ajustar nombres de archivos."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas de actividad en el .bib local de la materia.",
    "Usar derechos-de-contratos-mercantiles-y-titulos-valores.bib como archivo local confirmado.",
    "Priorizar fuentes institucionales UnADM y documentos curriculares locales cuando apliquen.",
    "Conservar entradas existentes unadmSitioWeb y unadmMallaDerecho2024.",
    "No incorporar fuentes no verificadas ni inventadas.",
    "Agregar fecha de consulta cuando se usen recursos web."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo reglas normalizadas y sin duplicados.",
    "Usar compresion union-dedupe lossless en cada fusion de memoria.",
    "Marcar como heredada la alerta de normalizacion manual en ciclo 1.",
    "Mantener alerta institucional sobre salida no JSON parseable hasta confirmacion.",
    "No propagar detalles locales de archivo si no aplican a materias laterales."
  ],
  "open_questions": [
    "Confirmar si la incidencia historica de salida no JSON parseable ya fue resuelta.",
    "Definir plantilla oficial de presentacion si difiere del reporte.",
    "Verificar si el README debe listar referencias como carpeta o archivo.",
    "Confirmar si el sitio UnADM debe conservar year 2026 o usar fecha de consulta solamente.",
    "Completar el resto de la plantilla .tex para revisar macros faltantes."
  ]
}