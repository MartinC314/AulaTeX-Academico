```json
{
  "summary": [
    "Materia destino UnADM Derecho: semestre 6, bloque 2, obligatoria, 8 creditos.",
    "La carpeta de materia es punto de entrada canonico para plantilla, programa analitico y bibliografia local.",
    "La pauta exige identidad UnADM, integridad academica, citas verificables y conclusion juridica propia.",
    "Existe bibliografia local confirmada: derechos-de-contratos-mercantiles-y-titulos-valores.bib.",
    "README y programa contienen placeholders de slug y nombres truncados verificables.",
    "La plantilla .tex contiene una macro truncada verificable: \\def\\universitydepartmen.",
    "Supuesto heredado: persiste alerta institucional por salida no JSON parseable desde Codex para UnADM.",
    "Supuesto heredado: persiste alerta por salida no JSON parseable desde GPT-Pro para esta materia.",
    "Supuesto heredado: fuente provisional Codex desde ingenieria-en-sistemas-computacionales."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, metadatos y redaccion academica.",
    "Alinear entregables a la Licenciatura en Derecho.",
    "Alinear contenidos a Derechos de contratos mercantiles y titulos valores.",
    "Conservar tono juridico-formal y postura academica propia en el cierre.",
    "Etiquetar como provisionales las fuentes heredadas no confirmadas.",
    "Registrar fuente provisional heredada: Codex desde ingenieria-en-sistemas-computacionales.",
    "Registrar fuente provisional heredada: GPT-Pro desde Actividad 1."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como nodo canonico para plantillas, programa analitico y bibliografia local.",
    "Mantener consistencia entre README, programa analitico, .tex y .bib de la materia.",
    "Estructurar cada actividad con problema, conceptos o normas, producto, analisis propio y conclusion transferible.",
    "Incluir transferencia profesional en el cierre.",
    "Corregir en README los nombres truncados de reporte y referencias.",
    "Sustituir placeholders de slug por nombres reales de archivo.",
    "Asegurar que README y programa apunten al .bib local real."
  ],
  "activity_rules": [
    "Contextualizar cada actividad con un problema juridico o social concreto.",
    "Vincular argumentos con normas, doctrina o datos pertinentes y verificables.",
    "Desarrollar el producto solicitado por la planeacion.",
    "Distinguir evidencia citada de analisis propio.",
    "Cerrar cada entrega con conclusion juridica aplicable a la practica profesional."
  ],
  "quality_gates": [
    "Validar que la salida sea JSON parseable antes de propagar memoria aguas abajo.",
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Revisar que no haya regresion de reglas utiles heredadas.",
    "Comprobar trazabilidad entre afirmaciones y fuentes citadas.",
    "Verificar que no se agreguen fuentes inventadas.",
    "Confirmar que README y programa apunten al .bib local real.",
    "Validar compilacion despues de ajustar nombres de archivos y macros."
  ],
  "latex_rules": [
    "Conservar plantilla base de reporte de la materia y completar metadatos del curso.",
    "Mantener nomenclatura consistente de archivos de reporte y presentacion por asignatura.",
    "Corregir y validar macros incompletas o truncadas antes de compilar.",
    "Revisar macro truncada \\def\\universitydepartmen en la plantilla.",
    "Validar compilacion despues de ajustar nombres de archivos."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas de actividad en el .bib local de la materia.",
    "Priorizar fuentes institucionales UnADM y documentos curriculares locales cuando apliquen.",
    "No incorporar fuentes no verificadas ni inventadas.",
    "Usar derechos-de-contratos-mercantiles-y-titulos-valores.bib como archivo local confirmado.",
    "Conservar entradas existentes unadmSitioWeb y unadmMallaDerecho2024.",
    "Agregar fecha de consulta cuando se usen recursos web."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo reglas normalizadas y sin duplicados.",
    "Usar compresion union-dedupe lossless en cada fusion de memoria.",
    "Mantener alerta institucional sobre salida no JSON parseable hasta confirmacion.",
    "No propagar detalles locales de archivo si no aplican a materias laterales.",
    "Marcar como heredada la alerta de normalizacion manual en ciclo 1.",
    "Ciclo 1 necesita normalizacion manual si se reutiliza.",
    "En ciclo 2, propagar lateralmente solo pautas academicas transversales."
  ],
  "open_questions": [
    "Confirmar si la incidencia historica de salida no JSON parseable ya fue resuelta en flujos actuales.",
    "Definir plantilla oficial de presentacion para esta materia si difiere del reporte.",
    "Verificar nombre final del archivo .bib generado por slug para evitar placeholders sin resolver.",
    "Verificar si el README debe listar referencias como carpeta o archivo.",
    "Confirmar si el sitio UnADM debe conservar year 2026 o usar fecha de consulta solamente.",
    "Completar el resto de la plantilla .tex para revisar macros faltantes."
  ],
  "sources": [
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
    "UnADM/licenciatura-en-derecho-unadm/derechos-de-contratos-mercantiles-y-titulos-valores-lde",
    "UnADM"
  ],
  "compression": {
    "method": "union-dedupe",
    "lossless": true
  },
  "schema_version": 1
}
```