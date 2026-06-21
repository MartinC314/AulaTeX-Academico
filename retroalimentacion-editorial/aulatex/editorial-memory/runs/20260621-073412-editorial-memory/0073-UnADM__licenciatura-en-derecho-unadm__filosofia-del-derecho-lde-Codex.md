{
  "summary": [
    "Se consolida memoria de materia desde actividad con abstraccion ascendente y deduplicacion lossless.",
    "Se preserva identidad UnADM, ubicacion curricular y pauta editorial como nucleo estable.",
    "Se refuerza el patron comun: problema, conceptos y fuentes, analisis propio, conclusion juridica transferible.",
    "Se mantiene normalizacion obligatoria de insumos no estructurados antes de cualquier propagacion.",
    "Se conserva trazabilidad entre consigna, archivo .tex y archivo .bib de la materia."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, redaccion y formato.",
    "Alinear entregables con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local. [supuesto]",
    "Usar malla-curricular-derecho-unadm.pdf como respaldo curricular verificado."
  ],
  "structure_rules": [
    "Abrir cada producto con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto solicitado en la planeacion semanal.",
    "Cerrar con conclusion juridica aplicable a la practica profesional.",
    "Mantener trazabilidad entre actividad, TEX principal y bibliografia de materia."
  ],
  "activity_rules": [
    "Delimitar problema y pregunta guia al inicio de cada actividad.",
    "Sustentar afirmaciones sustantivas con fuente verificable y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre objetivo, desarrollo y conclusion.",
    "No asumir que bibliografia de semanas posteriores aplica automaticamente a actividad inicial. [supuesto]",
    "Agregar fuentes especificas de actividad solo cuando exista verificacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no se eliminen reglas utiles previas en cada ciclo.",
    "Exigir marca de supuesto en toda afirmacion no verificable.",
    "Validar consistencia entre citas en TEX y entradas en BIB."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en espanol en TEX y BIB.",
    "Mantener claves BibTeX estables; no renombrar sin migracion completa.",
    "Compilar sin errores criticos, sin referencias rotas y sin tokens sin expandir.",
    "Resolver placeholders tipo $(@{...}.Slug) antes de fijar nombres canonicos.",
    "Conservar separacion por tipo de entregable en archivos TEX dedicados.",
    "Verificar rutas y nombres de archivo del README antes de referenciar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente editorial o URL.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "Registrar y deduplicar entradas sin perdida de informacion.",
    "Tratar entradas truncadas como pendientes hasta completar verificacion local. [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas por README, programa analitico y BIB local.",
    "Elevar al ancestro patrones reutilizables, no redaccion literal de actividades.",
    "Conservar trazabilidad de citas recurrentes al subir de actividad a materia.",
    "No propagar nombres de archivo anomalos hasta correccion local.",
    "Mantener etiqueta de compresion union-dedupe lossless en cada salto.",
    "Registrar ciclos con necesidad de normalizacion manual cuando haya insumo no estructurado."
  ],
  "open_questions": [
    "Confirmar nombre canonico final del BIB de materia frente a placeholders Slug. [supuesto]",
    "Confirmar si actividad 1 exige reporte, presentacion o mapa conceptual como producto principal. [supuesto]",
    "Confirmar rubrica especifica de evaluacion para calibrar profundidad argumentativa. [supuesto]",
    "Confirmar si filosofia-del-derecho-clean.bib es auxiliar de semana o base transversal. [supuesto]",
    "Completar y verificar campos faltantes en scjnIncapacidadResistencia2019. [supuesto]"
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
      "Conceptos, normas y doctrina pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos juridicamente fundados.",
      "Estandarizar calidad editorial sin perder especificidad por actividad.",
      "Garantizar trazabilidad entre aprendizaje, argumento y evidencia."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable.",
      "Postura propia explicita.",
      "Cierre aplicable a practica juridica.",
      "Marcado explicito de supuestos."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual y normativo.",
      "Contrastar fuentes y criterios.",
      "Sostener postura propia con evidencia.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofia del Derecho",
        "Hermeneutica juridica",
        "Interpretacion juridica",
        "Argumentacion juridica",
        "Derecho y moral",
        "Justicia",
        "Analisis critico del fenomeno juridico",
        "Trazabilidad TEX-BIB"
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
          "source": "Hermeneutica juridica",
          "target": "Interpretacion juridica",
          "kind": "supports",
          "justification": "La hermeneutica provee criterios para interpretar normas."
        },
        {
          "source": "Interpretacion juridica",
          "target": "Argumentacion juridica",
          "kind": "supports",
          "justification": "La interpretacion fundamenta razones juridicas defendibles."
        },
        {
          "source": "Argumentacion juridica",
          "target": "Analisis critico del fenomeno juridico",
          "kind": "develops",
          "justification": "Permite evaluar validez, coherencia y consecuencias."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion exige sustento normativo y doctrinal verificable."
        }
      ],
      "evidence": [
        "README de materia para identidad y ubicacion curricular.",
        "Programa analitico para proposito y ejes de trabajo.",
        "BIB local para claves juridicas recurrentes.",
        "Patron estable observado en actividad 1: problema-conceptos-evidencia-analisis-conclusion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 73: se elevo ADN editorial reusable de actividad a materia sin copiar redaccion literal.",
      "Ciclo 73: se deduplicaron reglas repetidas y se preservaron reglas utiles previas.",
      "Ciclo 73: se reforzo control de calidad sobre JSON parseable y normalizacion previa.",
      "Ciclo 73: se mantuvo trazabilidad de citas recurrentes y supuestos pendientes."
    ]
  }
}