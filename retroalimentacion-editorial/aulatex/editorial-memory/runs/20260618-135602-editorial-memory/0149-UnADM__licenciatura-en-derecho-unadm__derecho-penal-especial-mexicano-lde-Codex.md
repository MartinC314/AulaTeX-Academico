{
  "summary": [
    "Se mantiene identidad institucional UnADM y compresion union-dedupe sin perdida.",
    "Se conserva control de normalizacion para insumos no estructurados o no parseables.",
    "Se integra pauta editorial local de la materia con cierre juridico y citas verificables.",
    "Se confirma deuda tecnica local: placeholders de slug y campo truncado en plantilla TeX.",
    "No hay insumo tematico verificable desde actividad origen para transferir contenido disciplinar."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en todo entregable.",
    "Usar datos curriculares verificados: semestre 2, bloque 2, obligatoria, 8 creditos.",
    "Conservar autoria real del estudiante.",
    "No inventar figuras docentes.",
    "Marcar como supuesto cualquier dato no visible en origen o contexto local.",
    "Validar autor, matricula y figura docente antes de entrega final.",
    "Autor visible [supuesto hasta validar]: Martin Jonathan de la Cruz; matricula ES2611202040.",
    "Figura docente visible [supuesto]: Nombre por definir; resolver antes de entrega.",
    "Fuente provisional heredada: Codex desde ingenieria-en-sistemas-computacionales."
  ],
  "structure_rules": [
    "Tomar la carpeta de materia como punto de entrada canonico.",
    "Alinear cada producto a cinco ejes: problema, conceptos o norma, producto, analisis propio, conclusion transferible.",
    "Sincronizar reporte, presentacion y bibliografia local por actividad.",
    "Mantener nombres de archivos y slug de materia consistentes.",
    "Usar el programa analitico como guia editorial por actividad.",
    "Corregir nombres corruptos en README sin cambiar slug canonico.",
    "Sustituir placeholders de slug por derecho-penal-especial-mexicano.bib.",
    "Corregir expresiones de plantilla sin resolver en README y programa analitico."
  ],
  "activity_rules": [
    "Mapear cada actividad a un problema juridico o social concreto.",
    "Vincular el problema con normas, conceptos o doctrina penal aplicable.",
    "Incluir postura academica propia con fundamento juridico.",
    "Cerrar con conclusion juridica aplicable a la practica profesional.",
    "Agregar fuentes especificas de la actividad al .bib local antes de version final.",
    "No trasladar contenido tematico de filosofia del derecho sin insumo verificable."
  ],
  "quality_gates": [
    "Bloquear propagacion de contenido no JSON parseable.",
    "Revisar y normalizar manualmente insumos desestructurados antes de aplicar aguas abajo.",
    "Verificar coherencia entre README, programa analitico y plantillas TeX.",
    "Exigir citas verificables con correspondencia 1:1 contra bibliografia declarada.",
    "Detectar placeholders visibles antes de compilar.",
    "Detectar campos truncados antes de entrega final.",
    "Compilar LaTeX sin errores antes de salida final."
  ],
  "latex_rules": [
    "Conservar plantilla base article en espanol y letterpaper.",
    "Completar metadatos del documento antes de salida final.",
    "Corregir campos truncados o placeholders visibles en plantillas.",
    "Mantener portada, tabla de datos academicos y secciones alineadas al programa analitico.",
    "Usar curso Derecho penal especial mexicano en metadatos.",
    "Usar derecho-penal-especial-mexicano.bib como bibliografia local.",
    "Evitar macros o rutas con expresiones de plantilla sin resolver.",
    "Completar campo truncado Tipo/Creditos en authortable.",
    "Usar codigo LDE-S2B2 solo como dato pendiente de confirmacion."
  ],
  "bibliography_rules": [
    "Usar archivo .bib local de la materia como fuente unica de referencias del entregable.",
    "Conservar fuentes institucionales UnADM ya registradas.",
    "Agregar entradas BibTeX especificas por actividad solo con datos verificables.",
    "Mantener correspondencia exacta entre citas en texto y entradas .bib.",
    "Registrar fecha de consulta cuando aplique a sitios web o recursos variables.",
    "No inventar fuentes ni datos bibliograficos faltantes.",
    "No usar la actividad origen como fuente bibliografica si no aporta contenido verificable.",
    "Conservar entradas base: unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo reglas validadas y no contradictorias.",
    "Priorizar reglas institucionales UnADM cuando exista conflicto de nivel.",
    "Aplicar deduplicacion semantica sin recortar informacion util.",
    "Mantener bandera de normalizacion manual para insumos heredados no estructurados.",
    "Propagar correcciones de placeholders y campos truncados a materias laterales similares.",
    "Propagar reglas de integridad bibliografica a actividades de derecho.",
    "Ciclo 2: mantener control activo de calidad estructural antes de nueva propagacion."
  ],
  "open_questions": [
    "Confirmar memoria concreta de actividad origen para herencia tematica especifica.",
    "Definir nombre real de figura docente en plantillas de la materia.",
    "Verificar que autor y matricula visibles correspondan al estudiante real.",
    "Confirmar si LDE-S2B2 debe fijarse como regla global de materia.",
    "Corregir rutas o entradas con caracteres anómalos en README y estructura TeX.",
    "Cerrar correccion del campo truncado Tipo/Creditos en plantilla TeX."
  ]
}