{
  "summary": [
    "Memoria local canonizada con preservacion total y deduplicacion lossless.",
    "Se mantiene identidad UnADM y encuadre curricular verificable desde README.",
    "Se conserva normalizacion estructurada obligatoria antes de toda propagacion.",
    "Se refuerzan ejes editoriales: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se preserva TEX reconstruible del nodo y trazabilidad de fuentes locales."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Citar malla-curricular-derecho-unadm.pdf como fuente de ubicacion curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Transformar la planeacion en reporte, presentacion o producto visual segun consigna."
  ],
  "activity_rules": [
    "Definir objetivo puntual de la actividad antes del desarrollo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Verificar que el producto corresponda a la consigna de Actividad 1.",
    "No asumir que fuentes de semanas posteriores correspondan a Actividad 1."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Validar correspondencia del producto con la consigna de Actividad 1."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anomalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: archivo .bib canonico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de la actividad en el .bib de la asignatura.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No inventar referencias; usar solo obras realmente consultables.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "No asumir que filosofia-del-derecho-clean.bib corresponde a Actividad 1.",
    "Supuesto: filosofia-del-derecho-clean.bib esta orientado a Semana 7 (interpretacion juridica)."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Evitar regresiones respecto de reglas utiles previas.",
    "Aplicar normalizacion manual si se detecta salida no estructurada en nodos vecinos.",
    "Propagar solo reglas generales cuando falte consigna textual."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 1; confirmar producto exacto solicitado.",
    "Confirmar si la actividad requiere reporte, presentacion u otro formato principal.",
    "Confirmar rubrica de evaluacion especifica para ajustar profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar nombre canonico final del archivo .bib de la asignatura.",
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
      "Transformar la planeacion semanal en productos academicos con fundamento juridico, evidencia y cierre argumentativo.",
      "Asegurar trazabilidad entre consigna, fuentes, analisis y conclusion profesional."
    ],
    "style_markers": [
      "Explicitar objetivo y alcance al inicio.",
      "Usar secciones funcionales y cierre juridico transferible.",
      "Declarar supuestos cuando falte evidencia local.",
      "Mantener consistencia terminologica y de claves de cita."
    ],
    "argumentative_patterns": [
      "Plantear problema y pregunta guia.",
      "Definir conceptos y marco normativo-doctrinal.",
      "Contrastar fuentes y construir postura propia.",
      "Concluir con criterio juridico aplicable a la practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofia del Derecho",
        "Problema juridico o social",
        "Marco normativo y doctrinal",
        "Analisis propio",
        "Conclusion juridica",
        "Hermeneutica e interpretacion juridica",
        "Argumentacion juridica",
        "Derecho y moral"
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
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El encuadre inicial orienta la postura argumentada."
        },
        {
          "source": "Marco normativo y doctrinal",
          "target": "Conclusion juridica",
          "kind": "supports",
          "justification": "La conclusion debe derivar de normas, doctrina y evidencia citada."
        },
        {
          "source": "Hermeneutica e interpretacion juridica",
          "target": "Argumentacion juridica",
          "kind": "supports",
          "justification": "La interpretacion fundamenta la calidad del razonamiento juridico."
        },
        {
          "source": "Derecho y moral",
          "target": "Filosofia del Derecho",
          "kind": "develops",
          "justification": "Es un eje conceptual recurrente del curso."
        }
      ],
      "evidence": [
        "README.md: identidad UnADM, ubicacion curricular y pauta editorial.",
        "programa-analitico-filosofia-del-derecho.md: proposito y ejes de trabajo.",
        "reporte-filosofia-del-derecho-Actividad-1.tex: fuente TEX reconstruible del nodo.",
        "filosofia-del-derecho-clean.bib: evidencia local de orientacion a Semana 7."
      ]
    },
    "reinforcement_log": [
      "Ciclo 5: deduplicacion integral aplicada sin perdida semantica.",
      "Ciclo 5: reglas repetidas unificadas por forma canonica accionable.",
      "Ciclo 5: se conserva ADN editorial, grafo de conocimiento y trazabilidad local.",
      "Ciclo 5: se mantiene bloqueo de propagacion para salidas no JSON parseables."
    ]
  }
}