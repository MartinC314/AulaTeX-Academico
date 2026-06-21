{
  "summary": [
    "Memoria lateral consolidada para Actividad 5 con deduplicacion lossless y sin recorte de reglas utiles.",
    "Se preserva identidad UnADM y contexto curricular: Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se refuerzan ejes editoriales recurrentes: problema, conceptos, evidencia, analisis propio y conclusion juridica transferible.",
    "Se mantiene gate critico: no propagar nada sin JSON parseable y estructura minima completa.",
    "Se conserva criterio de transferencia entre hermanos: solo patrones reutilizables; no copiar conclusiones ni bibliografia exclusiva."
  ],
  "identity_rules": [
    "Mantener tono formal academico y precision juridica.",
    "Alinear todo entregable con identidad institucional UnADM.",
    "Vincular actividad a Filosofia del Derecho en Licenciatura en Derecho.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar memorias de modelos previos como provisionales hasta verificacion local.",
    "Conservar ubicacion curricular oficial: semestre 1, bloque 2, obligatoria, 8 creditos."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Distinguir afirmaciones, evidencia e inferencia juridica.",
    "Cerrar con conclusion juridica aplicable a practica profesional.",
    "Alinear estructura al producto pedido por la planeacion semanal.",
    "Mantener trazabilidad entre consigna, desarrollo y conclusion."
  ],
  "activity_rules": [
    "Adaptar el contenido al enunciado real de Actividad 5.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Evitar relleno descriptivo sin funcion argumentativa.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y cierre.",
    "No arrastrar bibliografia de otras semanas sin confirmar pertinencia.",
    "Si falta dato operativo, declarar supuesto y continuar con consistencia."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en cada afirmacion relevante.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Rechazar memoria no estructurada hasta normalizacion manual.",
    "Verificar que el producto responda al problema y no solo liste conceptos.",
    "Evitar regresiones: no eliminar reglas utiles previas."
  ],
  "latex_rules": [
    "Usar espanol con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables ya usadas en .tex.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Verificar nombres reales de archivos cuando README tenga tokens sin expandir.",
    "Resolver marcadores tipo $(@{...}.Slug) antes de referenciar rutas.",
    "Supuesto: nombre canonico esperado del .bib es filosofia-del-derecho.bib, pendiente confirmacion local."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Registrar en .bib solo fuentes realmente citadas.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Tratar filosofia-del-derecho-clean.bib como potencialmente tematico de otra semana hasta validar pertinencia.",
    "Conservar claves existentes para evitar rotura de compilacion."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Aplicar union y deduplicacion; no recortar contenido valido.",
    "Transferir entre hermanos solo patrones reutilizables de identidad, estructura y calidad.",
    "No transferir redaccion literal, conclusiones especificas ni bibliografia exclusiva.",
    "Mantener bandera historica por incidentes previos de parseo.",
    "Si hay duda local, propagar plantilla base y abrir preguntas."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 5.",
    "Confirmar rubrica de evaluacion de Actividad 5.",
    "Confirmar tipo de producto principal: reporte, presentacion o recurso visual.",
    "Confirmar nombre canonico final del .bib de asignatura.",
    "Confirmar si fuentes de Interpretacion juridica (Semana 7) aplican a Actividad 5.",
    "Supuesto: documentos con metadata de Actividad 1 no definen contenido especifico de Actividad 5."
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
        "Asignatura: Filosofia del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico bien delimitado.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable y trazable.",
      "Analisis propio con inferencia juridica.",
      "Conclusion transferible a practica profesional."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos utiles y verificables.",
      "Asegurar continuidad editorial entre actividades sin perder identidad institucional.",
      "Garantizar propagacion confiable mediante normalizacion estructurada."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales sin ornamento.",
      "Supuestos explicitados.",
      "Cierre juridico accionable."
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
          "justification": "La pauta institucional define tono, integridad y forma del entregable."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitacion del problema no hay argumentacion focalizada."
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
          "justification": "La base orienta; la especifica responde a la consigna concreta."
        }
      ],
      "evidence": [
        "README: identidad UnADM, citas verificables y conclusion juridica propia.",
        "Programa analitico: ejes problema-conceptos-fuentes-analisis-cierre.",
        "Historial de ciclo: incidentes de parseo exigen gate estructural."
      ]
    },
    "reinforcement_log": [
      "Se elimino duplicacion textual en reglas manteniendo cobertura completa.",
      "Se reforzo politica de supuestos para datos no visibles.",
      "Se mantuvo separacion entre bibliografia base y bibliografia por actividad.",
      "Se consolido regla de transferencia lateral sin copia literal entre hermanos.",
      "Se preservo ADN institucional sin importar variacion del producto final."
    ]
  }
}