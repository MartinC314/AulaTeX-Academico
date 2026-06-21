{
  "summary": [
    "Consolidar memoria de materia con abstraccion ascendente desde actividad-1.",
    "Preservar reglas utiles previas sin regresion y con union-dedupe lossless.",
    "Mantener normalizacion obligatoria para insumos no JSON parseable.",
    "Fijar ejes editoriales transferibles: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Mantener trazabilidad entre consigna, producto .tex y respaldo .bib."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y criterios de evaluacion.",
    "Alinear la materia a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local. [supuesto]",
    "Conservar referencia institucional a malla-curricular-derecho-unadm.pdf como respaldo curricular."
  ],
  "structure_rules": [
    "Abrir cada entrega con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en secciones: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear formato final al producto pedido por la planeacion semanal.",
    "Mantener trazabilidad entre actividad, archivo .tex y archivo .bib."
  ],
  "activity_rules": [
    "Evitar entregas solo descriptivas o de resumen.",
    "Incluir postura argumentada del estudiante en cada actividad.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Agregar fuentes especificas de actividad solo si son consultables y pertinentes.",
    "No asumir que bibliografia de semanas posteriores aplica automaticamente a actividad-1. [supuesto]"
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar memoria.",
    "Normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en .tex y entradas en .bib.",
    "Verificar correspondencia del producto con la consigna especifica de la actividad."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en espanol para .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "No renombrar claves citadas sin migracion completa.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, sin citas ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "No inventar referencias; usar solo obras realmente consultables.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Registrar en .bib de materia las fuentes nuevas realmente usadas en .tex.",
    "Tratar filosofia-del-derecho-clean.bib como insumo tematico de Semana 7 hasta confirmacion de alcance para actividad-1. [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas por README, programa analitico y .bib local.",
    "Elevar al ancestro patrones reutilizables, no redaccion literal de una actividad.",
    "Conservar trazabilidad de citas recurrentes y llaves bibliograficas estables.",
    "Reforzar puertas de calidad institucional en nodos laterales y superiores.",
    "Registrar incidencias de ingesta no parseable como riesgo, sin perder contenido util.",
    "Mantener etiqueta de compresion union-dedupe lossless en ciclos siguientes."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-1 para fijar producto obligatorio.",
    "Confirmar nombre canonico final del archivo .bib de la materia.",
    "Confirmar si actividad-1 reutiliza bibliografia existente o requiere .bib propio.",
    "Completar y verificar campos faltantes de scjnIncapacidadResistencia2019. [supuesto]",
    "Corregir nombres con caracteres anom alos y placeholders en README/programa analitico. [supuesto]"
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
      "Conceptos, normas, doctrina y datos pertinentes.",
      "Evidencia verificable y trazable.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos solidos.",
      "Asegurar fundamento juridico, claridad y aplicabilidad profesional.",
      "Sostener continuidad editorial entre actividades, materia y programa."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable y funcional.",
      "Criterio juridico propio en el cierre.",
      "Marcado explicito de supuestos.",
      "Trazabilidad tecnica entre .tex y .bib."
    ],
    "argumentative_patterns": [
      "Delimitar problema antes de exponer teoria.",
      "Vincular marco conceptual con marco normativo.",
      "Sustentar cada afirmacion sustantiva con evidencia.",
      "Pasar de descripcion a valoracion critica.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofia del Derecho",
        "Hermeneutica e interpretacion juridica",
        "Argumentacion juridica",
        "Derecho y moral",
        "Justicia",
        "Analisis critico del fenomeno juridico",
        "Conclusiones juridicas transferibles"
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
          "justification": "La interpretacion aporta criterios para construir razones juridicas."
        },
        {
          "source": "Argumentacion juridica",
          "target": "Analisis critico del fenomeno juridico",
          "kind": "develops",
          "justification": "Permite evaluar validez, coherencia y consecuencias."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "Integra debate axiologico y normativo en la formacion juridica."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion exige sustento verificable."
        }
      ],
      "evidence": [
        "README de materia: identidad, estructura y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "Bib local: llaves recurrentes para hermeneutica, argumentacion y marco normativo.",
        "Memoria de actividad-1: patron problema-conceptos-evidencia-analisis-conclusion."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin perdida semantica.",
      "Se conservaron controles de calidad heredados de nivel institucional.",
      "Se elevaron patrones reutilizables del hijo al ancestro.",
      "Se mantuvo trazabilidad de citas recurrentes y riesgos de ingesta.",
      "Se reforzo la regla de normalizacion previa a toda propagacion."
    ]
  }
}