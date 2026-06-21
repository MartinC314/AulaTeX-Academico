{
  "summary": [
    "Se consolida sincronizacion transversal entre nodos no equivalentes con reglas editoriales estables.",
    "Se preserva identidad UnADM y enfoque juridico del destino sin mezclar contenido tematico de Filosofia del Derecho.",
    "Se refuerza patron reusable: problema, fundamento, evidencia, analisis propio y conclusion juridica transferible.",
    "Se mantiene compresion lossless por union-dedupe y politica sin regresion.",
    "Se mantiene alerta institucional por salidas no parseables historicas y exigencia de normalizacion previa."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar.",
    "No propagar datos personales de plantilla a nodos laterales salvo requerimiento explicito [supuesto]."
  ],
  "structure_rules": [
    "Tomar README y programa analitico del destino como canon estructural local.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Organizar en secciones: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato y alcance al producto solicitado en planeacion semanal.",
    "Mantener consistencia editorial entre reporte y presentacion.",
    "Usar estructura minima verificable: portada, desarrollo, conclusion y referencias.",
    "Normalizar nombres de archivo cuando existan marcadores corruptos o tokens sin expandir."
  ],
  "activity_rules": [
    "Delimitar problema juridico desde el inicio.",
    "Vincular desarrollo con normas, doctrina, datos o jurisprudencia pertinentes al tema.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir hechos, conceptos, normas y opinion propia.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica aplicable a la practica profesional.",
    "No asumir fuentes de semanas distintas sin confirmacion local [supuesto]."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar manualmente toda respuesta no estructurada antes de reutilizar.",
    "Validar estructura minima completa antes de propagar recursivamente.",
    "Confirmar que toda afirmacion relevante tenga respaldo o etiqueta [supuesto].",
    "Comprobar consistencia entre citas en texto y archivo .bib local.",
    "Verificar correspondencia entre producto entregado y consigna vigente.",
    "Verificar que la compresion aplicada sea union-dedupe y no recorte.",
    "Verificar que no se eliminen reglas utiles previas."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion y acentos correctos en .tex y .bib.",
    "Mantener metadatos institucionales y de curso consistentes en todos los .tex.",
    "Evitar comandos no estandar sin justificacion editorial o tecnica.",
    "Compilar sin errores criticos, sin referencias rotas y sin claves faltantes.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Verificar rutas y nombres de archivo contra README antes de referenciar.",
    "Resolver tokens sin expandir en nombres de archivo antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central del destino.",
    "Priorizar fuentes institucionales UnADM y normatividad mexicana vigente verificable.",
    "Agregar solo referencias realmente consultables y pertinentes a la actividad.",
    "No inventar referencias; marcar faltantes como pendientes o [supuesto].",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/editorial o URL.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "Verificar que cada cita en LaTeX tenga su entrada BibTeX correspondiente."
  ],
  "propagation_hints": [
    "Propagar a laterales solo abstracciones estables: identidad, estructura reusable, gates y grafo conceptual.",
    "No transferir redaccion literal ni contenido tematico especifico de Filosofia al destino.",
    "Mantener reglas curriculares especificas del destino solo dentro de su materia.",
    "Propagar reglas generales de JSON, integridad academica y control bibliografico a nodos compatibles.",
    "Aplicar estrategia progresiva y conservadora: agregar mejoras verificables sin borrar reglas vigentes.",
    "Conservar bandera historica de riesgo por ciclos con salida no parseable."
  ],
  "open_questions": [
    "Confirmar si sigue vigente la fuente provisional heredada desde ingenieria para este destino [supuesto].",
    "Confirmar norma de citacion exigida por la materia: APA, ISO, institucional o juridica mexicana [supuesto].",
    "Confirmar datos oficiales de figura docente para completar portada.",
    "Confirmar si todas las actividades requieren reporte, presentacion o ambos productos.",
    "Confirmar si existen lineamientos locales adicionales de jurisprudencia obligatoria por actividad."
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
      "Identidad institucional consistente.",
      "Problema juridico claramente delimitado.",
      "Fundamento normativo verificable.",
      "Evidencia y citas trazables.",
      "Analisis propio con postura.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar consignas en productos juridicos verificables y utiles para practica profesional.",
      "Asegurar calidad reproducible mediante estructura canonica y control de evidencia.",
      "Permitir propagacion segura por JSON valido y compresion lossless."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Separacion explicita entre marco, analisis y cierre.",
      "Etiquetado visible de [supuesto].",
      "Cierre con implicacion juridica practica."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo.",
      "Exponer marco normativo y doctrinal.",
      "Contrastar evidencia pertinente.",
      "Sostener postura propia.",
      "Concluir con efecto juridico aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Problema juridico",
        "Marco normativo",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "JSON parseable",
        "Compresion union-dedupe"
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
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitacion del problema no hay argumentacion valida."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion exige base legal verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura requiere sustento documental."
        },
        {
          "source": "JSON parseable",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "La reutilizacion segura depende de estructura valida."
        },
        {
          "source": "Compresion union-dedupe",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Preserva reglas utiles sin perdida ni duplicados."
        }
      ],
      "evidence": [
        "README del destino define estructura canonica y artefactos base.",
        "Programa analitico del destino define proposito y ejes juridicos.",
        "Bib local del destino contiene fuentes institucionales y normativas verificables.",
        "Historial institucional registra incidentes de salida no parseable y exige normalizacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 55: se transfiere solo abstraccion estable desde actividad de Filosofia hacia materia de Seguridad Social.",
      "Se refuerzan reglas transversales de identidad, estructura, calidad y bibliografia.",
      "Se preservan reglas locales del destino y se evita contaminacion tematica entre materias.",
      "Se mantiene politica de compresion lossless por union-dedupe sin regresion."
    ]
  }
}