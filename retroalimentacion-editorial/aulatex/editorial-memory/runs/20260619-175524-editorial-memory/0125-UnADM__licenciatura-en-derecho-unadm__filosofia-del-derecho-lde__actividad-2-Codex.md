{
  "summary": [
    "Se consolida memoria editorial de actividad-2 en ciclo 10 con deduplicacion lossless por union.",
    "Se preservan reglas utiles previas sin recorte ni regresion.",
    "Se mantiene alineacion con README y programa analitico de Filosofia del Derecho en UnADM.",
    "Se registra propagacion recursiva desde actividad-1 hacia actividad-2 en ciclo 10.",
    "Se conserva trazabilidad historica de salidas no parseables como control de calidad.",
    "Supuesto: la consigna especifica de actividad-2 no esta confirmada localmente."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en redaccion y formato.",
    "Usar contexto de Licenciatura en Derecho, Filosofia del Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Mantener la carpeta de asignatura como punto de entrada canonico para productos academicos.",
    "Redactar con enfoque academico-juridico y transferencia a la practica profesional.",
    "Mantener integridad academica en todo producto.",
    "Diferenciar postura academica propia, cita y parafrasis.",
    "Incluir cierre con criterio juridico propio en cada entrega.",
    "Marcar como supuesto todo dato no confirmado por fuente local.",
    "Conservar antecedentes historicos de fuentes provisionales no canonicas sin tratarlas como definitivas."
  ],
  "structure_rules": [
    "Organizar cada actividad en problema, conceptos y fuentes, desarrollo del producto, analisis propio y conclusion.",
    "Alinear el contenido al producto solicitado por la planeacion semanal.",
    "Integrar un problema juridico o social pertinente.",
    "Usar conceptos, normas, doctrina o datos solo con respaldo verificable.",
    "Mantener trazabilidad entre afirmaciones y fuentes citadas.",
    "Cerrar con conclusion transferible a la practica juridica."
  ],
  "activity_rules": [
    "Ajustar actividad-2 a la instruccion docente disponible.",
    "No asumir tema, semana o formato de actividad-2 sin evidencia local.",
    "Transformar la planeacion semanal en reporte, presentacion o producto visual segun corresponda.",
    "Integrar problema juridico o social pertinente.",
    "Evitar afirmaciones factuales sin respaldo verificable.",
    "Usar fuentes sobre hermeneutica, argumentacion e interpretacion juridica solo si la consigna lo requiere.",
    "Mantener postura academica propia diferenciada de cita y parafrasis.",
    "Confirmar que el producto responda a la pauta editorial local."
  ],
  "quality_gates": [
    "Validar que la salida sea JSON parseable antes de propagar.",
    "Revisar respuestas no estructuradas heredadas antes de aplicarlas aguas abajo.",
    "Aplicar compresion por union-dedupe lossless, no por recorte.",
    "No eliminar reglas utiles previas.",
    "Agregar solo mejoras verificables.",
    "No propagar reglas especulativas como definitivas.",
    "Verificar que cada afirmacion sustantiva tenga respaldo o marca de supuesto.",
    "Comprobar consistencia entre texto, citas y bibliografia.",
    "Confirmar cumplimiento de pauta editorial local antes de cerrar.",
    "Mantener sin regresion reglas institucionales UnADM ya validadas."
  ],
  "latex_rules": [
    "Usar LaTeX con estructura academica clara y secciones coherentes con la pauta editorial.",
    "Mantener compatibilidad entre claves de cita en .tex y entradas .bib.",
    "No renombrar claves bibliograficas ya citadas.",
    "Mantener claves originales de filosofia-del-derecho-clean.bib cuando esten citadas.",
    "Evitar recompilaciones por cambios innecesarios de claves.",
    "Revisar rutas y nombres de archivos locales antes de referenciarlos.",
    "Confirmar nombres canonicos de archivos LaTeX locales por posibles caracteres anomalos en README."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y malla curricular de Derecho como base de contexto.",
    "Agregar fuentes especificas de la actividad en el .bib canonico de la asignatura.",
    "No inventar fuentes ni metadatos bibliograficos.",
    "Verificar URL, autor, ano y tipo de fuente antes de citar.",
    "Mantener trazabilidad entre citas en texto y referencias finales.",
    "Usar bibliografia depurada solo cuando sus entradas esten citadas en el documento.",
    "Tratar filosofia-del-derecho-clean.bib como complemento tematico, no como reemplazo automatico del .bib canonico.",
    "Supuesto: filosofia-del-derecho-clean.bib aplica a actividad-2 solo si la consigna coincide."
  ],
  "propagation_hints": [
    "Propagar en modo recursivo solo tras validacion JSON y deduplicacion.",
    "Aplicar union-dedupe como compresion lossless.",
    "Registrar ciclo y alcance de propagacion en cada actualizacion.",
    "Mantener normalizacion manual cuando reaparezcan entradas heredadas no estructuradas.",
    "Registrar ciclo 10 con normalizacion manual si reaparecen entradas no estructuradas.",
    "Ciclo 10 necesita normalizacion manual si se reutiliza.",
    "No propagar supuestos como reglas confirmadas.",
    "Mantener reglas institucionales UnADM ya validadas sin regresion.",
    "Conservar etiqueta de herencia provisional como antecedente historico."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-2: tema, semana y producto.",
    "Confirmar plantilla obligatoria de secciones segun docente.",
    "Definir si existe estilo de citacion obligatorio institucional.",
    "Supuesto: el estilo de citacion obligatorio aun no esta confirmado.",
    "Confirmar si filosofia-del-derecho-clean.bib complementa o sustituye el .bib canonico de la asignatura.",
    "Confirmar nombres canonicos de archivos LaTeX locales por posibles caracteres anomalos en README.",
    "Confirmar si las fuentes provisionales historicas pueden cerrarse como solo antecedente."
  ]
}