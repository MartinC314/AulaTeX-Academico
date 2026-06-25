{
  "summary": [
    "Se consolida memoria lateral de Actividad 4 con deduplicacion lossless y sin recorte util.",
    "Se preserva identidad UnADM, marco curricular y ejes editoriales comunes de Filosofia del Derecho.",
    "Se refuerza regla de normalizacion estructurada y bloqueo por JSON no parseable.",
    "Se transfieren solo patrones reutilizables; no se copian conclusiones ni bibliografia exclusiva de Actividad 1.",
    "Supuesto: la consigna especifica de Actividad 4 no esta visible y debe confirmarse."
  ],
  "identity_rules": [
    "Mantener tono formal academico y precision juridica alineada a UnADM.",
    "Vincular siempre la actividad a Licenciatura en Derecho y Filosofia del Derecho.",
    "Conservar ubicacion curricular: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica documental.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Incluir problema, conceptos, evidencia y postura propia en cada entrega.",
    "Evitar textos solo descriptivos o de resumen.",
    "Sustentar afirmaciones con citas verificables y explicitas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Adaptar nivel de profundidad a la rubrica real de Actividad 4 cuando se confirme."
  ],
  "quality_gates": [
    "Bloquear propagacion si salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Revisar consistencia entre citas en texto y entradas .bib.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Normalizar respuestas no estructuradas heredadas antes de propagar."
  ],
  "latex_rules": [
    "Mantener acentos y codificacion correcta en espanol en .tex y .bib.",
    "Usar solo claves BibTeX existentes en el .bib activo.",
    "No renombrar claves ya citadas en documentos activos sin migracion completa.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y rutas antes de compilar.",
    "Corregir nombres de archivo con caracteres danados detectados en README."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables (UnADM, SCJN, UNAM-IIJ).",
    "Registrar fuentes de actividad en el .bib canonico de la asignatura.",
    "No inventar referencias ni metadatos faltantes.",
    "Conservar metadatos minimos: autor, titulo, ano, editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a interpretacion juridica Semana 7; verificar aplicabilidad a Actividad 4."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Mantener union-dedupe sin eliminar reglas utiles previas.",
    "Transferir a hermanos solo patrones generales de identidad, estructura y calidad.",
    "Evitar arrastrar contenido tematico especifico no confirmado en nodo destino.",
    "Mantener bandera de normalizacion manual para ciclos con salidas historicamente no estructuradas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de Actividad 4: producto, extension y criterios.",
    "Confirmar si Actividad 4 requiere reporte, presentacion u otro formato.",
    "Confirmar rubrica docente especifica para ajustar densidad argumentativa.",
    "Confirmar nombre canonico final del .bib de asignatura tras resolver token Slug.",
    "Confirmar si bibliografia de interpretacion juridica aplica o se requiere .bib incremental propio."
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
        "Entrada canonica en carpeta de asignatura.",
        "Normalizacion estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura Filosofia del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por planeacion.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico y evidencia.",
      "Asegurar trazabilidad editorial y calidad tecnica en cada actividad."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y trazables.",
      "Cita explicita por afirmacion relevante.",
      "Supuestos marcados cuando falte dato local."
    ],
    "argumentative_patterns": [
      "Problematizar primero.",
      "Definir marco conceptual y normativo.",
      "Analizar evidencia con criterio propio.",
      "Fijar postura justificada.",
      "Concluir con aplicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales de Filosofia del Derecho",
        "Integridad academica",
        "Normalizacion estructurada",
        "Validacion JSON",
        "Coherencia problema-evidencia-conclusion"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "README.md de asignatura",
        "programa-analitico-filosofia-del-derecho.md"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Tono y formato academico",
          "kind": "supports",
          "justification": "La pauta editorial exige alineacion institucional explicita."
        },
        {
          "source": "Ejes editoriales de Filosofia del Derecho",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Los cinco ejes ordenan contenido y cierre argumentativo."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay reutilizacion segura."
        },
        {
          "source": "Integridad academica",
          "target": "Conclusion juridica propia",
          "kind": "supports",
          "justification": "La conclusion valida requiere evidencia verificable y postura propia."
        }
      ],
      "evidence": [
        "README establece identidad UnADM, citas verificables y conclusion juridica propia.",
        "Programa analitico define proposito y cinco ejes de trabajo.",
        "Historial de salidas no parseables justifica gate estricto de JSON."
      ]
    },
    "reinforcement_log": [
      "Ciclo 9: deduplicacion aplicada sin perdida de reglas utiles.",
      "Ciclo 9: se refuerza transferencia lateral por patrones, no por contenido especifico.",
      "Ciclo 9: se mantiene control de supuestos por falta de consigna local visible."
    ]
  }
}