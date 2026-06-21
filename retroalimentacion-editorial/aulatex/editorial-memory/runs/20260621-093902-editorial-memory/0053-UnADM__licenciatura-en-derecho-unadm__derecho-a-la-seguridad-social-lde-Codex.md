{
  "summary": [
    "Se sincroniza ADN editorial transversal sin mezclar contenido tematico de Filosofia del Derecho.",
    "Se preserva identidad UnADM y estructura por ejes como regla estable reutilizable.",
    "Se refuerza control de calidad: JSON parseable, normalizacion previa y compresion union-dedupe sin regresion.",
    "Se mantiene enfoque local de Derecho a la Seguridad Social con fuentes y contexto propios."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local [supuesto].",
    "No sobrescribir reglas validas previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README y programa analitico como canon estructural local.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Organizar desarrollo en: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por la planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y referencias."
  ],
  "activity_rules": [
    "Delimitar problema juridico desde el inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar aguas abajo.",
    "Validar estructura minima completa antes de propagacion recursiva.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que la compresion aplicada sea union-dedupe sin recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion correcta de español en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Corregir rutas, nombres corruptos o tokens sin expandir antes de compilar.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central local.",
    "Priorizar fuentes institucionales y juridicas verificables.",
    "Agregar solo referencias realmente consultables.",
    "No inventar fuentes; marcar faltantes como pendientes [supuesto].",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/editorial o URL.",
    "Distinguir bibliografia base de materia y bibliografia especifica de actividad."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo abstracciones editoriales estables, no redaccion literal.",
    "No transferir contenido tematico propio de Filosofia del Derecho al destino.",
    "Propagar reglas generales de identidad, estructura, calidad y trazabilidad.",
    "Mantener reglas curriculares especificas solo dentro de la materia destino.",
    "Conservar bandera historica: ciclo 1 con salida no parseable requiere normalizacion manual.",
    "Aplicar estrategia progresiva y conservadora: reforzar sin sustituir."
  ],
  "open_questions": [
    "Confirmar rubrica oficial de evaluacion por actividad en esta materia [supuesto].",
    "Confirmar norma de citacion requerida (APA, ISO o institucional juridica) [supuesto].",
    "Confirmar si Actividad 1 requiere reporte, presentacion o ambos.",
    "Confirmar datos faltantes de plantilla (figura docente) cuando existan.",
    "Verificar vigencia de fuentes provisionales heredadas de nodos no equivalentes [supuesto]."
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
      "Evidencia pertinente y trazable.",
      "Analisis propio con postura.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables y utiles profesionalmente.",
      "Sostener continuidad editorial entre actividades, formatos y ciclos sin perdida de reglas utiles."
    ],
    "style_markers": [
      "Frases directas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y cierre.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo y doctrinal.",
      "Contrastar evidencia relevante.",
      "Fijar postura sustentada.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
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
          "justification": "Sin delimitacion del problema no hay analisis juridico consistente."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida exige fundamento legal verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura argumentada requiere respaldo comprobable."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La consolidacion lossless requiere estructura valida."
        }
      ],
      "evidence": [
        "README local define estructura canonica de archivos y control editorial.",
        "Programa analitico local define proposito y ejes juridicos de la materia.",
        "Archivo .bib local contiene base institucional y normativa verificable.",
        "Historial institucional registra salidas no parseables y exige normalizacion previa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 53: se transfieren solo abstracciones estables desde actividad de otra materia.",
      "Ciclo 53: se preservan reglas previas del destino y se deduplican sin recorte.",
      "Ciclo 53: se refuerza gate de JSON parseable como requisito de propagacion recursiva.",
      "Ciclo 53: se mantiene separacion entre identidad editorial comun y contenido tematico local."
    ]
  }
}