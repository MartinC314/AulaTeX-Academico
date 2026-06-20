{
  "memoria_fundacional": {
    "summary": [
      "Nodo institucional IIIEPE reforzado como raíz editorial reusable dentro del estándar interinstitucional AulaTeX.",
      "La producción se organiza mediante entradas canónicas: reporte, actividad, presentación y bibliografía institucional.",
      "La estructura debe crecer por programa, carrera o materia sin romper contratos de compilación existentes.",
      "La memoria prioriza reutilización de plantillas compartidas, trazabilidad académica y compilación reproducible."
    ],
    "identity_rules": [
      "Mantener prefijo institucional en archivos raíz: reporte-iiiepe.tex, presentacion-iiiepe.tex y bibliografia-iiiepe.bib.",
      "Usar español académico claro, formal, didáctico y orientado a evidencias.",
      "Conservar trazabilidad institucional en portada, metadatos, rutas internas y nombres de entregables.",
      "Distinguir explícitamente institución, programa, materia, docente, periodo y tipo de documento.",
      "No asumir oferta académica, misión, reglamentos ni bibliografía sin verificación documental."
    ],
    "structure_rules": [
      "Definir IIIEPE como raíz institucional con subcarpetas por programa o carrera y materias dentro de cada programa.",
      "Incluir carpeta assets/ para imágenes, tablas, logos y recursos institucionales con nombres normalizados.",
      "Cada materia debe contener COMPILACION.md con comando exacto, archivo .bib esperado y contrato mínimo de compilación.",
      "Evitar duplicación de plantillas: referenciar base/ mediante \\input y rutas compatibles con TEXINPUTS.",
      "Separar documentos raíz institucionales de entregables específicos de materia.",
      "Mantener una estructura mínima por materia: objetivo, competencias, desarrollo, evidencias, evaluación y referencias.",
      "Usar nombres de carpetas en minúsculas, sin espacios y con guiones para portabilidad."
    ],
    "style_rules": [
      "Redactar párrafos breves, objetivos evaluables y secciones jerárquicas.",
      "Separar contenido base, instrucciones, entregables, criterios de evaluación y referencias.",
      "Usar listas y tablas solo cuando mejoren la claridad didáctica.",
      "Evitar relleno editorial, afirmaciones vagas y duplicación de apartados.",
      "Mantener consistencia terminológica entre reporte, actividad y presentación.",
      "Incluir marcadores [INV] cuando falten datos curriculares, normativos o bibliográficos."
    ],
    "quality_gates": [
      "El archivo objetivo compila sin errores con scripts/latexmk-build.ps1 recibiendo solo el .tex.",
      "No existen rutas duras a plantillas fuera del esquema TEXINPUTS/BIBINPUTS.",
      "Toda afirmación académica relevante tiene cita verificable o marcador de investigación pendiente.",
      "Cada entregable incluye objetivo, instrucciones o desarrollo, evidencias, evaluación y referencias.",
      "La bibliografía no contiene referencias inventadas ni claves BibTeX sin fuente rastreable.",
      "Las carpetas nuevas no rompen archivos existentes ni cambian nombres canónicos ya usados.",
      "El PDF final debe generarse en la carpeta del .tex objetivo conforme al flujo AulaTeX."
    ],
    "latex_rules": [
      "Usar plantilla institucional derivada de base/Template-Reporte, base/Templates-Informe o equivalente homologado.",
      "Centralizar bibliografía general en bibliografia-iiiepe.bib y permitir .bib local solo cuando la materia lo requiera.",
      "Declarar portada, índice, secciones y bibliografía con comandos estándar compatibles con el motor base.",
      "Evitar paquetes redundantes, conflictivos o no necesarios para el documento objetivo.",
      "Usar \\input para bloques reutilizables y evitar copiar plantillas completas en cada materia.",
      "Nombrar etiquetas LaTeX con prefijos estables: sec:, fig:, tab:, eq: y anexo:.",
      "Agregar comentarios TODO o [INV] sin impedir la compilación."
    ],
    "bibliography_rules": [
      "No inventar referencias; registrar solo fuentes verificables, consultables y trazables.",
      "Usar claves BibTeX legibles con patrón autorAnioTema cuando sea posible.",
      "Separar fuentes institucionales, normativas, teóricas y didácticas cuando aplique.",
      "Validar bibliografía oficial de cada asignatura antes de redactar contenido definitivo.",
      "Mantener homogeneidad de estilo bibliográfico en todos los documentos IIIEPE.",
      "Registrar fuentes pendientes como marcadores de investigación, no como entradas .bib ficticias."
    ],
    "research_markers": [
      "Confirmar nombre oficial, siglas y datos institucionales de IIIEPE.",
      "Confirmar oferta académica vigente y nomenclatura oficial de programas o carreras.",
      "Recabar lineamientos internos de formato, evaluación y citación si existen.",
      "Validar competencias institucionales transversales para integrarlas en plantillas.",
      "Identificar programas analíticos, sílabos o mapas curriculares por materia.",
      "Validar bibliografía mínima obligatoria antes de redacción final.",
      "Levantar inventario real de archivos .tex, .bib, assets y COMPILACION.md existentes."
    ]
  },
  "plan_editorial": {
    "objetivo_editorial": [
      "Consolidar una base editorial IIIEPE uniforme, escalable y compatible con el flujo AulaTeX.",
      "Preparar documentos institucionales reutilizables para que el Agente investigue, redacte, evalúe y compile después.",
      "Reducir variabilidad entre materias mediante contratos de estructura, bibliografía y compilación."
    ],
    "alcance": [
      "Reforzar memoria, plan editorial y maqueta institucional sin redactar actividades completas.",
      "Preparar artefactos base para reporte, actividad, presentación y bibliografía.",
      "Orientar la organización por programa o carrera, materia y entregable.",
      "Dejar marcadores de investigación donde falten fuentes, criterios o datos oficiales.",
      "No ejecutar investigación profunda ni validar contenido externo en esta fase."
    ],
    "estructura_base": [
      "IIIEPE/reporte-iiiepe.tex como entrada institucional para reportes generales.",
      "IIIEPE/presentacion-iiiepe.tex como entrada institucional para presentaciones.",
      "IIIEPE/bibliografia-iiiepe.bib como bibliografía central verificable.",
      "IIIEPE/assets/ para recursos institucionales normalizados.",
      "IIIEPE/<programa-o-carrera>/<materia>/ para contenidos específicos.",
      "Cada materia con reporte-<materia>.tex, actividad-<materia>.tex opcional, bibliografia local opcional y COMPILACION.md.",
      "Uso de base/ para plantillas compartidas mediante rutas resueltas por TEXINPUTS."
    ],
    "criterios_evaluacion": [
      "Homogeneidad formal entre documentos institucionales y de materia.",
      "Compilación reproducible con scripts oficiales de AulaTeX.",
      "Presencia de objetivo, competencias, resultados, evidencias, rúbrica y referencias.",
      "Claridad de instrucciones para el estudiante y de criterios para el docente.",
      "Trazabilidad de fuentes y ausencia de bibliografía inventada.",
      "Separación efectiva entre maqueta editorial, contenido investigado y redacción final.",
      "Compatibilidad con crecimiento futuro sin regresión de archivos existentes."
    ],
    "bibliografia_requerida": [
      "Lineamientos oficiales IIIEPE disponibles y verificables.",
      "Programas analíticos, sílabos o mapas curriculares por materia.",
      "Bibliografía oficial indicada por cada asignatura.",
      "Fuentes académicas primarias o secundarias validadas por el curso.",
      "Normas de citación adoptadas por el proyecto o por la institución.",
      "Documentos internos de evaluación, si existen y pueden citarse."
    ],
    "riesgos": [
      "Heterogeneidad de formatos heredados entre materias.",
      "Ausencia de lineamientos institucionales explícitos o accesibles.",
      "Uso de fuentes no verificables, incompletas o no citables.",
      "Duplicación de plantillas locales que dificulte mantenimiento.",
      "Rutas duras que rompan compilación fuera del entorno del autor.",
      "Confusión entre marcadores editoriales y contenido académico definitivo.",
      "Cambios de nomenclatura institucional no validados."
    ],
    "siguiente_fase_agente": [
      "Levantar inventario real de carpetas, archivos .tex, .bib, assets y COMPILACION.md en IIIEPE.",
      "Comparar la estructura existente contra el contrato canónico y proponer migración mínima sin regresión.",
      "Investigar datos institucionales oficiales y oferta académica vigente.",
      "Crear o normalizar esqueletos por materia con marcadores [INV] y rúbricas base.",
      "Validar compilación de al menos un reporte institucional y una presentación institucional.",
      "Validar que cada materia tenga comando de compilación documentado.",
      "Completar bibliografía solo con fuentes verificadas."
    ]
  },
  "maqueta_inicial": {
    "titulo": "IIIEPE | Maqueta editorial institucional reutilizable",
    "objetivo": [
      "Estandarizar la producción académica en LaTeX para IIIEPE con estructura, plantillas y criterios comunes.",
      "Servir como base editable para reportes, actividades y presentaciones posteriores.",
      "Dejar preparado el documento para investigación, redacción, evaluación y compilación por el Agente."
    ],
    "competencias": [
      "Organiza contenidos académicos con estructura formal, verificable y reutilizable.",
      "Integra objetivos, competencias, evidencias y criterios de evaluación en documentos académicos.",
      "Gestiona citas y referencias con buenas prácticas bibliográficas.",
      "Entrega documentos reproducibles mediante el flujo automatizado AulaTeX.",
      "Distingue contenido validado de información pendiente mediante marcadores de investigación."
    ],
    "resultados_esperados": [
      "Raíz IIIEPE con entradas canónicas institucionales y estructura por programa o materia.",
      "Documento maqueta listo para ser completado sin modificar el contrato de compilación.",
      "Matriz mínima de evaluación reutilizable por asignatura.",
      "Marcadores [INV] visibles para orientar investigación posterior.",
      "Bibliografía preparada para recibir únicamente fuentes verificables."
    ],
    "estructura_sugerida": [
      "00-portada-y-metadatos-institucionales",
      "01-proposito-y-alcance-del-documento",
      "02-datos-del-programa-materia-y-periodo",
      "03-competencias-y-resultados-de-aprendizaje",
      "04-contenido-base-por-unidades-o-temas",
      "05-actividades-evidencias-y-entregables",
      "06-criterios-de-evaluacion-y-rubrica",
      "07-recursos-assets-tablas-y-figuras",
      "08-referencias-anexos-y-marcadores-de-investigacion",
      "09-compilacion-control-de-version-y-checklist"
    ],
    "criterios_evaluacion": [
      "Pertinencia académica respecto al programa o materia validada.",
      "Claridad de objetivos, instrucciones, evidencias y entregables.",
      "Consistencia formal con plantillas institucionales AulaTeX.",
      "Uso correcto de citas, referencias y marcadores de investigación.",
      "Compilación limpia mediante el script oficial.",
      "Rúbrica breve, observable y alineada con resultados esperados."
    ],
    "bibliografia_requerida": [
      "Bibliografía oficial de cada asignatura.",
      "Lineamientos institucionales IIIEPE verificados.",
      "Normas de citación adoptadas por el proyecto.",
      "Documentos curriculares vigentes.",
      "Fuentes académicas validadas por el docente o programa.",
      "Recursos didácticos autorizados cuando aplique."
    ],
    "marcadores_investigacion": [
      "[INV] Confirmar nombre oficial, siglas y datos institucionales IIIEPE.",
      "[INV] Confirmar programas, carreras o materias activas.",
      "[INV] Identificar mapa curricular o programa analítico correspondiente.",
      "[INV] Validar competencias institucionales transversales.",
      "[INV] Recabar criterios de evaluación institucionales o de asignatura.",
      "[INV] Confirmar bibliografía mínima obligatoria.",
      "[INV] Verificar lineamientos de formato, portada y citación."
    ]
  },
  "tex_editorial": {
    "plantilla": [
      "Archivo sugerido: IIIEPE/reporte-iiiepe.tex.",
      "Debe iniciar con \\input{template} o mecanismo homologado por la plantilla base disponible.",
      "Variables editables mínimas: institucion, programa, materia, docente, estudiante, periodo, tipoDocumento.",
      "Secciones placeholder: portada, resumen, objetivo, competencias, desarrollo, evidencias, evaluación, referencias y anexos.",
      "Incluir comentarios seguros para compilación: % TODO y % [INV] sin romper LaTeX.",
      "Bibliografía sugerida: \\bibliography{bibliografia-iiiepe} cuando el template lo permita.",
      "No insertar referencias bibliográficas no verificadas en el .bib.",
      "Checklist final comentado: compila, citas resueltas, rutas relativas, assets existentes y PDF generado."
    ],
    "actividad": [
      "Archivo sugerido por materia: actividad-<materia>.tex.",
      "Estructura mínima: propósito, contexto, instrucciones, evidencia, formato de entrega, criterios de evaluación y referencias.",
      "Mantener la actividad como maqueta, sin desarrollar contenido disciplinar completo en esta fase.",
      "Agregar marcadores [INV] para fuentes, criterios específicos y datos del programa.",
      "Usar rúbrica breve con niveles o puntajes editables.",
      "Incluir sección de retroalimentación docente para uso posterior.",
      "Evitar dependencias visuales externas si no existen en assets/."
    ],
    "reporte": [
      "Archivo sugerido por materia: reporte-<materia>.tex.",
      "Estructura mínima: introducción, objetivo, marco o desarrollo por unidades, evidencias, conclusiones y referencias.",
      "Usar subsecciones para tablas y figuras desde assets/ con etiquetas estables.",
      "Insertar placeholders para citas como [INV: fuente requerida] hasta validar bibliografía.",
      "Agregar una tabla de control editorial con versión, fecha, responsable y estado.",
      "Incluir checklist previo a compilación y verificación de citas.",
      "Conservar compatibilidad con scripts/latexmk-build.ps1 pasando solo el .tex objetivo."
    ],
    "presentacion": [
      "Archivo sugerido: IIIEPE/presentacion-iiiepe.tex o presentacion-<materia>.tex según alcance.",
      "Estructura mínima: portada, agenda, objetivos, desarrollo por bloques, actividad o discusión, cierre y referencias.",
      "Usar máximo contenido por diapositiva: una idea central, hasta tres apoyos breves y recurso visual opcional.",
      "Mantener estilo institucional sobrio, legible y consistente con el reporte.",
      "Agregar diapositiva final de referencias y preguntas.",
      "No insertar imágenes, logos o gráficas si no están disponibles en assets/ o no tienen fuente validada.",
      "Dejar marcadores [INV] para datos institucionales, citas y recursos visuales pendientes."
    ]
  }
}