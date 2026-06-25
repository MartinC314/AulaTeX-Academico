{
  "summary": [
    "Se consolida sincronizacion transversal sin trasladar contenido tematico de Filosofia del Derecho.",
    "Se preservan reglas institucionales UnADM, normalizacion estructurada y compresion lossless por union-dedupe.",
    "Se refuerzan ejes editoriales reutilizables: problema, conceptos o normas, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene incidente historico de salidas no JSON parseables como gate activo hasta verificacion de cierre.",
    "Se confirma contexto local de materia destino: semestre 6, bloque 2, obligatoria, 8 creditos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de asignatura: Derecho de la contratacion internacional.",
    "Vincular entregas a Licenciatura en Derecho.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "Conservar trazabilidad de origen de reglas heredadas.",
    "Conservar coursecode local LDE-S6B2 cuando aplique plantilla actual."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto pedido por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "No eliminar reglas utiles previas; solo anexar mejoras verificables.",
    "Corregir placeholders y rutas corruptas de README y programa antes de reutilizar.",
    "Usar derecho-de-la-contratacion-internacional.bib como repositorio principal de la materia."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Diferenciar resumen descriptivo de postura propia.",
    "Vincular argumentos con norma, doctrina o evidencia verificable.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Declarar limites del analisis cuando falten datos.",
    "No asumir fuentes de semanas posteriores sin confirmacion de consigna.",
    "Incluir conclusion juridica aplicable a practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de propagar.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que toda afirmacion normativa tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna local.",
    "Verificar que nombres de archivos en README coincidan con archivos reales."
  ],
  "latex_rules": [
    "Mantener clase article en espanol con letterpaper y oneside si la plantilla local la usa.",
    "Conservar macros institucionales de curso, universidad y autor.",
    "Completar documenttitle y documentsubtitle segun actividad real.",
    "Evitar paquetes o comandos no estandar sin justificacion verificable.",
    "Compilar sin errores criticos, sin referencias rotas y con acentos correctos.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo obras consultables.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos aplicables.",
    "Agregar fuentes especificas de cada actividad al .bib local.",
    "No citar fuentes heredadas si no fueron usadas en actividad destino.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente o URL.",
    "Incluir fecha de consulta en recursos web o mutables.",
    "Distinguir bibliografia base de bibliografia especifica de actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Compartir entre nodos no equivalentes solo abstracciones editoriales estables.",
    "No sobrescribir reglas locales mas especificas con reglas institucionales generales.",
    "Mantener aviso historico de incidente JSON hasta evidencia de resolucion.",
    "Aplicar deduplicacion semantica por regla, no por recorte destructivo.",
    "Si falta consigna local, propagar solo reglas generales de calidad e identidad."
  ],
  "open_questions": [
    "Confirmar si el incidente de JSON no parseable ya quedo cerrado en este ciclo.",
    "Definir formato uniforme de citas juridicas para norma, jurisprudencia y doctrina.",
    "Confirmar checklist minimo por tipo de actividad: reporte, presentacion y visual.",
    "Confirmar planeacion oficial de actividades por semana para esta materia.",
    "Supuesto: deben corregirse entradas corruptas de README (reporte/referencias) y placeholder de .bib."
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
        "Semestre 6, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Derecho de la contratacion internacional."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto alineado a planeacion.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos claros, fundados y verificables.",
      "Asegurar trazabilidad editorial, calidad formal y utilidad profesional del cierre juridico."
    ],
    "style_markers": [
      "Supuestos explicitos cuando falte evidencia local.",
      "Separacion clara entre descripcion y argumentacion propia.",
      "Cierre con criterio juridico aplicable.",
      "Trazabilidad de herencia y verificabilidad de fuentes."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual o normativo -> evidencia -> analisis -> conclusion.",
      "Afirmacion juridica -> cita verificable -> interpretacion propia.",
      "Consigna local -> producto alineado -> validacion final de coherencia."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Compresion lossless por deduplicacion",
        "Problema juridico",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion juridica",
        "Bibliografia verificable",
        "Trazabilidad de herencia"
      ],
      "citations": [
        "unadmMallaDerecho2024",
        "unadmSitioWeb"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON valido no hay reutilizacion segura."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El analisis se organiza desde una pregunta juridica concreta."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion juridica",
          "kind": "supports",
          "justification": "La conclusion requiere sustento verificable."
        },
        {
          "source": "Compresion lossless por deduplicacion",
          "target": "Trazabilidad de herencia",
          "kind": "supports",
          "justification": "Conserva reglas utiles sin perdida de memoria editorial."
        }
      ],
      "evidence": [
        "README de materia con identidad UnADM y ubicacion curricular.",
        "Programa analitico con proposito y ejes de trabajo.",
        "Bib local canonico de la asignatura.",
        "Registro historico de salidas no JSON parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 9: se mantuvo union-dedupe lossless y no regresion.",
      "Ciclo 9: se reforzaron gates JSON y normalizacion previa a propagacion.",
      "Ciclo 9: se transfirieron solo abstracciones estables, sin arrastre tematico de la materia origen.",
      "Ciclo 9: se preservo identidad local de Derecho de la contratacion internacional con trazabilidad transversal."
    ]
  }
}