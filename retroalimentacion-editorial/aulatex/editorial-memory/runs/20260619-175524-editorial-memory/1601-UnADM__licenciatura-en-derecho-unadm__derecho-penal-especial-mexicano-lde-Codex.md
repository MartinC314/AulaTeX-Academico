{
  "summary": [
    "Materia consolidada con identidad UnADM y control de normalizacion activo.",
    "Compresion aplicada por union-dedupe sin perdida y sin regresion.",
    "No hay insumo tematico verificable desde actividad origen para transferir contenido disciplinar.",
    "Persisten deudas tecnicas locales verificadas: placeholders de slug, expresiones PowerShell sin resolver, nombres o rutas corruptas y campo TeX truncado en Tipo/Creditos.",
    "Ubicacion curricular local verificada: semestre 2, bloque 2, obligatoria, 8 creditos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en todo entregable.",
    "Usar datos curriculares verificados: semestre 2, bloque 2, obligatoria, 8 creditos.",
    "Conservar autoria real del estudiante y validar autor y matricula antes de entrega final.",
    "Autor local visible [supuesto hasta validar]: Martin Jonathan de la Cruz; matricula ES2611202040.",
    "Mantener figura docente como pendiente cuando solo exista placeholder y resolver antes de entrega.",
    "Figura docente visible [supuesto]: Nombre por definir.",
    "Marcar como supuesto cualquier dato no visible en origen o contexto local.",
    "Registrar fuentes provisionales heredadas como metadato de trazabilidad, no como fuente academica."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Mantener estructura local: reporte, presentacion, bibliografia, programa analitico y carpeta de referencias.",
    "Alinear cada producto a cinco ejes: problema, conceptos o norma, producto, analisis propio, conclusion transferible.",
    "Usar el programa analitico como guia editorial por actividad.",
    "Sincronizar README, programa analitico, plantillas TeX y .bib por actividad.",
    "Corregir placeholders de slug a derecho-penal-especial-mexicano.bib.",
    "Corregir expresiones de plantilla PowerShell sin resolver en README y programa analitico.",
    "Corregir nombres de archivo y rutas corruptas sin cambiar el slug canonico."
  ],
  "activity_rules": [
    "Mapear cada actividad a un problema juridico o social concreto.",
    "Vincular el problema con normas, conceptos o doctrina penal aplicable.",
    "Incluir postura academica propia con fundamento juridico.",
    "Cerrar con conclusion juridica aplicable a la practica profesional.",
    "Agregar fuentes especificas de la actividad al .bib local antes de la version final.",
    "No usar la actividad origen como base disciplinar si no aporta contenido verificable.",
    "No trasladar contenido tematico de filosofia del derecho sin evidencia verificable."
  ],
  "quality_gates": [
    "Bloquear propagacion de insumos no JSON parseable.",
    "Normalizar manualmente toda respuesta desestructurada antes de aplicar aguas abajo.",
    "Revisar coherencia entre README, programa analitico y plantillas TeX.",
    "Exigir citas verificables con correspondencia 1:1 contra bibliografia declarada.",
    "Detectar placeholders, expresiones PowerShell y rutas corruptas antes de compilar.",
    "Detectar campos truncados antes de entrega final.",
    "Compilar LaTeX sin errores antes de salida final."
  ],
  "latex_rules": [
    "Conservar plantilla base article en espanol y letterpaper.",
    "Completar metadatos del documento antes de salida final.",
    "Usar curso Derecho penal especial mexicano en metadatos.",
    "Usar derecho-penal-especial-mexicano.bib como bibliografia local.",
    "Evitar macros o rutas con expresiones de plantilla sin resolver.",
    "Completar authortable en campo Tipo/Creditos como Obligatoria / 8.",
    "Corregir campos truncados o placeholders visibles en plantillas.",
    "Mantener portada, tabla de datos academicos y secciones alineadas al programa analitico.",
    "Mantener LDE-S2B2 como dato supuesto hasta confirmacion institucional.",
    "Mantener figura docente como pendiente solo si no ha sido validada."
  ],
  "bibliography_rules": [
    "Usar el archivo .bib local como fuente unica de referencias del entregable.",
    "Conservar entradas institucionales base: unadmSitioWeb y unadmMallaDerecho2024.",
    "Agregar entradas BibTeX por actividad solo con datos verificables.",
    "No inventar fuentes ni metadatos bibliograficos faltantes.",
    "Registrar fecha de consulta en recursos web o variables.",
    "Mantener correspondencia exacta entre citas en texto y entradas .bib.",
    "No usar la actividad origen como fuente bibliografica si no aporta contenido verificable."
  ],
  "propagation_hints": [
    "Propagar solo reglas validadas y no contradictorias.",
    "Priorizar reglas institucionales UnADM en conflictos de nivel.",
    "Mantener bandera de normalizacion manual para insumos heredados no estructurados.",
    "Aplicar deduplicacion semantica sin recortar informacion util.",
    "Propagar a laterales las correcciones de placeholders, campos truncados, expresiones PowerShell y nombres o rutas corruptas.",
    "Propagar reglas de integridad bibliografica a materias de derecho.",
    "Ciclo 5: mantener control activo de calidad estructural antes de nueva propagacion.",
    "Ciclo 5 necesita normalizacion manual si se reutiliza.",
    "Supuesto: no existe nuevo contenido disciplinar valido en el origen para propagar."
  ],
  "open_questions": [
    "Confirmar memoria tematica concreta de la actividad origen para herencia disciplinar.",
    "Confirmar correspondencia real de autor y matricula visibles.",
    "Definir nombre real de figura docente en plantillas.",
    "Confirmar si LDE-S2B2 debe fijarse como regla global de materia.",
    "Cerrar correccion del placeholder de slug en README y programa analitico.",
    "Cerrar correccion de expresiones PowerShell sin resolver.",
    "Cerrar correccion de nombres y rutas corruptas en README y estructura TeX.",
    "Cerrar correccion del campo Tipo/Creditos truncado en plantilla TeX."
  ]
}