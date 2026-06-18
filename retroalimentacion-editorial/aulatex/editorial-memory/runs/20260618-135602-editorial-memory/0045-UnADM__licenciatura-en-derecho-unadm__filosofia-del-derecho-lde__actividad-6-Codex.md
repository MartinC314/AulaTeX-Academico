{
  "summary": [
    "Consolidacion aplicada con union-dedupe lossless entre actividad 1 y actividad 6.",
    "Asignatura destino confirmada: Filosofia del Derecho, Licenciatura en Derecho UnADM.",
    "Ubicacion curricular verificada: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Pauta editorial vigente: identidad UnADM, integridad academica, citas verificables y conclusion juridica propia.",
    "Ejes editoriales vigentes: problema, conceptos/normas, producto, analisis propio y conclusion transferible.",
    "Se mantiene advertencia historica de salida no JSON parseable en ciclos previos.",
    "Fuente heredada Codex fuera de Derecho se mantiene como provisional hasta validacion local.",
    "Existe bibliografia local depurada para interpretacion juridica en filosofia-del-derecho-clean.bib."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en toda entrega.",
    "Alinear contenido a Filosofia del Derecho de la Licenciatura en Derecho.",
    "Reconocer ubicacion curricular al citar la materia: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Marcar como provisional toda fuente heredada no normalizada.",
    "Etiquetar como provisional la memoria Codex originada fuera de Derecho hasta validarla localmente.",
    "Aplicar no regresion: no eliminar reglas utiles previamente vigentes."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable cuando la tarea pida consolidacion.",
    "Usar exactamente el esquema requerido y sin claves extra.",
    "Estructurar productos academicos con: problema, marco conceptual-normativo, desarrollo, analisis propio y conclusion.",
    "Incluir cierre con criterio juridico transferible a la practica.",
    "Mantener la carpeta de la asignatura como punto de entrada canonico."
  ],
  "activity_rules": [
    "Adaptar la redaccion al objetivo especifico de la actividad 6.",
    "No romper los ejes editoriales de la asignatura al adaptar la actividad.",
    "Explicitar el problema juridico o social que activa la respuesta.",
    "Relacionar conceptos, normas, doctrina o datos con el problema planteado.",
    "Sostener afirmaciones relevantes con fuentes verificables disponibles.",
    "Distinguir con claridad sintesis de fuente y postura propia.",
    "Evitar generalizaciones filosoficas sin anclaje juridico o academico.",
    "Agregar conclusion juridica argumentada en cada entrega.",
    "Supuesto: si actividad 6 aborda interpretacion juridica, integrar hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Validar JSON antes de propagar.",
    "Revisar que no exista respuesta no estructurada.",
    "Comprobar coherencia con la pauta editorial de la materia.",
    "Verificar trazabilidad minima de afirmaciones relevantes a fuente o a supuesto marcado.",
    "Separar reglas verificadas de supuestos editoriales.",
    "Revisar que la conclusion derive del desarrollo y no sea decorativa.",
    "Aplicar deduplicacion por union sin perdida de reglas vigentes.",
    "No eliminar reglas utiles previas durante consolidacion."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre archivos .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en .tex.",
    "Comprobar que toda clave citada exista en el archivo bibliografico activo.",
    "Usar el .bib local de la asignatura para nuevas referencias.",
    "Evitar renombrar archivos canonicos de la materia sin confirmacion.",
    "Preservar integridad de compilacion al actualizar citas y referencias.",
    "Marcar como supuesto cualquier nombre canonico ambiguo hasta confirmarlo."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar nuevas fuentes en el .bib de la asignatura.",
    "Mantener campos minimos: autor, titulo, ano, editor o nota, y URL cuando exista.",
    "Marcar como supuesto todo dato bibliografico incompleto hasta verificarlo.",
    "Usar la malla curricular de Derecho UnADM para datos de ubicacion curricular.",
    "Validar fuentes juridicas con repositorios oficiales o academicos accesibles.",
    "No citar entradas del .bib que no se usen en el producto final.",
    "Fuentes locales detectadas en clean.bib: hernandezManriquezHermeneutica2019, scjnMemoriaArgumentacion2008, scjnViolenciaFisica2022, scjnIncapacidadResistencia2019."
  ],
  "propagation_hints": [
    "Propagar arriba-y-laterales con union-dedupe lossless.",
    "Normalizar manualmente elementos heredados del ciclo 1 antes de reutilizarlos.",
    "Conservar advertencias historicas de JSON no parseable para nodos con herencia Codex.",
    "No propagar supuestos como hechos confirmados.",
    "Propagar identidad curricular verificada a actividades hermanas de Filosofia del Derecho.",
    "Mantener etiquetas de provisionalidad hasta validacion local."
  ],
  "open_questions": [
    "Confirmar rubrica especifica de evaluacion para actividad 6.",
    "Confirmar si se exige formato de citacion juridica adicional a BibTeX.",
    "Confirmar si la fuente provisional heredada debe reemplazarse por fuente local validada.",
    "Confirmar nombre canonico del .bib de la asignatura por plantilla variable en README.",
    "Confirmar si actividad 6 corresponde formalmente a interpretacion juridica.",
    "Confirmar uso obligatorio de fuentes locales de hermeneutica, argumentacion y tesis SCJN en actividad 6.",
    "Supuesto: el README presenta nombres de archivo con artefactos de formato y requiere saneamiento."
  ]
}