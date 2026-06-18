{
  "summary": [
    "Se consolida memoria editorial de actividad-2 con union-dedupe lossless y sin regresion.",
    "Se preserva herencia valida y su caracter provisional cuando el origen fue no estructurado.",
    "Se mantiene alineacion con README y programa analitico de Filosofia del Derecho en UnADM.",
    "Se conserva identidad institucional UnADM para Licenciatura en Derecho.",
    "Se registra propagacion desde actividad-1 hacia actividad-2 en ciclo 2 con alcance arriba-y-laterales.",
    "Se conserva antecedente de normalizacion manual en ciclo 1.",
    "Se conserva antecedente de salidas sin JSON parseable desde Codex y GPT-Pro.",
    "Supuesto: actividad-2 no tiene consigna local completa confirmada en esta entrada."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en redaccion y formato.",
    "Usar contexto de Licenciatura en Derecho.",
    "Usar Filosofia del Derecho como asignatura canonica.",
    "Ubicar la asignatura en semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Mantener la carpeta de asignatura como punto de entrada canonico para productos academicos.",
    "Redactar con enfoque academico-juridico y transferencia a la practica profesional.",
    "Incluir cierre con criterio juridico propio en cada entrega.",
    "Marcar como supuesto todo dato no confirmado por fuente local.",
    "Conservar antecedente historico de fuente provisional Codex desde ingenieria-en-sistemas-computacionales.",
    "Conservar antecedente historico de fuente provisional GPT-Pro desde actividad-1."
  ],
  "structure_rules": [
    "Organizar cada actividad en: problema, conceptos y fuentes, desarrollo del producto, analisis propio y conclusion.",
    "Integrar un problema juridico o social que active el analisis.",
    "Usar conceptos, normas, doctrina o datos solo con respaldo verificable.",
    "Alinear el contenido al producto solicitado por la planeacion semanal.",
    "Conservar trazabilidad entre afirmaciones y fuentes citadas.",
    "Diferenciar postura academica propia, cita y parafrasis.",
    "Cerrar con conclusion transferible a la practica juridica."
  ],
  "activity_rules": [
    "Redactar con enfoque academico-juridico y transferencia a practica profesional.",
    "Integrar problema juridico o social que active el analisis.",
    "Evitar afirmaciones factuales sin respaldo verificable.",
    "Transformar la planeacion semanal en reportes, presentaciones o productos visuales segun corresponda.",
    "Ajustar actividad-2 a la instruccion docente disponible.",
    "Usar fuentes locales sobre hermeneutica, argumentacion e interpretacion juridica solo si la consigna lo requiere.",
    "No asumir tema, semana o formato especifico de actividad-2 sin evidencia local.",
    "Mantener postura academica propia diferenciada de cita y parafrasis.",
    "Mantener integridad academica en todo producto.",
    "Confirmar que el producto responda a la pauta editorial local."
  ],
  "quality_gates": [
    "Validar que la salida sea JSON parseable antes de propagar.",
    "Revisar respuestas no estructuradas heredadas antes de aplicarlas aguas abajo.",
    "Comprobar consistencia entre texto, citas y bibliografia.",
    "No eliminar reglas utiles previas; solo unir y deduplicar.",
    "Agregar solo mejoras verificables.",
    "Aplicar compresion por union-dedupe lossless, no por recorte.",
    "Verificar que cada afirmacion sustantiva tenga respaldo o marca de supuesto.",
    "Confirmar cumplimiento de pauta editorial local antes de cerrar.",
    "No propagar reglas especulativas como definitivas.",
    "Mantener sin regresion las reglas institucionales UnADM ya validadas."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre claves de cita en .tex y entradas .bib.",
    "No renombrar claves bibliograficas ya citadas.",
    "Mantener claves originales de filosofia-del-derecho-clean.bib cuando esten citadas.",
    "Evitar recompilaciones por cambios innecesarios de claves.",
    "Usar LaTeX con estructura academica clara y secciones coherentes con la pauta editorial.",
    "Revisar rutas y nombres de archivos locales antes de referenciarlos.",
    "Confirmar nombres canonicos de archivos LaTeX por caracteres anomalos en README."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y malla curricular de Derecho como base de contexto.",
    "Agregar fuentes especificas de la actividad en el .bib canonico de la asignatura.",
    "No inventar fuentes ni metadatos bibliograficos.",
    "Verificar URL, autor, ano y tipo de fuente antes de citar.",
    "Usar bibliografia depurada solo cuando sus entradas esten citadas en el documento.",
    "Mantener trazabilidad entre citas en texto y referencias finales.",
    "Tratar filosofia-del-derecho-clean.bib como complemento tematico, no como reemplazo automatico del .bib canonico.",
    "Tratar entradas de filosofia-del-derecho-clean.bib como fuentes de hermeneutica, argumentacion e interpretacion juridica (supuesto: aplican solo si la consigna lo requiere).",
    "Tratar filosofia-del-derecho-clean.bib como bibliografia depurada para Interpretacion juridica, Semana 7.",
    "Supuesto: filosofia-del-derecho-clean.bib aplica a actividad-2 solo si la consigna coincide."
  ],
  "propagation_hints": [
    "Propagar arriba-y-laterales solo tras validacion JSON y deduplicacion.",
    "Aplicar union-dedupe como compresion lossless.",
    "No propagar reglas especulativas como definitivas.",
    "No propagar supuestos como reglas confirmadas.",
    "Mantener sin regresion las reglas institucionales UnADM ya validadas.",
    "Conservar etiqueta de herencia provisional como antecedente historico.",
    "Mantener normalizacion manual cuando haya entradas heredadas no estructuradas.",
    "Registrar ciclo 2 con normalizacion manual si reaparecen entradas no estructuradas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-2 (tema, semana y producto).",
    "Confirmar plantilla obligatoria de secciones para actividad-2 segun docente.",
    "Definir si existe estilo de citacion obligatorio institucional (supuesto: no confirmado).",
    "Confirmar si filosofia-del-derecho-clean.bib complementa o sustituye el .bib canonico de la asignatura.",
    "Confirmar nombres canonicos de archivos LaTeX locales por caracteres anomalos en README.",
    "Confirmar si la fuente provisional heredada debe reemplazarse por fuente canonica de Derecho."
  ],
  "sources": [
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-2"
  ],
  "compression": {
    "method": "union-dedupe",
    "lossless": true
  },
  "schema_version": 1
}