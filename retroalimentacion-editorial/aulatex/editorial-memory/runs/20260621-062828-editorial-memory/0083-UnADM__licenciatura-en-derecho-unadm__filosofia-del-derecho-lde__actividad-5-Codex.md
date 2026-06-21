{
  "summary": [
    "Se refuerza memoria lateral de Actividad 5 con patrones reutilizables de Actividad 1.",
    "Se conserva identidad UnADM, encuadre jurídico-académico y estructura por ejes del programa analítico.",
    "Se mantiene regla crítica: bloquear propagación sin JSON parseable y sin estructura mínima completa.",
    "Se preserva deduplicación lossless: unir reglas equivalentes sin recortar reglas útiles.",
    "Supuesto: falta consigna local de Actividad 5; se prioriza estructura base y preguntas abiertas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y encuadre.",
    "Vincular actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como punto de entrada canónico.",
    "Conservar enfoque jurídico-académico con claridad, fundamento y transferencia profesional.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas de modelos como provisionales hasta verificación local.",
    "No usar memoria de modelo como fuente académica."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir explícitamente afirmación, evidencia e inferencia.",
    "Alinear el entregable al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Transformar planeación en reporte, presentación o producto visual según consigna."
  ],
  "activity_rules": [
    "Adaptar el desarrollo al enunciado real de Actividad 5 sin romper reglas troncales.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar conclusiones específicas de Actividad 1.",
    "No arrastrar bibliografía exclusiva de otra actividad sin confirmar pertinencia.",
    "Registrar supuesto operativo cuando falte alcance o formato."
  ],
  "quality_gates": [
    "Bloquear propagación si salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en afirmaciones relevantes.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna local.",
    "Rechazar respuestas no estructuradas antes de reutilización recursiva.",
    "Aplicar revisión manual extra por historial de incidentes de parseo."
  ],
  "latex_rules": [
    "Usar acentos y codificación española de forma consistente en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar compilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Validar nombres reales de archivos cuando README tenga tokens sin expandir.",
    "Resolver tokens tipo $(@{...}.Slug) en README y programa analítico antes de automatizar rutas.",
    "Supuesto: .bib canónico esperado es filosofia-del-derecho.bib; confirmar localmente."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "Registrar en .bib solo fuentes realmente citadas.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Tratar filosofia-del-derecho-clean.bib como archivo temático; confirmar pertinencia para Actividad 5.",
    "Conservar claves ya citadas en .tex."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir solo patrones reutilizables: identidad, estructura, calidad y relaciones troncales.",
    "Evitar copia literal de redacción y conclusiones entre nodos hermanos.",
    "Evitar propagar bibliografía exclusiva no validada para la actividad destino.",
    "Mantener unión+deduplicación para compresión lossless.",
    "Preservar reglas útiles previas y agregar solo mejoras verificables."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 5.",
    "Confirmar rúbrica de evaluación de Actividad 5.",
    "Confirmar formato requerido: reporte, presentación o recurso visual.",
    "Confirmar si Actividad 5 usa bibliografía propia o reutiliza base de asignatura.",
    "Confirmar nombre canónico final del .bib en entorno local.",
    "Supuesto: referencias de Interpretación jurídica (Semana 7) podrían no corresponder a Actividad 5."
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
        "Carpeta de asignatura como entrada canónica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos.",
        "Asignatura: Filosofía del Derecho."
      ]
    },
    "essence": [
      "Problema jurídico delimitado.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos jurídicos sólidos.",
      "Asegurar trazabilidad entre consigna, argumentación y cierre."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones funcionales.",
      "Postura propia sustentada.",
      "Supuestos explícitos cuando falten datos."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> toma de postura."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Ejes editoriales troncales",
        "Normalización JSON",
        "Consistencia cita-.bib",
        "Transferencia lateral controlada"
      ],
      "citations": [
        "README.md",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Ejes editoriales troncales",
          "kind": "supports",
          "justification": "La identidad fija tono, rigor y finalidad profesional."
        },
        {
          "source": "Normalización JSON",
          "target": "Transferencia lateral controlada",
          "kind": "depends_on",
          "justification": "Sin parseo válido no hay propagación confiable."
        },
        {
          "source": "Consistencia cita-.bib",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La solidez argumentativa requiere evidencia trazable."
        },
        {
          "source": "Ejes editoriales troncales",
          "target": "Transferencia lateral controlada",
          "kind": "develops",
          "justification": "Permiten reutilizar estructura sin copiar contenido específico."
        }
      ],
      "evidence": [
        "README exige identidad UnADM, integridad académica y conclusión jurídica propia.",
        "Programa analítico define eje problema-conceptos-fuentes-análisis-cierre.",
        "Historial reporta incidentes de salida no parseable; se mantiene gate estricto."
      ]
    },
    "reinforcement_log": [
      "Ciclo 83: deduplicación de reglas repetidas en destino.",
      "Ciclo 83: conservación de reglas útiles previas sin eliminación regresiva.",
      "Ciclo 83: refuerzo lateral de estructura y calidad desde hermano Actividad 1.",
      "Ciclo 83: se evitaron transferencias prohibidas de conclusiones y bibliografía exclusiva."
    ]
  }
}