{
  "summary": [
    "Se sincroniza ADN editorial transversal sin mezclar contenido tematico de Filosofia del Derecho.",
    "Se preservan reglas utiles del destino y se agregan abstracciones estables del origen.",
    "Se mantiene compresion lossless por union-dedupe y sin regresion.",
    "Se refuerza patron comun: problema, conceptos/norma, evidencia, analisis propio y conclusion juridica.",
    "Se conserva alerta institucional: bloquear propagacion si no hay JSON parseable."
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
    "Tomar README y programa analitico como canon estructural local.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Organizar en secciones reutilizables: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato y alcance al producto solicitado por la planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y actividad."
  ],
  "activity_rules": [
    "Delimitar problema juridico al inicio de cada entrega.",
    "Distinguir hechos, conceptos, normas y opinion propia.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Evitar entregas solo descriptivas.",
    "Incluir postura argumentada del estudiante.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de propagar recursivamente.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Verificar que la compresion aplicada sea union-dedupe y no recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion correcta para espanol en .tex y .bib.",
    "Mantener metadatos institucionales y del curso consistentes.",
    "Evitar comandos no estandar sin justificacion tecnica.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir rutas, nombres corruptos o tokens sin expandir antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales UnADM y normas juridicas verificables.",
    "Agregar solo referencias consultables y verificables.",
    "No inventar fuentes.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar a laterales solo abstracciones editoriales estables.",
    "No transferir redaccion literal ni contenido tematico especifico de otra materia.",
    "Propagar reglas curriculares del destino solo dentro de esta materia.",
    "Propagar reglas generales de identidad, calidad, JSON y citas a nodos compatibles.",
    "Mantener bandera de riesgo por antecedentes de salida no parseable en ciclos previos."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida por la materia (APA, ISO, institucional o juridica mexicana) [supuesto].",
    "Confirmar si todas las actividades usan reporte, presentacion o ambos formatos.",
    "Confirmar si existe rubrica oficial por actividad para ajustar profundidad argumentativa.",
    "Confirmar dato oficial de figura docente para completar plantilla [supuesto]."
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
      "Resolver consignas con problema juridico claro.",
      "Fundamentar en marco normativo y doctrinal verificable.",
      "Sostener postura propia con evidencia.",
      "Cerrar con utilidad juridica profesional.",
      "Conservar trazabilidad y control de supuestos."
    ],
    "reason_for_being": [
      "Convertir cada consigna en producto juridico verificable y evaluable.",
      "Garantizar continuidad editorial entre actividades sin perder contexto local.",
      "Asegurar calidad tecnica de salida para propagacion segura."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiqueta [supuesto] cuando falte confirmacion.",
      "Separacion explicita entre marco, analisis y cierre.",
      "Sin duplicados y sin regresion de reglas utiles."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer conceptos y marco normativo aplicable.",
      "Contrastar evidencia relevante.",
      "Fijar postura propia sustentada.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema juridico",
        "Marco normativo/doctrinal",
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
          "justification": "El analisis requiere una pregunta delimitada."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida depende de fundamento verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Postura argumentada",
          "kind": "supports",
          "justification": "La postura gana solidez con fuentes comprobables."
        },
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
          "justification": "Conserva reglas utiles sin perdida."
        }
      ],
      "evidence": [
        "README local define estructura canonica y artefactos base.",
        "Programa analitico local define proposito y ejes de trabajo.",
        "Archivo .bib local contiene base normativa e institucional verificable.",
        "Historial institucional confirma gate de JSON parseable y normalizacion manual."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas de identidad, estructura y calidad.",
      "Se transfirieron solo abstracciones estables desde nodo transversal no equivalente.",
      "Se excluyo contenido tematico especifico de Filosofia del Derecho por no equivalencia de materia.",
      "Se mantuvo el nucleo local de Seguridad Social como contexto principal.",
      "Se reforzo control de supuestos y trazabilidad de fuentes provisionales."
    ]
  }
}