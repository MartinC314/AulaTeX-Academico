{
  "summary": [
    "Se consolida refuerzo lateral desde Actividad 1 hacia Actividad 4 con deduplicacion lossless.",
    "Se preserva identidad UnADM, marco curricular y ejes editoriales comunes de Filosofia del Derecho.",
    "Se mantiene normalizacion estructurada y validacion JSON estricta como puerta de propagacion.",
    "Se transfieren solo patrones reutilizables; no se copian conclusiones ni bibliografia exclusiva de un hermano.",
    "Supuesto: la consigna especifica de Actividad 4 no esta visible y debe confirmarse."
  ],
  "identity_rules": [
    "Mantener tono institucional UnADM, formal y juridicamente preciso.",
    "Alinear la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica documental.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar integridad academica con trazabilidad de fuentes verificables."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Separar hechos, conceptos, argumentos y postura personal."
  ],
  "activity_rules": [
    "Aplicar los cinco ejes del programa analitico en cada entrega.",
    "Incluir postura argumentada del estudiante; evitar resumen solo descriptivo.",
    "Sustentar afirmaciones con evidencia y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Confirmar el tipo de producto de Actividad 4 antes de cerrar redaccion.",
    "No extrapolar automaticamente fuentes de semanas distintas."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y entradas del .bib.",
    "Normalizar respuestas no estructuradas heredadas antes de propagarlas.",
    "Verificar correspondencia entre producto entregable y consigna local de Actividad 4."
  ],
  "latex_rules": [
    "Mantener acentos y codificacion correcta en .tex y .bib.",
    "Citar solo claves existentes en el .bib activo.",
    "Conservar claves BibTeX estables para evitar roturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, sin referencias rotas y sin tokens sin expandir.",
    "Resolver plantillas no expandidas tipo $(@{...}.Slug) en README y rutas antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables.",
    "Registrar en el .bib de asignatura solo fuentes realmente consultables.",
    "No inventar referencias ni metadatos faltantes.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib parece de Semana 7; verificar aplicabilidad a Actividad 4."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Reutilizar reglas institucionales estables y ajustar solo elementos locales de actividad.",
    "Preservar reglas utiles previas; evitar regresiones por simplificacion.",
    "Aplicar union y deduplicacion semantica, no recorte de reglas validas.",
    "Cuando falte consigna local, propagar plantilla base y abrir preguntas."
  ],
  "open_questions": [
    "Confirmar consigna textual de Actividad 4: producto, extension y criterios.",
    "Confirmar si Actividad 4 requiere reporte, presentacion u otro formato.",
    "Confirmar rubrica docente especifica para calibrar profundidad argumentativa.",
    "Confirmar nombre canonico final del .bib de asignatura derivado del Slug.",
    "Confirmar si la bibliografia de interpretacion juridica aplica o si requiere set propio."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro.",
        "Juridicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Carpeta de asignatura como entrada canonica.",
        "Integridad academica con citas verificables.",
        "Normalizacion obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Filosofia del Derecho.",
        "Semestre 1, bloque 2.",
        "Obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo-doctrinal.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico y utilidad profesional.",
      "Garantizar consistencia editorial institucional entre actividades hermanas."
    ],
    "style_markers": [
      "Objetivo puntual al inicio.",
      "Secciones funcionales claras.",
      "Cita explicita en afirmaciones relevantes.",
      "Supuestos marcados cuando falta evidencia local."
    ],
    "argumentative_patterns": [
      "Problema inicial -> marco conceptual -> contraste de fuentes -> postura propia -> conclusion aplicada.",
      "Hecho y norma separados antes de valorar.",
      "Cierre con implicacion practica juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Ejes editoriales",
        "Normalizacion estructurada",
        "Validacion JSON",
        "Integridad academica",
        "Coherencia problema-evidencia-conclusion"
      ],
      "citations": [
        "README.md",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Tono formal y preciso",
          "kind": "supports",
          "justification": "La pauta editorial institucional define registro y formato."
        },
        {
          "source": "Ejes editoriales",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Los ejes ordenan el desarrollo y el cierre."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay transferencia segura."
        },
        {
          "source": "Integridad academica",
          "target": "Conclusion juridica propia",
          "kind": "supports",
          "justification": "La conclusion exige respaldo verificable y analisis."
        }
      ],
      "evidence": [
        "README fija entrada canonica, identidad UnADM e integridad academica.",
        "Programa analitico fija cinco ejes transferibles.",
        "Antecedentes de salidas no parseables justifican gate JSON estricto."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas con variantes ortograficas.",
      "Se mantuvieron reglas utiles previas sin recorte funcional.",
      "Se eliminaron traslados literales de contenido especifico de Actividad 1.",
      "Se reforzo control de supuestos por falta de consigna local visible.",
      "Se priorizo transferencia de patrones reutilizables entre nodos hermanos."
    ]
  }
}