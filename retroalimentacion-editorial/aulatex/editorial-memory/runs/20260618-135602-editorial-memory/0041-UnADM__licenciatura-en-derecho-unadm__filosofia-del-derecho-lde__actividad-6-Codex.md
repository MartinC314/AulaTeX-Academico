{
  "summary": [
    "Base heredada indica salida no JSON parseable en ciclo previo.",
    "Asignatura destino exige identidad UnADM, integridad academica, citas verificables y conclusion juridica propia.",
    "Programa analitico define cinco ejes: problema, conceptos/normas, producto, analisis propio, conclusion transferible."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en toda actividad.",
    "Alinear contenido a Licenciatura en Derecho, Filosofia del Derecho, semestre 1, bloque 2.",
    "Marcar fuente como provisional cuando provenga de memoria heredada no normalizada.",
    "Conservar regla de no regresion en consolidaciones."
  ],
  "structure_rules": [
    "Entregar respuestas en JSON valido y parseable.",
    "Usar el esquema requerido sin omitir claves.",
    "Estructurar cada actividad con: problema, marco conceptual-normativo, desarrollo del producto, analisis propio, conclusion.",
    "Incluir cierre con criterio juridico transferible a la practica."
  ],
  "activity_rules": [
    "Adaptar la redaccion al objetivo especifico de la actividad 6 sin romper ejes de la asignatura.",
    "Explicitar el problema juridico o social que activa la respuesta.",
    "Sostener afirmaciones con fuentes verificables disponibles.",
    "Distinguir con claridad entre sintesis de fuente y postura propia.",
    "Agregar conclusion juridica argumentada en cada entrega."
  ],
  "quality_gates": [
    "Validar JSON antes de propagar aguas abajo.",
    "Revisar que no haya respuesta no estructurada.",
    "Comprobar coherencia con pauta editorial de la materia.",
    "Verificar trazabilidad minima de cada afirmacion relevante a una fuente o a un supuesto marcado.",
    "Aplicar deduplicacion por union sin perdida de reglas vigentes."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre .tex y .bib sin cambiar claves citadas.",
    "Usar el .bib local de la asignatura para nuevas referencias de actividad.",
    "Evitar editar nombres de archivos canonicos de la materia.",
    "Preservar integridad de compilacion al actualizar citas y referencias."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Priorizar fuentes institucionales UnADM y material juridico verificable.",
    "Registrar nuevas fuentes en el .bib de la asignatura.",
    "Mantener campos bibliograficos minimos: autor, titulo, ano, editor o nota, URL cuando exista.",
    "Marcar como supuesto cualquier dato bibliografico incompleto hasta verificarlo."
  ],
  "propagation_hints": [
    "Propagar arriba-y-laterales manteniendo union-dedupe lossless.",
    "Normalizar manualmente elementos heredados del ciclo 1 antes de reutilizarlos en nodos hermanos.",
    "No eliminar reglas utiles previas; solo agregar mejoras verificables.",
    "Etiquetar reglas heredadas de baja confianza como provisionales hasta confirmar."
  ],
  "open_questions": [
    "Supuesto: falta plantilla especifica de evaluacion para actividad 6; confirmar criterios de rubrica.",
    "Definir si se exige formato de citacion juridica adicional al BibTeX institucional.",
    "Confirmar si la fuente provisional heredada sigue vigente o debe reemplazarse por fuente local validada."
  ]
}