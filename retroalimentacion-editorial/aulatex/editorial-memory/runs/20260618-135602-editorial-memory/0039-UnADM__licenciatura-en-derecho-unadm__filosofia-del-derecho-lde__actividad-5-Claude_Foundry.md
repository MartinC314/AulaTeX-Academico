```json
{
  "summary": [
    "Asignatura objetivo: Filosofía del Derecho (UnADM, Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos).",
    "La carpeta de asignatura es punto de entrada canónico y exige identidad UnADM, integridad académica, citas verificables y conclusión jurídica propia.",
    "El programa analítico organiza productos con problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
    "Productos canónicos de la asignatura: reporte, presentación y recurso visual derivados de la planeación semanal.",
    "Antecedente heredado: salidas no parseables en JSON desde Codex y GPT-Pro; aplicar control de estructura antes de propagar.",
    "Antecedente heredado: fuente provisional Codex desde ingeniería-en-sistemas-computacionales.",
    "Supuesto: la actividad 5 debe mantener continuidad editorial con los ejes del programa analítico.",
    "Ciclo 2: consolidación posterior a incidentes de parseo."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y encuadre.",
    "Alinear contenido con Licenciatura en Derecho y Filosofía del Derecho.",
    "Conservar enfoque jurídico-académico, no divulgativo general.",
    "Usar claridad, fundamento jurídico, evidencia y transferencia profesional.",
    "Marcar explícitamente supuestos cuando falte instrucción de actividad.",
    "Tratar GPT-Pro desde Actividad 1 como fuente provisional de memoria.",
    "Tratar Codex desde ingeniería-en-sistemas-computacionales como fuente provisional heredada."
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
    "Registrar supuesto operativo si hay duda de alcance y continuar con consistencia.",
    "Integrar conceptos, normas, doctrina o datos pertinentes cuando el enunciado lo requiera."
  ],
  "quality_gates": [
    "Rechazar salidas no estructuradas o no parseables antes de aplicar aguas abajo.",
    "Verificar coherencia jurídica mínima entre premisas y conclusión.",
    "Confirmar que toda cita tenga referencia verificable en .bib o fuente institucional.",
    "Comprobar ausencia de contradicciones con reglas institucionales heredadas.",
    "Validar que el producto responda al problema y no solo resuma conceptos.",
    "Validar estructura JSON antes de guardar y propagar.",
    "Revisar manualmente memoria heredada de ciclos previos."
  ],
  "latex_rules": [
    "Mantener compatibilidad con archivos canónicos de la asignatura (.tex y .bib).",
    "No cambiar claves BibTeX ya usadas en .tex para evitar recompilaciones rotas.",
    "Usar acentos y caracteres en LaTeX de forma consistente.",
    "Evitar comandos no estándar si no son necesarios para el producto.",
    "Validar el nombre real del archivo .bib antes de compilar si el README muestra marcador o ruta anómala.",
    "Tratar marcadores PowerShell sin expandir en README como anomalía de ruta.",
    "Supuesto: el .bib canónico puede ser filosofia-del-derecho.bib; el README muestra plantilla PowerShell sin expandir.",
    "Supuesto: el .bib operativo puede ser filosofia-del-derecho-clean.bib mientras se confirma el nombre final."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Agregar en .bib solo fuentes realmente citadas en el texto.",
    "No inventar referencias ni metadatos bibliográficos.",
    "Mantener campos mínimos útiles: autor, título, año, editor o nota, URL cuando exista.",
    "Conservar claves bibliográficas originales cuando ya estén citadas en el .tex.",
    "Confirmar pertinencia antes de reutilizar bibliografía limpia de 'Interpretación jurídica' (Semana 7) en actividad 5.",
    "Fuentes verificables disponibles: hernandezManriquezHermeneutica2019, scjnMemoriaArgumentacion2008, scjnViolenciaFisica2022, scjnIncapacidadResistencia2019 (UNAM-IIJ y SCJN).",
    "Tratar UNAM-IIJ y SCJN como fuentes jurídicas verificables cuando sus URL estén disponibles."
  ],
  "propagation_hints": [
    "Propagar arriba-y-laterales preservando union-dedupe y sin regresión.",
    "Conservar reglas útiles previas; agregar solo mejoras verificables.",
    "Mantener bandera de riesgo histórico por salidas no parseables en ciclos previos.",
    "Aplicar control de estructura antes de propagar a actividades laterales.",
    "Aplicar normalización manual si se reutiliza memoria heredada de ciclo 1.",
    "No propagar fuentes no verificadas como bibliografía académica.",
    "Registrar ciclo 2 como consolidación posterior a incidentes de parseo."
  ],
  "open_questions": [
    "Falta el enunciado específico de la actividad 5.",
    "Falta la rúbrica de la actividad 5.",
    "Confirmar si la actividad 5 requiere reporte, presentación o recurso visual.",
    "Validar si la bibliografía limpia (Semana 7, Interpretación jurídica) corresponde a la actividad 5 o a otra actividad.",
    "Validar nombres canónicos de archivos en README porque aparecen marcadores o caracteres anómalos (plantilla PowerShell sin expandir).",
    "Confirmar si el .bib final es filosofia-del-derecho.bib o filosofia-del-derecho-clean.bib.",
    "Corregir marcadores o caracteres anómalos del README antes de automatizar compilación."
  ],
  "sources": [
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-5",
    "UnADM"
  ],
  "compression": {
    "method": "union-dedupe",
    "lossless": true
  },
  "schema_version": 1
}
```