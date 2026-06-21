{
  "summary": [
    "Se refuerza sincronizacion transversal con abstracciones estables y sin mezclar contenido tematico de Filosofia del Derecho.",
    "Se conserva identidad UnADM y estructura por ejes para productos juridicos verificables.",
    "Se mantiene compresion lossless por union-dedupe y politica de no regresion.",
    "Se confirma normalizacion obligatoria antes de propagacion recursiva.",
    "Se consolida control de calidad: JSON parseable, soporte verificable y marca de [supuesto]."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Conservar trazabilidad de reglas heredadas provisionales con marca [supuesto].",
    "No sobrescribir reglas validas previas; solo unir y deduplicar.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato y alcance al producto solicitado por planeacion semanal.",
    "Mantener consistencia entre README, programa analitico, reporte y presentacion.",
    "Usar estructura minima verificable: portada, desarrollo, conclusion y referencias."
  ],
  "activity_rules": [
    "Delimitar problema y pregunta guia al inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir hechos, norma, doctrina y opinion propia.",
    "Incluir postura argumentada del estudiante; evitar resumen solo descriptivo.",
    "Verificar coherencia entre objetivo, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar salidas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Comprobar que la compresion aplicada sea union-dedupe sin recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion y acentos correctos en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Normalizar rutas y nombres de archivo antes de compilar.",
    "Resolver tokens o marcadores sin expandir en README y programa analitico si aparecen."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como repositorio bibliografico central.",
    "Priorizar fuentes institucionales UnADM y normas juridicas vigentes verificables.",
    "No inventar referencias; agregar solo fuentes consultables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Verificar que cada cita en LaTeX tenga entrada BibTeX correspondiente."
  ],
  "propagation_hints": [
    "Propagar a nodos laterales solo reglas generales estables de identidad, estructura y calidad.",
    "No transferir redaccion literal ni contenidos tematicos propios de Filosofia del Derecho.",
    "Mantener reglas curriculares especificas solo dentro de la materia destino.",
    "Aplicar propagacion recursiva solo tras validar JSON y gates de calidad.",
    "Preservar alertas historicas de normalizacion manual de ciclos con salida no parseable."
  ],
  "open_questions": [
    "Confirmar si existe rubrica oficial de evaluacion por actividad en esta materia.",
    "Confirmar norma de citacion requerida por docente (APA, ISO o institucional) [supuesto].",
    "Confirmar si el codigo local LDE-S2B1 debe mantenerse como canon en todos los entregables [supuesto].",
    "Confirmar datos faltantes de figura docente en plantillas.",
    "Confirmar si persiste alguna fuente heredada de otra carrera que deba depurarse [supuesto]."
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
        "Normalizacion estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho a la Seguridad Social.",
        "Semestre 2, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Fundamento normativo verificable.",
      "Evidencia pertinente.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables y evaluables.",
      "Asegurar coherencia entre identidad institucional, estructura y evidencia.",
      "Permitir reutilizacion segura por memoria persistente sin regresion."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Separacion clara entre marco, analisis y cierre.",
      "Marcado explicito de [supuesto] cuando falten datos.",
      "Sin inventar fuentes ni hechos."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo.",
      "Exponer marco normativo/doctrinal.",
      "Contrastar evidencia.",
      "Fijar postura sustentada.",
      "Concluir con implicacion practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "JSON parseable",
        "Compresion union-dedupe",
        "Problema juridico",
        "Marco normativo",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024",
        "cpeum2026",
        "lss2026",
        "lissste2026"
      ],
      "relations": [
        {
          "source": "JSON parseable",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay reutilizacion segura."
        },
        {
          "source": "Compresion union-dedupe",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Conserva reglas utiles sin perdida ni duplicacion."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere una pregunta delimitada."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion debe derivar de fundamento verificable."
        }
      ],
      "evidence": [
        "README de materia como canon de estructura local.",
        "Programa analitico con ejes juridicos verificables.",
        ".bib local con base normativa e institucional vigente.",
        "Historial de alertas por salida no parseable y necesidad de normalizacion manual."
      ]
    },
    "reinforcement_log": [
      "Ciclo 41: se transfieren solo abstracciones editoriales estables por relacion transversal.",
      "Ciclo 41: se preservan reglas utiles previas del destino sin eliminacion.",
      "Ciclo 41: se refuerzan gates de calidad y criterio de [supuesto].",
      "Ciclo 41: se evita importar contenido tematico especifico del origen no equivalente."
    ]
  }
}