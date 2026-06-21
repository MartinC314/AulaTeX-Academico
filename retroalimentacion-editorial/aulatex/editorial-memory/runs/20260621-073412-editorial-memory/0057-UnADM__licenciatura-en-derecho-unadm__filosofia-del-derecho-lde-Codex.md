{
  "summary": [
    "Se consolida memoria de materia desde actividad-1 con abstraccion ascendente y deduplicacion lossless.",
    "Se preservan reglas utiles previas sin regresion y se refuerza trazabilidad actividad-materia.",
    "Se mantiene normalizacion obligatoria para toda salida no JSON parseable antes de propagar.",
    "Se fijan ejes editoriales transferibles: problema, conceptos, evidencia, analisis propio y conclusion juridica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y criterios academicos.",
    "Alinear la materia con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica de entregables y reglas.",
    "Marcar como [supuesto] todo dato no visible en consigna o documento local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local. [supuesto]",
    "Conservar referencia curricular verificable: malla-curricular-derecho-unadm.pdf."
  ],
  "structure_rules": [
    "Estructurar productos con: encuadre del problema, conceptos/marco, analisis propio y cierre.",
    "Separar secciones estables: introduccion, desarrollo, postura, conclusion.",
    "Definir objetivo puntual antes del desarrollo de cada actividad.",
    "Alinear el formato final al producto pedido en planeacion semanal.",
    "Mantener trazabilidad entre actividad, archivo .tex y archivo .bib de materia."
  ],
  "activity_rules": [
    "Iniciar cada actividad con problema juridico o social delimitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar resumen solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "No asumir que bibliografia de semanas posteriores aplica automaticamente a actividad-1. [supuesto]"
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Exigir estructura minima completa antes de reutilizacion aguas abajo.",
    "Normalizar respuestas no estructuradas antes de integrar memoria.",
    "Validar correspondencia entre citas en .tex y entradas reales en .bib.",
    "Confirmar que no se eliminen reglas utiles heredadas en cada ciclo.",
    "Registrar incidencias de ingesta sin perder contenido verificable."
  ],
  "latex_rules": [
    "Usar acentos y codificacion en espanol de forma consistente en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migracion completa.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo con caracteres anomalos antes de canonizarlos. [supuesto]",
    "Mantener separacion por tipo de entregable en archivos .tex dedicados."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente/editorial o URL.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "Registrar nuevas fuentes de actividad en el .bib de materia con trazabilidad.",
    "No completar entradas truncadas sin verificacion documental local. [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas por README, programa analitico y .bib local.",
    "Elevar al ancestro patrones reutilizables, no redaccion literal de actividad.",
    "Conservar citas recurrentes y relaciones conceptuales transferibles.",
    "Aplicar union-dedupe lossless en cada salto para evitar duplicados y regresiones.",
    "Mantener etiqueta de riesgo para ciclos con salida no estructurada heredada."
  ],
  "open_questions": [
    "Confirmar nombre canonico final del .bib de materia frente a placeholders en README. [supuesto]",
    "Confirmar consigna textual exacta de actividad-1 para fijar producto obligatorio. [supuesto]",
    "Verificar si filosofia-del-derecho-clean.bib es solo de Semana 7 o reutilizable parcial. [supuesto]",
    "Completar verificacion de entrada truncada scjnIncapacidadResistencia2019 en .bib local. [supuesto]"
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
        "Carpeta de materia como punto de entrada canonico."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Filosofia del Derecho."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas, doctrina y evidencia.",
      "Analisis propio con postura.",
      "Conclusion juridica transferible.",
      "Trazabilidad editorial y tecnica."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos solidos y verificables.",
      "Garantizar coherencia institucional, curricular y argumentativa en toda actividad.",
      "Preservar memoria util para reutilizacion segura entre nodos."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado explicito y estable.",
      "Citas verificables en afirmaciones sustantivas.",
      "Cierre con criterio juridico propio.",
      "Marcado explicito de [supuesto] cuando falte evidencia."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Construir marco conceptual-normativo.",
      "Analizar con postura propia sustentada.",
      "Concluir con aplicabilidad juridica.",
      "Verificar coherencia interna y trazabilidad de fuentes."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofia del Derecho",
        "Hermeneutica e interpretacion juridica",
        "Argumentacion juridica",
        "Derecho y moral",
        "Justicia",
        "Analisis critico del fenomeno juridico",
        "Problema-conceptos-evidencia-analisis-conclusion"
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
          "justification": "Permite evaluar razones, validez y efectos normativos."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "Articula la dimension axiologica del razonamiento juridico."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion requiere sustento legal verificable."
        }
      ],
      "evidence": [
        "README de materia y programa analitico validan identidad y ejes de trabajo.",
        "Actividad-1 confirma patron argumentativo base reutilizable.",
        "Bibliografia local muestra claves recurrentes para hermeneutica y argumentacion.",
        "Incidencias de salida no parseable justifican gate de normalizacion previa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 57: se eleva ADN editorial desde actividad-1 a materia sin copia literal.",
      "Ciclo 57: se deduplican reglas repetidas y se preserva contenido valido.",
      "Ciclo 57: se refuerza control de calidad JSON + trazabilidad .tex/.bib.",
      "Ciclo 57: se mantienen fuentes provisionales etiquetadas como [supuesto] hasta verificacion."
    ]
  }
}