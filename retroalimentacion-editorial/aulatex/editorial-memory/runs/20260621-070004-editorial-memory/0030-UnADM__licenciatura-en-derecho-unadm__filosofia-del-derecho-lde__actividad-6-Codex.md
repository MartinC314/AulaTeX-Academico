{
  "summary": [
    "Se consolida refuerzo lateral entre actividades hermanas con union y deduplicacion lossless.",
    "Se preserva identidad UnADM y ubicacion curricular verificada: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se mantiene regla critica: no propagar contenido no estructurado sin normalizacion JSON.",
    "Se transfieren solo patrones reutilizables de estructura, calidad, estilo y argumentacion.",
    "Se evita copiar conclusiones especificas o bibliografia exclusiva de una actividad hermana.",
    "Supuesto: la consigna puntual de Actividad 6 no esta visible y requiere confirmacion local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear contenido a Licenciatura en Derecho y asignatura Filosofia del Derecho.",
    "Reconocer ubicacion curricular al contextualizar: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar regla de no regresion en consolidaciones."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable cuando la tarea sea consolidacion.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Definir objetivo puntual antes del desarrollo.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica."
  ],
  "activity_rules": [
    "Adaptar la redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Explicitar el problema juridico o social que activa la respuesta.",
    "Relacionar conceptos, normas, doctrina o datos con el problema planteado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir sintesis de fuentes y postura propia.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Supuesto: si la actividad trata interpretacion juridica, vincular hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de propagar.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que toda afirmacion relevante tenga fuente o marca de supuesto.",
    "Separar reglas confirmadas de supuestos editoriales.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No eliminar reglas utiles previas durante consolidacion."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener compatibilidad entre .tex y .bib.",
    "No cambiar claves BibTeX ya citadas.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir rutas o nombres anomalos antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar fuentes especificas de actividad en el .bib de la asignatura.",
    "Distinguir bibliografia base y bibliografia especifica de actividad.",
    "Mantener metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Marcar como supuesto cualquier dato bibliografico incompleto."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir a hermanos solo patrones generales y verificables.",
    "No propagar redaccion literal ni conclusiones especificas entre hermanos.",
    "Conservar advertencias historicas de salidas no parseables para prevenir regresiones.",
    "Aplicar union-dedupe lossless en cada ciclo.",
    "Etiquetar como provisional toda regla de fuente no confirmada localmente."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 6; confirmar producto exacto solicitado.",
    "Confirmar rubrica de evaluacion especifica de Actividad 6.",
    "Confirmar si Actividad 6 exige reporte, presentacion u otro formato principal.",
    "Confirmar nombre canonico final del .bib de asignatura por token Slug sin resolver.",
    "Confirmar si se reutiliza bibliografia depurada de interpretacion juridica o se requiere corpus distinto."
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
        "Asignatura Filosofia del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo.",
      "Producto segun planeacion.",
      "Analisis propio con postura.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con evidencia y criterio juridico.",
      "Asegurar coherencia entre identidad institucional, metodo argumentativo y utilidad profesional."
    ],
    "style_markers": [
      "Inicio breve con delimitacion del problema.",
      "Secciones explicitas y ordenadas.",
      "Citas verificables con trazabilidad.",
      "Diferenciacion clara entre fuente y postura propia.",
      "Cierre con aplicacion juridica concreta."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Presentar marco conceptual o normativo.",
      "Analizar evidencia pertinente.",
      "Sostener postura propia fundamentada.",
      "Concluir con criterio transferible."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco normativo y doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion JSON",
        "Trazabilidad de fuentes"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/programa-analitico-filosofia-del-derecho.md"
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
          "justification": "No hay analisis solido sin delimitacion previa del problema."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida debe derivar del desarrollo argumentativo."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Trazabilidad de fuentes",
          "kind": "supports",
          "justification": "La estructura valida permite auditar reglas, supuestos y evidencia."
        }
      ],
      "evidence": [
        "README: identidad UnADM, entrada canonica y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo estables.",
        "Historial de ciclo: incidentes de salida no parseable y regla de bloqueo."
      ]
    },
    "reinforcement_log": [
      "Ciclo 30: se reforzo normalizacion obligatoria previa a propagacion recursiva.",
      "Ciclo 30: se consolido union-dedupe sin eliminar reglas utiles previas.",
      "Ciclo 30: se mantuvo separacion entre hechos confirmados y supuestos.",
      "Ciclo 30: se transfirieron patrones reutilizables de identidad, estructura, calidad y argumentacion."
    ]
  }
}