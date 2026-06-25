{
  "summary": [
    "Se consolida refuerzo lateral desde Actividad 1 hacia Actividad 4 sin copiar contenido específico.",
    "Se preserva identidad UnADM y ubicación curricular verificable: semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Se mantiene normalización estructurada obligatoria y bloqueo por JSON no parseable.",
    "Se refuerzan ejes editoriales reutilizables: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Supuesto: falta consigna textual local de Actividad 4; se conserva estructura base y preguntas abiertas."
  ],
  "identity_rules": [
    "Mantener tono formal académico y precisión jurídica.",
    "Alinear toda salida con UnADM y Licenciatura en Derecho.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validación local.",
    "Conservar integridad académica con trazabilidad de fuentes."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto final a la planeación semanal y a la consigna vigente.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Separar hechos, conceptos, argumentos y postura personal."
  ],
  "activity_rules": [
    "Evitar entregas solo descriptivas; incluir postura argumentada propia.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Adaptar Actividad 4 a los cinco ejes del programa analítico.",
    "No trasladar conclusiones específicas de Actividad 1 a Actividad 4.",
    "Usar solo patrones reutilizables entre actividades hermanas."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de reutilizar aguas abajo.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Normalizar salidas no estructuradas heredadas antes de propagación recursiva.",
    "Verificar correspondencia del producto con la consigna específica de Actividad 4."
  ],
  "latex_rules": [
    "Usar acentos y codificación correcta en español en .tex y .bib.",
    "Citar en .tex solo claves existentes en .bib.",
    "No renombrar claves BibTeX ya usadas en documentos activos.",
    "Compilar sin errores críticos, sin referencias rotas y sin tokens sin expandir.",
    "Verificar nombres reales de archivo cuando README tenga plantilla sin resolver.",
    "Evitar comandos no estándar sin justificación editorial."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y jurídicas verificables.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Registrar fuentes de Actividad 4 en el .bib canónico de la asignatura.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a interpretación jurídica; validar si aplica a Actividad 4."
  ],
  "propagation_hints": [
    "Propagar lateral y recursivamente solo tras validación JSON y estructura.",
    "Aplicar deduplicación lossless por unión semántica sin recorte.",
    "Preservar reglas útiles previas y evitar regresiones editoriales.",
    "Transferir solo identidad, estructura, calidad y patrones argumentativos reutilizables.",
    "Si faltan datos locales, propagar plantilla base más preguntas abiertas.",
    "Mantener bandera de normalización manual para ciclos con antecedentes no estructurados."
  ],
  "open_questions": [
    "Confirmar consigna exacta de Actividad 4: producto, extensión y rúbrica.",
    "Confirmar si Actividad 4 requiere reporte, presentación u otro formato.",
    "Confirmar nombre canónico final del .bib por plantilla Slug no resuelta en README.",
    "Confirmar si se reutiliza bibliografía existente o se crea bloque incremental para Actividad 4.",
    "Confirmar fuentes obligatorias de la semana correspondiente."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Normalización estructurada obligatoria antes de propagar.",
        "Carpeta de asignatura como entrada canónica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Filosofía del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos, normas, doctrina y datos pertinentes.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos.",
      "Asegurar coherencia argumentativa con base jurídica verificable.",
      "Formar criterio propio con estándar institucional UnADM."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secciones funcionales con lógica jurídica.",
      "Citas trazables y verificables.",
      "Supuestos marcados cuando falten datos locales."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Definir marco conceptual y normativo.",
      "Contrastar evidencia.",
      "Desarrollar postura propia.",
      "Cerrar con conclusión jurídica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización estructurada",
        "Validación JSON estricta",
        "Ejes editoriales de Filosofía del Derecho",
        "Integridad académica y verificabilidad",
        "Consigna local de actividad"
      ],
      "citations": [
        "README.md de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Tono y formato académico",
          "kind": "supports",
          "justification": "La pauta editorial exige alineación explícita institucional."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia segura."
        },
        {
          "source": "Ejes editoriales de Filosofía del Derecho",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Los cinco ejes ordenan el desarrollo argumentativo."
        },
        {
          "source": "Integridad académica y verificabilidad",
          "target": "Conclusión jurídica propia",
          "kind": "supports",
          "justification": "La conclusión requiere respaldo y análisis propio."
        },
        {
          "source": "Consigna local de actividad",
          "target": "Producto final",
          "kind": "depends_on",
          "justification": "El formato y alcance dependen de instrucción específica."
        }
      ],
      "evidence": [
        "README fija identidad, entrada canónica y exigencia de conclusión jurídica.",
        "Programa analítico define cinco ejes reutilizables.",
        "Antecedentes de salidas no parseables justifican gate JSON estricto.",
        "Plantilla Slug no resuelta en README exige validación de nombres reales."
      ]
    },
    "reinforcement_log": [
      "Ciclo 15: deduplicación semántica de reglas repetidas con conservación total de validez.",
      "Ciclo 15: refuerzo lateral de patrones reutilizables sin copiar redacción ni conclusiones de Actividad 1.",
      "Ciclo 15: se mantiene control de supuestos por ausencia de consigna local visible.",
      "Ciclo 15: se consolida dependencia crítica entre normalización estructurada y propagación recursiva."
    ]
  }
}