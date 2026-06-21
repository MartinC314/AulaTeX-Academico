{
  "summary": [
    "Se consolida memoria lateral de Actividad 1 a Actividad 6 con union y deduplicacion sin perdida.",
    "Se preserva identidad UnADM y ubicacion curricular verificada: Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se refuerzan ejes editoriales estables: problema, conceptos o normas, producto, analisis propio, conclusion juridica transferible.",
    "Se mantiene regla critica: normalizar antes de propagar cualquier salida no estructurada.",
    "Se mantiene uso de supuestos marcados cuando falte consigna local verificable.",
    "Se detecta token Slug sin resolver en README y programa analitico; requiere normalizacion de nombre canonico .bib."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear toda entrega a Filosofia del Derecho de la Licenciatura en Derecho.",
    "Contextualizar la materia como semestre 1, bloque 2, obligatoria, 8 creditos cuando aplique.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar regla de no regresion: no eliminar reglas utiles previas."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido y sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el formato final al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Adaptar la redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Explicitar la pregunta o problema que guia la actividad.",
    "Relacionar conceptos, normas o doctrina con el problema planteado.",
    "Distinguir sintesis de fuente y postura propia.",
    "Evitar entregas solo descriptivas.",
    "Sustentar afirmaciones relevantes con fuentes verificables.",
    "Verificar coherencia entre objetivo, desarrollo y conclusion.",
    "Supuesto: si Actividad 6 aborda interpretacion juridica, integrar hermeneutica y argumentacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar.",
    "Revisar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Separar reglas confirmadas de supuestos editoriales.",
    "Comprobar que la conclusion derive del analisis.",
    "Validar consistencia entre citas en texto y archivo .bib activo.",
    "No propagar contenido no estructurado sin normalizacion previa."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en archivos .tex.",
    "Comprobar que toda clave citada exista en el archivo bibliografico activo.",
    "Usar acentos y codificacion correcta en español en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Normalizar tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Marcar como supuesto el nombre canonico .bib si persiste ambiguedad."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar fuentes especificas de la actividad en el .bib de la asignatura.",
    "Conservar metadatos minimos: autor, titulo, ano, editorial o nota, URL cuando exista.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No asumir que clean.bib aplica a toda actividad; verificar consigna local.",
    "Marcar como supuesto cualquier dato bibliografico incompleto."
  ],
  "propagation_hints": [
    "Propagar a nodos hermanos solo reglas reutilizables de identidad, estructura y calidad.",
    "No transferir conclusiones especificas ni bibliografia exclusiva de una actividad a otra.",
    "Aplicar union-dedupe lossless en cada ciclo.",
    "Conservar advertencias historicas sobre salidas no parseables.",
    "Propagar supuestos como preguntas abiertas, no como hechos.",
    "Priorizar consistencia curricular comun antes de detalles tematicos locales."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 6; confirmar producto exacto solicitado.",
    "Confirmar rubrica de evaluacion especifica de Actividad 6.",
    "Confirmar si Actividad 6 exige reporte, presentacion o ambos.",
    "Confirmar si requiere formato de citacion juridica adicional a BibTeX.",
    "Confirmar nombre canonico final del .bib por token Slug sin resolver en README.",
    "Confirmar si fuentes de interpretacion juridica de clean.bib son obligatorias en Actividad 6."
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
      "Conceptos y normas pertinentes.",
      "Producto alineado a planeacion.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico y utilidad profesional.",
      "Garantizar trazabilidad entre afirmaciones, fuentes y postura propia.",
      "Sostener continuidad editorial entre actividades hermanas sin perder especificidad local."
    ],
    "style_markers": [
      "Inicio breve con problema.",
      "Secciones claras y ordenadas.",
      "Citas verificables con claves estables.",
      "Postura personal diferenciada de la sintesis.",
      "Cierre aplicable a practica juridica."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual y normativo.",
      "Contrastar fuentes relevantes.",
      "Tomar postura fundamentada.",
      "Derivar conclusion coherente del analisis."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco conceptual-normativo",
        "Analisis propio",
        "Conclusion transferible",
        "Hermeneutica juridica [supuesto tematico]",
        "Argumentacion juridica [supuesto tematico]"
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
          "justification": "La pauta institucional exige citas verificables y formato coherente."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitacion del problema no hay argumentacion focalizada."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida debe derivar del desarrollo."
        },
        {
          "source": "Hermeneutica juridica [supuesto tematico]",
          "target": "Argumentacion juridica [supuesto tematico]",
          "kind": "supports",
          "justification": "Si la consigna trata interpretacion, la hermeneutica fundamenta la argumentacion."
        }
      ],
      "evidence": [
        "README de asignatura: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo.",
        "Regla historica consolidada: no propagar salidas no estructuradas.",
        "Coexistencia de filosofia-del-derecho.bib y filosofia-del-derecho-clean.bib con token Slug sin resolver."
      ]
    },
    "reinforcement_log": [
      "Ciclo 33: deduplicacion completa de reglas repetidas sin recorte semantico.",
      "Ciclo 33: reforzada frontera entre reglas transferibles y contenido especifico no transferible entre hermanos.",
      "Ciclo 33: mantenida advertencia de normalizacion previa para salidas no parseables.",
      "Ciclo 33: mantenida trazabilidad curricular y editorial de UnADM."
    ]
  }
}