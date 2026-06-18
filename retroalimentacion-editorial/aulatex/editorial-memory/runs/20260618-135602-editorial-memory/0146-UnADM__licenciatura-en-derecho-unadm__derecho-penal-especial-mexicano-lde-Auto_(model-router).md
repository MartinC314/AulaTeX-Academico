{
  "summary": [
    "Materia destino con identidad institucional UnADM.",
    "Conservar compresion union-dedupe sin perdida.",
    "Integrar memoria institucional heredada solo tras normalizacion.",
    "Mantener citas verificables y cierre juridico propio.",
    "No hay memoria tematica concreta de la actividad origen."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en todo entregable.",
    "Usar datos curriculares verificados: semestre 2, bloque 2, obligatoria, 8 creditos.",
    "Marcar como supuesto cualquier dato no visible en el origen o contexto local.",
    "Conservar autoria real del estudiante.",
    "No inventar figuras docentes.",
    "Validar autor, matricula y figura docente antes de entrega final."
  ],
  "structure_rules": [
    "Tomar la carpeta de materia como punto de entrada canonico.",
    "Alinear cada producto a problema, conceptos o norma, producto, analisis propio y conclusion transferible.",
    "Sincronizar reporte, presentacion y bibliografia local por actividad.",
    "Mantener nombres de archivos y slug de materia consistentes.",
    "Corregir nombres corruptos en README sin cambiar el slug canonico.",
    "Sustituir placeholders de slug por derecho-penal-especial-mexicano.bib.",
    "Usar el programa analitico como guia editorial de cada actividad."
  ],
  "activity_rules": [
    "Mapear cada actividad a un problema juridico o social concreto.",
    "Vincular el problema con normas, conceptos o doctrina penal aplicable.",
    "Incluir postura academica propia con fundamento juridico.",
    "Cerrar con conclusion juridica aplicable a la practica profesional.",
    "Agregar fuentes especificas de la actividad al .bib local antes de redactar version final.",
    "No trasladar contenido tematico de filosofia del derecho sin insumo verificable."
  ],
  "quality_gates": [
    "Bloquear propagacion de contenido no JSON parseable.",
    "Revisar estructura y normalizar manualmente cuando el insumo venga desestructurado.",
    "Verificar coherencia entre README, programa analitico y plantillas TeX.",
    "Exigir citas verificables y correspondencia 1:1 con bibliografia declarada.",
    "Detectar placeholders visibles antes de compilar.",
    "Detectar campos truncados antes de entrega final.",
    "Compilar LaTeX sin errores antes de generar salida final.",
    "Revisar respuesta no estructurada heredada antes de aplicar aguas abajo."
  ],
  "latex_rules": [
    "Conservar plantilla base article en espanol y formato letterpaper.",
    "Completar metadatos del documento antes de generar salida final.",
    "Corregir campos truncados o placeholders visibles en plantillas.",
    "Mantener portada, tabla de datos academicos y secciones alineadas al programa analitico.",
    "Usar curso Derecho penal especial mexicano en metadatos.",
    "Usar codigo LDE-S2B2 solo como dato pendiente de confirmacion.",
    "Usar derecho-penal-especial-mexicano.bib como bibliografia local.",
    "Evitar macros o rutas con expresiones de plantilla sin resolver."
  ],
  "bibliography_rules": [
    "Usar archivo .bib local de la materia como fuente unica de referencias del entregable.",
    "Conservar fuentes institucionales UnADM ya registradas.",
    "No inventar fuentes ni datos bibliograficos faltantes.",
    "Registrar fecha de consulta cuando aplique a sitios web o recursos variables.",
    "Agregar entradas BibTeX especificas por actividad solo con datos verificables.",
    "Mantener correspondencia exacta entre citas en texto y entradas .bib.",
    "No usar la actividad origen como fuente bibliografica si no aporta contenido verificable."
  ],
  "propagation_hints": [
    "Propagar hacia arriba y laterales solo reglas validadas y no contradictorias.",
    "Priorizar reglas institucionales UnADM cuando exista conflicto de nivel.",
    "Mantener bandera de normalizacion manual en ciclo 1 para insumos heredados de Codex.",
    "Aplicar deduplicacion semantica sin recortar informacion util.",
    "Propagar correcciones de placeholders si aparecen en materias laterales.",
    "Propagar reglas de integridad bibliografica a actividades de derecho."
  ],
  "open_questions": [
    "Confirmar memoria concreta de la actividad origen para herencia tematica especifica.",
    "Definir nombre real de figura docente en plantillas de la materia.",
    "Verificar y corregir rutas o entradas con caracteres anomalos en README y estructura TeX.",
    "Confirmar si el codigo de curso LDE-S2B2 debe fijarse como regla global de materia.",
    "Confirmar que autor y matricula visibles corresponden al estudiante real.",
    "Confirmar cierre del campo truncado Tipo/Creditos en la plantilla TeX."
  ]
}