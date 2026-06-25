{
  "summary": [
    "Sincronizacion transversal conservadora aplicada desde actividad no equivalente hacia materia destino.",
    "Se preserva identidad UnADM y contexto curricular local del destino sin arrastrar contenido tematico de Filosofia del Derecho.",
    "Se refuerza nucleo editorial estable reusable: problema, conceptos/normas, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene gate critico: bloquear propagacion de salidas no JSON parseable y normalizar antes de reutilizar.",
    "Se consolida correccion obligatoria de placeholders y rutas corruptas en README y programa analitico.",
    "Se conserva trazabilidad entre consigna, desarrollo, producto solicitado y cierre."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en tono, metadatos y formato.",
    "Usar nombre canonico de la materia: Derechos de la persona y familia.",
    "Conservar encuadre curricular local: Licenciatura en Derecho, semestre 3, bloque 1, obligatoria seriada, 8 creditos.",
    "Mantener carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no confirmado por consigna o documento local.",
    "No modificar datos de alumno/matricula de plantilla sin verificacion local. [supuesto]"
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: marco conceptual-normativo, analisis propio y cierre.",
    "Alinear el desarrollo al producto solicitado por planeacion/consigna.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener trazabilidad explicita entre consigna, desarrollo y conclusion."
  ],
  "activity_rules": [
    "Identificar consigna, rubrica y tipo de producto antes de redactar.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar resumen descriptivo puro.",
    "Evitar texto generico; vincular argumentos al problema planteado.",
    "No trasladar contenido tematico de otra asignatura sin validar pertinencia. [supuesto]",
    "Registrar vacios de contexto local en preguntas abiertas."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar esquema minimo completo antes de guardar memoria.",
    "Exigir respaldo verificable o marca [supuesto] en cada afirmacion no confirmada.",
    "Verificar coherencia entre consigna, rubrica, producto y estructura final.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Mantener plantilla local como base y completar metadatos antes de redactar.",
    "Conservar configuracion academica estable (article, spanish, letterpaper, oneside) salvo consigna distinta.",
    "Actualizar documentsubtitle al numero real de actividad.",
    "Corregir rutas y nombres corruptos en README antes de compilar.",
    "Resolver placeholders dinamicos de slug en README/programa analitico.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar derechos-de-la-persona-y-familia.bib como archivo canonico local.",
    "Conservar fuentes base institucionales ya registradas.",
    "Agregar solo fuentes verificables y pertinentes a cada actividad.",
    "No inventar referencias; marcar ausencias como pendiente.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables en nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar propagar redaccion literal o contenidos disciplinares especificos de otra materia.",
    "Aplicar union-dedupe lossless y sin regresion en cada ciclo.",
    "Si reaparece salida no estructurada, forzar normalizacion manual previa.",
    "Mantener reglas locales del destino como autoridad primaria."
  ],
  "open_questions": [
    "Confirmar si LDE-S3B1 es obligatorio en todos los entregables.",
    "Confirmar vigencia de datos de alumno y matricula en plantilla. [supuesto]",
    "Confirmar figura docente vigente para reemplazar 'Nombre por definir'.",
    "Confirmar formato obligatorio por actividad (reporte, presentacion u otro).",
    "Validar correccion definitiva de nombres corruptos en README ('reporte'/'referencias').",
    "Validar sustitucion definitiva del placeholder de slug .bib en README y programa analitico."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 3, bloque 1, obligatoria seriada, 8 creditos.",
        "Asignatura: Derechos de la persona y familia."
      ]
    },
    "essence": [
      "Resolver un problema juridico con fundamento y postura propia.",
      "Transformar planeacion en producto academico verificable.",
      "Sostener conclusiones transferibles a practica juridica."
    ],
    "reason_for_being": [
      "Estandarizar calidad editorial juridica en entregables de la materia.",
      "Asegurar trazabilidad entre consigna, evidencia y conclusion.",
      "Garantizar reutilizacion segura de memoria mediante estructura JSON valida."
    ],
    "style_markers": [
      "Frases directas y verificables.",
      "Separacion nitida entre marco conceptual y postura propia.",
      "Marcado explicito de [supuesto] cuando falte verificacion."
    ],
    "argumentative_patterns": [
      "Problematizar primero.",
      "Fundamentar con norma/doctrina/fuente.",
      "Analizar con criterio propio.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Estructura argumentativa juridica",
        "Integridad de evidencia y citas",
        "Normalizacion JSON",
        "Consistencia LaTeX/BibTeX",
        "Problema-conceptos-evidencia-analisis-conclusion"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura argumentativa juridica",
          "kind": "supports",
          "justification": "El marco institucional define tono, formato y exigencia academica."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Integridad de evidencia y citas",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay trazabilidad confiable."
        },
        {
          "source": "Consistencia LaTeX/BibTeX",
          "target": "Integridad de evidencia y citas",
          "kind": "supports",
          "justification": "Evita referencias rotas y perdida de respaldo."
        },
        {
          "source": "Problema-conceptos-evidencia-analisis-conclusion",
          "target": "Estructura argumentativa juridica",
          "kind": "develops",
          "justification": "Es el patron reusable comun entre actividades."
        }
      ],
      "evidence": [
        "README local de la materia destino.",
        "Programa analitico local de la materia destino.",
        "Archivo derechos-de-la-persona-y-familia.bib.",
        "Regla institucional heredada: no reutilizar salida no estructurada sin normalizacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 20: deduplicacion semantica aplicada sin recorte de reglas utiles.",
      "Ciclo 20: transferidas solo abstracciones estables transversales desde origen no equivalente.",
      "Ciclo 20: preservada autoridad curricular y tecnica del nodo destino.",
      "Ciclo 20: reforzado gate de JSON parseable y control de supuestos.",
      "Ciclo 20: reforzada disciplina de placeholders/rutas como requisito operativo."
    ]
  }
}