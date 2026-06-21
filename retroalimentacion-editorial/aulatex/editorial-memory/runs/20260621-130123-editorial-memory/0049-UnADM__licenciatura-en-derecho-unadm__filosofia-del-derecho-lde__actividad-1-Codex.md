{
  "summary": [
    "Memoria local canonizada por union y deduplicacion lossless.",
    "Se preserva identidad UnADM y ubicacion curricular verificable.",
    "Se mantiene normalizacion JSON obligatoria antes de propagacion.",
    "Se consolidan ejes: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se preserva TEX reconstruible de Actividad 1 y sus claves de cita.",
    "Se refuerza regla de marcar supuestos cuando falte consigna textual."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular Actividad 1 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como punto de entrada canonico.",
    "Citar malla-curricular-derecho-unadm.pdf para ubicacion curricular.",
    "Marcar como supuesto todo dato no visible en consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Verificar que el producto corresponda a la consigna de Actividad 1.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir que fuentes de semanas posteriores aplican a Actividad 1."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Validar correspondencia del producto con la consigna de Actividad 1."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Verificar nombres de archivo contra README y programa analitico.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir caracteres anomalos en rutas o nombres antes de compilar.",
    "Supuesto: .bib canonico esperado es filosofia-del-derecho.bib por Slug local."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de la actividad en el .bib de la asignatura.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a Semana 7 y no a Actividad 1."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Reutilizar reglas institucionales de calidad sin perder especificidad local.",
    "Aplicar normalizacion manual en nodos con salida no estructurada.",
    "Evitar regresiones: no eliminar reglas utiles previas.",
    "Propagar solo reglas generales cuando falte consigna textual."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 1; confirmar producto exacto.",
    "Confirmar si el formato principal es reporte, presentacion u otro.",
    "Confirmar rubrica de evaluacion especifica.",
    "Confirmar fuentes obligatorias de la semana de Actividad 1.",
    "Confirmar nombre canonico final del .bib de la asignatura.",
    "Confirmar si Actividad 1 reutiliza bibliografia existente o requiere .bib propio."
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
      "Problema juridico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion transferible a la practica juridica."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos con fundamento juridico y evidencia.",
      "Asegurar cierre argumentativo con utilidad profesional."
    ],
    "style_markers": [
      "Apertura con problema y objetivo.",
      "Desarrollo por secciones funcionales.",
      "Citas verificables y consistentes con .bib.",
      "Marcado explicito de supuestos."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos y marco -> analisis propio -> conclusion juridica.",
      "Afirmacion -> evidencia verificable -> inferencia juridica.",
      "Consigna -> adecuacion de formato -> entrega final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofia del Derecho",
        "Objeto de estudio",
        "Principios y normas juridicas",
        "Justicia",
        "Fundamentos del derecho",
        "Analisis critico del fenomeno juridico",
        "Evolucion historica: antiguedad, edad media y moderna, contemporaneidad",
        "Derecho y moral",
        "Hermeneutica e interpretacion juridica",
        "Argumentacion juridica"
      ],
      "citations": [
        "finnis_estudios_2017",
        "lovon_manual_2020",
        "ruiz_rodriguez_filosofia_derecho_2009",
        "noauthor_constitucion_nodate",
        "generales_ley_2021",
        "de_victimas_ley_2013",
        "franzoni_acevedo_ley_2017",
        "rojas_gonzalez_filosofia_derecho_2018",
        "gandara_ley_2015",
        "hernandezManriquezHermeneutica2019",
        "scjnMemoriaArgumentacion2008",
        "scjnViolenciaFisica2022",
        "scjnIncapacidadResistencia2019"
      ],
      "relations": [
        {
          "source": "Problema juridico o social",
          "target": "Analisis critico del fenomeno juridico",
          "kind": "develops",
          "justification": "El encuadre inicial activa el desarrollo argumentativo."
        },
        {
          "source": "Conceptos, normas y doctrina",
          "target": "Postura academica propia",
          "kind": "supports",
          "justification": "La postura se valida con marco conceptual y normativo."
        },
        {
          "source": "Evidencia bibliografica verificable",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion requiere respaldo trazable."
        },
        {
          "source": "Consigna de Actividad 1",
          "target": "Tipo de artefacto",
          "kind": "depends_on",
          "justification": "El formato final depende de la instruccion explicita."
        }
      ],
      "evidence": [
        "README.md: identidad UnADM, ubicacion curricular y pauta editorial.",
        "programa-analitico-filosofia-del-derecho.md: proposito y ejes de trabajo.",
        "reporte-filosofia-del-derecho-Actividad-1.tex: fuente TEX reconstruible.",
        "filosofia-del-derecho-clean.bib: marcado local de Semana 7 como contexto distinto."
      ]
    },
    "reinforcement_log": [
      "Ciclo 13: deduplicacion integral sin perdida semantica.",
      "Ciclo 13: preservacion de reglas de normalizacion JSON y compresion lossless.",
      "Ciclo 13: refuerzo de dependencia consigna-producto y marcado de supuestos.",
      "Ciclo 13: continuidad de claves BibTeX y trazabilidad TEX/.bib."
    ]
  }
}