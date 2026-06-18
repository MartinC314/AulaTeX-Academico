```json
{
  "summary": [
    "Materia destino con plantilla base, programa analitico y bibliografia local definidos.",
    "Asignatura de Licenciatura en Derecho UnADM, semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Se conserva incidencia historica de salida sin JSON parseable en ciclo previo.",
    "Supuesto: actividad origen (filosofia-del-derecho) no aporta reglas nuevas estructuradas en este ciclo."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada y metadatos.",
    "Usar nombre oficial de la materia: Bases de derecho internacional publico.",
    "Alinear entregables a Licenciatura en Derecho, semestre 4, bloque 1.",
    "Usar codigo de curso LDE-S4B1 en metadatos.",
    "Tratar la fuente provisional Codex como metadato de procedencia, no como identidad del entregable."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Organizar cada entrega con problema juridico o social, conceptos, analisis propio y conclusion juridica.",
    "Conservar separacion entre reporte, presentacion, programa analitico y bibliografia.",
    "Transformar la planeacion semanal en el producto academico solicitado.",
    "Mantener programa analitico como guia editorial de actividades.",
    "Conservar carpeta referencias-bases-de-derecho-internacional-publico como repositorio de apoyo."
  ],
  "activity_rules": [
    "Adaptar cada actividad al producto solicitado por la planeacion semanal.",
    "Incluir postura academica propia sustentada en fuentes verificables.",
    "Cerrar con conclusion transferible a la practica juridica.",
    "Integrar conceptos, normas, doctrina o datos pertinentes cuando correspondan.",
    "Distinguir hechos, argumentos, normas y criterio propio."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de propagar memoria aguas abajo.",
    "Revisar consistencia entre instrucciones de actividad y programa analitico.",
    "Bloquear afirmaciones sin respaldo documental o normativo.",
    "Revisar respuestas no estructuradas antes de aplicarlas aguas abajo.",
    "Validar citas y referencias antes de cerrar entregables.",
    "Validar sintaxis LaTeX y cierre de entornos antes de compilar.",
    "Marcar faltantes como pendientes sin sustituirlos por invenciones."
  ],
  "latex_rules": [
    "Reutilizar la plantilla .tex local de la materia como base de nuevas actividades.",
    "Completar metadatos de portada sin alterar identidad institucional.",
    "Mantener compatibilidad con clase article, spanish, letterpaper y oneside.",
    "Usar reporte-bases-de-derecho-internacional-publico.tex para reportes base.",
    "Usar presentacion-bases-de-derecho-internacional-publico.tex solo para productos de presentacion.",
    "Conservar nombres de archivo locales salvo normalizacion acordada.",
    "Definir titulo, subtitulo y subject coherentes con la actividad en curso."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y documentos juridicos verificables.",
    "Conservar la malla curricular de Derecho como fuente institucional local.",
    "No inventar referencias; marcar faltantes como pendientes.",
    "Agregar entradas BibTeX especificas solo cuando la fuente exista y sea verificable.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar hacia arriba y laterales solo reglas verificadas y no duplicadas.",
    "Mantener compresion union-dedupe con criterio lossless.",
    "Conservar la incidencia historica de salida no estructurada detectada en ciclo 1.",
    "Normalizar manualmente memorias heredadas del ciclo 1 si se reutilizan.",
    "No propagar supuestos como reglas definitivas.",
    "Preservar reglas utiles previas aunque se reubiquen por categoria."
  ],
  "open_questions": [
    "Confirmar si existe memoria util adicional en actividad-1 de filosofia-del-derecho para fusion posterior.",
    "Definir formato minimo de conclusion juridica por tipo de evidencia.",
    "Validar si se normaliza nomenclatura de archivos con caracteres acentuados.",
    "Revisar nombres en README con caracteres anomalos y tokens sin expandir ($(@{...}.Slug)).",
    "Confirmar si el nombre editorial debe conservar publico sin acento o usar publico con acento."
  ],
  "sources": [
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
    "UnADM/licenciatura-en-derecho-unadm/bases-de-derecho-internacional-publico-lde"
  ],
  "compression": {
    "method": "union-dedupe",
    "lossless": true
  },
  "schema_version": 1
}
```