{
  "summary": [
    "Materia destino consolidada con identidad institucional UnADM y control de normalizacion activo.",
    "Compresion aplicada por union-dedupe sin perdida y sin regresion.",
    "Se mantiene pauta editorial local: citas verificables, analisis propio y cierre juridico aplicable.",
    "Ubicacion curricular local verificada: semestre 2, bloque 2, obligatoria, 8 creditos.",
    "Persisten deudas tecnicas locales verificadas: placeholders de slug, expresiones PowerShell sin resolver, nombres o rutas corruptas y campo TeX truncado en Tipo/Creditos.",
    "No hay insumo tematico verificable desde la actividad origen para transferir contenido disciplinar."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en todo entregable.",
    "Usar datos curriculares verificados: semestre 2, bloque 2, obligatoria, 8 creditos.",
    "Conservar autoria real del estudiante y validar autor y matricula antes de entrega final.",
    "Autor local visible [supuesto hasta validar]: Martin Jonathan de la Cruz; matricula ES2611202040.",
    "Mantener figura docente como pendiente cuando solo exista placeholder y resolver antes de entrega.",
    "Figura docente visible [supuesto]: Nombre por definir.",
    "Marcar como supuesto cualquier dato no visible en origen o contexto local.",
    "Registrar fuentes provisionales heredadas como metadato de trazabilidad, no como fuente academica.",
    "Fuente provisional heredada: Codex desde ingenieria-en-sistemas-computacionales.",
    "Fuente provisional heredada: GPT-Pro desde Actividad 1.",
    "Fuente provisional heredada: Auto (model-router) desde Actividad 1.",
    "Fuente provisional heredada: Claude Foundry desde Actividad 1."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Mantener estructura local: reporte, presentacion, bibliografia, programa analitico y carpeta de referencias.",
    "Alinear cada producto a cinco ejes: problema, conceptos o norma, producto, analisis propio, conclusion transferible.",
    "Usar el programa analitico como guia editorial por actividad.",
    "Sincronizar README, programa analitico, plantillas TeX y .bib por actividad.",
    "Mantener nombres de archivos y slug de materia consistentes.",
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
    "No trasladar contenido tematico de filosofia del derecho sin evidencia verificable.",
    "No usar la actividad origen como base disciplinar si no aporta contenido verificable."
  ],
  "quality_gates": [
    "Bloquear propagacion de insumos no JSON parseable.",
    "Revisar y normalizar manualmente insumos desestructurados antes de aplicar aguas abajo.",
    "Revisar coherencia entre README, programa analitico y plantillas TeX.",
    "Detectar placeholders, expresiones PowerShell y rutas corruptas antes de compilar.",
    "Detectar campos truncados antes de entrega final.",
    "Detectar nombres de archivo corruptos antes de entrega final.",
    "Exigir citas verificables con correspondencia 1:1 contra bibliografia declarada.",
    "Compilar LaTeX sin errores antes de salida final."
  ],
  "latex_rules": [
    "Conservar plantilla base article en espanol y letterpaper.",
    "Completar metadatos del documento antes de salida final.",
    "Usar curso Derecho penal especial mexicano en metadatos.",
    "Mantener LDE-S2B2 como dato supuesto hasta confirmacion institucional.",
    "Usar derecho-penal-especial-mexicano.bib como bibliografia local.",
    "Corregir campos truncados o placeholders visibles en plantillas.",
    "Completar authortable en campo Tipo/Creditos como Obligatoria / 8.",
    "Mantener portada, tabla de datos academicos y secciones alineadas al programa analitico.",
    "Evitar macros o rutas con expresiones de plantilla sin resolver."
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
    "Aplicar deduplicacion semantica sin recortar informacion util.",
    "Mantener bandera de normalizacion manual para insumos heredados no estructurados.",
    "Propagar a laterales las correcciones de placeholders, campos truncados, expresiones PowerShell y nombres o rutas corruptas.",
    "Propagar reglas de integridad bibliografica a materias de derecho.",
    "Ciclo 1 necesita normalizacion manual si se reutiliza.",
    "Ciclo 2 necesita normalizacion manual si se reutiliza.",
    "Ciclo 3 necesita normalizacion manual si se reutiliza.",
    "Ciclo 4 necesita normalizacion manual si se reutiliza.",
    "Ciclo 5 necesita normalizacion manual si se reutiliza.",
    "Ciclo 6 necesita normalizacion manual si se reutiliza.",
    "Ciclo 7 necesita normalizacion manual si se reutiliza.",
    "Ciclo 8 necesita normalizacion manual si se reutiliza.",
    "Ciclo 9 necesita normalizacion manual si se reutiliza.",
    "Ciclo 10 necesita normalizacion manual si se reutiliza.",
    "Ciclo 11 necesita normalizacion manual si se reutiliza.",
    "Supuesto: no existe nuevo contenido disciplinar valido en el origen para propagar.",
    "Ciclo 4: mantener control activo de calidad estructural antes de nueva propagacion."
  ],
  "open_questions": [
    "Confirmar memoria tematica concreta de la actividad origen para herencia disciplinar.",
    "Confirmar correspondencia real de autor y matricula visibles.",
    "Definir nombre real de figura docente en plantillas.",
    "Confirmar si LDE-S2B2 debe fijarse como regla global de materia.",
    "Cerrar correccion del placeholder de slug en README y programa analitico.",
    "Cerrar correccion de expresiones PowerShell sin resolver en README y programa analitico.",
    "Cerrar correccion de nombres y rutas corruptas en README y estructura TeX.",
    "Cerrar correccion del campo Tipo/Creditos truncado en plantilla TeX."
  ]
}