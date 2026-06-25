{
  "summary": [
    "Se consolida memoria lateral de Actividad 5 con deduplicacion lossless.",
    "Se preservan reglas troncales: identidad UnADM, estructura argumentativa y control de calidad.",
    "Se refuerza transferencia por patrones reutilizables, sin copiar conclusiones ni bibliografia exclusiva de Actividad 1.",
    "Se mantiene gate estricto: no propagar sin JSON parseable y estructura minima completa.",
    "Supuesto: falta consigna local de Actividad 5; se conserva plantilla base y preguntas abiertas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y encuadre.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Conservar enfoque juridico-academico con claridad, fundamento y transferencia profesional.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas de modelos como provisionales hasta verificacion local.",
    "No usar memoria de modelos como fuente academica."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Distinguir explicitamente afirmacion, evidencia e inferencia.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica aplicable a practica profesional."
  ],
  "activity_rules": [
    "Adaptar el producto al enunciado real de Actividad 5 sin romper reglas de asignatura.",
    "Incluir postura argumentada del estudiante y evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No arrastrar bibliografia de otra semana sin confirmar pertinencia.",
    "Registrar supuesto operativo si hay duda de alcance."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en afirmaciones relevantes.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Rechazar respuestas no estructuradas antes de reutilizar.",
    "Aplicar revision manual extra en memoria con historial de fallas de parseo."
  ],
  "latex_rules": [
    "Usar acentos y codificacion en espanol de forma consistente en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres/rutas anomales antes de compilar.",
    "Supuesto: .bib canonico esperado es filosofia-del-derecho.bib; confirmar localmente."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar en .bib solo fuentes realmente citadas en el texto.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Tratar filosofia-del-derecho-clean.bib como potencialmente tematico de otra semana hasta confirmar pertinencia.",
    "Conservar claves ya usadas en .tex cuando la fuente sea valida."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Reutilizar reglas institucionales y de calidad sin perder especificidad local.",
    "Aplicar union-dedupe; no eliminar reglas utiles previas.",
    "Transferir solo patrones reutilizables entre hermanos.",
    "Evitar copiar redaccion literal, conclusiones concretas o bibliografia exclusiva.",
    "Mantener bandera historica de riesgo por salidas no parseables en ciclos previos."
  ],
  "open_questions": [
    "Confirmar consigna textual de Actividad 5.",
    "Confirmar rubrica de evaluacion de Actividad 5.",
    "Confirmar formato requerido: reporte, presentacion o recurso visual.",
    "Confirmar nombre canonico final del archivo .bib de la asignatura.",
    "Confirmar si bibliografia de Semana 7 aplica total, parcial o nada a Actividad 5."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de asignatura como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Filosofia del Derecho."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir la planeacion semanal en productos academicos con rigor juridico.",
      "Asegurar trazabilidad entre consigna, desarrollo, evidencia y cierre.",
      "Mantener continuidad editorial institucional entre actividades."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones funcionales y claras.",
      "Supuestos declarados cuando falten datos.",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> inferencia juridica.",
      "Contraste doctrinal breve -> toma de postura.",
      "Cierre con transferencia a practica profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Problema juridico",
        "Marco normativo/doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion JSON",
        "Consistencia cita-.bib"
      ],
      "citations": [
        "README.md",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Estructura de actividad",
          "kind": "supports",
          "justification": "Define tono, rigor y formato del entregable."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin problema delimitado no hay argumentacion pertinente."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La validez del cierre depende del respaldo trazable."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "La transferencia confiable exige estructura parseable."
        },
        {
          "source": "Bibliografia especifica de actividad",
          "target": "Bibliografia base",
          "kind": "contrasts",
          "justification": "La base orienta curso; la especifica responde consigna."
        }
      ],
      "evidence": [
        "README: identidad UnADM, citas verificables y conclusion juridica propia.",
        "Programa analitico: ejes problema-conceptos-fuentes-analisis-cierre.",
        "Historial de parseo: gate de JSON obligatorio antes de propagar."
      ]
    },
    "reinforcement_log": [
      "Ciclo 8: deduplicacion integral de reglas repetidas.",
      "Ciclo 8: se refuerza transferencia lateral por analogia controlada.",
      "Ciclo 8: se conserva ADN editorial y se evita copia de contenido especifico de hermano.",
      "Ciclo 8: se mantienen supuestos abiertos donde faltan datos locales verificables."
    ]
  }
}