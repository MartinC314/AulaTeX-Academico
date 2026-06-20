{
  "memoria_fundacional": {
    "summary": [
      "Nodo institucional UAS reforzado como raíz editorial reutilizable dentro de AulaTeX-Academico.",
      "Se mantiene compatibilidad con flujo canónico: memoria, investigación, extracción, generación/agente y compilación.",
      "La salida institucional debe habilitar reportes, actividades y presentaciones con bibliografía centralizada por institución."
    ],
    "identity_rules": [
      "Usar nombre institucional corto: UAS.",
      "Mantener ruta objetivo estable: UAS/.",
      "Alinear nomenclatura de artefactos con patrón institucional: reporte-uas.tex, presentacion-uas.tex, bibliografia-uas.bib.",
      "Tomar https://www.uas.edu.mx/ como fuente primaria de validación institucional (sin copiar contenido no verificado)."
    ],
    "structure_rules": [
      "Conservar raíz con archivos canónicos institucionales en UAS/.",
      "Crear/normalizar carpeta assets/ para recursos gráficos y tablas reutilizables.",
      "Organizar contenido académico por carrera/programa dentro de subcarpetas dedicadas.",
      "Incluir referencias explícitas a plantillas compartidas en base/ mediante \\input o contrato de compilación.",
      "Agregar COMPILACION.md por nivel institucional o por materia cuando aplique."
    ],
    "style_rules": [
      "Redacción formal académica en español claro, sin tono promocional.",
      "Bullets breves y accionables en guías editoriales.",
      "Consistencia terminológica entre portada, objetivos, competencias y evaluación.",
      "Evitar afirmaciones institucionales no verificadas durante fase de memoria."
    ],
    "quality_gates": [
      "Compila sin errores con scripts/latexmk-build.ps1 pasando solo el .tex objetivo.",
      "Cada .tex declara bibliografía institucional o de materia existente.",
      "No hay rutas rotas de assets ni includes de plantillas.",
      "Se distingue claramente contenido base (plantilla) de contenido investigado (por completar).",
      "No se inventan referencias bibliográficas."
    ],
    "latex_rules": [
      "Usar punto de entrada .tex por tipo de entrega: reporte, actividad, presentacion.",
      "Resolver plantillas mediante TEXINPUTS configurado en .latexmkrc; no hardcodear rutas absolutas.",
      "Resolver .bib mediante BIBINPUTS y nombre consistente por institución/materia.",
      "Mantener preámbulo mínimo estable y delegar estilo visual a plantillas de base/."
    ],
    "bibliography_rules": [
      "Priorizar archivo institucional bibliografia-uas.bib como contenedor maestro inicial.",
      "Permitir .bib por materia cuando el volumen crezca, manteniendo trazabilidad.",
      "Registrar solo fuentes verificables y citables; sin placeholders falsos.",
      "Separar normativa institucional, bibliografía académica y fuentes web oficiales."
    ],
    "research_markers": [
      "Validar oferta académica y denominaciones oficiales en https://www.uas.edu.mx/.",
      "Confirmar estructura de carreras/facultades para crear subcarpetas reales.",
      "Recuperar lineamientos de evaluación o formato institucional, si existen públicamente.",
      "Identificar documentos base (planes, programas, reglamentos) para futuras actividades."
    ]
  },
  "plan_editorial": {
    "objetivo_editorial": [
      "Consolidar UAS como nodo institucional homogéneo con el estándar interinstitucional de AulaTeX.",
      "Dejar infraestructura editorial lista para que el Agente investigue y complete contenidos por materia."
    ],
    "alcance": [
      "Reforzamiento de memoria, estructura y convenciones de archivos.",
      "Definición de maqueta inicial reusable para actividades y reportes.",
      "Sin redacción completa de actividades ni investigación profunda en esta fase."
    ],
    "estructura_base": [
      "UAS/reporte-uas.tex",
      "UAS/presentacion-uas.tex",
      "UAS/bibliografia-uas.bib",
      "UAS/assets/",
      "UAS/{carrera-o-programa}/",
      "UAS/{carrera-o-programa}/{materia}/",
      "UAS/COMPILACION.md"
    ],
    "criterios_evaluacion": [
      "Coherencia con contrato canónico interinstitucional.",
      "Reutilización de plantillas base sin duplicación innecesaria.",
      "Nomenclatura uniforme y deduplicada.",
      "Preparación efectiva para fase de investigación del Agente."
    ],
    "bibliografia_requerida": [
      "Sitio oficial UAS: https://www.uas.edu.mx/ (verificación institucional).",
      "Lineamientos/planes oficiales UAS por confirmar en fase de investigación.",
      "Fuentes disciplinares se incorporarán en la siguiente fase, no en memoria."
    ],
    "riesgos": [
      "Ambigüedad de nombres de carreras si no se valida fuente oficial.",
      "Deriva de estilo entre materias sin guía institucional mínima.",
      "Errores de compilación por rutas o bibliografía no alineadas a .latexmkrc."
    ],
    "siguiente_fase_agente": [
      "Inventariar estructura real de UAS en disco y normalizar nombres.",
      "Investigar oferta académica oficial y mapear carpetas por carrera.",
      "Generar esqueletos .tex por materia prioritaria con objetivos y evaluación.",
      "Construir bibliografia-uas.bib inicial con fuentes verificadas."
    ]
  },
  "maqueta_inicial": {
    "titulo": "UAS",
    "objetivo": [
      "Establecer una base institucional compilable y reutilizable para producción académica en LaTeX.",
      "Estandarizar entradas de reporte, actividad y presentación para programas UAS."
    ],
    "competencias": [
      "Gestión editorial académica con estructura modular.",
      "Uso de plantillas LaTeX institucionales con control bibliográfico.",
      "Trazabilidad entre investigación, redacción y compilación."
    ],
    "resultados_esperados": [
      "Nodo UAS con artefactos canónicos listos para completar.",
      "Rutas y convenciones estables para crecimiento por carrera/materia.",
      "Checklist mínimo de calidad para compilación y citación."
    ],
    "estructura_sugerida": [
      "Portada institucional y metadatos de asignatura.",
      "Objetivo y competencias de la actividad/reporte.",
      "Desarrollo por secciones con evidencias y citas.",
      "Criterios de evaluación/rúbrica resumida.",
      "Conclusiones, referencias y anexos (si aplica)."
    ],
    "criterios_evaluacion": [
      "Pertinencia académica respecto a programa/materia validada.",
      "Claridad argumentativa y coherencia interna.",
      "Uso correcto de citas y referencias verificables.",
      "Compilación limpia y formato consistente."
    ],
    "bibliografia_requerida": [
      "Archivo base: bibliografia-uas.bib.",
      "Fuentes oficiales UAS y documentos académicos verificables.",
      "Norma de citación definida por plantilla o lineamiento de curso."
    ],
    "marcadores_investigacion": [
      "[pendiente: catálogo oficial de carreras UAS]",
      "[pendiente: lineamientos de evaluación por unidad académica]",
      "[pendiente: programa analítico de materia objetivo]",
      "[pendiente: fuentes troncales por disciplina]"
    ]
  },
  "tex_editorial": {
    "plantilla": [
      "% Archivo: UAS/reporte-uas.tex",
      "% Estructura mínima: \\input{template} + metadatos + secciones base + \\bibliography{bibliografia-uas}",
      "% Mantener compatibilidad con TEXINPUTS/BIBINPUTS del repositorio."
    ],
    "actividad": [
      "% Archivo sugerido por materia: UAS/<carrera>/<materia>/actividad-<slug>.tex",
      "% Secciones: contexto, instrucciones, desarrollo, evidencia, criterios de evaluación, referencias.",
      "% Incluir marcador de investigación pendiente en comentarios."
    ],
    "reporte": [
      "% Archivo sugerido por materia: UAS/<carrera>/<materia>/reporte-<slug>.tex",
      "% Secciones: introducción, objetivos, marco conceptual, desarrollo, conclusiones, bibliografía.",
      "% Usar bibliografía institucional o específica de materia según volumen."
    ],
    "presentacion": [
      "% Archivo: UAS/presentacion-uas.tex o por materia.",
      "% Estructura: portada, objetivo, puntos clave, cierre, referencias.",
      "% Diseñar para síntesis visual; contenido extenso queda en reporte."
    ]
  }
}