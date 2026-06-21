{
  "summary": [
    "Se consolida refuerzo lateral desde Actividad 1 hacia Actividad 4 sin copiar contenido específico.",
    "Se preserva identidad UnADM y marco curricular verificable: semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Se mantiene normalización estructurada y validación JSON estricta como precondición de propagación.",
    "Se fijan patrones reutilizables: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Supuesto: la consigna exacta de Actividad 4 no está visible y debe confirmarse localmente."
  ],
  "identity_rules": [
    "Mantener tono formal académico UnADM.",
    "Alinear la actividad a Licenciatura en Derecho y Filosofía del Derecho.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validación local.",
    "Conservar integridad académica con citas verificables."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto al formato pedido por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Separar hechos, conceptos, argumentos y postura personal."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 a los cinco ejes del programa analítico.",
    "Incluir explícitamente problema, conceptos, evidencia y análisis propio.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar cada afirmación relevante con fuente verificable y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No trasladar conclusiones específicas de Actividad 1."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de reutilizar.",
    "Normalizar respuestas no estructuradas heredadas antes de propagar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregable y consigna local de Actividad 4."
  ],
  "latex_rules": [
    "Usar acentos y codificación correctos en .tex y .bib.",
    "Citar en .tex solo claves existentes en .bib.",
    "No renombrar claves bibliográficas ya usadas en documentos activos.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y referencias de archivos."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y jurídicas verificables.",
    "Registrar fuentes específicas de Actividad 4 en el .bib canónico de asignatura.",
    "No inventar referencias ni metadatos faltantes.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib parece orientado a otra semana; validar pertinencia antes de reutilizar."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir a nodos hermanos solo patrones reutilizables, no redacción literal.",
    "Preservar reglas útiles previas sin regresión.",
    "Aplicar unión y deduplicación lossless en cada ciclo.",
    "Mantener banderas de normalización manual para ciclos con antecedentes no parseables.",
    "Cuando falte dato local, propagar plantilla base y pregunta abierta."
  ],
  "open_questions": [
    "Confirmar consigna exacta de Actividad 4: producto, extensión y criterios.",
    "Confirmar rúbrica docente específica para ajustar profundidad argumentativa.",
    "Confirmar nombre canónico final del archivo .bib de asignatura.",
    "Confirmar si Actividad 4 reutiliza bibliografía existente o requiere bloque bibliográfico propio.",
    "Verificar nombres de archivos afectados por caracteres dañados en README.",
    "Supuesto: documenttitle/documentsubtitle en metadata aún reflejan Actividad 1; confirmar actualización para Actividad 4."
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
        "Entrada canónica en carpeta de asignatura."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos.",
        "Asignatura: Filosofía del Derecho."
      ]
    },
    "essence": [
      "Problema jurídico o social como punto de partida.",
      "Conceptos y marco normativo con evidencia verificable.",
      "Análisis propio del estudiante como núcleo.",
      "Conclusión jurídica aplicable a práctica profesional.",
      "Normalización estructurada antes de cualquier propagación."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos.",
      "Asegurar trazabilidad entre consigna, evidencia y conclusión.",
      "Sostener continuidad editorial entre actividades hermanas sin contaminar contenido específico."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Cita explícita en afirmaciones sustantivas.",
      "Uso explícito de supuestos cuando falten datos.",
      "Cierre con criterio jurídico propio."
    ],
    "argumentative_patterns": [
      "Problematizar primero, definir alcance después.",
      "Delimitar conceptos antes de argumentar.",
      "Relacionar norma/doctrina con caso o situación.",
      "Contrastar evidencia y postura propia.",
      "Concluir con implicación jurídica transferible."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales de Filosofía del Derecho",
        "Normalización estructurada",
        "Validación JSON",
        "Integridad académica y verificabilidad",
        "Relación problema-evidencia-conclusión"
      ],
      "citations": [
        "README de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad académica y verificabilidad",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y formato académico."
        },
        {
          "source": "Ejes editoriales de Filosofía del Derecho",
          "target": "Relación problema-evidencia-conclusión",
          "kind": "develops",
          "justification": "Los ejes ordenan el desarrollo argumentativo completo."
        },
        {
          "source": "Normalización estructurada",
          "target": "Validación JSON",
          "kind": "depends_on",
          "justification": "La propagación recursiva requiere salida estructurada y parseable."
        }
      ],
      "evidence": [
        "README establece identidad UnADM, integridad académica y conclusión jurídica propia.",
        "Programa analítico define cinco ejes reutilizables para cualquier actividad.",
        "Antecedentes de salidas no parseables justifican compuerta de JSON estricto."
      ]
    },
    "reinforcement_log": [
      "Ciclo 11: deduplicación de reglas repetidas con preservación semántica.",
      "Ciclo 11: refuerzo lateral de patrones estructurales y de calidad desde Actividad 1.",
      "Ciclo 11: se evita transferencia de conclusiones y bibliografía exclusiva de hermano.",
      "Ciclo 11: se mantiene etiqueta de supuestos en datos no confirmados localmente."
    ]
  }
}