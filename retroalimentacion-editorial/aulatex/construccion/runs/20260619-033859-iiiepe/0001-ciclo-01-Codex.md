{
  "memoria_fundacional": {
    "summary": [
      "Nodo institucional IIIEPE reforzado como raíz editorial reusable alineada al estándar interinstitucional AulaTeX.",
      "Se prioriza consistencia de entradas canónicas (reporte, actividad, presentación, bibliografía) y compilación por script.",
      "La memoria queda orientada a crecimiento por carreras/materias sin romper contratos existentes."
    ],
    "identity_rules": [
      "Mantener prefijo institucional en archivos raíz: reporte-iiiepe.tex, presentacion-iiiepe.tex, bibliografia-iiiepe.bib.",
      "Usar español académico claro, tono formal y enfoque didáctico aplicado.",
      "Conservar trazabilidad institucional en portada, metadatos y rutas internas."
    ],
    "structure_rules": [
      "Definir raíz IIIEPE con subcarpetas por programa/carrera y materias dentro de cada programa.",
      "Incluir carpeta assets institucional (imagenes, tablas, logos) con nombres normalizados.",
      "Cada materia debe contener COMPILACION.md con comando exacto, .bib esperado y contrato mínimo.",
      "Evitar duplicación de plantillas: referenciar siempre base/ mediante \\input y rutas compatibles con TEXINPUTS."
    ],
    "style_rules": [
      "Párrafos breves, secciones jerárquicas y objetivos evaluables por unidad.",
      "Separar contenido base, instrucciones y entregables para facilitar reutilización.",
      "Incluir criterios de evaluación explícitos en toda actividad o reporte."
    ],
    "quality_gates": [
      "Compila sin errores con scripts/latexmk-build.ps1 pasando solo el .tex objetivo.",
      "No hay rutas duras a plantillas fuera del esquema TEXINPUTS/BIBINPUTS.",
      "Toda afirmación académica relevante tiene cita o marcador de investigación pendiente.",
      "Estructura mínima presente: objetivo, desarrollo, evidencias, evaluación, referencias."
    ],
    "latex_rules": [
      "Usar plantilla institucional derivada de base/Template-Reporte o equivalente homologado.",
      "Centralizar bibliografía en bibliografia-iiiepe.bib y bibs locales solo cuando el curso lo requiera.",
      "Declarar portada, índice y secciones con comandos estándar para compatibilidad de compilación.",
      "Evitar paquetes redundantes o conflictivos con el motor base del repositorio."
    ],
    "bibliography_rules": [
      "No inventar referencias; registrar solo fuentes verificables y trazables.",
      "Preferir estilo homogéneo institucional y claves BibTeX legibles.",
      "Separar fuentes normativas, teóricas y recursos didácticos cuando aplique."
    ],
    "research_markers": [
      "Confirmar oferta académica vigente de IIIEPE y nomenclatura oficial de programas.",
      "Recabar lineamientos internos de evaluación y formato si existen.",
      "Validar bibliografía base por asignatura antes de redacción final.",
      "Identificar competencias institucionales transversales para insertar en plantillas."
    ]
  },
  "plan_editorial": {
    "objetivo_editorial": [
      "Consolidar una base editorial IIIEPE uniforme, escalable y compatible con el flujo AulaTeX."
    ],
    "alcance": [
      "Reforzar memoria, plan y maqueta institucional sin redactar contenidos completos de asignaturas.",
      "Preparar artefactos reutilizables para reporte, actividad y presentación."
    ],
    "estructura_base": [
      "Raíz IIIEPE con archivos canónicos institucionales y bibliografía central.",
      "Subestructura por carrera/programa > materia > entregables.",
      "Carpeta assets y referencias a plantillas compartidas en base/."
    ],
    "criterios_evaluacion": [
      "Homogeneidad formal entre materias y documentos institucionales.",
      "Compilación reproducible con scripts oficiales.",
      "Cobertura de objetivos, competencias, evidencias y rúbrica básica.",
      "Trazabilidad de fuentes y ausencia de bibliografía no verificable."
    ],
    "bibliografia_requerida": [
      "Lineamientos oficiales IIIEPE (si disponibles).",
      "Programas analíticos o sílabos por materia.",
      "Fuentes académicas primarias/secundarias validadas para cada curso."
    ],
    "riesgos": [
      "Heterogeneidad de formatos heredados entre materias.",
      "Falta de lineamientos institucionales explícitos documentados.",
      "Dependencia de fuentes no normalizadas o no citables."
    ],
    "siguiente_fase_agente": [
      "Levantar inventario real de carpetas y .tex existentes en IIIEPE.",
      "Mapear brechas contra estructura canónica y proponer migración mínima sin regresión.",
      "Generar esqueletos por materia con marcadores de investigación y rúbricas base.",
      "Validar compilación de al menos un reporte y una presentación institucional."
    ]
  },
  "maqueta_inicial": {
    "titulo": "IIIEPE | Maqueta editorial institucional reutilizable",
    "objetivo": [
      "Estandarizar la producción académica en LaTeX para IIIEPE con plantillas y criterios comunes."
    ],
    "competencias": [
      "Organiza contenidos académicos con estructura formal y verificable.",
      "Integra citas y referencias con buenas prácticas bibliográficas.",
      "Entrega documentos reproducibles en flujo automatizado de compilación."
    ],
    "resultados_esperados": [
      "Repositorio IIIEPE con entradas canónicas y estructura por programas.",
      "Documentos base listos para investigación/redacción posterior.",
      "Matriz mínima de evaluación reutilizable por asignatura."
    ],
    "estructura_sugerida": [
      "00-portada-y-datos-institucionales",
      "01-proposito-y-alcance",
      "02-competencias-y-resultados",
      "03-contenido-base-por-unidades",
      "04-actividades-y-evidencias",
      "05-criterios-de-evaluacion",
      "06-referencias-y-anexos",
      "07-compilacion-y-control-de-version"
    ],
    "criterios_evaluacion": [
      "Pertinencia académica del contenido respecto al programa.",
      "Claridad de instrucciones y entregables.",
      "Calidad formal LaTeX y consistencia visual.",
      "Uso correcto de citas y bibliografía."
    ],
    "bibliografia_requerida": [
      "Bibliografía oficial de cada asignatura.",
      "Normas de citación adoptadas por el proyecto.",
      "Documentos curriculares institucionales vigentes."
    ],
    "marcadores_investigacion": [
      "[INV] Perfil institucional y misión educativa IIIEPE.",
      "[INV] Programas/carreras activos y mapa curricular.",
      "[INV] Criterios de evaluación institucionales.",
      "[INV] Bibliografía mínima obligatoria por materia."
    ]
  },
  "tex_editorial": {
    "plantilla": [
      "Archivo raíz sugerido: IIIEPE/reporte-iiiepe.tex con secciones placeholder y \\input a plantilla base.",
      "Incluir variables editables: institución, programa, materia, docente, periodo, estudiante.",
      "Agregar bloques TODO: objetivo, competencias, unidades, evidencias, rúbrica, referencias."
    ],
    "actividad": [
      "Plantilla de actividad corta con: propósito, instrucciones, evidencia, formato de entrega, rúbrica.",
      "Marcadores de investigación para fuentes y criterios específicos de la materia.",
      "Sección de retroalimentación docente preparada para uso iterativo."
    ],
    "reporte": [
      "Plantilla de reporte académico con: introducción, desarrollo por unidades, conclusiones y referencias.",
      "Subsecciones para integración de tablas/figuras desde assets/ con etiquetas estables.",
      "Checklist previo a compilación y verificación de citas."
    ],
    "presentacion": [
      "Plantilla de presentación institucional homologada con portada, agenda, desarrollo y cierre.",
      "Máximo contenido por diapositiva definido como regla editorial breve y visual.",
      "Diapositiva final con referencias y preguntas."
    ]
  }
}