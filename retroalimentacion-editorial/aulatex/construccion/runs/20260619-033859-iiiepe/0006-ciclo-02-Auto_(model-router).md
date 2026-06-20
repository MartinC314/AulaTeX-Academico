{
  "memoria_fundacional": {
    "summary": [
      "IIIEPE se consolida como raíz editorial institucional reusable dentro del estándar interinstitucional AulaTeX.",
      "La producción institucional debe organizarse mediante entradas canónicas para reporte, actividad, presentación y bibliografía.",
      "El nodo debe crecer por programa, carrera o materia sin romper rutas, nombres ni contratos de compilación existentes.",
      "La memoria prioriza trazabilidad académica, reutilización de plantillas compartidas, bibliografía verificable y compilación reproducible."
    ],
    "identity_rules": [
      "Mantener archivos canónicos institucionales: reporte-iiiepe.tex, presentacion-iiiepe.tex y bibliografia-iiiepe.bib.",
      "Usar español académico formal, claro, didáctico y orientado a evidencias.",
      "Incluir metadatos trazables: institución, programa, carrera, materia, docente, estudiante, periodo y tipo de documento cuando apliquen.",
      "No asumir misión, oferta académica, reglamentos, competencias ni bibliografía institucional sin verificación documental.",
      "Marcar datos faltantes o no verificados con [INV] sin convertirlos en contenido definitivo."
    ],
    "structure_rules": [
      "Conservar IIIEPE como raíz institucional con subcarpetas por programa o carrera y materias dentro de cada programa.",
      "Mantener assets/ para imágenes, tablas, logos y recursos compartidos con nombres normalizados, portables y sin espacios.",
      "Separar documentos raíz institucionales de entregables específicos de materia.",
      "Cada carpeta de materia debe incluir COMPILACION.md con comando exacto, .bib esperado y contrato mínimo de compilación.",
      "Usar estructura mínima por materia: objetivo, competencias, desarrollo o instrucciones, evidencias, evaluación y referencias.",
      "Evitar duplicación de plantillas locales; reutilizar base/ mediante \\input y rutas resueltas por TEXINPUTS/BIBINPUTS.",
      "Nombrar carpetas y archivos derivados en minúsculas, con guiones y sin espacios salvo artefactos heredados ya estables."
    ],
    "style_rules": [
      "Redactar con párrafos breves, secciones jerárquicas y objetivos evaluables.",
      "Separar contenido base, instrucciones, evidencias, entregables, criterios de evaluación y referencias.",
      "Mantener terminología consistente entre reporte, actividad y presentación.",
      "Usar listas, tablas y rúbricas solo cuando mejoren claridad didáctica o evaluación.",
      "Evitar relleno editorial, afirmaciones vagas, duplicación de apartados y contenido disciplinar no investigado.",
      "Usar [INV] para vacíos curriculares, normativos, bibliográficos o institucionales críticos."
    ],
    "quality_gates": [
      "El archivo objetivo debe compilar sin errores con scripts/latexmk-build.ps1 recibiendo solo el .tex.",
      "El PDF final debe generarse en la carpeta del .tex objetivo conforme al flujo AulaTeX.",
      "No usar rutas duras fuera del esquema TEXINPUTS/BIBINPUTS definido por el repositorio.",
      "Cada entregable debe incluir objetivo, desarrollo o instrucciones, evidencias, evaluación y referencias.",
      "Toda afirmación académica relevante debe tener cita verificable o marcador [INV].",
      "No registrar bibliografía inventada ni claves BibTeX sin fuente rastreable.",
      "No renombrar ni romper archivos canónicos o rutas existentes durante refuerzos posteriores."
    ],
    "latex_rules": [
      "Usar plantilla homologada desde base/Template-Reporte, base/Templates-Informe, base/Template-Presentacion o equivalente disponible.",
      "El archivo raíz institucional sugerido debe resolver \\input{template} mediante TEXINPUTS, no por rutas absolutas.",
      "Centralizar bibliografía institucional en bibliografia-iiiepe.bib; usar .bib local solo si la materia lo requiere.",
      "Declarar portada, índice, secciones, anexos y bibliografía con comandos compatibles con el motor base del repositorio.",
      "Nombrar etiquetas con prefijos estables: sec:, fig:, tab:, eq: y anexo:.",
      "Usar comentarios seguros para compilación: % TODO y % [INV].",
      "Evitar paquetes redundantes, conflictivos o no necesarios para el documento objetivo.",
      "No insertar imágenes, logos o gráficas si no existen en assets/ o no cuentan con fuente validada."
    ],
    "bibliography_rules": [
      "Registrar únicamente fuentes verificables, consultables y trazables.",
      "Usar claves BibTeX legibles y homogéneas, preferentemente con patrón autorAnioTema.",
      "Separar fuentes institucionales, normativas, teóricas y didácticas cuando aplique.",
      "Validar bibliografía oficial de cada asignatura antes de redactar contenido definitivo.",
      "Mantener homogeneidad de estilo bibliográfico en todos los documentos IIIEPE.",
      "Registrar pendientes bibliográficos como marcadores [INV], no como entradas .bib ficticias."
    ],
    "research_markers": [
      "[INV] Confirmar nombre oficial, siglas, datos de contacto y metadatos institucionales de IIIEPE.",
      "[INV] Validar oferta académica vigente y nomenclatura oficial de programas o carreras.",
      "[INV] Recabar lineamientos institucionales de formato, evaluación, portada y citación si existen.",
      "[INV] Identificar competencias institucionales transversales para integrarlas en plantillas.",
      "[INV] Localizar programas analíticos, sílabos o mapas curriculares por materia.",
      "[INV] Validar bibliografía mínima obligatoria antes de redacción final.",
      "[INV] Levantar inventario real de archivos .tex, .bib, assets y COMPILACION.md existentes en IIIEPE."
    ]
  },
  "plan_editorial": {
    "objetivo_editorial": [
      "Reforzar una base editorial IIIEPE uniforme, escalable y compatible con el flujo AulaTeX.",
      "Dejar preparada una maqueta institucional para que el Agente investigue, redacte, evalúe y compile después.",
      "Reducir variabilidad entre materias mediante reglas comunes de estructura, bibliografía, evaluación y compilación.",
      "Preservar contratos existentes sin regresión de nombres, rutas ni artefactos canónicos."
    ],
    "alcance": [
      "Actualizar memoria fundacional, plan editorial y maqueta inicial sin redactar actividades completas.",
      "Cubrir entradas canónicas institucionales: reporte, actividad, presentación y bibliografía.",
      "Orientar réplica por programa, carrera, materia y entregable.",
      "Incluir marcadores [INV] para vacíos documentales, curriculares, normativos y bibliográficos.",
      "No ejecutar investigación profunda ni validar contenido externo en esta fase."
    ],
    "estructura_base": [
      "IIIEPE/reporte-iiiepe.tex como entrada institucional para reportes generales.",
      "IIIEPE/presentacion-iiiepe.tex como entrada institucional para presentaciones.",
      "IIIEPE/bibliografia-iiiepe.bib como bibliografía central verificable.",
      "IIIEPE/assets/ para recursos institucionales normalizados.",
      "IIIEPE/<programa-o-carrera>/<materia>/ para contenidos específicos.",
      "Cada materia debe contener reporte-<materia>.tex, actividad-<materia>.tex si aplica, bibliografía local opcional y COMPILACION.md.",
      "Las plantillas compartidas deben invocarse desde base/ mediante rutas resueltas por TEXINPUTS."
    ],
    "criterios_evaluacion": [
      "Consistencia formal entre documentos institucionales y documentos de materia.",
      "Compilación reproducible con scripts oficiales de AulaTeX.",
      "Presencia explícita de objetivos, competencias, resultados, evidencias, rúbrica y referencias.",
      "Claridad de instrucciones para el estudiante y criterios de revisión para el docente.",
      "Trazabilidad bibliográfica sin referencias inventadas.",
      "Separación efectiva entre maqueta editorial, contenido investigado y redacción final.",
      "Compatibilidad con crecimiento futuro sin romper archivos existentes."
    ],
    "bibliografia_requerida": [
      "Lineamientos oficiales IIIEPE verificables, si existen.",
      "Programas analíticos, sílabos o mapas curriculares por materia.",
      "Bibliografía oficial indicada por cada asignatura.",
      "Fuentes académicas primarias o secundarias validadas por docente o programa.",
      "Normas de citación adoptadas por el proyecto o por la institución.",
      "Documentos internos de evaluación solo si son accesibles, citables y autorizados."
    ],
    "riesgos": [
      "Heterogeneidad de formatos heredados entre materias.",
      "Ausencia o baja disponibilidad de lineamientos institucionales explícitos.",
      "Uso de fuentes no verificables, incompletas o no citables.",
      "Duplicación de plantillas locales que dificulte mantenimiento.",
      "Rutas duras que rompan compilación fuera del entorno del autor.",
      "Confusión entre placeholders editoriales y contenido académico definitivo.",
      "Cambios de nomenclatura institucional no validados."
    ],
    "siguiente_fase_agente": [
      "Inventariar estructura real de IIIEPE: carpetas, .tex, .bib, assets y COMPILACION.md.",
      "Comparar la estructura existente contra el contrato canónico y proponer migración mínima sin regresión.",
      "Investigar datos institucionales oficiales y oferta académica vigente.",
      "Normalizar esqueletos por materia con marcadores [INV] y rúbricas base.",
      "Validar compilación de reporte-iiiepe.tex y presentacion-iiiepe.tex.",
      "Verificar que cada materia tenga comando de compilación documentado.",
      "Completar bibliografía únicamente con fuentes verificadas."
    ]
  },
  "maqueta_inicial": {
    "titulo": "IIIEPE | Maqueta editorial institucional base",
    "objetivo": [
      "Estandarizar la producción académica en LaTeX para IIIEPE con estructura, plantillas y criterios comunes.",
      "Servir como base reusable para reportes, actividades y presentaciones por materia.",
      "Dejar preparado el documento para investigación, redacción, evaluación y compilación posterior por el Agente.",
      "Mantener trazabilidad institucional y bibliográfica sin asumir datos no verificados."
    ],
    "competencias": [
      "Organiza documentos académicos con estructura formal, verificable y reutilizable.",
      "Integra objetivos, competencias, evidencias y criterios de evaluación observables.",
      "Gestiona citas y referencias con buenas prácticas bibliográficas.",
      "Distingue contenido validado de información pendiente mediante marcadores [INV].",
      "Entrega documentos reproducibles mediante el flujo automatizado AulaTeX."
    ],
    "resultados_esperados": [
      "Raíz IIIEPE con entradas canónicas institucionales listas para completar.",
      "Estructura replicable por programa, carrera y materia.",
      "Documento maqueta listo para ser completado sin modificar el contrato de compilación.",
      "Marcadores [INV] explícitos para orientar investigación posterior.",
      "Bibliografía preparada para recibir únicamente fuentes verificables.",
      "Matriz mínima de evaluación reutilizable por asignatura."
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
      "Lineamientos institucionales IIIEPE verificados.",
      "Documentos curriculares vigentes.",
      "Bibliografía oficial por asignatura.",
      "Norma de citación institucional o del proyecto.",
      "Fuentes académicas validadas por docente o programa.",
      "Recursos didácticos autorizados cuando aplique."
    ],
    "marcadores_investigacion": [
      "[INV] Datos institucionales oficiales IIIEPE para portada y metadatos.",
      "[INV] Perfil institucional, misión educativa o equivalente verificable.",
      "[INV] Programas, carreras y materias activas.",
      "[INV] Mapa curricular o programa analítico correspondiente.",
      "[INV] Competencias transversales institucionales.",
      "[INV] Criterios de evaluación institucionales o de asignatura.",
      "[INV] Bibliografía mínima obligatoria por materia.",
      "[INV] Lineamientos de formato, portada y citación."
    ]
  },
  "tex_editorial": {
    "plantilla": [
      "Archivo sugerido: IIIEPE/reporte-iiiepe.tex.",
      "Debe iniciar con \\input{template} o mecanismo homologado por la plantilla base disponible.",
      "Variables mínimas: institucion, programa, carrera, materia, docente, estudiante, periodo y tipoDocumento.",
      "Secciones placeholder: portada, resumen, objetivo, competencias, desarrollo, evidencias, evaluación, referencias y anexos.",
      "Incluir comentarios seguros para compilación: % TODO y % [INV].",
      "Usar \\bibliography{bibliografia-iiiepe} cuando el template y el flujo bibliográfico lo permitan.",
      "No insertar referencias bibliográficas no verificadas en el .bib.",
      "Agregar checklist comentado: compila, citas resueltas, rutas relativas, assets existentes y PDF final generado."
    ],
    "actividad": [
      "Archivo sugerido por materia: actividad-<materia>.tex.",
      "Estructura mínima: propósito, contexto, instrucciones, evidencia, formato de entrega, rúbrica y referencias.",
      "Mantener la actividad como maqueta; no desarrollar contenido disciplinar completo en esta fase.",
      "Agregar marcadores [INV] para fuentes, criterios específicos y datos del programa.",
      "Usar rúbrica breve con niveles o puntajes editables.",
      "Incluir sección de retroalimentación docente para uso posterior.",
      "Evitar dependencias visuales externas si no existen en assets/."
    ],
    "reporte": [
      "Archivo sugerido por materia: reporte-<materia>.tex.",
      "Bloques mínimos: introducción, objetivo, desarrollo por unidades, evidencias, conclusiones y referencias.",
      "Integrar tablas y figuras desde assets/ con etiquetas estables.",
      "Insertar placeholders de cita como [INV: fuente requerida] hasta validar bibliografía.",
      "Agregar tabla breve de control editorial: versión, fecha, responsable y estado.",
      "Incluir checklist previo a compilación y verificación de citas.",
      "Conservar compatibilidad con scripts/latexmk-build.ps1 pasando solo el .tex objetivo."
    ],
    "presentacion": [
      "Archivo sugerido: IIIEPE/presentacion-iiiepe.tex o presentacion-<materia>.tex según alcance.",
      "Secuencia mínima: portada, agenda, objetivos, desarrollo por bloques, actividad o discusión, cierre, referencias y preguntas.",
      "Regla visual: una idea central por diapositiva, hasta tres apoyos breves y recurso visual opcional.",
      "Mantener estilo institucional sobrio, legible y consistente con el reporte.",
      "No insertar imágenes, logos o gráficas si no están disponibles en assets/ o no tienen fuente validada.",
      "Dejar marcadores [INV] para datos institucionales, citas y recursos visuales pendientes."
    ]
  }
}