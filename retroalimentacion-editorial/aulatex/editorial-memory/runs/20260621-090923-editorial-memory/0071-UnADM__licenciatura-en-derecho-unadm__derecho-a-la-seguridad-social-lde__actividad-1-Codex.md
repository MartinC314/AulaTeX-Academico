{
  "summary": [
    "Se consolida refuerzo lateral con transferencia solo de patrones reutilizables.",
    "Se preserva identidad UnADM y contexto local verificado en README y programa analitico.",
    "Se mantiene compresion lossless por deduplicacion sin recorte de reglas utiles.",
    "Se fija secuencia editorial estable: problema, fundamento, analisis, evidencia, postura y cierre.",
    "Se mantiene bloqueo de propagacion ante JSON invalido o salida no estructurada."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho y Derecho a la Seguridad Social.",
    "Basar ubicacion curricular en semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Usar README y programa analitico locales como fuentes primarias.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto pedido en la consigna semanal.",
    "Permitir reporte o presentacion segun instruccion local.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Sustentar cada afirmacion con fuente verificable y cita explicita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Verificar correspondencia exacta con consigna de Actividad 1.",
    "No asumir fuentes de otras semanas sin validacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si no hay JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Rechazar afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Normalizar respuestas no estructuradas antes de reutilizar.",
    "Verificar ajuste del producto a consigna local de Actividad 1."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Verificar nombres canonicos de archivo segun README local.",
    "Usar derecho-a-la-seguridad-social.bib como base canonica local.",
    "Corregir rutas o caracteres anomalos antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y normatividad vigente verificable.",
    "Registrar fuentes especificas de actividad en el .bib local.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Usar cpeum2026, lss2026 y lissste2026 solo cuando la consigna lo requiera."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir lateralmente solo identidad, estructura, calidad y patrones argumentativos.",
    "No copiar redaccion literal, conclusiones ni bibliografia exclusiva entre nodos hermanos.",
    "Aplicar analogia controlada: primero reglas institucionales y calidad, luego estructura y conceptos.",
    "Preservar reglas utiles previas y sumar solo mejoras verificables."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual completa de Actividad 1; confirmar entregable exacto.",
    "Confirmar si el formato requerido es reporte, presentacion o mixto.",
    "Confirmar rubrica especifica de evaluacion para calibrar profundidad.",
    "Confirmar fuentes obligatorias de la semana en planeacion local.",
    "Confirmar si se exige jurisprudencia especifica en esta actividad."
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
        "Carpeta de asignatura como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Derecho a la Seguridad Social.",
        "Semestre 2, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Fundamento normativo verificable.",
      "Analisis propio con postura.",
      "Evidencia trazable.",
      "Cierre profesional transferible."
    ],
    "reason_for_being": [
      "Transformar cada consigna en producto juridico verificable sin perder identidad institucional.",
      "Asegurar consistencia entre consigna, argumentacion y evidencia.",
      "Habilitar propagacion segura por reglas y no por texto literal."
    ],
    "style_markers": [
      "Objetivo puntual al inicio.",
      "Secciones claras y trazables.",
      "Supuestos marcados de forma explicita.",
      "Postura personal sustentada.",
      "Conclusion no descriptiva y aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> fundamento normativo -> analisis -> evidencia -> conclusion.",
      "Regla general -> contraste contextual -> postura -> implicacion practica.",
      "Pregunta guia -> criterio juridico -> inferencia razonada."
    ],
    "knowledge_graph": {
      "concepts": [
        "Derecho a la seguridad social",
        "Marco constitucional en Mexico",
        "Ley del Seguro Social",
        "Ley del ISSSTE",
        "Universalidad",
        "Progresividad",
        "Igualdad y no discriminacion",
        "Acceso, cobertura y justiciabilidad",
        "Calidad editorial verificable"
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
          "source": "Marco constitucional en Mexico",
          "target": "Derecho a la seguridad social",
          "kind": "supports",
          "justification": "Define base juridica del derecho en el curso."
        },
        {
          "source": "Ley del Seguro Social",
          "target": "Derecho a la seguridad social",
          "kind": "develops",
          "justification": "Operativiza prestaciones y mecanismos del regimen."
        },
        {
          "source": "Ley del ISSSTE",
          "target": "Derecho a la seguridad social",
          "kind": "develops",
          "justification": "Regula cobertura para personas servidoras publicas."
        },
        {
          "source": "Universalidad",
          "target": "Acceso, cobertura y justiciabilidad",
          "kind": "supports",
          "justification": "Permite evaluar alcance real y brechas."
        },
        {
          "source": "Progresividad",
          "target": "Acceso, cobertura y justiciabilidad",
          "kind": "supports",
          "justification": "Permite analizar avances y retrocesos estatales."
        },
        {
          "source": "Calidad editorial verificable",
          "target": "Propagacion recursiva segura",
          "kind": "depends_on",
          "justification": "Sin JSON valido y estructura minima no hay transferencia confiable."
        }
      ],
      "evidence": [
        "README local de la asignatura.",
        "Programa analitico local de Derecho a la Seguridad Social.",
        "Archivo derecho-a-la-seguridad-social.bib.",
        "Reglas de control: JSON parseable, estructura minima y trazabilidad de citas."
      ]
    },
    "reinforcement_log": [
      "Ciclo 71: deduplicacion integral aplicada sin eliminar reglas utiles previas.",
      "Ciclo 71: se refuerza transferencia lateral por patrones y no por contenido tematico exclusivo.",
      "Ciclo 71: se mantiene politica de supuestos explicitos ante faltantes de consigna."
    ]
  }
}