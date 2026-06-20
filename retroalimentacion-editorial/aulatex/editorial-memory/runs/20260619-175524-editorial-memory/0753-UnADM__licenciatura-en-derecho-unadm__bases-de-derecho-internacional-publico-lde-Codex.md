{
  "summary": [
    "Materia destino con plantilla base, programa analitico y bibliografia local definidos.",
    "Asignatura UnADM de Licenciatura en Derecho: semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Se conservan incidencias historicas de salidas no estructuradas en ciclos previos.",
    "Propagacion recursiva activa en ciclo 13 con compresion union-dedupe lossless.",
    "Supuesto: actividad origen no aporta reglas nuevas estructuradas verificables en este ciclo.",
    "Se detectan tokens sin expandir en README y programa analitico.",
    "Se detectan caracteres anomalos en README.",
    "Se detecta corte de entorno tabular en reporte-bases-de-derecho-internacional-publico.tex."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada y metadatos.",
    "Usar nombre oficial/local de la materia: Bases de derecho internacional publico.",
    "Alinear entregables a Licenciatura en Derecho, semestre 4, bloque 1.",
    "Usar codigo de curso LDE-S4B1 en metadatos.",
    "Conservar al alumno registrado en plantilla si no hay instruccion local que lo sustituya.",
    "Tratar fuentes provisionales (Codex, GPT-Pro, Auto, Claude Foundry) como procedencia, no como identidad del entregable."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Conservar separacion entre reporte, presentacion, programa analitico y bibliografia.",
    "Mantener el programa analitico como guia editorial de actividades.",
    "Transformar la planeacion semanal en el producto academico solicitado.",
    "Organizar cada entrega con problema juridico o social, conceptos, fuentes, analisis propio y conclusion juridica.",
    "Distinguir reporte, presentacion y productos visuales segun la planeacion.",
    "Conservar la carpeta referencias-bases-de-derecho-internacional-publico como repositorio de apoyo."
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
    "Validar JSON parseable antes de propagar memoria.",
    "Revisar respuestas no estructuradas antes de aplicarlas aguas abajo.",
    "Revisar consistencia entre instrucciones de actividad y programa analitico.",
    "Bloquear afirmaciones sin respaldo documental o normativo.",
    "Validar citas y referencias antes de cerrar entregables.",
    "Validar sintaxis LaTeX y cierre de entornos antes de compilar.",
    "Verificar que README, programa analitico, .bib y plantillas locales coincidan.",
    "Marcar faltantes como pendientes sin sustituirlos por invenciones."
  ],
  "latex_rules": [
    "Reutilizar la plantilla .tex local de la materia como base de nuevas actividades.",
    "Usar reporte-bases-de-derecho-internacional-publico.tex para reportes base.",
    "Usar presentacion-bases-de-derecho-internacional-publico.tex solo para productos de presentacion.",
    "Completar metadatos de portada sin alterar identidad institucional.",
    "Mantener compatibilidad con clase article, spanish, letterpaper y oneside.",
    "Definir titulo, subtitulo y subject coherentes con la actividad en curso.",
    "Revisar y cerrar correctamente entornos tabular antes de compilar.",
    "Conservar nombres de archivo locales salvo normalizacion acordada.",
    "No cambiar la estructura base de portada sin instruccion editorial."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y documentos juridicos verificables.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Agregar entradas BibTeX especificas solo cuando la fuente exista y sea verificable.",
    "Validar que las claves citadas existan en el .bib local.",
    "No inventar referencias; marcar faltantes como pendientes."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas y no duplicadas.",
    "Mantener compresion union-dedupe con criterio lossless.",
    "Preservar reglas utiles previas aunque se reubiquen por categoria.",
    "No propagar supuestos como reglas definitivas.",
    "Conservar incidencias historicas de salida no estructurada de ciclos previos.",
    "Mantener auditoria de parseo JSON antes de nueva propagacion.",
    "Ciclo 1 requiere normalizacion manual si se reutiliza.",
    "Ciclo 2 requiere normalizacion manual si se reutiliza.",
    "Ciclo 3 requiere normalizacion manual si se reutiliza.",
    "Ciclo 4 requiere normalizacion manual si se reutiliza.",
    "Ciclo 5 requiere normalizacion manual si se reutiliza.",
    "Ciclo 6 requiere normalizacion manual si se reutiliza.",
    "Ciclo 7 requiere normalizacion manual si se reutiliza.",
    "Ciclo 8 requiere normalizacion manual si se reutiliza.",
    "Ciclo 9 requiere normalizacion manual si se reutiliza.",
    "Ciclo 10 requiere normalizacion manual si se reutiliza.",
    "Ciclo 11 requiere normalizacion manual si se reutiliza.",
    "Ciclo 12 requiere normalizacion manual si se reutiliza.",
    "Ciclo 13: mantener auditoria de parseo JSON antes de nueva propagacion."
  ],
  "open_questions": [
    "Supuesto: confirmar si actividad-1 de filosofia-del-derecho aporta memoria estructurada adicional para fusion futura.",
    "Confirmar criterio editorial sobre publico sin acento frente a publico con acento.",
    "Normalizar nombres con caracteres anomalos en README.",
    "Corregir tokens sin expandir ($(@{...}.Slug)) en README y programa analitico.",
    "Reparar corte de entorno tabular en reporte-bases-de-derecho-internacional-publico.tex.",
    "Validar si se normaliza nomenclatura de archivos con caracteres acentuados."
  ]
}