```json
{
  "summary": [
    "Asignatura destino: Filosofia del Derecho, Licenciatura en Derecho UnADM.",
    "Ubicacion curricular verificada: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Fuente de ubicacion: UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
    "Pauta editorial exige identidad UnADM, integridad academica, citas verificables y conclusion juridica propia.",
    "Programa analitico define cinco ejes: problema, conceptos/normas, producto, analisis propio, conclusion transferible.",
    "Consolidacion union-dedupe lossless desde actividad 1 hacia actividad 6.",
    "Memoria heredada reporta salida no JSON parseable en ciclo previo.",
    "Fuente Codex heredada desde ingenieria-en-sistemas-computacionales es provisional.",
    "Existe bibliografia depurada filosofia-del-derecho-clean.bib orientada a interpretacion juridica (Semana 7)."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en toda actividad.",
    "Alinear contenido a Licenciatura en Derecho, Filosofia del Derecho, semestre 1, bloque 2.",
    "Reconocer la materia como obligatoria de 8 creditos al citar la ubicacion curricular.",
    "Marcar como provisional toda fuente proveniente de memoria heredada no normalizada.",
    "Etiquetar como provisional la memoria Codex originada fuera de Derecho hasta validarla localmente.",
    "Conservar regla de no regresion en consolidaciones."
  ],
  "structure_rules": [
    "Entregar respuestas en JSON valido y parseable.",
    "Usar el esquema requerido sin omitir claves.",
    "No agregar claves fuera del esquema requerido en la respuesta final.",
    "Estructurar cada actividad con problema, marco conceptual-normativo, desarrollo del producto, analisis propio y conclusion.",
    "Incluir cierre con criterio juridico transferible a la practica.",
    "Mantener la carpeta de la asignatura como punto de entrada canonico."
  ],
  "activity_rules": [
    "Adaptar la redaccion al objetivo especifico de la actividad 6.",
    "No romper los ejes editoriales de la asignatura al adaptar la actividad.",
    "Explicitar el problema juridico o social que activa la respuesta.",
    "Relacionar conceptos, normas, doctrina o datos con el problema planteado.",
    "Sostener afirmaciones relevantes con fuentes verificables disponibles.",
    "Distinguir con claridad entre sintesis de fuente y postura propia.",
    "Agregar conclusion juridica argumentada en cada entrega.",
    "Evitar generalizaciones filosoficas sin anclaje juridico o academico.",
    "Supuesto: si la actividad 6 trata interpretacion juridica, vincular hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Validar JSON antes de propagar aguas abajo.",
    "Revisar que no haya respuesta no estructurada.",
    "Comprobar coherencia con la pauta editorial de la materia.",
    "Verificar trazabilidad minima de cada afirmacion relevante a una fuente o a un supuesto marcado.",
    "Separar reglas verificadas de supuestos editoriales.",
    "Revisar que la conclusion derive del desarrollo y no sea decorativa.",
    "Aplicar deduplicacion por union sin perdida de reglas vigentes.",
    "No eliminar reglas utiles previas durante la consolidacion."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre archivos .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en archivos .tex.",
    "Comprobar que toda clave citada exista en el archivo bibliografico usado.",
    "Usar el .bib local de la asignatura para nuevas referencias de actividad.",
    "Conservar claves locales existentes si se reutilizan fuentes depuradas.",
    "Evitar editar nombres de archivos canonicos de la materia.",
    "Preservar integridad de compilacion al actualizar citas y referencias.",
    "Marcar como supuesto cualquier nombre de archivo canonico ambiguo hasta confirmarlo."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Priorizar fuentes institucionales UnADM y material juridico verificable.",
    "Registrar nuevas fuentes en el .bib de la asignatura.",
    "Mantener campos bibliograficos minimos: autor, titulo, ano, editor o nota, URL cuando exista.",
    "Marcar como supuesto cualquier dato bibliografico incompleto hasta verificarlo.",
    "Usar la malla curricular de Derecho UnADM como fuente para ubicacion curricular cuando corresponda.",
    "Validar fuentes juridicas contra repositorios oficiales o academicos accesibles.",
    "No citar fuentes locales depuradas si no aparecen efectivamente citadas en el producto final.",
    "Fuentes locales disponibles en clean.bib: hernandezManriquezHermeneutica2019, scjnMemoriaArgumentacion2008, scjnViolenciaFisica2022, scjnIncapacidadResistencia2019."
  ],
  "propagation_hints": [
    "Propagar arriba-y-laterales manteniendo union-dedupe lossless.",
    "Normalizar manualmente elementos heredados del ciclo 1 antes de reutilizarlos en nodos hermanos.",
    "No eliminar reglas utiles previas; solo agregar mejoras verificables.",
    "Etiquetar reglas heredadas de baja confianza como provisionales hasta confirmar.",
    "Propagar la identidad curricular verificada a actividades hermanas de Filosofia del Derecho.",
    "No propagar supuestos como hechos confirmados.",
    "Mantener advertencia de salida no JSON parseable en nodos que hereden memoria Codex."
  ],
  "open_questions": [
    "Supuesto: falta plantilla especifica de evaluacion para actividad 6; confirmar criterios de rubrica.",
    "Definir si se exige formato de citacion juridica adicional al BibTeX institucional.",
    "Confirmar si la fuente provisional heredada sigue vigente o debe reemplazarse por fuente local validada.",
    "Confirmar el nombre canonico del archivo .bib de la asignatura porque el README usa una plantilla variable sin resolver y coexiste filosofia-del-derecho-clean.bib.",
    "Confirmar si la actividad 6 corresponde a interpretacion juridica o a otro producto de la planeacion semanal.",
    "Confirmar si deben usarse las fuentes locales sobre hermeneutica, argumentacion y tesis SCJN en la actividad 6."
  ],
  "sources": [
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-6",
    "UnADM",
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/filosofia-del-derecho-clean.bib"
  ],
  "compression": {
    "method": "union-dedupe",
    "lossless": true
  },
  "schema_version": 1
}
```