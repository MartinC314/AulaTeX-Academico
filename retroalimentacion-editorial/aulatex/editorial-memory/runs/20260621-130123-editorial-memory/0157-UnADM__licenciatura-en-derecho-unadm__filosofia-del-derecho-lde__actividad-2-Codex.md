{
  "summary": [
    "Se consolida actividad-2 con transferencia lateral desde actividad-1 sin copiar contenido exclusivo.",
    "Se preservan reglas institucionales UnADM, estructura troncal y controles de calidad ya validados.",
    "Se refuerza normalizacion obligatoria de salidas no estructuradas antes de propagacion recursiva.",
    "Se mantiene compresion lossless por union y deduplicacion.",
    "Se incorporan supuestos explicitos cuando falta consigna local de actividad-2."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular actividad-2 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Mantener enfoque academico-juridico con transferencia a practica profesional."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto solicitado por la planeacion semanal.",
    "Diferenciar postura propia, cita textual y parafrasis.",
    "Cerrar con conclusion juridica transferible."
  ],
  "activity_rules": [
    "Ajustar actividad-2 a instruccion docente disponible.",
    "Evitar asumir tema, semana o formato sin evidencia local.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Mantener integridad academica en todo producto."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de reutilizar.",
    "Verificar que cada afirmacion sustantiva tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No eliminar reglas utiles previas; solo unir y deduplicar."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en espanol en .tex y .bib.",
    "Mantener compatibilidad entre claves citadas en .tex y entradas .bib.",
    "No renombrar claves bibliograficas ya citadas sin necesidad.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en README y referencias de archivo."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y malla curricular como base contextual.",
    "Agregar fuentes especificas de actividad-2 en el .bib canonico de la asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Tratar filosofia-del-derecho-clean.bib como complemento tematico, no reemplazo automatico del .bib canonico [supuesto].",
    "Usar entradas de hermeneutica/argumentacion solo si la consigna de actividad-2 lo requiere."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir a nodos hermanos solo patrones reutilizables, no conclusiones especificas.",
    "Mantener historial de fuentes provisionales como antecedente, no como verdad canonica.",
    "Aplicar union-dedupe lossless en cada ciclo para evitar regresiones.",
    "Si falta consigna local, propagar estructura base y abrir preguntas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-2: tema, semana y producto.",
    "Confirmar si el producto final es reporte, presentacion u otro formato.",
    "Confirmar rubrica de evaluacion especifica para calibrar profundidad argumentativa.",
    "Confirmar nombre canonico final del .bib de la asignatura.",
    "Confirmar si existe estilo de citacion institucional obligatorio.",
    "Confirmar si las fuentes de interpretacion juridica aplican a actividad-2 o solo a semana 7 [supuesto actual]."
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
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Filosofia del Derecho."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y fuentes pertinentes.",
      "Producto segun planeacion.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables academicos trazables y verificables.",
      "Sostener coherencia entre identidad institucional, evidencia y argumento propio."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales y trazables.",
      "Cierre con criterio juridico propio.",
      "Supuestos marcados de forma explicita."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> analisis -> conclusion.",
      "Afirmacion juridica -> respaldo verificable -> interpretacion propia.",
      "Consigna local -> adecuacion de formato -> verificacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion de salidas",
        "Ejes editoriales troncales",
        "Trazabilidad cita-bibliografia",
        "Integridad academica",
        "Transferencia lateral controlada"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/programa-analitico-filosofia-del-derecho.md"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Ejes editoriales troncales",
          "kind": "supports",
          "justification": "Define tono, formato y finalidad comun."
        },
        {
          "source": "Normalizacion de salidas",
          "target": "Transferencia lateral controlada",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay propagacion segura."
        },
        {
          "source": "Trazabilidad cita-bibliografia",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Permite verificar respaldo de afirmaciones."
        },
        {
          "source": "Ejes editoriales troncales",
          "target": "Actividad-2",
          "kind": "develops",
          "justification": "Son patrones reutilizables entre nodos hermanos."
        }
      ],
      "evidence": [
        "README fija identidad UnADM e integridad academica.",
        "Programa analitico define proposito y ejes de trabajo.",
        "Regla persistente: bloquear propagacion sin JSON parseable.",
        "Transferencia entre hermanos exige deduplicacion lossless y no copia literal."
      ]
    },
    "reinforcement_log": [
      "Ciclo 18: se mantiene ADN institucional sin regresion.",
      "Ciclo 18: se refuerza regla de transferencia por patrones reutilizables.",
      "Ciclo 18: se consolidan gates de JSON, supuestos y trazabilidad bibliografica.",
      "Ciclo 18: se preserva caracter provisional de fuentes heredadas no verificadas."
    ]
  }
}