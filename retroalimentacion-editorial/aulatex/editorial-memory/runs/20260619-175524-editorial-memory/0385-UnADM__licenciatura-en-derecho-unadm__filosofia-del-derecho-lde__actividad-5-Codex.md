{
  "summary": [
    "Asignatura objetivo: Filosofía del Derecho (UnADM, Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos).",
    "La carpeta de asignatura es punto de entrada canónico y exige identidad UnADM, integridad académica, citas verificables y conclusión jurídica propia.",
    "Antecedente de riesgo persistente: hubo salidas no parseables en JSON en ciclos previos; validar estructura antes de guardar y propagar.",
    "El programa analítico organiza productos con problema, conceptos, fuentes, análisis propio y cierre argumentativo transferible a la práctica jurídica.",
    "Productos canónicos de la asignatura: reporte, presentación y recurso visual según planeación semanal.",
    "Supuesto: la actividad 5 debe mantener continuidad editorial con los ejes del programa analítico.",
    "Supuesto: el README contiene marcadores PowerShell sin expandir y anomalías de nombre/ruta que deben validarse antes de automatizar.",
    "Supuesto: existe bibliografía depurada para Semana 7 en filosofia-del-derecho-clean.bib; confirmar pertinencia para actividad 5.",
    "Ciclo 9: consolidación posterior a incidentes de parseo."
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
    "Registrar supuesto operativo si hay duda de alcance y continuar con consistencia."
  ],
  "quality_gates": [
    "Rechazar salidas no estructuradas o no parseables antes de aplicar aguas abajo.",
    "Validar estructura JSON antes de guardar y propagar.",
    "Verificar coherencia jurídica mínima entre premisas y conclusión.",
    "Validar que el producto responda al problema y no solo resuma conceptos.",
    "Confirmar que toda cita tenga referencia verificable en .bib o fuente institucional.",
    "Comprobar ausencia de contradicciones con reglas institucionales heredadas.",
    "Aplicar revisión manual extra en memoria afectada por incidentes de parseo previos."
  ],
  "latex_rules": [
    "Mantener compatibilidad con archivos canónicos de la asignatura .tex y .bib.",
    "No cambiar claves BibTeX ya usadas en .tex para evitar recompilaciones rotas.",
    "Usar acentos y caracteres en LaTeX de forma consistente.",
    "Evitar comandos no estándar si no son necesarios para el producto.",
    "Validar el nombre real del archivo .bib antes de compilar.",
    "Tratar marcadores PowerShell sin expandir en README como anomalía de ruta.",
    "Supuesto: el .bib canónico puede ser filosofia-del-derecho.bib; confirmar en repositorio antes de automatizar.",
    "Supuesto: el .bib operativo puede ser filosofia-del-derecho-clean.bib mientras se confirma el nombre final."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Agregar en .bib solo fuentes realmente citadas en el texto.",
    "No inventar referencias ni metadatos bibliográficos.",
    "Mantener campos mínimos útiles: autor, título, año, editor o nota, URL cuando exista.",
    "Conservar claves bibliográficas originales cuando ya estén citadas en el .tex.",
    "Confirmar pertinencia antes de reutilizar bibliografía limpia de Interpretación jurídica (Semana 7) en actividad 5.",
    "Tratar UNAM-IIJ y SCJN como fuentes jurídicas verificables cuando sus URL estén disponibles.",
    "Fuentes verificables disponibles: hernandezManriquezHermeneutica2019, scjnMemoriaArgumentacion2008, scjnViolenciaFisica2022, scjnIncapacidadResistencia2019."
  ],
  "propagation_hints": [
    "Propagar de forma recursiva preservando unión por deduplicación y sin regresión.",
    "Conservar reglas útiles previas; agregar solo mejoras verificables.",
    "No propagar fuentes no verificadas como bibliografía académica.",
    "Aplicar control de estructura antes de propagar a actividades laterales.",
    "Mantener bandera de riesgo histórico por salidas no parseables en ciclos previos.",
    "Aplicar normalización manual si se reutiliza memoria marcada por incidentes de parseo.",
    "Registrar ciclo 9 como consolidación posterior a incidentes de parseo.",
    "Ciclo 9 necesita normalización manual si se reutiliza."
  ],
  "open_questions": [
    "Falta el enunciado específico de la actividad 5.",
    "Falta la rúbrica de la actividad 5.",
    "Confirmar si la actividad 5 requiere reporte, presentación o recurso visual.",
    "Validar si la bibliografía limpia actual corresponde a actividad 5, semana 7 u otra actividad.",
    "Validar nombres canónicos de archivos en README por marcadores o caracteres anómalos.",
    "Confirmar si el .bib final es filosofia-del-derecho.bib o filosofia-del-derecho-clean.bib.",
    "Corregir marcadores PowerShell del README antes de automatizar compilación."
  ]
}