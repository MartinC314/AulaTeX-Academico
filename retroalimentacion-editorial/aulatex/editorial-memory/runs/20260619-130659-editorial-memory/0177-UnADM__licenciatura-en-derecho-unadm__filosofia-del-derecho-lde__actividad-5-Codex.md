{
  "summary": [
    "Asignatura objetivo: Filosofía del Derecho (UnADM, Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos).",
    "La carpeta de asignatura es punto de entrada canónico y exige identidad UnADM, integridad académica, citas verificables y conclusión jurídica propia.",
    "El programa analítico organiza productos con problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
    "Productos canónicos de la asignatura: reporte, presentación y recurso visual derivados de la planeación semanal.",
    "Antecedente de riesgo: hubo salidas no parseables en JSON; validar estructura antes de guardar y propagar.",
    "Supuesto: la actividad 5 debe mantener continuidad editorial con los ejes del programa analítico.",
    "Supuesto: el README contiene marcadores PowerShell sin expandir y posibles anomalías de ruta/nombre de archivos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y encuadre.",
    "Alinear contenido con Licenciatura en Derecho y Filosofía del Derecho.",
    "Conservar enfoque jurídico-académico, no divulgativo general.",
    "Usar claridad, fundamento jurídico, evidencia y transferencia profesional.",
    "Marcar explícitamente supuestos cuando falte instrucción de actividad.",
    "Tratar fuentes de memoria de modelos previos como provisionales, no como fuentes académicas."
  ],
  "structure_rules": [
    "Usar esquema problema-conceptos-producto-análisis-conclusión.",
    "Alinear cada sección con el producto solicitado por la planeación.",
    "Separar afirmaciones, evidencia y conclusión en bloques claros.",
    "Incluir cierre con postura propia y transferencia a práctica jurídica.",
    "Validar formato de salida JSON parseable antes de guardar o propagar."
  ],
  "activity_rules": [
    "Adaptar el producto al enunciado específico de la actividad 5 sin romper reglas de asignatura.",
    "Conservar trazabilidad entre instrucciones, desarrollo y criterio de evaluación.",
    "Evitar relleno; cada sección debe aportar al problema jurídico planteado.",
    "Integrar conceptos, normas, doctrina o datos pertinentes cuando el enunciado lo requiera.",
    "Si hay duda de alcance, registrar supuesto operativo y continuar con consistencia."
  ],
  "quality_gates": [
    "Rechazar salidas no estructuradas o no parseables.",
    "Validar estructura JSON antes de guardar y propagar.",
    "Verificar coherencia jurídica mínima entre premisas y conclusión.",
    "Validar que el producto responda al problema y no solo resuma conceptos.",
    "Confirmar que toda cita tenga referencia verificable en .bib o fuente institucional.",
    "Comprobar ausencia de contradicciones con reglas institucionales heredadas.",
    "Aplicar revisión manual extra en memoria afectada por incidentes de parseo previos."
  ],
  "latex_rules": [
    "Mantener compatibilidad con archivos canónicos de la asignatura (.tex y .bib).",
    "No cambiar claves BibTeX ya usadas en .tex para evitar recompilaciones rotas.",
    "Usar acentos y caracteres en LaTeX de forma consistente.",
    "Evitar comandos no estándar si no son necesarios para el producto.",
    "Validar el nombre real del archivo .bib antes de compilar.",
    "Tratar marcadores PowerShell sin expandir en README como anomalía de ruta.",
    "Supuesto: el .bib canónico final puede diferir entre plantilla y archivo operativo; confirmar antes de automatizar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Agregar en .bib solo fuentes realmente citadas en el texto.",
    "No inventar referencias ni metadatos bibliográficos.",
    "Mantener campos mínimos útiles: autor, título, año, editor o nota, URL cuando exista.",
    "Conservar claves bibliográficas originales cuando ya estén citadas en el .tex.",
    "Confirmar pertinencia antes de reutilizar bibliografía limpia de 'Interpretación jurídica' (Semana 7) en actividad 5.",
    "Tratar UNAM-IIJ y SCJN como fuentes jurídicas verificables cuando sus URL estén disponibles."
  ],
  "propagation_hints": [
    "Propagar de forma recursiva preservando union-dedupe y sin regresión.",
    "Conservar reglas útiles previas; agregar solo mejoras verificables.",
    "No propagar fuentes no verificadas como bibliografía académica.",
    "Mantener bandera de riesgo histórico por salidas no parseables en ciclos previos.",
    "Aplicar control de estructura antes de propagar a actividades laterales.",
    "Aplicar normalización manual si se reutiliza memoria marcada por incidentes de parseo."
  ],
  "open_questions": [
    "Falta el enunciado específico de la actividad 5.",
    "Falta la rúbrica de la actividad 5.",
    "Confirmar si la actividad 5 requiere reporte, presentación o recurso visual.",
    "Validar si la bibliografía limpia actual corresponde a actividad 5, semana 7 u otra actividad.",
    "Confirmar si el .bib final es filosofia-del-derecho.bib o filosofia-del-derecho-clean.bib.",
    "Corregir marcadores o caracteres anómalos del README antes de automatizar compilación."
  ]
}