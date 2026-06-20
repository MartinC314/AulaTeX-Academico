{
  "summary": [
    "Consolidar memoria base de la materia Filosofía del Derecho con identidad UnADM.",
    "Aplicar compresión union-dedupe lossless sin regresión en cada ciclo.",
    "Usar la carpeta de materia como punto de entrada canónico para actividades y entregables.",
    "Mantener integridad académica, citas verificables y conclusión jurídica con criterio propio.",
    "Normalizar insumos no JSON parseable antes de reutilizarlos.",
    "Registrar salidas no JSON parseable de Codex, GPT-Pro, Auto (model-router) y Claude Foundry como riesgo de ingesta.",
    "Mantener registro histórico de incidencias de parseo como control de calidad de ingesta."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en redacción y formato.",
    "Alinear entregables con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la malla curricular de Derecho UnADM como fuente curricular verificada.",
    "No eliminar reglas heredadas de control de calidad y normalización.",
    "Conservar referencias de fuente provisional hasta sustitución verificada: Codex, GPT-Pro, Auto (model-router) y Claude Foundry. [supuesto]"
  ],
  "structure_rules": [
    "Usar la materia como nodo canónico para reportes, presentaciones y bibliografía.",
    "Separar productos en reporte, presentación, programa analítico y referencias locales.",
    "Estructurar cada producto con problema, conceptos o fuentes, análisis propio y cierre argumentativo.",
    "Reflejar los cinco ejes editoriales del programa analítico en cada actividad.",
    "Mantener trazabilidad entre actividad, archivo .tex y .bib de materia.",
    "Tratar nombres anómalos del README como pendientes de corrección, no como canon definitivo. [supuesto]",
    "Tratar el placeholder PowerShell del .bib como pendiente, no como nombre canónico. [supuesto]"
  ],
  "activity_rules": [
    "Iniciar cada actividad con problema jurídico o social delimitado.",
    "Integrar conceptos, normas, doctrina o datos pertinentes al problema.",
    "Cumplir el tipo de producto solicitado por la planeación semanal.",
    "Incluir análisis propio, postura académica y conclusión transferible a la práctica jurídica.",
    "Agregar fuentes específicas de actividad solo cuando sean verificables.",
    "Conservar el vínculo editorial con actividad-1 al propagar reglas a la materia."
  ],
  "quality_gates": [
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Validar coherencia curricular con datos del README de materia.",
    "Exigir citas verificables para toda afirmación sustantiva.",
    "Verificar que cada cita en .tex tenga entrada BibTeX correspondiente.",
    "Compilar o revisar referencias antes de cerrar entregables.",
    "Confirmar que no se eliminen reglas útiles previas en cada ciclo.",
    "Normalizar insumos no JSON parseable antes de reutilizarlos."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre claves BibTeX y citas usadas en .tex.",
    "No renombrar claves bibliográficas citadas sin migración completa.",
    "Separar entregables por tipo en archivos .tex dedicados.",
    "Preservar rutas y nombres canónicos de la materia para evitar roturas de compilación.",
    "Usar filosofia-del-derecho-clean.bib como archivo depurado disponible mientras se confirma el .bib canónico. [supuesto]",
    "Mantener claves originales de filosofia-del-derecho-clean.bib si ya están citadas en .tex.",
    "No adoptar nombres de archivo anómalos del README hasta corregirlos localmente. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y malla curricular como base contextual.",
    "Agregar fuentes específicas de actividad en el .bib de la materia.",
    "Usar solo fuentes verificables; no inventar referencias.",
    "Conservar entradas depuradas ya existentes y deduplicar sin pérdida.",
    "Preservar entradas académicas verificables de UNAM, IIJ y SCJN ya incluidas.",
    "Registrar URL, año, autor institucional y datos de tesis cuando existan.",
    "Conservar claves verificables: hernandezManriquezHermeneutica2019, scjnMemoriaArgumentacion2008, scjnViolenciaFisica2022, scjnIncapacidadResistencia2019.",
    "No completar entradas BibTeX truncadas sin verificación local.",
    "Tratar scjnIncapacidadResistencia2019 como entrada truncada en el .bib depurado hasta verificar campos completos. [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente estas reglas a actividades de la materia.",
    "Propagar estas reglas arriba al nivel licenciatura y lateralmente a materias afines de Derecho.",
    "Propagar reglas bibliográficas y de trazabilidad a materias afines con entregables LaTeX.",
    "Evitar propagar nombres de archivo anómalos hasta resolverlos localmente.",
    "Mantener etiqueta de compresión union-dedupe lossless en toda propagación.",
    "Propagar solo reglas verificadas por README, programa analítico y .bib local.",
    "Ciclos 1 al 20 necesitan normalización manual si se reutilizan.",
    "Ciclo 21 necesita normalización manual si se reutiliza."
  ],
  "open_questions": [
    "Definir fuente definitiva para reemplazar fuentes provisionales heredadas.",
    "Confirmar nombre final del archivo .bib canónico de la materia. [supuesto]",
    "Resolver placeholder PowerShell del nombre .bib en README y programa analítico. [supuesto]",
    "Corregir nombres de archivo con caracteres anómalos en README. [supuesto]",
    "Precisar plantilla mínima obligatoria para reporte vs presentación.",
    "Determinar si filosofia-del-derecho-clean.bib reemplaza al .bib placeholder del README. [supuesto]",
    "Confirmar si las fuentes depuradas de Semana 7 aplican también a actividad-1. [supuesto]",
    "Confirmar integridad completa de la entrada scjnIncapacidadResistencia2019 en el .bib local. [supuesto]"
  ]
}