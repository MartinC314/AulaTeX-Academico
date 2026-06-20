{
  "memoria_fundacional": {
    "summary": [
      "IIIEPE se refuerza como raíz editorial institucional reusable y compatible con el estándar interinstitucional AulaTeX.",
      "Se consolida un contrato mínimo estable para reporte, actividad, presentación y bibliografía institucional.",
      "La memoria prioriza escalabilidad por programa/carrera y materia, sin regresión en rutas, nombres ni compilación."
    ],
    "identity_rules": [
      "Mantener archivos canónicos: reporte-iiiepe.tex, presentacion-iiiepe.tex y bibliografia-iiiepe.bib.",
      "Usar español académico formal, claro y orientado a evidencias.",
      "Incluir metadatos trazables: institución, programa, materia, docente, periodo y tipo de documento.",
      "No asumir datos institucionales no verificados; marcar faltantes con [INV]."
    ],
    "structure_rules": [
      "Conservar raíz IIIEPE con subcarpetas por programa/carrera y luego por materia.",
      "Mantener assets/ para recursos compartidos con nombres normalizados y portables.",
      "Exigir COMPILACION.md por materia con comando exacto, .bib esperado y contrato mínimo.",
      "Evitar duplicación de plantillas; reutilizar base/ mediante \\input y rutas compatibles con TEXINPUTS."
    ],
    "style_rules": [
      "Usar secciones jerárquicas y párrafos breves con objetivos evaluables.",
      "Separar contenido base, instrucciones, evidencias, evaluación y referencias.",
      "Mantener terminología consistente entre reporte, actividad y presentación.",
      "Eliminar redundancias editoriales y usar [INV] en vacíos críticos."
    ],
    "quality_gates": [
      "Compilar con scripts/latexmk-build.ps1 pasando solo el .tex objetivo.",
      "No usar rutas duras fuera de TEXINPUTS/BIBINPUTS.",
      "Incluir estructura mínima: objetivo, desarrollo/instrucciones, evidencias, evaluación y referencias.",
      "No registrar bibliografía inventada ni claves sin fuente rastreable."
    ],
    "latex_rules": [
      "Usar plantilla homologada desde base/Template-Reporte o base/Templates-Informe.",
      "Centralizar bibliografía institucional en bibliografia-iiiepe.bib; usar .bib local solo si aplica.",
      "Nombrar etiquetas con prefijos estables: sec:, fig:, tab:, eq:, anexo:.",
      "Permitir comentarios % TODO y % [INV] sin romper compilación."
    ],
    "bibliography_rules": [
      "Registrar únicamente fuentes verificables y consultables.",
      "Usar claves BibTeX legibles y homogéneas.",
      "Separar fuentes institucionales, normativas, teóricas y didácticas cuando aplique.",
      "Tratar pendientes como marcadores de investigación, no como entradas ficticias."
    ],
    "research_markers": [
      "[INV] Confirmar nombre oficial y metadatos institucionales IIIEPE.",
      "[INV] Validar oferta académica vigente y nomenclatura de programas/carreras.",
      "[INV] Verificar lineamientos institucionales de formato, evaluación y citación.",
      "[INV] Levantar inventario real de .tex, .bib, assets y COMPILACION.md en IIIEPE."
    ]
  },
  "plan_editorial": {
    "objetivo_editorial": [
      "Reforzar la base editorial IIIEPE con contrato estable, reusable y compilable.",
      "Dejar lista una maqueta institucional para investigación y redacción posterior por el Agente.",
      "Reducir variabilidad entre materias mediante reglas comunes de estructura y calidad."
    ],
    "alcance": [
      "Actualizar memoria fundacional, plan y maqueta inicial sin redactar actividades completas.",
      "Cubrir entradas canónicas institucionales y patrón de réplica por materia.",
      "Incluir marcadores [INV] para vacíos documentales y curriculares."
    ],
    "estructura_base": [
      "IIIEPE/reporte-iiiepe.tex",
      "IIIEPE/presentacion-iiiepe.tex",
      "IIIEPE/bibliografia-iiiepe.bib",
      "IIIEPE/assets/",
      "IIIEPE/<programa-o-carrera>/<materia>/ con reporte, actividad opcional, .bib opcional y COMPILACION.md"
    ],
    "criterios_evaluacion": [
      "Consistencia formal entre documentos institucionales y de materia.",
      "Compilación reproducible con scripts oficiales.",
      "Presencia explícita de objetivos, evidencias y rúbrica breve.",
      "Trazabilidad bibliográfica sin referencias inventadas."
    ],
    "bibliografia_requerida": [
      "Lineamientos oficiales IIIEPE verificables.",
      "Programas analíticos/sílabos/mapas curriculares por materia.",
      "Bibliografía oficial de asignatura y normas de citación vigentes.",
      "Documentos internos de evaluación, si existen y son citables."
    ],
    "riesgos": [
      "Heterogeneidad de formatos heredados.",
      "Ausencia o baja disponibilidad de lineamientos institucionales.",
      "Duplicación de plantillas locales y rutas duras.",
      "Confusión entre placeholders editoriales y contenido final."
    ],
    "siguiente_fase_agente": [
      "Inventariar estructura real IIIEPE y detectar brechas contra contrato canónico.",
      "Normalizar esqueletos por materia sin renombrar artefactos ya estables.",
      "Validar compilación de reporte-iiiepe.tex y presentacion-iiiepe.tex.",
      "Completar bibliografía únicamente con fuentes verificadas."
    ]
  },
  "maqueta_inicial": {
    "titulo": "IIIEPE | Maqueta editorial institucional base",
    "objetivo": [
      "Estandarizar la producción académica LaTeX de IIIEPE con estructura y reglas comunes.",
      "Servir como base reusable para reportes, actividades y presentaciones por materia."
    ],
    "competencias": [
      "Organiza documentos académicos con estructura verificable.",
      "Integra evidencias y criterios de evaluación observables.",
      "Aplica buenas prácticas de citación y compilación reproducible."
    ],
    "resultados_esperados": [
      "Entradas canónicas institucionales listas para completar.",
      "Estructura replicable por programa/carrera y materia.",
      "Marcadores [INV] explícitos para orientar investigación posterior."
    ],
    "estructura_sugerida": [
      "00-portada-y-metadatos",
      "01-proposito-y-alcance",
      "02-programa-materia-periodo",
      "03-competencias-y-resultados",
      "04-contenido-base-por-unidades",
      "05-actividades-evidencias-entregables",
      "06-criterios-de-evaluacion-rubrica",
      "07-recursos-assets",
      "08-referencias-y-anexos",
      "09-compilacion-y-checklist"
    ],
    "criterios_evaluacion": [
      "Pertinencia académica frente al programa validado.",
      "Claridad de instrucciones, entregables y evidencias.",
      "Consistencia formal con plantillas AulaTeX.",
      "Compilación limpia y bibliografía trazable."
    ],
    "bibliografia_requerida": [
      "Bibliografía oficial por asignatura.",
      "Documentos curriculares vigentes.",
      "Norma de citación institucional/proyecto.",
      "Fuentes académicas validadas por docente o programa."
    ],
    "marcadores_investigacion": [
      "[INV] Datos institucionales oficiales IIIEPE para portada y metadatos.",
      "[INV] Programas/carreras/materias activas.",
      "[INV] Competencias transversales institucionales.",
      "[INV] Criterios de evaluación institucionales y bibliografía mínima por materia."
    ]
  },
  "tex_editorial": {
    "plantilla": [
      "Archivo: IIIEPE/reporte-iiiepe.tex con \\input{template} homologado.",
      "Variables mínimas: institucion, programa, materia, docente, estudiante, periodo, tipoDocumento.",
      "Secciones placeholder: resumen, objetivo, competencias, desarrollo, evidencias, evaluación, referencias, anexos.",
      "Checklist comentado: compilación, citas, rutas relativas, assets existentes, PDF final."
    ],
    "actividad": [
      "Archivo sugerido: actividad-<materia>.tex.",
      "Estructura mínima: propósito, contexto, instrucciones, evidencia, formato de entrega, rúbrica, referencias.",
      "Incluir [INV] para fuentes y criterios no confirmados.",
      "Mantener en nivel maqueta; sin desarrollo disciplinar completo."
    ],
    "reporte": [
      "Archivo sugerido: reporte-<materia>.tex.",
      "Bloques mínimos: introducción/objetivo, desarrollo por unidades, evidencias, conclusiones, referencias.",
      "Integrar tablas/figuras desde assets/ con etiquetas estables.",
      "Agregar tabla breve de control editorial: versión, fecha, responsable, estado."
    ],
    "presentacion": [
      "Archivo sugerido: presentacion-iiiepe.tex o presentacion-<materia>.tex.",
      "Secuencia: portada, agenda, objetivos, desarrollo por bloques, cierre, referencias, preguntas.",
      "Regla visual: una idea central por diapositiva y apoyos breves.",
      "No insertar recursos sin disponibilidad en assets/ o sin fuente validada."
    ]
  }
}