{
  "summary": [
    "Se consolida memoria de materia desde actividad-1 con abstraccion ascendente y deduplicacion lossless.",
    "Se preservan reglas utiles previas sin regresion y se refuerza normalizacion estructurada obligatoria.",
    "Se institucionaliza el patron editorial comun: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene trazabilidad entre README, programa analitico, .tex y .bib de la materia.",
    "Se registran salidas no JSON parseable como riesgo de ingesta, sin perder contenido verificable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y redaccion.",
    "Alinear toda salida con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica de trabajo editorial.",
    "Marcar como [supuesto] cualquier dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local. [supuesto]",
    "Conservar referencia a malla-curricular-derecho-unadm.pdf como soporte curricular verificado."
  ],
  "structure_rules": [
    "Abrir cada producto con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto solicitado en planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener trazabilidad entre actividad, archivo .tex y archivo .bib."
  ],
  "activity_rules": [
    "Evitar entregas solo descriptivas; exigir postura argumentada del estudiante.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir que fuentes de semanas posteriores aplican automaticamente a actividad-1. [supuesto]",
    "Validar que el producto corresponda exactamente a la consigna de la actividad.",
    "Agregar bibliografia especifica de actividad solo tras verificacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar memoria aguas abajo.",
    "Normalizar toda respuesta no estructurada antes de propagar.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en .tex y entradas en .bib.",
    "Confirmar en cada ciclo que no se eliminen reglas utiles previas."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migracion completa.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo anommalos antes de tratarlos como canonicos. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "Registrar fuentes de actividad en el .bib canonico de la asignatura tras validar nombre final. [supuesto]",
    "Mantener y verificar claves recurrentes de SCJN, UNAM e institucionales ya presentes."
  ],
  "propagation_hints": [
    "Propagar hacia ancestros solo reglas generales, reutilizables y verificadas.",
    "No copiar redaccion literal de actividad; elevar patrones y relaciones editoriales.",
    "Conservar trazabilidad de citas recurrentes al subir de actividad a materia.",
    "Aplicar compresion por union-dedupe lossless en cada ciclo.",
    "Si faltan consignas textuales, propagar solo reglas transversales y marcar [supuesto].",
    "Mantener registro de incidencias de parseo como control de riesgo editorial."
  ],
  "open_questions": [
    "Confirmar consigna textual completa de actividad-1 para fijar producto exacto.",
    "Confirmar nombre canonico definitivo del .bib de la materia.",
    "Definir si filosofia-del-derecho-clean.bib es auxiliar o canonico. [supuesto]",
    "Completar y verificar la entrada truncada scjnIncapacidadResistencia2019. [supuesto]",
    "Confirmar rubrica de evaluacion especifica para calibrar profundidad argumentativa."
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
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Filosofia del Derecho."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo-doctrinal.",
      "Evidencia verificable.",
      "Analisis propio con postura.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y evaluables.",
      "Asegurar coherencia entre identidad institucional, rigor juridico y calidad tecnica en LaTeX."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable por funcion argumentativa.",
      "Cierre con aplicabilidad profesional.",
      "Marcado explicito de [supuesto] cuando falte evidencia."
    ],
    "argumentative_patterns": [
      "Delimitar problema antes de teorizar.",
      "Fundamentar con doctrina, norma y fuente verificable.",
      "Contrastar y justificar postura propia.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofia del Derecho",
        "Hermeneutica e interpretacion juridica",
        "Argumentacion juridica",
        "Derecho y moral",
        "Justicia",
        "Analisis critico del fenomeno juridico"
      ],
      "citations": [
        "hernandezManriquezHermeneutica2019",
        "scjnMemoriaArgumentacion2008",
        "scjnViolenciaFisica2022",
        "scjnIncapacidadResistencia2019",
        "ruiz_rodriguez_filosofia_derecho_2009",
        "rojas_gonzalez_filosofia_derecho_2018",
        "noauthor_constitucion_nodate",
        "de_victimas_ley_2013"
      ],
      "relations": [
        {
          "source": "Hermeneutica e interpretacion juridica",
          "target": "Argumentacion juridica",
          "kind": "supports",
          "justification": "La interpretacion provee criterios para construir argumentos."
        },
        {
          "source": "Argumentacion juridica",
          "target": "Analisis critico del fenomeno juridico",
          "kind": "develops",
          "justification": "La argumentacion permite evaluar razones y consecuencias normativas."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "La materia integra el debate entre validez, justicia y etica."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion requiere sustento legal verificable."
        }
      ],
      "evidence": [
        "README de materia: pauta editorial e identidad UnADM.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "Bibliografia local: claves recurrentes UNAM/SCJN y textos base juridicos.",
        "Regla persistente: normalizar antes de propagar cuando no hay JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 41: se elevaron patrones de actividad-1 a nivel materia sin copia literal.",
      "Ciclo 41: se deduplicaron reglas repetidas y se preservo contenido valido.",
      "Ciclo 41: se reforzo gate de parseo JSON y normalizacion previa como regla no negociable.",
      "Ciclo 41: se mantuvo trazabilidad curricular y bibliografica con marcacion de supuestos."
    ]
  }
}