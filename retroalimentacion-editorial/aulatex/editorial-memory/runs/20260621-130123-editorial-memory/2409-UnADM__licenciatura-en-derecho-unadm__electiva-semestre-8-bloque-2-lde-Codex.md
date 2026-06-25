{
  "summary": [
    "Sincronizacion transversal consolidada con estrategia conservadora y deduplicacion lossless.",
    "Se preservan reglas estables de identidad UnADM, estructura argumentativa y control de supuestos.",
    "Se refuerza normalizacion obligatoria de salidas no estructuradas antes de propagacion recursiva.",
    "Se evita transferir contenido tematico especifico de Filosofia del Derecho al nodo Electiva sin validacion local.",
    "Se mantiene foco en ejes reutilizables: problema, conceptos/fuentes, analisis propio y conclusion juridica transferible."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, metadatos y formato.",
    "Alinear entregables con Licenciatura en Derecho, semestre 8, bloque 2, tipo Electiva.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no confirmado en consigna o documentos locales.",
    "Mantener autor y matricula confirmados en front matter: Martin Jonathan de la Cruz, ES2611202040.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion manual."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en secciones: conceptos/fuentes, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto final con consigna y planeacion semanal.",
    "Cerrar con conclusion juridica aplicable a la practica profesional.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib."
  ],
  "activity_rules": [
    "Traducir cada consigna semanal a un producto concreto verificable.",
    "Incluir postura argumentada del estudiante y evitar resumen descriptivo puro.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Vincular conceptos, normas y doctrina con el problema juridico tratado.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir fuentes de otras semanas o materias sin confirmacion local."
  ],
  "quality_gates": [
    "Bloquear consolidacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de propagacion aguas abajo.",
    "Confirmar trazabilidad entre afirmaciones, citas en texto y .bib.",
    "Confirmar ausencia de placeholders y tokens sin expandir en README, programa, .tex y .bib.",
    "Validar correspondencia entre producto entregado y consigna vigente.",
    "Exigir marca [supuesto] en datos no verificables."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y metadatos institucionales.",
    "Actualizar titulo, subtitulo y numero real de actividad antes de compilar.",
    "Corregir nombres truncados de archivos en listados y referencias.",
    "Resolver tokens tipo $(@{...}.Slug) a nombres literales de archivo.",
    "Mantener compatibilidad entre nombres de .tex, recursos y .bib.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas por actividad en electiva-semestre-8-bloque-2.bib.",
    "Priorizar fuentes institucionales UnADM cuando corresponda.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Mantener correspondencia exacta entre claves citadas y entradas BibTeX."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones estables por relacion transversal entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "No propagar redaccion literal ni contenido tematico local no validado.",
    "Mantener compresion por union-dedupe sin eliminar reglas utiles previas.",
    "Etiquetar como provisional toda herencia de ciclos con salida no estructurada.",
    "Aplicar normalizacion manual al detectar artefactos de ciclo 1/2 reutilizados."
  ],
  "open_questions": [
    "[supuesto] Confirmar creditos oficiales de la materia destino para front matter.",
    "[supuesto] Confirmar nombre oficial de figura docente.",
    "[supuesto] Confirmar si existe nombre oficial alterno de la electiva.",
    "[supuesto] Confirmar politica institucional para year y fecha de consulta en @misc.",
    "[supuesto] Confirmar si se requiere .bib por actividad ademas del .bib de materia."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante datos no confirmados."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Entrada canonica por carpeta de materia.",
        "Control explicito de supuestos."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 8, bloque 2, tipo Electiva.",
        "Codigo de curso LDE-S8B2.",
        "[supuesto] Creditos pendientes de confirmacion."
      ]
    },
    "essence": [
      "Problema juridico contextual.",
      "Conceptos y fuentes verificables.",
      "Analisis propio no descriptivo.",
      "Conclusion juridica transferible.",
      "Normalizacion estructurada previa a propagacion."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y utiles para practica juridica.",
      "Preservar identidad institucional y rigor de evidencia en todo entregable.",
      "Sostener continuidad editorial transversal sin contaminar contexto local."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Objetivo explicito.",
      "Secciones ordenadas y funcionales.",
      "Marcado [supuesto] visible.",
      "Cierre profesional aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> objetivo -> marco conceptual/normativo -> analisis propio -> conclusion.",
      "Afirmacion juridica -> evidencia verificable -> interpretacion razonada.",
      "Evitar resumen; priorizar toma de postura sustentada."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Integridad academica",
        "Control de supuestos",
        "Trazabilidad cita-texto-bib",
        "Analisis juridico propio",
        "Conclusion juridica transferible",
        "Consistencia documental local"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva segura",
          "kind": "supports",
          "justification": "Evita heredar memoria no parseable y errores de formato."
        },
        {
          "source": "Integridad academica",
          "target": "Trazabilidad cita-texto-bib",
          "kind": "depends_on",
          "justification": "La verificabilidad exige correspondencia entre afirmaciones y fuentes."
        },
        {
          "source": "Analisis juridico propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La aplicacion practica surge del razonamiento del estudiante."
        },
        {
          "source": "Control de supuestos",
          "target": "Rigor editorial",
          "kind": "supports",
          "justification": "Separa datos confirmados de datos pendientes."
        },
        {
          "source": "Consistencia documental local",
          "target": "Calidad de entrega",
          "kind": "supports",
          "justification": "Alinea README, programa, .tex y .bib."
        }
      ],
      "evidence": [
        "README local de Electiva S8B2.",
        "programa-analitico-electiva-semestre-8-bloque-2.md.",
        "electiva-semestre-8-bloque-2.bib.",
        "Regla heredada: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 9: deduplicadas reglas repetidas de identidad, estructura y calidad sin perdida semantica.",
      "Ciclo 9: reforzada regla transversal de no propagar contenido tematico especifico entre nodos no equivalentes.",
      "Ciclo 9: mantenida herencia institucional de normalizacion manual para salidas historicas no estructuradas.",
      "Ciclo 9: reforzado control de placeholders y tokens Slug sin expandir como riesgo operativo recurrente."
    ]
  }
}