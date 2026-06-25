{
  "summary": [
    "Sincronizacion transversal consolidada entre actividad origen y materia destino.",
    "Se preservan reglas utiles vigentes sin regresion.",
    "Se refuerzan ejes estables: problema, conceptos o normas, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene normalizacion obligatoria antes de propagar.",
    "Se corrigen abstracciones de plantilla no expandida como riesgo editorial recurrente.",
    "Se conserva enfoque juridico-laboral local del destino.",
    "Supuesto: no se cuenta con consignas especificas por actividad en esta sincronizacion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Vincular toda entrega a Licenciatura en Derecho y a la materia destino.",
    "Usar contexto curricular verificado del destino: semestre 7, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna o evidencia local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada producto a la consigna y planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Normalizar nombres y rutas antes de canonizarlos."
  ],
  "activity_rules": [
    "Contextualizar cada actividad en conflicto o situacion laboral verificable.",
    "Sustentar afirmaciones con norma, doctrina o datos verificables.",
    "Incluir postura argumentada del estudiante; evitar solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No transferir contenido literal de otras materias sin validar pertinencia local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad de citas y ausencia de fuentes inventadas.",
    "Validar consistencia entre texto, .bib, README y programa analitico.",
    "Detectar y corregir marcadores de plantilla sin expandir.",
    "Marcar como supuesto cualquier afirmacion sin respaldo verificable."
  ],
  "latex_rules": [
    "Usar plantilla .tex local como base por actividad.",
    "Mantener codificacion y acentos correctos en espanol en .tex y .bib.",
    "Completar metadatos reales de actividad antes de compilar.",
    "Mantener macros institucionales estables.",
    "Compilar sin errores criticos, sin referencias rotas y con entornos cerrados.",
    "Resolver tokens sin expandir en nombres de archivo y referencias."
  ],
  "bibliography_rules": [
    "Centralizar bibliografia local en derecho-laboral-y-relaciones-laborales.bib.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Agregar solo entradas BibTeX verificables y pertinentes.",
    "No inventar referencias, jurisprudencia, doctrina ni URLs.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Marcar como supuesto metadatos faltantes."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Compartir entre nodos no equivalentes solo abstracciones editoriales estables.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Aplicar deduplicacion semantica lossless por union; no recortar reglas utiles.",
    "Corregir primero artefactos de plantilla antes de nueva propagacion."
  ],
  "open_questions": [
    "Confirmar formato de cita juridica exigido por docente.",
    "Confirmar si autor en plantilla es fijo institucional o variable por alumno.",
    "Confirmar rubrica oficial por actividad para convertirla en checklist.",
    "Confirmar nombres canonicos finales de artefactos y carpeta de referencias.",
    "Supuesto: falta mapa de actividades del destino con consignas textuales."
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
        "Normalizacion obligatoria de salidas no estructuradas."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Derecho laboral y relaciones laborales.",
        "Semestre 7, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables.",
      "Asegurar coherencia entre consigna, evidencia y conclusion.",
      "Sostener calidad editorial reutilizable en propagacion recursiva."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Supuestos marcados de forma explicita.",
      "Evitar literalidad heredada entre materias.",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Definir conceptos y norma aplicable.",
      "Contrastar evidencia.",
      "Sostener postura propia.",
      "Concluir con aplicacion profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema juridico laboral",
        "Marco normativo o doctrinal",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Normalizacion de salidas no parseables"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad institucional exige trazabilidad y rigor de fuentes."
        },
        {
          "source": "Problema juridico laboral",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitacion del problema no hay argumentacion pertinente."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida requiere fundamento juridico verificable."
        },
        {
          "source": "Normalizacion de salidas no parseables",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Evita contaminar nodos con memoria defectuosa."
        }
      ],
      "evidence": [
        "README de materia con identidad y ubicacion curricular.",
        "Programa analitico con ejes de trabajo y proposito.",
        "Bibliografia local con claves institucionales verificables.",
        "Registro historico de salidas no parseables que exige normalizacion previa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 9: se transfiere solo abstraccion estable desde Filosofia del Derecho.",
      "Ciclo 9: se conserva ADN previo del destino sin eliminar reglas utiles.",
      "Ciclo 9: se refuerza gate de JSON parseable y normalizacion obligatoria.",
      "Ciclo 9: se mantiene compresion lossless por deduplicacion semantica."
    ]
  }
}