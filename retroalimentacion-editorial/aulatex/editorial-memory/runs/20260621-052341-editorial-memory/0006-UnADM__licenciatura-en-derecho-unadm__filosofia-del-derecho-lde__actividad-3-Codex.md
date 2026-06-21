{
  "summary": [
    "Se consolida refuerzo lateral desde actividad-1 hacia actividad-3 sin copiar contenido especifico.",
    "Se preservan reglas utiles previas y se deduplican por union lossless.",
    "Se mantiene identidad UnADM, estructura argumentativa y control de calidad parseable.",
    "Se conserva politica de supuestos para datos no confirmados de la consigna local.",
    "Se mantiene separacion entre memoria editorial y evidencia academica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memorias heredadas no verificadas como antecedente provisional.",
    "No usar antecedentes editoriales como fuente academica."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al tipo solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Si falta consigna local, usar estructura base y marcar supuestos."
  ],
  "activity_rules": [
    "Heredar solo patrones reutilizables entre actividades hermanas.",
    "No copiar redaccion literal ni conclusiones especificas de otra actividad.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir semana, formato o bibliografia especifica sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado y propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que cada afirmacion tenga respaldo o marca de supuesto.",
    "Aplicar no regresion: no eliminar reglas utiles previas.",
    "Verificar trazabilidad entre citas en texto y archivo .bib.",
    "Normalizar manualmente memorias con incidencias de parseo."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener claves BibTeX estables y no renombrarlas sin necesidad.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Corregir caracteres anómalos y tokens sin expandir en rutas o nombres.",
    "Supuesto: el .bib canonico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM, normativas, doctrinales y jurisprudenciales verificables.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Registrar en .bib solo entradas realmente citadas.",
    "Conservar metadatos minimos: autor, titulo, año y fuente editorial o URL."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir a nodos hermanos solo reglas generales reutilizables.",
    "No propagar supuestos como hechos confirmados.",
    "Mantener bandera de riesgo por antecedentes de parseo no estructurado.",
    "Aplicar compresion lossless por union y deduplicacion en cada ciclo.",
    "Escalar primero reglas institucionales y de calidad; luego reglas locales verificadas."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de actividad-3; confirmar producto exacto solicitado.",
    "Confirmar si actividad-3 requiere reporte, presentacion u otro formato.",
    "Confirmar rubrica de evaluacion especifica para profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana correspondiente a actividad-3.",
    "Confirmar si bibliografia depurada de Semana 7 aplica o no a actividad-3.",
    "Confirmar nombre canonico final del archivo .bib en uso efectivo."
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
      "Evidencia verificable y cita explicita.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos con fundamento juridico.",
      "Asegurar claridad, evidencia y transferencia profesional.",
      "Sostener continuidad editorial entre actividades sin perdida de calidad."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explicitas y orden logico.",
      "Afirmacion seguida de evidencia e interpretacion.",
      "Supuestos marcados cuando falte evidencia local.",
      "Cierre aplicable a practica juridica."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis propio -> conclusion.",
      "Afirmacion -> fuente -> interpretacion -> postura.",
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
        "Bibliografia verificable",
        "Politica de supuestos"
      ],
      "citations": [
        "README.md de la asignatura",
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
          "justification": "Sin estructura valida no hay trazabilidad ni control editorial."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El analisis se activa desde un problema delimitado."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion depende de argumentacion sustentada."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad academica y conclusion juridica.",
        "Programa analitico: ejes de trabajo y proposito de realizacion.",
        "Regla persistente: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 6: se refuerza transferibilidad lateral sin copiar contenido especifico.",
      "Ciclo 6: se preservan gates de parseo y no regresion.",
      "Ciclo 6: se consolida politica de supuestos para falta de consigna local.",
      "Ciclo 6: se mantiene deduplicacion lossless en todas las listas."
    ]
  }
}