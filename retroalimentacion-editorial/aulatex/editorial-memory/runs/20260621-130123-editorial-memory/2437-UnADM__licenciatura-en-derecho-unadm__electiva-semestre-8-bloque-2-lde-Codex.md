{
  "summary": [
    "Se consolida sincronizacion transversal conservadora desde actividad de Filosofia del Derecho hacia materia Electiva S8B2.",
    "Se preservan reglas estables: identidad UnADM, estructura por ejes, analisis propio, conclusion juridica y control de supuestos.",
    "Se refuerza gate transversal: no propagar memoria no parseable y normalizar antes de reutilizar.",
    "Se mantiene transferencia por abstracciones editoriales; no se transfiere contenido tematico especifico entre materias no equivalentes.",
    "Se confirma riesgo operativo local por placeholders y nombres truncados; queda como regla transversal de higiene documental."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, metadatos y formato.",
    "Alinear entregables con Licenciatura en Derecho, semestre 8, bloque 2, tipo Electiva.",
    "Usar carpeta de materia como entrada canonica.",
    "Mantener autor y matricula confirmados en front matter: Martin Jonathan de la Cruz, ES2611202040.",
    "Marcar como [supuesto] todo dato no confirmado en consigna o documentos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear siempre el formato final al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener consistencia entre README, programa analitico, .tex y .bib."
  ],
  "activity_rules": [
    "Traducir cada consigna semanal a producto concreto verificable.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar resumen puramente descriptivo.",
    "Vincular problema, fuentes, desarrollo y conclusion sin saltos logicos.",
    "No asumir fuentes de otras semanas o materias sin confirmacion local.",
    "Verificar correspondencia exacta entre actividad y artefacto entregado."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizacion aguas abajo.",
    "Validar estructura minima completa del nodo antes de propagar.",
    "Confirmar trazabilidad entre afirmaciones, citas en texto y archivo .bib.",
    "Confirmar ausencia de placeholders o tokens sin expandir en README, programa, .tex y .bib.",
    "Verificar coherencia de nombres de archivo entre documentos y carpeta real."
  ],
  "latex_rules": [
    "Usar espanol con acentos correctos en .tex y .bib.",
    "Conservar plantilla base de la materia y metadatos institucionales.",
    "Actualizar titulo, subtitulo y numero real de actividad antes de compilar.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens tipo $(@{...}.Slug) y corregir nombres truncados antes de entrega."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas por actividad en electiva-semestre-8-bloque-2.bib.",
    "Priorizar fuentes institucionales UnADM y materiales verificables.",
    "No inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Mantener correspondencia uno-a-uno entre citas usadas y claves BibTeX existentes."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas estables y abstractas entre nodos transversales.",
    "Evitar transferencia de redaccion literal o contenido tematico de Filosofia del Derecho.",
    "Conservar union-dedupe sin eliminar reglas utiles previas.",
    "Mantener etiqueta de herencia provisional para insumos no verificados.",
    "Aplicar primero gates de parseo, estructura y trazabilidad antes de cualquier fusion lateral."
  ],
  "open_questions": [
    "[supuesto] Confirmar creditos oficiales de la materia destino para completar metadatos.",
    "[supuesto] Confirmar nombre de figura docente para front matter.",
    "[supuesto] Confirmar si el nombre oficial de la electiva difiere del slug actual.",
    "[supuesto] Confirmar politica institucional sobre year y fecha de consulta en @misc.",
    "[supuesto] Confirmar si se requiere artefacto adicional al reporte y presentacion en esta materia."
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
        "Normalizacion estructurada antes de propagar.",
        "Control explicito de supuestos."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 8, bloque 2, tipo Electiva.",
        "Codigo de curso LDE-S8B2.",
        "[supuesto] Creditos por confirmar."
      ]
    },
    "essence": [
      "Problema juridico.",
      "Conceptos y fuentes pertinentes.",
      "Producto alineado a consigna.",
      "Analisis propio.",
      "Conclusion juridica transferible.",
      "Trazabilidad cita-texto-bib.",
      "Higiene estructural y tecnica."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables juridicos claros, verificables y utiles para practica profesional.",
      "Preservar coherencia editorial institucional en todo el nodo materia."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones explicitas.",
      "Postura propia sustentada.",
      "Cierre aplicable.",
      "Marcado visible de [supuesto]."
    ],
    "argumentative_patterns": [
      "Problema -> objetivo -> marco conceptual/normativo -> analisis propio -> conclusion aplicada.",
      "Afirmacion -> evidencia -> interpretacion -> implicacion juridica.",
      "Evitar descripcion pura; priorizar razonamiento."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Integridad academica",
        "Control de supuestos",
        "Trazabilidad cita-texto-bib",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Compresion union-dedupe"
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
          "justification": "Reduce herencia de errores no parseables."
        },
        {
          "source": "Integridad academica",
          "target": "Trazabilidad cita-texto-bib",
          "kind": "depends_on",
          "justification": "La verificabilidad depende de correspondencia documental."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La aplicacion profesional surge del razonamiento del estudiante."
        },
        {
          "source": "Control de supuestos",
          "target": "Rigor editorial",
          "kind": "supports",
          "justification": "Distingue datos confirmados de pendientes."
        }
      ],
      "evidence": [
        "README local de la materia destino.",
        "Programa analitico local con ejes de trabajo.",
        "Archivo electiva-semestre-8-bloque-2.bib.",
        "Memoria origen con gates de parseo JSON y normalizacion previa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 16: deduplicacion completa de reglas repetidas en origen y destino.",
      "Ciclo 16: se refuerza regla transversal de no propagar salidas no estructuradas.",
      "Ciclo 16: se preserva ADN argumentativo comun sin trasladar contenido tematico no equivalente.",
      "Ciclo 16: se mantiene estrategia progresiva y conservadora en salto transversal."
    ]
  }
}