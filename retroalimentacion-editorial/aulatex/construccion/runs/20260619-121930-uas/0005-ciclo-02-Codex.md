{
  "memoria_fundacional": {
    "summary": [
      "Se refuerza UAS como nodo institucional estable, compilable y reutilizable dentro del marco interinstitucional.",
      "Se conserva el flujo editorial canónico: memoria, investigación, extracción, generación/agente y compilación.",
      "La raíz UAS debe servir como punto de entrada para reporte, actividad y presentación con bibliografía institucional trazable.",
      "Se depuran salidas no estructuradas previas y se prioriza contrato editorial verificable."
    ],
    "identity_rules": [
      "Usar identificador institucional único: UAS.",
      "Mantener ruta canónica fija: UAS/.",
      "Nombrar artefactos base como reporte-uas.tex, presentacion-uas.tex y bibliografia-uas.bib.",
      "Tomar https://www.uas.edu.mx/ como referencia institucional primaria para validación de nombres oficiales.",
      "Evitar variantes de nombre de institución en archivos y metadatos."
    ],
    "structure_rules": [
      "Conservar en UAS/ los puntos de entrada institucionales y carpeta assets/.",
      "Organizar crecimiento en UAS/<carrera>/<materia>/ con slug consistente.",
      "Incluir COMPILACION.md institucional y permitir COMPILACION.md por materia cuando se requiera.",
      "Referenciar plantillas compartidas de base/ por contrato de compilación, sin duplicarlas localmente.",
      "Separar plantilla base de contenido académico en desarrollo."
    ],
    "style_rules": [
      "Redacción académica formal en español, clara y no promocional.",
      "Bullets operativos, breves y sin redundancias.",
      "Alinear terminología entre objetivo, competencias, evidencias y evaluación.",
      "Marcar explícitamente vacíos de investigación con pendientes."
    ],
    "quality_gates": [
      "Compilación limpia con scripts/latexmk-build.ps1 pasando solo el .tex objetivo.",
      "Sin rutas rotas en \\input, assets o bibliografía.",
      "Toda salida .tex declara .bib existente y coherente con BIBINPUTS.",
      "No incluir referencias inventadas ni datos institucionales no verificados.",
      "Checklist editorial completado antes de pasar a fase de agente."
    ],
    "latex_rules": [
      "Mantener puntos de entrada por tipo: reporte, actividad y presentación.",
      "Resolver plantillas vía TEXINPUTS definido en .latexmkrc.",
      "Resolver bibliografía vía BIBINPUTS, evitando rutas absolutas.",
      "Usar preámbulo mínimo y delegar formato visual a plantillas base.",
      "Incluir marcadores de investigación en comentarios cuando falte información."
    ],
    "bibliography_rules": [
      "Usar bibliografia-uas.bib como contenedor maestro inicial.",
      "Permitir .bib por materia si mejora mantenibilidad y trazabilidad.",
      "Diferenciar fuentes oficiales UAS, normativa y literatura disciplinar.",
      "Incorporar únicamente fuentes verificables con metadatos mínimos completos."
    ],
    "research_markers": [
      "Verificar denominaciones oficiales de unidades académicas en https://www.uas.edu.mx/.",
      "Confirmar oferta académica real antes de crear o renombrar carpetas de carrera.",
      "Localizar lineamientos públicos de evaluación, formato o reglamentación aplicable.",
      "Priorizar recuperación de planes/programas de estudio para poblar materias."
    ]
  },
  "plan_editorial": {
    "objetivo_editorial": [
      "Reforzar UAS con una memoria editorial deduplicada y lista para ejecución por agente.",
      "Homogeneizar estructura institucional con el estándar interinstitucional vigente.",
      "Dejar preparada una maqueta .tex base reutilizable para escalamiento por carrera y materia."
    ],
    "alcance": [
      "Ajuste de reglas editoriales, de estructura y de compilación del nodo UAS.",
      "Definición de plantilla operativa para reporte, actividad y presentación.",
      "Sin investigación profunda ni redacción completa de productos académicos."
    ],
    "estructura_base": [
      "UAS/reporte-uas.tex",
      "UAS/presentacion-uas.tex",
      "UAS/bibliografia-uas.bib",
      "UAS/assets/",
      "UAS/COMPILACION.md",
      "UAS/<carrera>/",
      "UAS/<carrera>/<materia>/",
      "UAS/<carrera>/<materia>/actividad-<slug>.tex",
      "UAS/<carrera>/<materia>/reporte-<slug>.tex"
    ],
    "criterios_evaluacion": [
      "Compatibilidad total con flujo editorial AulaTeX y contrato de compilación.",
      "Consistencia de nomenclatura y ausencia de duplicados regresivos.",
      "Preparación efectiva para que el agente investigue y complete contenido.",
      "Claridad en separación de plantilla, contenido y pendientes de investigación."
    ],
    "bibliografia_requerida": [
      "Fuente institucional primaria: https://www.uas.edu.mx/.",
      "Documentos oficiales UAS por validar en fase de investigación.",
      "Bibliografía disciplinar incorporada posteriormente por materia y evidencia."
    ],
    "riesgos": [
      "Crear estructura de carreras no alineada con denominaciones oficiales.",
      "Deriva de formato entre materias por falta de plantilla compartida efectiva.",
      "Fallas de compilación por desalineación entre .tex, .bib y .latexmkrc.",
      "Contaminación de memoria con texto no estructurado o no verificable."
    ],
    "siguiente_fase_agente": [
      "Auditar estructura real en disco de UAS y normalizar slugs.",
      "Mapear carreras y materias desde fuente oficial UAS.",
      "Generar esqueletos por materia con objetivos, evidencias y rúbrica mínima.",
      "Poblar bibliografia-uas.bib con entradas verificadas y citables.",
      "Validar compilación de muestras institucionales y por materia."
    ]
  },
  "maqueta_inicial": {
    "titulo": "Nodo institucional UAS - maqueta editorial base",
    "objetivo": [
      "Disponer de una base institucional compilable para producción académica UAS.",
      "Estandarizar estructura mínima de reporte, actividad y presentación.",
      "Facilitar escalamiento por carrera/materia con trazabilidad editorial."
    ],
    "competencias": [
      "Gestión de documentos académicos LaTeX bajo contrato institucional.",
      "Aplicación de criterios de calidad editorial y citación verificable.",
      "Organización modular de contenidos por carrera y materia."
    ],
    "resultados_esperados": [
      "Entradas .tex institucionales listas para completar por agente.",
      "Estructura de carpetas estable y reutilizable.",
      "Bibliografía base institucional preparada para crecimiento controlado."
    ],
    "estructura_sugerida": [
      "Portada y metadatos institucionales/materia.",
      "Objetivo, competencias y alcance de la entrega.",
      "Desarrollo seccionado con evidencias y citas.",
      "Criterios de evaluación o rúbrica breve.",
      "Cierre, referencias y anexos opcionales.",
      "Bloque de pendientes de investigación en comentarios."
    ],
    "criterios_evaluacion": [
      "Coherencia entre propósito, desarrollo y evaluación.",
      "Cumplimiento de formato y compilación sin errores.",
      "Uso correcto de fuentes verificables y citas trazables.",
      "Consistencia terminológica en toda la entrega."
    ],
    "bibliografia_requerida": [
      "bibliografia-uas.bib como base institucional.",
      "Fuentes oficiales UAS y normativa académica pública.",
      "Fuentes disciplinares validadas en fase de investigación."
    ],
    "marcadores_investigacion": [
      "[pendiente] catálogo oficial de carreras UAS vigente",
      "[pendiente] programas analíticos por materia prioritaria",
      "[pendiente] lineamientos de evaluación institucionales o por unidad académica",
      "[pendiente] corpus bibliográfico troncal por disciplina"
    ]
  },
  "tex_editorial": {
    "plantilla": [
      "% UAS/reporte-uas.tex",
      "% \\input{template} desde base/ por TEXINPUTS",
      "% Metadatos: institucion, carrera, materia, periodo, autor",
      "% Secciones mínimas: objetivo, competencias, desarrollo, evaluacion, cierre",
      "% \\bibliography{bibliografia-uas}"
    ],
    "actividad": [
      "% UAS/<carrera>/<materia>/actividad-<slug>.tex",
      "% Secciones: contexto, instrucciones, entregables, criterios, referencias",
      "% Incluir bloque % [pendiente-investigacion] cuando aplique",
      "% Mantener actividad como plantilla incompleta, no contenido final"
    ],
    "reporte": [
      "% UAS/<carrera>/<materia>/reporte-<slug>.tex",
      "% Secciones: introduccion, objetivos, marco, desarrollo, conclusiones, referencias",
      "% Reusar estructura institucional y ajustar a materia",
      "% Citar solo entradas existentes en .bib verificado"
    ],
    "presentacion": [
      "% UAS/presentacion-uas.tex o UAS/<carrera>/<materia>/presentacion-<slug>.tex",
      "% Estructura: portada, objetivo, hallazgos clave, cierre, referencias",
      "% Priorizar sintesis visual y consistencia con reporte asociado",
      "% Sin duplicar desarrollo extenso del reporte"
    ]
  }
}