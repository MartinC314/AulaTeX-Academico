```json
{
  "summary": [
    "Memoria editorial consolidada para Actividad 1 de Derecho a la Seguridad Social con identidad UnADM.",
    "Refuerzo lateral desde Filosofía del Derecho limitado a patrones reutilizables.",
    "Compresión lossless aplicada por deduplicación y unión de reglas vigentes.",
    "Secuencia editorial estable reforzada: problema, fundamento, análisis, evidencia, postura y cierre.",
    "Normalización estructurada obligatoria antes de cualquier propagación."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho y a Derecho a la Seguridad Social.",
    "Basar ubicación curricular en semestre 2, bloque 1, obligatoria, 8 créditos.",
    "Usar README y programa analítico locales como fuentes primarias.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear formato final al producto solicitado en la planeación.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Adaptar el formato a reporte, presentación u otro permitido por la consigna."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Confirmar correspondencia exacta con la consigna de Actividad 1.",
    "No asumir fuentes de otras semanas sin validación local."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de reutilizar.",
    "Rechazar afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Normalizar respuestas no estructuradas antes de aplicar aguas abajo."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Verificar nombres canónicos de archivos según README local.",
    "Usar derecho-a-la-seguridad-social.bib como .bib canónico.",
    "Corregir rutas o caracteres anómalos antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y normatividad vigente.",
    "Registrar fuentes específicas de la actividad en el .bib local.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir lateralmente solo identidad, estructura, calidad y patrones argumentativos.",
    "No copiar redacción literal, conclusiones ni bibliografía exclusiva entre nodos hermanos.",
    "Aplicar analogía controlada: primero identidad y calidad, luego estructura y conceptos.",
    "Preservar reglas útiles previas y agregar solo mejoras verificables."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual completa de Actividad 1; confirmar entregable exacto.",
    "Confirmar si el formato requerido es reporte, presentación o mixto.",
    "Confirmar rúbrica específica para calibrar profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana.",
    "Confirmar si se exige jurisprudencia específica en esta actividad."
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
        "Control editorial desde la carpeta de asignatura."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Derecho a la Seguridad Social.",
        "Semestre 2, bloque 1, obligatoria, 8 créditos."
      ]
    },
    "essence": [
      "Producto jurídico verificable.",
      "Fundamento constitucional y legal.",
      "Análisis propio con evidencia.",
      "Postura argumentada.",
      "Cierre transferible a la práctica profesional."
    ],
    "reason_for_being": [
      "Transformar cada consigna en un producto jurídico claro, fundado y argumentado.",
      "Garantizar coherencia entre identidad institucional, estructura y calidad académica."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secciones claras y trazables.",
      "Supuestos marcados.",
      "Cierre profesional no descriptivo."
    ],
    "argumentative_patterns": [
      "Problema -> fundamento normativo -> análisis -> evidencia -> conclusión.",
      "Regla general -> contraste contextual -> postura -> implicación práctica.",
      "Pregunta guía -> criterios jurídicos -> inferencia razonada."
    ],
    "knowledge_graph": {
      "concepts": [
        "Derecho a la seguridad social",
        "Marco constitucional",
        "Ley del Seguro Social",
        "Ley del ISSSTE",
        "Universalidad",
        "Progresividad",
        "Acceso, cobertura y justiciabilidad"
      ],
      "citations": [
        "cpeum2026",
        "lss2026",
        "lissste2026",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Marco constitucional",
          "target": "Derecho a la seguridad social",
          "kind": "supports",
          "justification": "El programa analítico fija el fundamento constitucional como eje central."
        },
        {
          "source": "Ley del Seguro Social",
          "target": "Derecho a la seguridad social",
          "kind": "develops",
          "justification": "Concreta prestaciones y mecanismos institucionales."
        },
        {
          "source": "Ley del ISSSTE",
          "target": "Derecho a la seguridad social",
          "kind": "develops",
          "justification": "Regula el régimen aplicable a trabajadores del Estado."
        },
        {
          "source": "Universalidad",
          "target": "Acceso, cobertura y justiciabilidad",
          "kind": "supports",
          "justification": "Permite evaluar alcance real y barreras del derecho."
        }
      ],
      "evidence": [
        "README local y programa analítico.",
        "Bibliografía base en derecho-a-la-seguridad-social.bib."
      ]
    },
    "reinforcement_log": [
      "Transferencia lateral aplicada sin copiar contenido temático exclusivo.",
      "Ejes editoriales reforzados por analogía controlada.",
      "Reglas previas preservadas y deduplicadas."
    ]
  }
}
```