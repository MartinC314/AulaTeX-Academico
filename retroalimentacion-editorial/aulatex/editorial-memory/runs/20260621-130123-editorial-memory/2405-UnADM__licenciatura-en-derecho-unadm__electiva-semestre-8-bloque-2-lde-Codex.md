{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad de origen y materia destino.",
    "Se preservan reglas estables: identidad UnADM, estructura argumentativa juridica y control de supuestos.",
    "Se refuerza normalizacion obligatoria: solo memoria JSON parseable y deduplicada.",
    "Se evita transferir contenido tematico especifico de Filosofia del Derecho sin validacion local.",
    "Se agrega correccion operativa transversal: resolver placeholders y nombres truncados en README/programa."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, metadatos y formato.",
    "Alinear entregables al contexto de Licenciatura en Derecho, semestre 8, bloque 2, tipo Electiva.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no confirmado en consigna o documentos locales.",
    "Mantener autor y matricula confirmados en front matter: Martin Jonathan de la Cruz, ES2611202040.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib."
  ],
  "activity_rules": [
    "Traducir cada consigna semanal a producto concreto solicitado.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Vincular conceptos, normas, doctrina o datos con el problema juridico tratado.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir fuentes de otras semanas o materias sin validacion."
  ],
  "quality_gates": [
    "Bloquear consolidacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de propagar aguas abajo.",
    "Confirmar trazabilidad entre afirmaciones, citas en texto y archivo .bib.",
    "Confirmar ausencia de placeholders o tokens sin expandir en README, programa, .tex y .bib.",
    "Validar correspondencia del producto con la consigna local vigente.",
    "Revisar manualmente herencias de ciclo 1 y fuentes provisionales."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Conservar claves BibTeX estables para evitar referencias rotas.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir nombres de archivo truncados en README (eporte/eferencias).",
    "Resolver tokens tipo $(@{...}.Slug) a nombres literales de archivo.",
    "Actualizar titulo, subtitulo y numero real de actividad antes de compilar.",
    "Completar campos de portada solo con datos confirmados; marcar faltantes como [supuesto]."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas por actividad en electiva-semestre-8-bloque-2.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No reutilizar automaticamente bibliografia de Filosofia del Derecho sin pertinencia local comprobada."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas editoriales estables y abstractas.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferir redaccion literal o contenido tematico dependiente de una actividad concreta.",
    "Mantener compresion lossless por union-dedupe sin regresion de reglas utiles.",
    "Etiquetar reglas de normalizacion JSON como control transversal institucional."
  ],
  "open_questions": [
    "[supuesto] Confirmar creditos oficiales de la materia para metadatos finales.",
    "[supuesto] Confirmar figura docente para front matter.",
    "[supuesto] Confirmar si year=2026 en unadmSitioWeb es dato definitivo o temporal.",
    "[supuesto] Confirmar politica local de fecha de consulta en @misc institucional.",
    "[supuesto] Confirmar si existe nombre oficial alterno de la electiva."
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
        "Carpeta de materia como entrada canonica.",
        "Control explicito de supuestos."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 8, bloque 2, tipo Electiva.",
        "[supuesto] Creditos por confirmar.",
        "Codigo de curso: LDE-S8B2."
      ]
    },
    "essence": [
      "Problema juridico.",
      "Conceptos y fuentes pertinentes.",
      "Producto alineado a consigna.",
      "Analisis propio.",
      "Conclusion juridica transferible.",
      "Normalizacion estructurada previa a propagacion."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables juridicos claros, verificables y utiles profesionalmente.",
      "Asegurar consistencia editorial entre documentos de la materia.",
      "Preservar memoria institucional sin contaminar con datos no validados."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones explicitas y ordenadas.",
      "Postura propia sustentada.",
      "Cierre aplicado a practica juridica.",
      "Marcado explicito de [supuesto]."
    ],
    "argumentative_patterns": [
      "Problema -> objetivo -> marco conceptual/normativo -> analisis propio -> conclusion.",
      "Afirmacion -> evidencia verificable -> inferencia juridica.",
      "Evitar descripcion pura; priorizar razonamiento juridico."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad academica",
        "Normalizacion JSON",
        "Control de supuestos",
        "Trazabilidad cita-texto-bib",
        "Analisis juridico propio",
        "Conclusion transferible",
        "Correccion de placeholders"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva segura",
          "kind": "supports",
          "justification": "Evita heredar memoria no estructurada."
        },
        {
          "source": "Integridad academica",
          "target": "Trazabilidad cita-texto-bib",
          "kind": "depends_on",
          "justification": "La verificabilidad exige correspondencia entre texto y fuentes."
        },
        {
          "source": "Analisis juridico propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La aplicacion profesional deriva del razonamiento del estudiante."
        },
        {
          "source": "Control de supuestos",
          "target": "Rigor editorial",
          "kind": "supports",
          "justification": "Separa datos confirmados de datos pendientes."
        },
        {
          "source": "Correccion de placeholders",
          "target": "Consistencia documental",
          "kind": "supports",
          "justification": "Evita errores operativos entre README, programa y archivos reales."
        }
      ],
      "evidence": [
        "README local de materia con pauta editorial UnADM.",
        "Programa analitico local con ejes de trabajo reutilizables.",
        "Archivo .bib local con claves institucionales base.",
        "Memoria origen con regla estable de normalizacion estructurada obligatoria."
      ]
    },
    "reinforcement_log": [
      "Ciclo 8: deduplicacion completa sin recorte semantico.",
      "Ciclo 8: se refuerza gate de JSON parseable como requisito de propagacion.",
      "Ciclo 8: se mantiene transferencia transversal por abstracciones estables.",
      "Ciclo 8: se incorpora correccion de tokens Slug y nombres truncados como riesgo transversal."
    ]
  }
}