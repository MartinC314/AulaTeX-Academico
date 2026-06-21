{
  "summary": [
    "Memoria lateral consolidada para Actividad 5 con deduplicacion lossless.",
    "Se preserva identidad UnADM y contexto curricular de Filosofia del Derecho.",
    "Se refuerza pauta troncal: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene control estricto de JSON parseable antes de propagacion.",
    "Se conserva regla de no transferir redaccion literal ni bibliografia exclusiva entre hermanos.",
    "Supuesto: falta consigna local completa de Actividad 5; se mantiene estructura base reusable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y encuadre.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Conservar enfoque juridico-academico con claridad, fundamento y transferencia profesional.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas de modelos como provisionales hasta verificacion local.",
    "No usar memoria de modelo como fuente academica."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Distinguir afirmacion, evidencia e inferencia juridica en bloques claros.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Validar salida JSON parseable antes de guardar o propagar."
  ],
  "activity_rules": [
    "Adaptar el producto al enunciado real de Actividad 5 sin romper reglas de asignatura.",
    "Incluir postura argumentada del estudiante y evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No arrastrar conclusiones especificas de Actividad 1.",
    "No arrastrar bibliografia exclusiva de otra semana sin confirmar pertinencia.",
    "Si falta alcance local, registrar supuesto operativo y continuar con consistencia."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en afirmaciones relevantes.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que el producto responda a la consigna y no solo resuma conceptos.",
    "Aplicar revision manual extra a memoria con historial de incidentes de parseo."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Validar nombres reales de archivos cuando README tenga tokens sin expandir.",
    "Resolver token tipo $(@{...}.Slug) antes de fijar nombre canonico de .bib.",
    "Supuesto: .bib canonico esperado filosofia-del-derecho.bib; confirmar localmente."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar en .bib solo fuentes realmente citadas en el texto.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Tratar filosofia-del-derecho-clean.bib como orientado a Semana 7 hasta confirmar pertinencia para Actividad 5.",
    "Conservar claves existentes ya usadas por el .tex."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura minima.",
    "Transferir solo patrones reutilizables de identidad, estructura, calidad y grafo conceptual.",
    "Evitar regresiones: no eliminar reglas utiles previas ya validadas.",
    "Aplicar union-dedupe en cada ciclo para compresion lossless.",
    "No propagar bibliografia no verificada como si fuera obligatoria.",
    "Cuando falten datos locales, propagar plantilla base y preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar consigna textual completa de Actividad 5.",
    "Confirmar rubrica de evaluacion especifica de Actividad 5.",
    "Confirmar tipo de producto requerido: reporte, presentacion o recurso visual.",
    "Confirmar nombre canonico final del archivo .bib de la asignatura.",
    "Confirmar si bibliografia de Semana 7 es pertinente para Actividad 5.",
    "Supuesto: los metadatos curriculares del README siguen vigentes sin cambios."
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
      "Problema juridico o social delimitado.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable con trazabilidad.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos consistentes.",
      "Garantizar coherencia juridica y calidad formal en cada actividad.",
      "Preservar continuidad editorial entre nodos hermanos sin copiar contenido especifico."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales y trazables.",
      "Uso explicito de supuestos cuando falte informacion.",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> inferencia juridica.",
      "Contraste doctrinal breve -> toma de postura."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Problema juridico",
        "Marco normativo/doctrinal",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion JSON",
        "Consistencia cita-bib"
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
          "justification": "La pauta institucional define tono, forma y criterio."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitacion del problema no hay analisis consistente."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica valida requiere respaldo trazable."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia confiable."
        },
        {
          "source": "Bibliografia especifica de actividad",
          "target": "Bibliografia base",
          "kind": "contrasts",
          "justification": "La base orienta; la especifica responde a la consigna."
        }
      ],
      "evidence": [
        "README establece identidad UnADM e integridad academica.",
        "Programa analitico define ejes problema-conceptos-fuentes-analisis-cierre.",
        "Historial reporta incidentes de salida no parseable y exige gate estructural.",
        "Token Slug sin expandir en README obliga validacion de nombre .bib."
      ]
    },
    "reinforcement_log": [
      "Ciclo 55: deduplicacion de reglas repetidas en destino.",
      "Ciclo 55: preservacion de reglas utiles previas sin recorte semantico.",
      "Ciclo 55: refuerzo lateral con patrones reutilizables, sin copiar conclusiones de Actividad 1.",
      "Ciclo 55: mantenimiento de banderas de supuesto por falta de consigna local completa."
    ]
  }
}