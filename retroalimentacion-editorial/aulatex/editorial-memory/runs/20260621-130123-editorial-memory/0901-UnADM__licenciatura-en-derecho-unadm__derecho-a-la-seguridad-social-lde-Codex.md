{
  "summary": [
    "Sincronizacion transversal consolidada entre nodos no equivalentes con enfoque conservador.",
    "Se preserva identidad UnADM y estructura canonica del destino sin mezclar contenido tematico de Filosofia del Derecho.",
    "Se refuerza patron estable reutilizable: problema, fundamento, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene control de calidad institucional: JSON parseable, normalizacion previa y trazabilidad de supuestos.",
    "Compresion aplicada por union-dedupe lossless y sin regresion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar datos curriculares oficiales del destino: Licenciatura en Derecho, semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica editorial.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local [supuesto].",
    "No sobrescribir reglas validas previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README y programa analitico del destino como canon estructural.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Separar desarrollo en: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto solicitado por la planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y bibliografia local."
  ],
  "activity_rules": [
    "Delimitar problema juridico desde el inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar aguas abajo.",
    "Validar estructura minima completa antes de propagar recursivamente.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Verificar correspondencia exacta entre producto entregable y consigna vigente."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion y acentos correctos en espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion tecnica.",
    "Compilar sin errores criticos, referencias rotas ni rutas corruptas.",
    "Normalizar nombres de archivo cuando existan marcadores o tokens sin expandir.",
    "Mantener metadatos institucionales consistentes en todos los .tex."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central del destino.",
    "Priorizar fuentes institucionales UnADM y normas juridicas vigentes verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "Agregar nuevas fuentes solo si son verificables y pertinentes a la consigna local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas abstractas estables entre nodos no equivalentes.",
    "No transferir redaccion literal ni contenido tematico especifico de Filosofia del Derecho.",
    "Priorizar en saltos transversales: identidad, estructura reusable, quality gates y grafo conceptual.",
    "Mantener bandera historica: ciclo 1 requiere normalizacion manual si se reutiliza.",
    "Preservar reglas locales del destino cuando exista conflicto con herencia transversal.",
    "Aplicar siempre compresion lossless por union-dedupe sin recorte."
  ],
  "open_questions": [
    "Confirmar norma de citacion obligatoria de la materia (APA, ISO, institucional o juridica mexicana) [supuesto].",
    "Confirmar si LDE-S2B1 es codigo oficial o solo etiqueta operativa [supuesto].",
    "Confirmar figura docente oficial para plantillas de actividad [supuesto].",
    "Confirmar consignas especificas por actividad en planeaciones locales antes de redactar.",
    "Verificar si persiste vigencia de fuentes heredadas externas a Derecho [supuesto]."
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
        "Normalizacion estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho a la Seguridad Social.",
        "Semestre 2, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Fundamento normativo verificable.",
      "Evidencia pertinente.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir cada consigna en producto juridico verificable y profesional.",
      "Conservar memoria editorial persistente sin perdida por deduplicacion."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y cierre.",
      "Cierre con utilidad practica profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo y doctrinal.",
      "Contrastar evidencia relevante.",
      "Fijar postura propia sustentada.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema juridico",
        "Marco normativo",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "JSON parseable",
        "Compresion union-dedupe"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024",
        "cpeum2026",
        "lss2026",
        "lissste2026"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Tono y formato de entregas",
          "kind": "supports",
          "justification": "Asegura coherencia transversal y trazabilidad institucional."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "No hay analisis valido sin pregunta juridica delimitada."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion exige fundamento legal verificable."
        },
        {
          "source": "JSON parseable",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "La reutilizacion segura requiere estructura valida."
        },
        {
          "source": "Compresion union-dedupe",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Preserva reglas utiles sin duplicidad ni recorte."
        }
      ],
      "evidence": [
        "README del destino define estructura canonica local y archivos base.",
        "Programa analitico del destino fija proposito y ejes de trabajo.",
        "derecho-a-la-seguridad-social.bib confirma base normativa e institucional verificable.",
        "Historial institucional registra salida no parseable en ciclo 1 y exige normalizacion manual."
      ]
    },
    "reinforcement_log": [
      "Ciclo 6: se consolidan abstracciones estables transversales sin mover contenido disciplinar especifico del origen.",
      "Ciclo 6: se refuerzan quality gates de parseo JSON, supuestos y consistencia bibtex-citas.",
      "Ciclo 6: se mantiene ADN UnADM y estructura por ejes como nucleo persistente.",
      "Ciclo 6: se confirma estrategia progresiva y conservadora con union-dedupe lossless."
    ]
  }
}