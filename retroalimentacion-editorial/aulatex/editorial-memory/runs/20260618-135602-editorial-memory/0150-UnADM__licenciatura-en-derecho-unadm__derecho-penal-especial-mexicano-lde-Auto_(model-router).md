{
  "summary": [
    "Materia destino: Derecho penal especial mexicano, Licenciatura en Derecho UnADM.",
    "Ubicacion curricular verificada localmente: semestre 2, bloque 2, obligatoria, 8 creditos.",
    "Conservar identidad institucional UnADM en todos los entregables.",
    "Mantener compresion union-dedupe sin perdida y sin regresion.",
    "Integrar memoria heredada solo tras normalizacion.",
    "Conservar control de normalizacion para insumos no estructurados o no parseables.",
    "Insumos previos de Codex y GPT-Pro llegaron sin JSON parseable.",
    "No hay memoria tematica verificable de la actividad origen para transferir contenido disciplinar.",
    "Mantener pauta editorial local: citas verificables, analisis propio y cierre juridico.",
    "Deuda tecnica local: placeholders de slug, nombres corruptos y campo truncado en plantillas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM.",
    "Usar datos curriculares verificados: semestre 2, bloque 2, obligatoria, 8 creditos.",
    "Marcar como supuesto cualquier dato no visible en origen o contexto local.",
    "Conservar autoria real del estudiante.",
    "No inventar figuras docentes.",
    "Validar autor, matricula y figura docente antes de entrega final.",
    "Autor local visible: Martin Jonathan de la Cruz; matricula ES2611202040; verificar correspondencia real.",
    "Figura docente visible como placeholder: Nombre por definir; resolver antes de entrega.",
    "Fuente provisional heredada: Codex desde ingenieria-en-sistemas-computacionales.",
    "Fuente provisional heredada: GPT-Pro desde Actividad 1."
  ],
  "structure_rules": [
    "Tomar la carpeta de materia como punto de entrada canonico.",
    "Usar el programa analitico como guia editorial por actividad.",
    "Alinear cada producto a problema, conceptos o norma, producto, analisis propio y conclusion transferible.",
    "Sincronizar reporte, presentacion y bibliografia local por actividad.",
    "Mantener nombres de archivos y slug de materia consistentes.",
    "Corregir nombres corruptos en README sin cambiar el slug canonico.",
    "Corregir expresiones de plantilla sin resolver en README y programa analitico.",
    "Sustituir placeholders de slug por derecho-penal-especial-mexicano.bib.",
    "Corregir entradas corruptas de reporte y referencias en README.",
    "Mantener estructura local: reporte, presentacion, bibliografia, programa analitico y carpeta de referencias."
  ],
  "activity_rules": [
    "Mapear cada actividad a un problema juridico o social concreto.",
    "Vincular el problema con normas, conceptos o doctrina penal aplicable.",
    "Incluir postura academica propia con fundamento juridico.",
    "Cerrar con conclusion juridica aplicable a la practica profesional.",
    "Agregar fuentes especificas de la actividad al .bib local antes de redactar version final.",
    "No trasladar contenido tematico de filosofia del derecho sin insumo verificable.",
    "No usar la actividad origen como base disciplinar si no aporta contenido verificable."
  ],
  "quality_gates": [
    "Bloquear propagacion de contenido no JSON parseable.",
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Normalizar manualmente insumos desestructurados antes de aplicarlos.",
    "Verificar coherencia entre README, programa analitico y plantillas TeX.",
    "Exigir citas verificables con correspondencia 1:1 contra bibliografia declarada.",
    "Detectar placeholders visibles antes de compilar.",
    "Detectar campos truncados antes de entrega final.",
    "Detectar expresiones PowerShell o plantillas sin resolver.",
    "Detectar nombres de archivo corruptos antes de entrega final.",
    "Compilar LaTeX sin errores antes de generar salida final."
  ],
  "latex_rules": [
    "Conservar plantilla base article en espanol y letterpaper.",
    "Completar metadatos del documento antes de salida final.",
    "Mantener portada, tabla de datos academicos y secciones alineadas al programa analitico.",
    "Usar curso Derecho penal especial mexicano en metadatos.",
    "Usar codigo LDE-S2B2 solo como dato pendiente de confirmacion.",
    "Usar derecho-penal-especial-mexicano.bib como bibliografia local.",
    "Evitar macros o rutas con expresiones de plantilla sin resolver.",
    "Corregir campos truncados o placeholders visibles en plantillas.",
    "Completar campo Tipo/Creditos en authortable como Obligatoria / 8.",
    "Mantener Figura docente como dato pendiente solo si no ha sido validada."
  ],
  "bibliography_rules": [
    "Usar archivo .bib local de la materia como fuente unica de referencias del entregable.",
    "Conservar fuentes institucionales UnADM ya registradas.",
    "Conservar entradas base: unadmSitioWeb y unadmMallaDerecho2024.",
    "No inventar fuentes ni datos bibliograficos faltantes.",
    "Registrar fecha de consulta cuando aplique a sitios web o recursos variables.",
    "Agregar entradas BibTeX especificas por actividad solo con datos verificables.",
    "Mantener correspondencia exacta entre citas en texto y entradas .bib.",
    "No usar la actividad origen como fuente bibliografica si no aporta contenido verificable."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo reglas validadas y no contradictorias.",
    "Priorizar reglas institucionales UnADM cuando exista conflicto de nivel.",
    "Aplicar deduplicacion semantica sin recortar informacion util.",
    "Mantener bandera de normalizacion manual para insumos heredados no estructurados.",
    "Propagar reglas de integridad bibliografica a actividades de derecho.",
    "Propagar correcciones de placeholders y campos truncados a materias laterales similares.",
    "Propagar correcciones de nombres corruptos si aparecen en materias laterales.",
    "Ciclo 1 necesita normalizacion manual si se reutiliza.",
    "Ciclo 2 mantiene control activo de calidad estructural antes de nueva propagacion."
  ],
  "open_questions": [
    "Confirmar memoria concreta de la actividad origen para herencia tematica especifica.",
    "Definir nombre real de figura docente en plantillas de la materia.",
    "Confirmar que autor y matricula visibles correspondan al estudiante real.",
    "Confirmar si LDE-S2B2 debe fijarse como regla global de materia.",
    "Verificar y corregir rutas o entradas con caracteres anomalos en README y estructura TeX.",
    "Cerrar correccion de nombres corruptos en README.",
    "Cerrar correccion del placeholder de slug en README y programa analitico.",
    "Cerrar correccion del campo Tipo/Creditos en plantilla TeX."
  ]
}