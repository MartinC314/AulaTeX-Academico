{
  "summary": [
    "Se consolida memoria lateral de Actividad 1 a Actividad 6 con union y deduplicacion lossless.",
    "Se preserva identidad UnADM y ubicacion curricular verificada: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se mantiene regla critica: no propagar contenido no estructurado; normalizar antes de reutilizar.",
    "Se refuerzan ejes editoriales estables: problema, conceptos o normas, producto, analisis propio y conclusion juridica transferible.",
    "Se conserva manejo de fuentes heredadas como provisionales hasta verificacion local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear cada entrega a Licenciatura en Derecho, asignatura Filosofia del Derecho.",
    "Contextualizar con ubicacion curricular: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar regla de no regresion: no eliminar reglas utiles previas."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el producto al formato pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Distinguir sintesis de fuentes y postura propia del estudiante.",
    "Sustentar afirmaciones relevantes con fuentes verificables.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Relacionar conceptos, normas y doctrina con el problema planteado.",
    "Supuesto: si la consigna aborda interpretacion juridica, articular hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar aguas abajo.",
    "Separar reglas confirmadas de supuestos marcados.",
    "Confirmar trazabilidad de afirmaciones a fuente o supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar que la conclusion derive del analisis y no sea decorativa.",
    "Aplicar deduplicacion por union sin perdida de reglas vigentes."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en .tex.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Usar acentos y codificacion correcta en espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico antes de fijar nombres canonicos.",
    "Marcar como supuesto el nombre canonico de .bib mientras exista ambiguedad entre filosofia-del-derecho.bib y filosofia-del-derecho-clean.bib."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas oficiales o academicas.",
    "Registrar fuentes especificas de actividad en el .bib de la asignatura.",
    "Conservar metadatos minimos: autor, titulo, ano, editor o nota, URL cuando exista.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No asumir que un .bib depurado de otra semana aplica automaticamente a Actividad 6.",
    "Marcar como supuesto cualquier dato bibliografico incompleto."
  ],
  "propagation_hints": [
    "Propagar a nodos hermanos solo reglas reutilizables de identidad, estructura, calidad y trazabilidad.",
    "No copiar redaccion literal ni conclusiones especificas entre actividades hermanas.",
    "Conservar advertencia historica de salidas no estructuradas en ciclos tempranos.",
    "Aplicar normalizacion manual al detectar memoria heredada no parseable.",
    "Propagar supuestos como preguntas abiertas, no como hechos.",
    "Mantener estrategia de union-dedupe lossless en ciclos recursivos."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual completa de Actividad 6; confirmar producto exacto solicitado.",
    "Confirmar rubrica de evaluacion especifica de Actividad 6.",
    "Confirmar si se exige formato juridico de citacion adicional a BibTeX.",
    "Confirmar nombre canonico final del .bib de la asignatura tras resolver token Slug.",
    "Confirmar si deben incorporarse fuentes de hermeneutica y SCJN segun la consigna local."
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
      "Conceptos, normas y doctrina pertinentes.",
      "Producto alineado a planeacion.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos con fundamento, evidencia y criterio juridico propio.",
      "Asegurar coherencia entre identidad institucional, calidad tecnica y rigor argumentativo."
    ],
    "style_markers": [
      "Inicio breve con delimitacion del problema.",
      "Secciones explicitas y ordenadas.",
      "Diferenciacion visible entre fuente y postura propia.",
      "Cierre con utilidad profesional juridica.",
      "Supuestos marcados de forma explicita."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Construir marco conceptual y normativo.",
      "Contrastar fuentes relevantes.",
      "Sostener postura propia con evidencia.",
      "Concluir con criterio juridico aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco conceptual-normativo",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion JSON",
        "Trazabilidad de citas",
        "Hermeneutica juridica [supuesto condicionado por consigna]"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/programa-analitico-filosofia-del-derecho.md",
        "hernandezManriquezHermeneutica2019",
        "scjnMemoriaArgumentacion2008"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y formato consistente."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitacion del problema no hay analisis juridico valido."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion debe derivar del razonamiento previo."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "supports",
          "justification": "La memoria solo se reutiliza si es estructurada y parseable."
        },
        {
          "source": "Hermeneutica juridica [supuesto condicionado por consigna]",
          "target": "Marco conceptual-normativo",
          "kind": "develops",
          "justification": "Aplica solo si Actividad 6 trata interpretacion juridica."
        }
      ],
      "evidence": [
        "README: identidad UnADM, ubicacion curricular y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo.",
        "Memoria de origen: regla de normalizacion previa y ejes argumentativos estables.",
        "Contexto local: coexistencia de .bib y token Slug sin resolver."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas de identidad, estructura, calidad y bibliografia.",
      "Se conservaron reglas utiles previas sin recorte semantico.",
      "Se removio transferencia de conclusiones especificas entre hermanos.",
      "Se reforzo trazabilidad fuente-supuesto para evitar invenciones.",
      "Se mantuvo condicionamiento explicito en temas de interpretacion juridica."
    ]
  }
}