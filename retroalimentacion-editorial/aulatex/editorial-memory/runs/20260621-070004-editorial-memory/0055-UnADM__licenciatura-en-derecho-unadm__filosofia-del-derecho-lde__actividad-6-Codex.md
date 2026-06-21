{
  "summary": [
    "Se consolida memoria lateral de Actividad 1 a Actividad 6 con union y deduplicacion lossless.",
    "Se preserva identidad UnADM y contexto curricular verificado: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se refuerzan ejes editoriales estables: problema, conceptos o normas, producto, analisis propio y conclusion juridica transferible.",
    "Se mantiene regla critica: no propagar contenido no estructurado; normalizar antes de reutilizar.",
    "Se conserva estatus provisional para fuentes heredadas no verificadas localmente."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear toda actividad a Licenciatura en Derecho y asignatura Filosofia del Derecho.",
    "Usar como contexto curricular: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar regla de no regresion: no eliminar reglas utiles previas."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable cuando la tarea sea consolidacion de memoria.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el formato final al producto pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica aplicable a practica profesional."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Distinguir con claridad sintesis de fuentes y postura propia.",
    "Sostener afirmaciones relevantes con fuentes verificables o con supuesto marcado.",
    "Evitar entregas solo descriptivas.",
    "Relacionar conceptos, normas o doctrina con el problema planteado.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Supuesto: si Actividad 6 trata interpretacion juridica, integrar hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar toda respuesta no estructurada antes de reutilizarla.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib activo.",
    "Revisar que la conclusion derive del analisis y no sea decorativa.",
    "Aplicar deduplicacion por union sin perdida de reglas vigentes."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: el .bib canonico esperado es filosofia-del-derecho.bib por Slug del README; confirmar localmente."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas oficiales o academicas.",
    "Registrar fuentes especificas de la actividad en el .bib de la asignatura.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente editorial o URL.",
    "No asumir que filosofia-del-derecho-clean.bib aplica a toda actividad; usarlo solo si coincide la consigna."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir a hermanos solo patrones reutilizables de identidad, estructura, calidad y trazabilidad.",
    "No transferir redaccion literal ni conclusiones especificas entre actividades hermanas.",
    "Mantener advertencias historicas de nodos con salidas no parseables en ciclos previos.",
    "Separar reglas confirmadas de supuestos al propagar.",
    "Reforzar conexiones estables: problema -> analisis propio -> conclusion transferible."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 6; confirmar producto exacto solicitado.",
    "Confirmar rubrica especifica de evaluacion para Actividad 6.",
    "Confirmar si Actividad 6 exige reporte, presentacion u otro formato principal.",
    "Confirmar nombre canonico final del .bib por token Slug sin resolver en README.",
    "Confirmar si se reutiliza bibliografia existente o se requiere .bib especifico de Actividad 6."
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
      "Problema juridico o social.",
      "Conceptos y marco normativo pertinente.",
      "Producto alineado a planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con rigor juridico.",
      "Preservar identidad UnADM y trazabilidad de evidencia.",
      "Garantizar calidad estructural y argumentativa reutilizable entre actividades."
    ],
    "style_markers": [
      "Encuadre inicial breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Diferenciacion entre fuente y postura propia.",
      "Cierre con utilidad profesional juridica.",
      "Marcado explicito de supuestos."
    ],
    "argumentative_patterns": [
      "Delimitar problema antes de argumentar.",
      "Construir marco conceptual y normativo.",
      "Contrastar fuentes verificables.",
      "Sostener postura propia fundamentada.",
      "Derivar conclusion desde el desarrollo."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco conceptual y normativo",
        "Analisis propio",
        "Conclusion transferible",
        "Hermeneutica juridica [supuesto condicionado a consigna]",
        "Argumentacion juridica [supuesto condicionado a consigna]"
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
          "justification": "La pauta institucional exige citas verificables y consistencia editorial."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere un problema delimitado."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion debe derivar del razonamiento previo."
        },
        {
          "source": "Hermeneutica juridica [supuesto condicionado a consigna]",
          "target": "Argumentacion juridica [supuesto condicionado a consigna]",
          "kind": "supports",
          "justification": "En actividades de interpretacion, la hermeneutica fundamenta la argumentacion."
        }
      ],
      "evidence": [
        "README de asignatura: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: ejes de trabajo y proposito.",
        "Regla historica consolidada: normalizar salidas no estructuradas antes de propagar.",
        "Coexistencia de filosofia-del-derecho.bib y filosofia-del-derecho-clean.bib."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin recortar alcance.",
      "Se conservaron advertencias de fuentes provisionales y JSON no parseable historico.",
      "Se reforzo trazabilidad entre estructura, evidencia y conclusion.",
      "Se mantuvo separacion entre hechos confirmados y supuestos."
    ]
  }
}