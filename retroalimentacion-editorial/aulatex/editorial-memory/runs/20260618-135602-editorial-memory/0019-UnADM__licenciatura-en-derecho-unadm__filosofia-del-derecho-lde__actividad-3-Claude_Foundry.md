{
  "summary": [
    "La materia exige identidad UnADM, integridad académica, citas verificables y cierre jurídico propio.",
    "Contexto confirmado: Filosofía del Derecho, Licenciatura en Derecho UnADM, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Actividad-3 hereda antecedente de salida no JSON parseable en ciclo previo.",
    "Se requiere normalización manual antes de propagar automáticamente.",
    "Bibliografía local depurada corresponde a actividad de Interpretación jurídica (Semana 7); confirmar si aplica a actividad-3 (supuesto)."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en toda actividad.",
    "Alinear contenido con Licenciatura en Derecho, Filosofía del Derecho, semestre 1, bloque 2.",
    "Marcar como supuesto cualquier dato no confirmado por fuentes locales.",
    "Tratar la memoria Codex institucional como antecedente provisional, no como fuente académica."
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
    "Registrar diferencias específicas de la actividad como supuestos hasta confirmar guía oficial.",
    "Incluir postura académica propia sustentada en fuentes verificables.",
    "No asumir consigna, semana ni formato de actividad-3 sin evidencia local.",
    "Si la actividad trata interpretación jurídica, usar solo fuentes citadas y verificables."
  ],
  "quality_gates": [
    "Validar que la salida sea JSON parseable antes de guardar memoria.",
    "Revisar respuestas no estructuradas antes de aplicar propagación aguas abajo.",
    "Verificar trazabilidad entre afirmaciones y fuentes citadas.",
    "Aplicar no regresión: no eliminar reglas útiles previas.",
    "Confirmar que cada fuente citada exista en bibliografía local o sea agregada con datos verificables.",
    "Distinguir fuentes académicas, normativas y antecedentes editoriales."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre claves BibTeX y citas en .tex.",
    "No renombrar claves bibliográficas ya usadas en documentos.",
    "Usar acentos y nombres propios correctos en metadatos BibTeX.",
    "Mantener las claves originales del archivo .bib para evitar recompilaciones.",
    "Usar archivos .tex de reporte o presentación según el producto solicitado.",
    "Corregir rutas o nombres de archivo solo cuando exista verificación local.",
    "Archivos canónicos: reporte-filosofia-del-derecho.tex y presentacion-filosofia-del-derecho.tex (supuesto de README)."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Priorizar fuentes institucionales UnADM y normativas, doctrinales o jurisprudenciales verificables.",
    "Agregar en .bib solo entradas realmente citadas por la actividad.",
    "Mantener URLs verificables cuando existan.",
    "Usar la bibliografía local depurada cuando coincida con las citas del documento.",
    "Conservar fuentes UNAM-IIJ y SCJN solo si están efectivamente citadas.",
    "No usar memoria editorial como bibliografía académica.",
    "Claves verificadas en .bib local: hernandezManriquezHermeneutica2019, scjnMemoriaArgumentacion2008, scjnViolenciaFisica2022, scjnIncapacidadResistencia2019."
  ],
  "propagation_hints": [
    "Propagar arriba-y-laterales solo después de normalización manual en ciclo 1.",
    "Usar compresión union-dedupe lossless para consolidar memoria.",
    "Conservar bandera de riesgo por antecedente de salida no estructurada.",
    "Propagar reglas institucionales a materias UnADM compatibles.",
    "Propagar reglas específicas de Filosofía del Derecho solo a actividades laterales de la misma asignatura.",
    "No propagar supuestos como hechos confirmados."
  ],
  "open_questions": [
    "Falta confirmar consigna exacta de actividad-3.",
    "Falta confirmar formato de entrega requerido en actividad-3 (reporte, presentación u otro).",
    "Falta confirmar bibliografía obligatoria específica de actividad-3.",
    "Falta confirmar si actividad-3 corresponde a interpretación jurídica o a otra semana.",
    "Falta confirmar archivo .tex principal de actividad-3.",
    "Falta confirmar si la bibliografía depurada (Semana 7) aplica a actividad-3."
  ],
  "sources": [
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-3",
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/README.md",
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/programa-analitico-filosofia-del-derecho.md",
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/filosofia-del-derecho-clean.bib"
  ],
  "compression": {
    "method": "union-dedupe",
    "lossless": true
  },
  "schema_version": 1
}