{
  "summary": [
    "Se consolida memoria de materia desde actividad-1 con abstraccion ascendente y deduplicacion lossless.",
    "Se preserva identidad UnADM, trazabilidad curricular y reglas de no regresion.",
    "Se fija normalizacion obligatoria para insumos no JSON parseable antes de cualquier propagacion.",
    "Se elevan patrones transferibles: problema, conceptos, evidencia, analisis propio y conclusion juridica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en redaccion, tono y formato.",
    "Alinear la materia a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica de entregables.",
    "Marcar como [supuesto] todo dato no visible en la consigna.",
    "Conservar fuentes heredadas no verificadas como provisionales hasta confirmacion local. [supuesto]",
    "Usar malla-curricular-derecho-unadm.pdf como respaldo curricular verificado."
  ],
  "structure_rules": [
    "Abrir cada producto con encuadre breve del problema juridico o social.",
    "Separar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el producto al tipo solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener trazabilidad entre actividad, .tex y .bib."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante y evitar resumen solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir que bibliografia de semanas posteriores aplica a actividad-1. [supuesto]",
    "Agregar fuentes especificas de actividad solo si son consultables y verificables."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en .tex y entradas en .bib.",
    "Confirmar no regresion de reglas utiles previas en cada ciclo."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "No renombrar claves citadas sin migracion completa.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo anomalos antes de fijarlos como canon. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "Registrar fuentes de actividad en el .bib de la asignatura con metadatos minimos.",
    "No inventar referencias; usar solo obras realmente consultables.",
    "Conservar y deduplicar entradas sin perdida semantica.",
    "Tratar filosofia-del-derecho-clean.bib como insumo tematico puntual, no canon global de materia. [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas por README, programa analitico y .bib local.",
    "Elevar al ancestro patrones editoriales y puertas de calidad, no redaccion literal de actividad.",
    "Mantener etiqueta de compresion union-dedupe lossless en cada salto.",
    "Registrar incidencias de ingesta no parseable como riesgo, sin perder contenido util.",
    "Reutilizar puertas institucionales de calidad en nodos laterales de Derecho."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-1 para cerrar supuestos de formato.",
    "Confirmar nombre canonico final del .bib de materia.",
    "Confirmar si reporte-filosofia-del-derecho-Actividad-1.tex se integra como artefacto canonico de materia.",
    "Completar y verificar la entrada truncada scjnIncapacidadResistencia2019 en .bib local. [supuesto]"
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
      "Conceptos y marco normativo/doctrinal.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos con fundamento juridico y utilidad profesional.",
      "Estandarizar calidad editorial y trazabilidad LaTeX-BibTeX en toda la materia."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable.",
      "Cierre con criterio juridico propio.",
      "Marcado explicito de [supuesto]."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer conceptos y normas pertinentes.",
      "Contrastar evidencia doctrinal y normativa.",
      "Sostener postura propia con citas.",
      "Concluir con aplicabilidad profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofia del Derecho",
        "Hermeneutica e interpretacion juridica",
        "Argumentacion juridica",
        "Derecho y moral",
        "Justicia",
        "Analisis critico del fenomeno juridico",
        "Trazabilidad actividad-.tex-.bib",
        "Normalizacion de insumos no parseables"
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
          "justification": "La interpretacion sustenta la construccion de razones juridicas."
        },
        {
          "source": "Argumentacion juridica",
          "target": "Analisis critico del fenomeno juridico",
          "kind": "develops",
          "justification": "Permite evaluar validez, coherencia y consecuencias."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion exige fundamento verificable."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "Integra el debate entre validez juridica y contenido axiologico."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "Actividad-1: patron problema-conceptos-evidencia-analisis-conclusion.",
        "Regla persistente: bloquear propagacion sin JSON parseable.",
        "Registro de riesgo: salidas no parseables heredadas de Codex y GPT-Pro."
      ]
    },
    "reinforcement_log": [
      "Ciclo 19: se consolidan reglas de actividad-1 en nivel materia sin perdida.",
      "Ciclo 19: se deduplican reglas repetidas y se conserva trazabilidad conceptual.",
      "Ciclo 19: se refuerzan puertas de calidad y normalizacion previa a propagacion.",
      "Ciclo 19: se elevan citas y relaciones reutilizables sin copiar redaccion literal."
    ]
  }
}