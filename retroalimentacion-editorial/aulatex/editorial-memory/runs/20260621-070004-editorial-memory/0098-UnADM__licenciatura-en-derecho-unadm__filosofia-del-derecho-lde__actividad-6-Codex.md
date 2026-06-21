{
  "summary": [
    "Memoria lateral consolidada de Actividad 1 a Actividad 6 con union y deduplicacion sin perdida.",
    "Se preserva identidad institucional UnADM y ubicacion curricular verificada de la asignatura.",
    "Se refuerzan ejes estables: problema, conceptos o normas, producto, analisis propio y conclusion juridica transferible.",
    "Se mantiene regla critica: no propagar contenido no estructurado sin normalizacion previa.",
    "Se conserva control de fuentes provisionales heredadas hasta validacion local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear cada entrega a Licenciatura en Derecho, asignatura Filosofia del Derecho.",
    "Citar ubicacion curricular al contextualizar: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar regla de no regresion: no eliminar reglas utiles previas."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido y sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el producto final a la consigna semanal de Actividad 6.",
    "Cerrar con conclusion juridica aplicable a practica profesional."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Distinguir de forma explicita sintesis de fuente y postura propia.",
    "Sustentar afirmaciones relevantes con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Relacionar conceptos, normas y doctrina con el problema planteado.",
    "Supuesto: si la consigna aborda interpretacion juridica, integrar hermeneutica y argumentacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib activo.",
    "Separar reglas verificadas de supuestos editoriales.",
    "Verificar que la conclusion derive del desarrollo."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Verificar nombres de archivo del README antes de referenciarlos.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: el .bib canonico esperado es filosofia-del-derecho.bib hasta confirmacion final."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas oficiales o academicas.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Registrar fuentes de actividad en el .bib de la asignatura.",
    "Mantener metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "No asumir que filosofia-del-derecho-clean.bib aplica a toda actividad.",
    "Supuesto: clean.bib esta orientado a interpretacion juridica de Semana 7."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones reutilizables, no redaccion literal ni conclusiones especificas.",
    "Mantener union-dedupe lossless en saltos entre nodos hermanos.",
    "No propagar supuestos como hechos confirmados.",
    "Conservar advertencias historicas de salidas no parseables en nodos con herencia Codex/GPT-Pro.",
    "Aplicar normalizacion manual a ciclos heredados con baja confianza antes de reutilizar."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 6.",
    "Confirmar rubrica de evaluacion especifica de Actividad 6.",
    "Confirmar tipo de producto principal requerido en Actividad 6: reporte, presentacion u otro.",
    "Confirmar nombre canonico final del .bib de la asignatura.",
    "Confirmar si Actividad 6 exige formato de citacion juridica adicional a BibTeX.",
    "Confirmar si las fuentes de hermeneutica y SCJN son obligatorias o solo opcionales en Actividad 6."
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
        "Carpeta de asignatura como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Filosofia del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social delimitado.",
      "Conceptos, normas y doctrina pertinentes.",
      "Producto alineado a planeacion semanal.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, fundados y utiles para la practica juridica.",
      "Preservar coherencia institucional y trazabilidad de evidencia en cada actividad."
    ],
    "style_markers": [
      "Inicio con encuadre breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Postura personal diferenciada de la sintesis.",
      "Cierre con utilidad profesional juridica.",
      "Supuestos etiquetados de forma visible."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual y normativo.",
      "Contrastar fuentes pertinentes.",
      "Sostener postura propia con evidencia.",
      "Derivar conclusion del analisis."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Conceptos y normas",
        "Analisis propio",
        "Conclusion transferible",
        "Hermeneutica juridica",
        "Argumentacion juridica",
        "Normalizacion de salidas estructuradas"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
        "hernandezManriquezHermeneutica2019",
        "scjnMemoriaArgumentacion2008",
        "scjnViolenciaFisica2022",
        "scjnIncapacidadResistencia2019"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige verificabilidad y forma academica consistente."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere un objeto de estudio delimitado."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida debe derivar del desarrollo argumentativo."
        },
        {
          "source": "Hermeneutica juridica",
          "target": "Argumentacion juridica",
          "kind": "supports",
          "justification": "Cuando hay interpretacion normativa, la hermeneutica fortalece la argumentacion."
        },
        {
          "source": "Normalizacion de salidas estructuradas",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita reutilizar contenido ambiguo o no verificable."
        }
      ],
      "evidence": [
        "README de asignatura: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo.",
        "Regla historica consolidada: bloquear propagacion sin JSON parseable.",
        "clean.bib: corpus especializado disponible para uso condicionado por consigna."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas y se mantuvo cobertura completa.",
      "Se preservaron reglas utiles previas sin recorte funcional.",
      "Se reforzo control de supuestos y fuentes provisionales.",
      "Se estabilizo patron argumentativo transversal para actividades hermanas.",
      "Se mantuvo separacion entre datos confirmados y preguntas abiertas."
    ]
  }
}