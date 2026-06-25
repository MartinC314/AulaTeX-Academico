{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora y sin regresion.",
    "Se preservan reglas institucionales UnADM, normalizacion JSON y estructura argumentativa reusable.",
    "Se transfieren solo abstracciones estables desde actividad origen, sin arrastre tematico literal.",
    "Se refuerzan alertas locales verificables: placeholders sin resolver, rutas truncadas y plantilla .tex incompleta [supuesto].",
    "Compresion lossless aplicada por union y deduplicacion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar contexto curricular local confirmado: Licenciatura en Derecho, semestre 6, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna o guia oficial.",
    "Tratar memorias heredadas no verificadas como provisionales hasta confirmacion local.",
    "No declarar oficial el codigo de curso LDE-S6B1 sin fuente documental explicita [supuesto].",
    "No cambiar la convencion local danos/daños sin confirmacion documental."
  ],
  "structure_rules": [
    "Iniciar cada entrega con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto final con planeacion semanal y consigna vigente.",
    "Mantener separacion editorial entre reporte, presentacion, programa analitico y .bib.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Formular un problema juridico activador de responsabilidad civil y dano.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Separar fundamento juridico, evidencia y criterio propio.",
    "No arrastrar contenido tematico de otras materias si no aplica al nodo destino.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que afirmaciones juridicas tengan fuente o marca de analisis propio.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar control de no regresion sobre reglas utiles previas.",
    "Detectar y corregir placeholders sin resolver y rutas truncadas antes de compilar."
  ],
  "latex_rules": [
    "Usar español con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, sin referencias rotas y sin tokens sin expandir.",
    "Resolver placeholders tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres truncados en README antes de referenciarlos.",
    "Completar la plantilla .tex local truncada en authortable antes de compilar [supuesto]."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Registrar fuentes especificas por actividad en derecho-de-la-responsabilidad-civil-y-danos.bib.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener como base local: unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Compartir solo abstracciones estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferencia de redaccion literal o contenido tematico puntual del origen.",
    "Mantener normalizacion manual en ciclos con antecedente de salida no estructurada."
  ],
  "open_questions": [
    "Confirmar guia oficial de formato para actividades de la materia.",
    "Confirmar convencion final de nombres con danos vs daños en todo el arbol.",
    "Confirmar si el codigo LDE-S6B1 es oficial.",
    "Corregir definitivamente placeholders de .bib en README y programa analitico.",
    "Validar y completar authortable truncada en plantilla .tex local."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante datos no verificados.",
        "Orientado a practica profesional."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada previa a propagacion.",
        "Entrada canonica por carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 1, obligatoria, 8 creditos.",
        "Asignatura: Derecho de la responsabilidad civil y danos [convencion local pendiente].",
        "Fuente curricular: UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Problema juridico claro.",
      "Conceptos y fuentes pertinentes.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible.",
      "Control tecnico y editorial verificable."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos con fundamento juridico, evidencia y criterio propio.",
      "Asegurar consistencia institucional y trazabilidad editorial entre actividades y materia."
    ],
    "style_markers": [
      "Supuestos marcados explicitamente.",
      "Secciones funcionales y verificables.",
      "Cierre con utilidad profesional.",
      "Sin invencion de fuentes.",
      "Sin propagacion de salida no estructurada."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual-normativo con fuentes.",
      "Analisis propio con contraste.",
      "Cierre con conclusion juridica aplicada."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion JSON",
        "Problema juridico",
        "Marco normativo/doctrinal",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Responsabilidad civil",
        "Daño",
        "Integridad academica"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y formato consistente."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita reutilizar salidas ambiguas o no trazables."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere una pregunta juridica definida."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion se legitima con base normativa verificable."
        },
        {
          "source": "Responsabilidad civil",
          "target": "Daño",
          "kind": "depends_on",
          "justification": "La materia articula imputacion y reparacion desde el daño."
        },
        {
          "source": "Estructura argumentativa reusable",
          "target": "Sincronizacion transversal",
          "kind": "develops",
          "justification": "Permite transferencia estable entre nodos no equivalentes."
        }
      ],
      "evidence": [
        "README local: ubicacion curricular, pauta editorial y estructura.",
        "Programa analitico local: proposito y ejes de trabajo.",
        "Bib local: unadmSitioWeb y unadmMallaDerecho2024.",
        "Plantilla .tex local truncada en authortable [supuesto].",
        "Antecedente de salidas no JSON parseable en ciclos previos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 15: dedupe de reglas repetidas y conservacion de todas las reglas utiles.",
      "Ciclo 15: transferencia transversal de ejes estables problema-fuentes-analisis-conclusion.",
      "Ciclo 15: reforzada barrera JSON parseable y normalizacion previa a propagacion.",
      "Ciclo 15: mantenidas alertas tecnicas locales sin convertir supuestos en hechos."
    ]
  }
}