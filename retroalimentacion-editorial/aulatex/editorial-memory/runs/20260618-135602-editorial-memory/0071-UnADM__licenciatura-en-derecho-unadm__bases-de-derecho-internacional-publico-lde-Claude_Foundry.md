```json
{
  "summary": [
    "Materia destino: Bases de derecho internacional publico (UnADM, Licenciatura en Derecho).",
    "Ubicacion curricular: semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Plantilla base, programa analitico y bibliografia local ya definidos.",
    "Propagacion solicitada: arriba-y-laterales, ciclo 2.",
    "Se conserva incidencia historica de salida sin JSON parseable desde Codex para UnADM.",
    "Se conserva incidencia historica de salida sin JSON parseable desde GPT-Pro para la materia destino.",
    "Supuesto: actividad origen (filosofia-del-derecho/actividad-1) no aporta reglas nuevas estructuradas en este ciclo."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada y metadatos.",
    "Usar nombre oficial/local de la materia: Bases de derecho internacional publico.",
    "Alinear entregables a Licenciatura en Derecho, semestre 4, bloque 1.",
    "Usar codigo de curso LDE-S4B1 en metadatos.",
    "Tratar Codex y GPT-Pro como procedencia provisional, no como identidad del entregable.",
    "Conservar al alumno registrado en plantilla si no hay instruccion local que lo sustituya."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Conservar separacion entre reporte, presentacion, programa analitico y bibliografia.",
    "Organizar cada entrega con problema juridico o social, conceptos, fuentes, analisis propio y conclusion juridica.",
    "Transformar la planeacion semanal en el producto academico solicitado.",
    "Mantener el programa analitico como guia editorial de actividades.",
    "Conservar la carpeta referencias-bases-de-derecho-internacional-publico como repositorio de apoyo.",
    "Distinguir reporte, presentacion y productos visuales segun la planeacion."
  ],
  "activity_rules": [
    "Adaptar cada actividad al producto solicitado por la planeacion semanal.",
    "Incluir postura academica propia sustentada en fuentes verificables.",
    "Integrar conceptos, normas, doctrina o datos pertinentes cuando correspondan.",
    "Distinguir hechos, argumentos, normas y criterio propio.",
    "Cerrar con conclusion transferible a la practica juridica.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de propagar memoria aguas abajo.",
    "Revisar respuestas no estructuradas antes de aplicarlas aguas abajo.",
    "Revisar consistencia entre instrucciones de actividad y programa analitico.",
    "Bloquear afirmaciones sin respaldo documental o normativo.",
    "Validar sintaxis LaTeX y cierre de entornos antes de compilar.",
    "Validar citas y referencias antes de cerrar entregables.",
    "Verificar que README, programa analitico, .bib y plantillas locales coincidan.",
    "Marcar faltantes como pendientes sin sustituirlos por invenciones."
  ],
  "latex_rules": [
    "Reutilizar la plantilla .tex local de la materia como base de nuevas actividades.",
    "Usar reporte-bases-de-derecho-internacional-publico.tex para reportes base.",
    "Usar presentacion-bases-de-derecho-internacional-publico.tex solo para productos de presentacion.",
    "Completar metadatos de portada sin alterar identidad institucional.",
    "Definir titulo, subtitulo y subject coherentes con la actividad en curso.",
    "Mantener compatibilidad con clase article, spanish, letterpaper y oneside.",
    "Revisar y cerrar correctamente entornos tabular antes de compilar.",
    "No cambiar la estructura base de portada sin instruccion editorial.",
    "Conservar nombres de archivo locales salvo normalizacion acordada."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y documentos juridicos verificables.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Conservar la malla curricular de Derecho como fuente institucional local.",
    "Agregar entradas BibTeX especificas solo cuando la fuente exista y sea verificable.",
    "Validar que las claves citadas existan en el .bib local.",
    "No inventar referencias; marcar faltantes como pendientes."
  ],
  "propagation_hints": [
    "Propagar hacia arriba y laterales solo reglas verificadas y no duplicadas.",
    "Mantener compresion union-dedupe con criterio lossless.",
    "Preservar reglas utiles previas aunque se reubiquen por categoria.",
    "No propagar supuestos como reglas definitivas.",
    "Conservar incidencias historicas de salida no estructurada detectadas en ciclos previos.",
    "Normalizar manualmente memorias heredadas del ciclo 1 si se reutilizan.",
    "Propagar correcciones locales solo despues de verificar archivos afectados."
  ],
  "open_questions": [
    "Confirmar si existe memoria util adicional en actividad-1 de filosofia-del-derecho para fusion posterior.",
    "Definir formato minimo de conclusion juridica por tipo de evidencia.",
    "Corregir en README los nombres con caracteres anomalos y tokens sin expandir ($(@{...}.Slug)).",
    "Corregir tokens sin expandir en README y programa analitico.",
    "Revisar y reparar corte de entorno tabular en el archivo de reporte .tex.",
    "Confirmar criterio editorial sobre publico sin acento frente a publico con acento.",
    "Validar si se normaliza nomenclatura de archivos con caracteres acentuados."
  ],
  "sources": [
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
    "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde",
    "UnADM"
  ],
  "compression": {
    "method": "union-dedupe",
    "lossless": true
  },
  "schema_version": 1
}
```