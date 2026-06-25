{
  "summary": [
    "Se consolida refuerzo lateral ciclo 7 con deduplicacion lossless y sin recorte util.",
    "Se preserva identidad UnADM y contexto local de Derecho a la Seguridad Social.",
    "Se mantiene transferencia por patrones reutilizables: identidad, estructura, calidad, argumentos y trazabilidad.",
    "Se excluye contenido tematico exclusivo del nodo hermano por regla de salto lateral.",
    "Se conserva bloqueo de propagacion ante JSON invalido o salida no estructurada."
  ],
  "identity_rules": [
    "Mantener tono institucional UnADM, formal y juridicamente preciso.",
    "Vincular toda salida a Licenciatura en Derecho y asignatura Derecho a la Seguridad Social.",
    "Usar carpeta de asignatura como entrada canonica de control editorial.",
    "Basar ubicacion curricular en semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Usar README y programa analitico locales como fuentes primarias de identidad."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato y extension al producto pedido en la consigna semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Permitir reporte o presentacion solo si la consigna local lo autoriza."
  ],
  "activity_rules": [
    "Sustentar cada afirmacion con fuente verificable y cita explicita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Verificar correspondencia exacta del producto con Actividad 1 local.",
    "No asumir fuentes de otras semanas sin validacion de pertinencia."
  ],
  "quality_gates": [
    "Bloquear propagacion si no hay JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Rechazar afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Normalizar respuestas no estructuradas antes de reutilizar.",
    "Verificar ajuste del producto a la consigna local de Actividad 1."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables y sin renombres innecesarios.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Verificar nombres canonicos de archivo segun README local.",
    "Usar derecho-a-la-seguridad-social.bib como base canonica local.",
    "Corregir rutas y caracteres anomalos antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y normatividad vigente verificable.",
    "Registrar fuentes especificas de actividad en el .bib local.",
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base y bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir lateralmente solo patrones reutilizables, no contenido exclusivo.",
    "Aplicar analogia controlada: primero identidad y calidad, luego estructura y conceptos.",
    "Preservar reglas utiles previas y agregar solo mejoras verificables.",
    "Si falta consigna local, propagar estructura base y abrir preguntas."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual completa de Actividad 1; confirmar entregable exacto.",
    "Confirmar si formato requerido es reporte, presentacion o mixto.",
    "Confirmar rubrica especifica para calibrar profundidad argumentativa.",
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
        "Control editorial desde la carpeta de asignatura."
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
      "Analisis propio con evidencia.",
      "Postura argumentada.",
      "Cierre profesional transferible."
    ],
    "reason_for_being": [
      "Transformar cada consigna en producto juridico verificable con trazabilidad editorial."
    ],
    "style_markers": [
      "Objetivo puntual al inicio.",
      "Secciones claras y trazables.",
      "Supuestos marcados de forma explicita.",
      "Cierre no meramente descriptivo."
    ],
    "argumentative_patterns": [
      "Problema -> fundamento normativo -> analisis -> evidencia -> conclusion.",
      "Regla general -> contraste contextual -> postura -> implicacion practica.",
      "Pregunta guia -> criterios juridicos -> inferencia razonada."
    ],
    "knowledge_graph": {
      "concepts": [
        "Derecho a la seguridad social",
        "Marco constitucional",
        "Ley del Seguro Social",
        "Ley del ISSSTE",
        "Universalidad",
        "Progresividad",
        "Igualdad y no discriminacion",
        "Acceso, cobertura y justiciabilidad"
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
          "source": "Marco constitucional",
          "target": "Derecho a la seguridad social",
          "kind": "supports",
          "justification": "Proporciona base juridica primaria del derecho."
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
          "justification": "Permite evaluar alcance real y barreras."
        },
        {
          "source": "Progresividad",
          "target": "Acceso, cobertura y justiciabilidad",
          "kind": "supports",
          "justification": "Permite evaluar avances y retrocesos estatales."
        }
      ],
      "evidence": [
        "README local de la asignatura.",
        "Programa analitico local.",
        "derecho-a-la-seguridad-social.bib."
      ]
    },
    "reinforcement_log": [
      "Ciclo 7: deduplicacion integral aplicada en reglas e identidad.",
      "Ciclo 7: se conservaron reglas utiles previas sin eliminacion regresiva.",
      "Ciclo 7: se reforzo transferencia lateral por patrones y no por contenido tematico hermano."
    ]
  }
}