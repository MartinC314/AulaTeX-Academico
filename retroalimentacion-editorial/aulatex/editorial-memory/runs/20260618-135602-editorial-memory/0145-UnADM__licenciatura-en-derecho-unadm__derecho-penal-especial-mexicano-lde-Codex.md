{
  "summary": [
    "Materia destino inicializada con memoria institucional UnADM y control de normalizacion.",
    "Se mantiene compresion union-dedupe sin perdida y sin regresion.",
    "Se agrega pauta editorial local: identidad UnADM, citas verificables y cierre juridico propio."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en todo entregable.",
    "Usar datos curriculares de la materia: semestre 2, bloque 2, obligatoria, 8 creditos.",
    "Marcar como supuesto cualquier dato no visible en la actividad origen.",
    "Conservar autoria real del estudiante y no inventar figuras docentes."
  ],
  "structure_rules": [
    "Tomar la carpeta de materia como punto de entrada canonico.",
    "Alinear cada producto a los cinco ejes: problema, conceptos/norma, producto, analisis propio, conclusion transferible.",
    "Sincronizar reporte, presentacion y bibliografia local por actividad.",
    "Mantener nombres de archivos y slug de materia consistentes."
  ],
  "activity_rules": [
    "Mapear cada actividad a un problema juridico o social concreto.",
    "Incluir postura academica propia con fundamento juridico.",
    "Cerrar con conclusion juridica aplicable a practica profesional.",
    "Agregar fuentes especificas de la actividad al .bib local antes de redactar version final."
  ],
  "quality_gates": [
    "Bloquear propagacion de contenido no JSON parseable.",
    "Revisar estructura y normalizar manualmente cuando el insumo venga desestructurado.",
    "Verificar coherencia entre README, programa analitico y plantillas TeX.",
    "Exigir citas verificables y correspondencia 1:1 con bibliografia declarada."
  ],
  "latex_rules": [
    "Conservar plantilla base article en espanol y formato letterpaper.",
    "Completar metadatos del documento antes de generar salida final.",
    "Corregir campos truncados o placeholders visibles en plantillas.",
    "Mantener portada, tabla de datos academicos y secciones alineadas al programa analitico."
  ],
  "bibliography_rules": [
    "Usar archivo .bib local de la materia como fuente unica de referencias del entregable.",
    "Conservar fuentes institucionales UnADM ya registradas.",
    "No inventar fuentes ni datos bibliograficos faltantes.",
    "Registrar fecha de consulta cuando aplique a sitios web o recursos variables."
  ],
  "propagation_hints": [
    "Propagar hacia arriba y laterales solo reglas validadas y no contradictorias.",
    "Priorizar reglas institucionales UnADM cuando exista conflicto de nivel.",
    "Mantener bandera de normalizacion manual en ciclo 1 para insumos heredados de Codex.",
    "Aplicar deduplicacion semantica sin recortar informacion util."
  ],
  "open_questions": [
    "Confirmar memoria concreta de la actividad origen para herencia tematica especifica.",
    "Definir nombre real de figura docente en plantillas de la materia.",
    "Verificar y corregir rutas/entradas con caracteres anómalos en README y estructura TeX.",
    "Confirmar si el codigo de curso LDE-S2B2 debe fijarse como regla global de materia."
  ]
}