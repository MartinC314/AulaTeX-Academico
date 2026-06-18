{
  "summary": [
    "Actividad-3 hereda antecedente de salida no JSON parseable en ciclos previos.",
    "Se requiere normalizacion manual antes de propagar automaticamente.",
    "La materia exige identidad UnADM, integridad academica, citas verificables y cierre juridico propio.",
    "Contexto confirmado: Filosofia del Derecho, Licenciatura en Derecho UnADM, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Bibliografia local depurada corresponde a actividad de Interpretacion juridica (Semana 7); su aplicacion a actividad-3 es supuesto hasta confirmar consigna.",
    "Existen incidencias previas de parseo desde Codex y GPT-Pro; no tratarlas como evidencia academica.",
    "Memoria de actividad-3 consolidada con deduplicacion lossless y sin regresion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en toda actividad.",
    "Alinear contenido con Licenciatura en Derecho, Filosofia del Derecho, semestre 1, bloque 2.",
    "Marcar como supuesto cualquier dato no confirmado por fuentes locales.",
    "Tratar memoria editorial Codex/GPT-Pro como antecedente provisional, no como fuente academica.",
    "Registrar origen provisional de incidencias de parseo sin convertirlo en evidencia academica.",
    "Fuente provisional: GPT-Pro desde actividad-1.",
    "Fuente provisional: Codex desde ingenieria en sistemas computacionales."
  ],
  "structure_rules": [
    "Usar estructura minima: problema, conceptos/fuentes, analisis propio, conclusion juridica transferible.",
    "Ajustar el producto al tipo solicitado por la planeacion semanal.",
    "Conservar consistencia con README y programa analitico de la asignatura.",
    "Transformar la planeacion semanal en reporte, presentacion o producto visual segun corresponda.",
    "Integrar claridad, fundamento juridico, evidencia y transferencia profesional."
  ],
  "activity_rules": [
    "Para actividad-3, heredar reglas validas de actividad-1 sin eliminar ninguna util.",
    "Registrar diferencias especificas de actividad-3 como supuestos hasta confirmar guia oficial.",
    "Incluir postura academica propia sustentada en fuentes verificables.",
    "No asumir consigna, semana ni formato de actividad-3 sin evidencia local.",
    "Si el tema es interpretacion juridica, usar solo fuentes citadas y verificables."
  ],
  "quality_gates": [
    "Validar que la salida sea JSON parseable antes de guardar memoria.",
    "Revisar respuestas no estructuradas antes de aplicar propagacion aguas abajo.",
    "Verificar trazabilidad entre afirmaciones y fuentes citadas.",
    "Aplicar no regresion: no eliminar reglas utiles previas.",
    "Confirmar que cada fuente citada exista en bibliografia local o se agregue con datos verificables.",
    "Distinguir fuentes academicas, normativas, jurisprudenciales y antecedentes editoriales.",
    "Normalizar manualmente memorias con incidencias de parseo antes de reutilizarlas."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre claves BibTeX y citas en .tex.",
    "No renombrar claves bibliograficas ya usadas en documentos.",
    "Usar acentos y nombres propios correctos en metadatos BibTeX.",
    "Mantener las claves originales del archivo .bib para evitar recompilaciones.",
    "Usar archivos .tex de reporte o presentacion segun el producto solicitado.",
    "Corregir rutas o nombres de archivo solo con verificacion local.",
    "Archivos canonicos supuestos por README: reporte-filosofia-del-derecho.tex y presentacion-filosofia-del-derecho.tex."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Priorizar fuentes institucionales UnADM y normativas, doctrinales o jurisprudenciales verificables.",
    "Agregar en .bib solo entradas realmente citadas por la actividad.",
    "Mantener URLs verificables cuando existan.",
    "Usar la bibliografia local depurada solo cuando coincida con las citas del documento.",
    "Conservar fuentes UNAM-IIJ y SCJN solo si estan efectivamente citadas.",
    "No usar memoria editorial como bibliografia academica.",
    "Claves registradas en .bib local: hernandezManriquezHermeneutica2019, scjnMemoriaArgumentacion2008, scjnViolenciaFisica2022, scjnIncapacidadResistencia2019."
  ],
  "propagation_hints": [
    "Propagar arriba-y-laterales solo despues de normalizacion manual.",
    "Usar compresion union-dedupe lossless para consolidar memoria.",
    "Conservar bandera de riesgo por antecedente de salida no estructurada.",
    "Propagar reglas institucionales a materias UnADM compatibles.",
    "Propagar reglas especificas de Filosofia del Derecho solo a actividades laterales de la misma asignatura.",
    "No propagar supuestos como hechos confirmados.",
    "Ciclo 1 necesita normalizacion manual si se reutiliza.",
    "En ciclo 2, mantener deduplicacion semantica sin recortar reglas utiles."
  ],
  "open_questions": [
    "Falta confirmar consigna exacta de actividad-3.",
    "Falta confirmar formato de entrega requerido en actividad-3 (reporte, presentacion u otro).",
    "Falta confirmar bibliografia obligatoria especifica de actividad-3.",
    "Falta confirmar si actividad-3 corresponde a interpretacion juridica o a otra semana.",
    "Falta confirmar archivo .tex principal de actividad-3.",
    "Falta confirmar si la bibliografia depurada de Semana 7 aplica a actividad-3."
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