```json
{
  "summary": [
    "Asignatura objetivo: Filosofía del Derecho (UnADM, Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos).",
    "La carpeta de asignatura es punto de entrada canónico y exige identidad UnADM, integridad académica, citas verificables y conclusión jurídica propia.",
    "El programa analítico organiza productos con problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
    "Supuesto: la actividad 5 debe mantener continuidad editorial con los ejes del programa analítico de la asignatura.",
    "Antecedente heredado: salida no parseable en JSON desde Codex para UnADM; aplicar control de estructura antes de propagar.",
    "Antecedente heredado: fuente provisional Codex desde ingeniería-en-sistemas-computacionales.",
    "Productos canónicos de la asignatura: reporte, presentación y recurso visual derivados de la planeación semanal."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y encuadre.",
    "Alinear contenido con Licenciatura en Derecho y materia Filosofía del Derecho.",
    "Conservar enfoque jurídico-académico, no divulgativo general.",
    "Marcar explícitamente supuestos cuando falte instrucción de actividad.",
    "Usar claridad, fundamento jurídico, evidencia y transferencia profesional."
  ],
  "structure_rules": [
    "Usar esquema problema-conceptos-producto-análisis-conclusión.",
    "Incluir cierre con postura propia y transferencia a práctica jurídica.",
    "Separar afirmaciones, evidencia y conclusión en bloques claros.",
    "Validar formato de salida parseable antes de guardar o propagar.",
    "Alinear cada sección con el producto solicitado por la planeación."
  ],
  "activity_rules": [
    "Adaptar el producto al enunciado específico de la actividad 5 sin romper reglas de asignatura.",
    "Conservar trazabilidad entre instrucciones, desarrollo y criterio de evaluación.",
    "Evitar relleno; cada sección debe aportar al problema jurídico planteado.",
    "Si hay duda de alcance, registrar supuesto operativo y continuar con consistencia.",
    "Integrar conceptos, normas, doctrina o datos pertinentes cuando el enunciado lo requiera."
  ],
  "quality_gates": [
    "Rechazar salidas no estructuradas o no parseables antes de aplicar aguas abajo.",
    "Verificar coherencia jurídica mínima entre premisas y conclusión.",
    "Confirmar que toda cita tenga referencia verificable en .bib o fuente institucional.",
    "Comprobar ausencia de contradicciones con reglas institucionales heredadas.",
    "Validar que el producto responda al problema y no solo resuma conceptos."
  ],
  "latex_rules": [
    "Mantener compatibilidad con archivos canónicos de la asignatura (.tex y .bib).",
    "No cambiar claves BibTeX ya usadas en .tex para evitar recompilaciones rotas.",
    "Usar acentos y caracteres en LaTeX de forma consistente.",
    "Evitar comandos no estándar si no son necesarios para el producto.",
    "Validar el nombre real del archivo .bib antes de compilar si el README muestra marcador o ruta anómala.",
    "Supuesto: el .bib canónico se llama filosofia-del-derecho.bib; el README muestra plantilla PowerShell sin expandir."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Agregar en .bib solo fuentes realmente citadas en el texto.",
    "No inventar referencias ni metadatos bibliográficos.",
    "Mantener campos mínimos útiles: autor, título, año, editor o nota, URL cuando exista.",
    "Conservar claves bibliográficas originales cuando ya estén citadas en el .tex.",
    "Bibliografía limpia actual corresponde a 'Interpretación jurídica' (Semana 7); confirmar antes de reutilizar en actividad 5.",
    "Fuentes verificables disponibles: hernandezManriquezHermeneutica2019, scjnMemoriaArgumentacion2008, scjnViolenciaFisica2022, scjnIncapacidadResistencia2019 (UNAM-IIJ y SCJN)."
  ],
  "propagation_hints": [
    "Propagar arriba-y-laterales preservando union-dedupe y sin regresión.",
    "Mantener bandera de riesgo histórico: posible salida no parseable en ciclo 1.",
    "Conservar reglas útiles previas; solo agregar mejoras verificables.",
    "Aplicar normalización manual si se reutiliza memoria heredada de ciclo 1.",
    "No propagar fuentes no verificadas como bibliografía académica."
  ],
  "open_questions": [
    "Falta el enunciado específico y rúbrica de la actividad 5 para reglas de producto más finas.",
    "Confirmar si la actividad 5 requiere formato adicional: presentación, reporte o recurso visual.",
    "Validar si la bibliografía limpia (Semana 7, Interpretación jurídica) corresponde a la actividad 5 o a otra actividad.",
    "Validar nombres canónicos de archivos en README porque aparecen marcadores o caracteres anómalos (plantilla PowerShell sin expandir)."
  ],
  "sources": [
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5"
  ],
  "compression": {
    "method": "union-dedupe",
    "lossless": true
  },
  "schema_version": 1
}
```