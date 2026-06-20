{
  "summary": [
    "Memoria de actividad-3 consolidada con deduplicación semántica lossless y sin regresión.",
    "Persisten incidencias históricas de salida no JSON parseable; aplicar normalización manual antes de propagación automática.",
    "Contexto confirmado: Filosofía del Derecho, Licenciatura en Derecho UnADM, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "La pauta editorial exige identidad UnADM, integridad académica, citas verificables y conclusión jurídica propia.",
    "La bibliografía local depurada corresponde a Interpretación jurídica (Semana 7); su uso en actividad-3 queda como supuesto hasta confirmar consigna.",
    "Las incidencias de parseo de herramientas previas son antecedentes técnicos, no evidencia académica.",
    "Ciclo 19: mantener deduplicación semántica lossless sin recortar reglas útiles."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en toda actividad.",
    "Alinear contenido con Licenciatura en Derecho, Filosofía del Derecho, semestre 1, bloque 2.",
    "Marcar como supuesto todo dato no confirmado por evidencia local.",
    "Tratar la memoria editorial como antecedente provisional, no como fuente académica.",
    "Registrar origen de incidencias de parseo sin convertirlo en evidencia académica.",
    "Fuentes provisionales de incidencias: Codex, GPT-Pro, Auto (model-router), Claude Foundry.",
    "Fuente provisional de propagación: actividad-1."
  ],
  "structure_rules": [
    "Usar estructura mínima: problema, conceptos y fuentes, análisis propio, conclusión jurídica transferible.",
    "Ajustar el producto al tipo solicitado por la planeación semanal.",
    "Conservar consistencia con README y programa analítico de la asignatura.",
    "Transformar la planeación semanal en reporte, presentación o producto visual según corresponda.",
    "Integrar claridad, fundamento jurídico, evidencia y transferencia profesional."
  ],
  "activity_rules": [
    "Para actividad-3, heredar reglas válidas de actividad-1 sin eliminar ninguna útil.",
    "Registrar diferencias específicas de actividad-3 como supuestos hasta confirmar guía oficial.",
    "Incluir postura académica propia sustentada en fuentes verificables.",
    "No asumir consigna, semana ni formato de actividad-3 sin evidencia local.",
    "Si el tema es interpretación jurídica, usar solo fuentes citadas y verificables."
  ],
  "quality_gates": [
    "Validar que la salida sea JSON parseable antes de guardar memoria.",
    "Revisar respuesta no estructurada antes de aplicar propagación aguas abajo.",
    "Verificar trazabilidad entre afirmaciones y fuentes citadas.",
    "Aplicar no regresión: no eliminar reglas útiles previas.",
    "Confirmar que cada fuente citada exista en bibliografía local o se agregue con datos verificables.",
    "Distinguir fuentes académicas, normativas, jurisprudenciales y antecedentes editoriales.",
    "Normalizar manualmente memorias con incidencias de parseo antes de reutilizarlas."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre claves BibTeX y citas en .tex.",
    "No renombrar claves bibliográficas ya usadas en documentos.",
    "Mantener las claves originales del .bib para evitar recompilaciones.",
    "Usar acentos y nombres propios correctos en metadatos BibTeX.",
    "Usar archivos .tex de reporte o presentación según producto solicitado.",
    "Corregir rutas o nombres de archivo solo con verificación local.",
    "Archivos canónicos (supuesto por README): reporte-filosofia-del-derecho.tex y presentacion-filosofia-del-derecho.tex."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Priorizar fuentes institucionales UnADM y fuentes normativas, doctrinales o jurisprudenciales verificables.",
    "Agregar en .bib solo entradas realmente citadas por la actividad.",
    "Usar la bibliografía local depurada solo cuando coincida con las citas del documento.",
    "Conservar fuentes UNAM-IIJ y SCJN solo si están efectivamente citadas.",
    "Mantener URLs verificables cuando existan.",
    "No usar memoria editorial como bibliografía académica.",
    "Claves registradas en .bib local: hernandezManriquezHermeneutica2019, scjnMemoriaArgumentacion2008, scjnViolenciaFisica2022, scjnIncapacidadResistencia2019."
  ],
  "propagation_hints": [
    "Usar compresión union-dedupe lossless para consolidar memoria.",
    "Conservar bandera de riesgo por antecedente de salida no estructurada.",
    "No propagar supuestos como hechos confirmados.",
    "Propagar reglas institucionales a materias UnADM compatibles.",
    "Propagar reglas específicas de Filosofía del Derecho solo a actividades de la misma asignatura.",
    "Propagar recursivamente solo después de normalización manual por incidencias de parseo.",
    "Ciclos 1 a 19 requieren normalización manual si se reutilizan.",
    "En ciclo 19 mantener deduplicación semántica lossless sin recortar reglas útiles."
  ],
  "open_questions": [
    "Falta confirmar consigna exacta de actividad-3.",
    "Falta confirmar formato de entrega requerido en actividad-3: reporte, presentación u otro.",
    "Falta confirmar bibliografía obligatoria específica de actividad-3.",
    "Falta confirmar si actividad-3 corresponde a interpretación jurídica o a otra semana.",
    "Falta confirmar si la bibliografía depurada de Semana 7 aplica a actividad-3.",
    "Falta confirmar archivo .tex principal de actividad-3."
  ]
}