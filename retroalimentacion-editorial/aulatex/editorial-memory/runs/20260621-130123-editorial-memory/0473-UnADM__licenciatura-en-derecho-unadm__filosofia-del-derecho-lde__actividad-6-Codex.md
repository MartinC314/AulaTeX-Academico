{
  "summary": [
    "Se consolida refuerzo lateral desde actividad 1 hacia actividad 6 con union-dedupe sin perdida.",
    "Se preserva identidad UnADM y ubicacion curricular verificada: Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se mantiene regla critica: no propagar salidas no estructuradas; normalizar antes de reutilizar.",
    "Se conservan ejes editoriales estables: problema, conceptos o normas, producto, analisis propio y conclusion juridica transferible.",
    "Se refuerza control de supuestos por falta de consigna local completa de actividad 6."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear contenido a Filosofia del Derecho de la Licenciatura en Derecho.",
    "Reconocer ubicacion curricular al contextualizar: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar regla de no regresion editorial en consolidaciones."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de memoria editorial.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el producto al formato solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica derivada del analisis y transferible a practica."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de actividad 6 sin romper ejes base.",
    "Distinguir con claridad sintesis de fuentes y postura propia.",
    "Sostener afirmaciones relevantes con fuentes verificables o marcar supuesto.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Relacionar conceptos, normas y doctrina con el problema delimitado.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Supuesto: si actividad 6 aborda interpretacion juridica, vincular hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar.",
    "Revisar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Separar reglas confirmadas de supuestos editoriales.",
    "Validar coherencia entre citas en texto y archivo .bib activo.",
    "No eliminar reglas utiles previas durante consolidacion.",
    "Revisar que la conclusion derive del desarrollo y no sea decorativa."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir caracteres anomalos en nombres de archivo antes de compilar.",
    "Supuesto: .bib canonico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar fuentes especificas de cada actividad en el .bib de la asignatura.",
    "Conservar metadatos minimos: autor, titulo, ano, editorial o nota, URL cuando exista.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No asumir que filosofia-del-derecho-clean.bib aplica a toda actividad; verificar consigna.",
    "Supuesto: clean.bib esta orientado a actividad de interpretacion juridica (Semana 7)."
  ],
  "propagation_hints": [
    "Propagar a nodos hermanos solo reglas reutilizables de identidad, estructura, calidad y metodo.",
    "No transferir conclusiones especificas ni bibliografia exclusiva entre actividades hermanas.",
    "Aplicar union-dedupe lossless en cada ciclo de consolidacion.",
    "Mantener advertencia historica sobre salidas no estructuradas en ciclos tempranos.",
    "Normalizar manualmente memoria heredada de baja confianza antes de repropagar.",
    "Cuando falten datos locales, propagar plantilla base y preguntas abiertas."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual completa de actividad 6; confirmar producto exacto.",
    "Confirmar rubrica especifica de evaluacion para ajustar profundidad argumentativa.",
    "Confirmar si actividad 6 exige reporte, presentacion u otro formato principal.",
    "Confirmar nombre canonico final del .bib por coexistencia entre filosofia-del-derecho.bib y clean.bib.",
    "Confirmar si se requiere formato de citacion juridica adicional a BibTeX."
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
        "Entrada canonica en carpeta de asignatura."
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
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos solidos y verificables.",
      "Asegurar coherencia entre fundamento teorico, evidencia y criterio juridico propio.",
      "Preservar continuidad editorial entre actividades sin perder especificidad local."
    ],
    "style_markers": [
      "Inicio con encuadre breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Diferenciacion clara entre fuente y postura propia.",
      "Cierre con utilidad profesional juridica.",
      "Marcado explicito de supuestos."
    ],
    "argumentative_patterns": [
      "Delimitar problema antes de argumentar.",
      "Construir marco conceptual y normativo pertinente.",
      "Contrastar fuentes antes de concluir.",
      "Derivar postura propia desde evidencia.",
      "Cerrar con conclusion juridica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco normativo y doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Hermeneutica juridica [supuesto condicionado por consigna]",
        "Argumentacion juridica [supuesto condicionado por consigna]"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
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
          "justification": "La pauta institucional exige citas verificables y trazabilidad."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "La postura argumentada requiere problema delimitado."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida debe derivar del desarrollo."
        },
        {
          "source": "Hermeneutica juridica [supuesto condicionado por consigna]",
          "target": "Argumentacion juridica [supuesto condicionado por consigna]",
          "kind": "supports",
          "justification": "En tareas de interpretacion, la hermeneutica fundamenta la argumentacion."
        }
      ],
      "evidence": [
        "README de asignatura: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo.",
        "Regla persistente: bloquear propagacion de salida no estructurada.",
        "Coexistencia de filosofia-del-derecho.bib y filosofia-del-derecho-clean.bib con uso condicionado."
      ]
    },
    "reinforcement_log": [
      "Ciclo 9: deduplicacion completa de reglas repetidas en identidad, estructura y calidad.",
      "Ciclo 9: se mantiene advertencia de normalizacion previa para salidas no JSON.",
      "Ciclo 9: se evita transferencia de conclusiones o bibliografia exclusiva entre hermanos.",
      "Ciclo 9: se refuerza marcado de supuestos por falta de consigna local completa."
    ]
  }
}