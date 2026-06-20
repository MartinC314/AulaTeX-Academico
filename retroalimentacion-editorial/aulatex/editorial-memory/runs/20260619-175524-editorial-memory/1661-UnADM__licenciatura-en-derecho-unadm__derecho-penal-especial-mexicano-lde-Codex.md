{
  "summary": [
    "Materia consolidada con identidad institucional UnADM y control de normalizacion activo.",
    "Compresion vigente por union-dedupe sin perdida y sin regresion.",
    "Pauta editorial local activa: citas verificables, analisis propio y cierre juridico aplicable.",
    "Ubicacion curricular verificada localmente: semestre 2, bloque 2, obligatoria, 8 creditos.",
    "Insumos heredados no parseables requieren normalizacion manual previa.",
    "Supuesto: no existe contenido disciplinar verificable desde actividad origen para transferencia tematica.",
    "Persisten deudas tecnicas verificadas: placeholders de slug, expresiones PowerShell sin resolver, nombres o rutas corruptas y campo TeX truncado en Tipo/Creditos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en todo entregable.",
    "Usar datos curriculares verificados: semestre 2, bloque 2, obligatoria, 8 creditos.",
    "Conservar autoria real del estudiante y validar autor y matricula antes de entrega final.",
    "Autor local visible [supuesto hasta validar]: Martin Jonathan de la Cruz; matricula ES2611202040.",
    "Mantener figura docente como pendiente solo si existe placeholder y resolver antes de entrega.",
    "Figura docente visible [supuesto]: Nombre por definir.",
    "Marcar como supuesto cualquier dato no visible en origen o contexto local.",
    "Registrar fuentes provisionales heredadas como trazabilidad tecnica, no como fuente academica."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Mantener estructura local: reporte, presentacion, bibliografia, programa analitico y carpeta de referencias.",
    "Alinear cada producto a cinco ejes: problema, conceptos o norma, producto, analisis propio, conclusion transferible.",
    "Sincronizar README, programa analitico, plantillas TeX y .bib por actividad.",
    "Mantener nombres de archivo y slug canonico consistentes.",
    "Corregir placeholders de slug a derecho-penal-especial-mexicano.bib.",
    "Corregir expresiones PowerShell sin resolver en README y programa analitico.",
    "Corregir nombres de archivo y rutas corruptas sin cambiar el slug canonico."
  ],
  "activity_rules": [
    "Mapear cada actividad a un problema juridico o social concreto.",
    "Vincular el problema con normas, conceptos o doctrina penal aplicable.",
    "Incluir analisis y postura academica propia con fundamento juridico.",
    "Cerrar con conclusion juridica aplicable a la practica profesional.",
    "Agregar fuentes especificas de la actividad al .bib local antes de la version final.",
    "No trasladar contenido tematico de filosofia del derecho sin evidencia verificable.",
    "No usar la actividad origen como base disciplinar si no aporta contenido verificable."
  ],
  "quality_gates": [
    "Bloquear propagacion de insumos no JSON parseable.",
    "Normalizar manualmente toda respuesta desestructurada antes de aplicar aguas abajo.",
    "Revisar coherencia entre README, programa analitico y plantillas TeX.",
    "Detectar placeholders, expresiones PowerShell y rutas corruptas antes de compilar.",
    "Detectar campos truncados antes de entrega final.",
    "Exigir citas verificables con correspondencia 1:1 contra bibliografia declarada.",
    "Compilar LaTeX sin errores antes de salida final."
  ],
  "latex_rules": [
    "Conservar plantilla base article en espanol y letterpaper.",
    "Completar metadatos del documento antes de salida final.",
    "Usar curso Derecho penal especial mexicano en metadatos.",
    "Mantener LDE-S2B2 como dato supuesto hasta confirmacion institucional.",
    "Usar derecho-penal-especial-mexicano.bib como bibliografia local.",
    "Evitar macros o rutas con expresiones de plantilla sin resolver.",
    "Completar authortable en campo Tipo/Creditos como Obligatoria / 8.",
    "Corregir campos truncados o placeholders visibles en plantillas.",
    "Mantener figura docente como pendiente solo si no ha sido validada."
  ],
  "bibliography_rules": [
    "Usar el archivo .bib local como fuente unica de referencias del entregable.",
    "Conservar entradas institucionales base: unadmSitioWeb y unadmMallaDerecho2024.",
    "Agregar entradas BibTeX por actividad solo con datos verificables.",
    "No inventar fuentes ni metadatos bibliograficos faltantes.",
    "Mantener correspondencia exacta entre citas en texto y entradas .bib.",
    "Registrar fecha de consulta en recursos web o variables.",
    "No usar la actividad origen como fuente bibliografica si no aporta contenido verificable."
  ],
  "propagation_hints": [
    "Propagar solo reglas validadas y no contradictorias.",
    "Priorizar reglas institucionales UnADM en conflictos de nivel.",
    "Aplicar deduplicacion semantica sin recorte de informacion util.",
    "Propagar a laterales correcciones de placeholders, campos truncados, expresiones PowerShell y nombres o rutas corruptas.",
    "Propagar reglas de integridad bibliografica a materias de derecho.",
    "Ciclo 20: mantener control activo de calidad estructural antes de nueva propagacion.",
    "Ciclo 20 necesita normalizacion manual si se reutiliza.",
    "Supuesto: no existe nuevo contenido disciplinar valido en el origen para propagar."
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