{
  "summary": [
    "Se consolida transferencia lateral desde actividad-1 a actividad-3 con deduplicacion lossless.",
    "Se preserva identidad UnADM y contexto curricular confirmado en README y programa analitico.",
    "Se refuerzan ejes editoriales reutilizables: problema, conceptos y fuentes, analisis propio, conclusion juridica.",
    "Se mantiene regla critica: no propagar sin JSON parseable y estructura minima valida.",
    "Se mantiene politica de supuestos para datos no visibles en consigna local de actividad-3.",
    "Se evita copiar conclusiones o bibliografia exclusiva del nodo hermano sin verificacion local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular actividad-3 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memorias editoriales Codex o GPT-Pro como antecedente provisional, no como fuente academica.",
    "Usar malla-curricular-derecho-unadm.pdf solo para ubicacion curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el documento al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Si falta consigna local, usar estructura base y marcar supuestos."
  ],
  "activity_rules": [
    "Heredar solo patrones reutilizables de actividad-1.",
    "No copiar redaccion literal ni conclusiones especificas del hermano.",
    "Incluir postura argumentada del estudiante y evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir semana, formato o tema de actividad-3 sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado y propagacion si la salida no es JSON parseable.",
    "Validar esquema completo antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en cada afirmacion sensible.",
    "Aplicar no regresion: no eliminar reglas utiles previas.",
    "Verificar correspondencia entre consigna local y tipo de producto final.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Corregir tokens sin expandir en README o programa analitico antes de automatizar rutas.",
    "Supuesto: archivo .bib canonico esperado por Slug es filosofia-del-derecho.bib."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar en .bib solo fuentes realmente citadas por la actividad.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No trasladar bibliografia exclusiva de actividad-1 a actividad-3 sin evidencia de uso.",
    "Supuesto: filosofia-del-derecho-clean.bib es tematico de interpretacion juridica y su uso en actividad-3 debe confirmarse."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir a nodos hermanos solo reglas generales y patrones argumentativos.",
    "No propagar supuestos como hechos confirmados.",
    "Mantener compresion por union y deduplicacion sin recorte semantico.",
    "Conservar bandera de riesgo cuando existan antecedentes de parseo defectuoso.",
    "Priorizar refuerzo-lateral de identidad, calidad y estructura sobre contenido especifico."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-3.",
    "Confirmar formato de entrega requerido en actividad-3.",
    "Confirmar rubrica de evaluacion especifica de actividad-3.",
    "Confirmar fuentes obligatorias de la semana correspondiente a actividad-3.",
    "Confirmar si actividad-3 reutiliza bibliografia existente o requiere .bib propio.",
    "Confirmar nombre canonico final de artefacto .tex para actividad-3."
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
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible.",
      "Trazabilidad entre afirmaciones y fuentes."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico.",
      "Garantizar calidad formal, argumentativa y bibliografica en cada actividad.",
      "Sostener continuidad editorial entre actividades sin contaminar evidencia."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones explicitas y orden logico.",
      "Citas verificables en afirmaciones clave.",
      "Supuestos marcados cuando falte evidencia local.",
      "Cierre juridico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual y normativo -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> postura.",
      "Objetivo declarado -> desarrollo coherente -> cierre consistente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalizacion JSON",
        "Integridad academica",
        "Problema juridico",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Bibliografia verificable"
      ],
      "citations": [
        "README.md",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib [supuesto de aplicacion condicionada]"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y criterio propio."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Integridad academica",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay trazabilidad editorial confiable."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El analisis parte de una delimitacion clara del problema."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion depende de argumentacion sustentada."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad academica, conclusion juridica propia.",
        "Programa analitico: ejes problema-conceptos-fuentes-analisis-cierre.",
        "Regla persistente: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 21: deduplicacion completa sin perdida de reglas utiles.",
      "Ciclo 21: refuerzo lateral de estructura y compuertas de calidad.",
      "Ciclo 21: se preserva politica de supuestos y no invencion de fuentes.",
      "Ciclo 21: se evita transferencia de contenido especifico no verificable entre hermanos."
    ]
  }
}