{
  "summary": [
    "Sincronizacion transversal aplicada entre nodos no equivalentes con estrategia conservadora.",
    "Se preserva identidad UnADM y estructura editorial reusable sin transferir redaccion literal.",
    "Se refuerza normalizacion obligatoria de salidas antes de propagacion recursiva.",
    "Se mantiene eje comun: problema, fundamentos, analisis propio y conclusion juridica transferible.",
    "Se consolida cerebro editorial minimo de materia con vacios locales explicitados como supuestos."
  ],
  "identity_rules": [
    "Mantener identidad explicita UnADM en tono, portada y metadatos.",
    "Conservar programa: Licenciatura en Derecho.",
    "Usar nombre canonico de materia: Derecho de la propiedad y registro.",
    "Mantener ubicacion curricular verificada: semestre 7, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar desarrollo en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al entregable solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Adaptar la forma final a reporte o presentacion segun consigna."
  ],
  "activity_rules": [
    "Exigir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Vincular el analisis al campo de propiedad y registro cuando corresponda.",
    "No extrapolar fuentes de otras semanas sin validacion contextual."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Normalizar manualmente respuestas no estructuradas heredadas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar trazabilidad entre citas en texto y archivo .bib.",
    "Confirmar que el producto final coincide con la consigna de la actividad."
  ],
  "latex_rules": [
    "Mantener plantilla base .tex de la materia como punto de partida.",
    "Usar clase article con spanish, letterpaper y oneside salvo instruccion distinta.",
    "Completar metadatos academicos obligatorios antes de compilar.",
    "Evitar placeholders sin resolver en portada y tabla de autor.",
    "Corregir tokens sin expandir en rutas y nombres de archivo del README o programa.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Usar acentos y codificacion correctos en espanol en .tex y .bib."
  ],
  "bibliography_rules": [
    "Usar derecho-de-la-propiedad-y-registro.bib como archivo canonico local.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "No inventar referencias; registrar solo obras consultables.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Agregar nuevas fuentes de actividad en el .bib local con claves estables."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo abstracciones editoriales estables.",
    "Priorizar transferencia de identidad, estructura reusable, gates y grafo conceptual.",
    "Evitar transferir datos hiperlocales de una actividad de otra materia.",
    "Mantener compresion lossless por union y deduplicacion.",
    "Evitar regresiones: no eliminar reglas utiles ya vigentes en destino."
  ],
  "open_questions": [
    "Supuesto: falta rubrica docente especifica de la materia destino.",
    "Confirmar formato exigido por actividad concreta: reporte, presentacion u otro.",
    "Confirmar estilo de citacion juridica requerido por figura docente.",
    "Confirmar sustitucion del placeholder de figura docente en plantilla.",
    "Confirmar si existen fuentes obligatorias de propiedad y registro por semana."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante evidencia incompleta."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion obligatoria antes de propagar.",
        "Supuestos explicitos cuando falte evidencia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho de la propiedad y registro.",
        "Semestre 7, bloque 1, obligatoria, 8 creditos.",
        "Fuente curricular: malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Fundamento conceptual y normativo pertinente.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible.",
      "Trazabilidad entre consigna, desarrollo y evidencia."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros y verificables.",
      "Asegurar calidad editorial uniforme en entregables LaTeX de la materia.",
      "Preservar identidad institucional y rigor juridico en cada actividad."
    ],
    "style_markers": [
      "Estructura problema-fundamento-analisis-cierre.",
      "Citas verificables en afirmaciones sustantivas.",
      "Uso explicito de supuestos cuando falte informacion.",
      "Metadatos academicos completos y consistentes."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo al inicio.",
      "Construir marco conceptual o normativo minimo suficiente.",
      "Contrastar fuentes y desarrollar postura propia.",
      "Cerrar respondiendo la pregunta guia con aplicacion juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Citas verificables",
        "Problema juridico",
        "Analisis propio",
        "Conclusion transferible",
        "Propiedad y registro",
        "Normalizacion de salidas"
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
          "justification": "La pauta institucional exige rigor y trazabilidad."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere una pregunta delimitada."
        },
        {
          "source": "Citas verificables",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La evidencia evita afirmaciones infundadas."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion valida aplicabilidad profesional."
        },
        {
          "source": "Propiedad y registro",
          "target": "Problema juridico",
          "kind": "develops",
          "justification": "El problema se contextualiza en el campo disciplinar destino."
        },
        {
          "source": "Normalizacion de salidas",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita propagacion de reglas ambiguas o rotas."
        }
      ],
      "evidence": [
        "README de materia: pauta editorial e identidad UnADM.",
        "Programa analitico: proposito y ejes de trabajo.",
        "Bib local: unadmSitioWeb y unadmMallaDerecho2024.",
        "Antecedente institucional: salidas no JSON requieren normalizacion previa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: deduplicadas reglas repetidas de origen y destino sin perdida semantica.",
      "Ciclo 2: transferidas solo abstracciones estables transversales entre materias.",
      "Ciclo 2: reforzado gate de JSON parseable como condicion de propagacion recursiva.",
      "Ciclo 2: conservadas reglas utiles previas del destino; no se eliminaron."
    ]
  }
}