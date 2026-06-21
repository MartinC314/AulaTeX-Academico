{
  "summary": [
    "Se consolida refuerzo lateral de Actividad 1 a Actividad 6 con union-dedupe lossless.",
    "Se preserva identidad UnADM y ubicacion curricular verificada: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se mantienen ejes editoriales estables: problema, conceptos o normas, producto, analisis propio y conclusion juridica transferible.",
    "Se refuerza regla critica: no propagar salidas no estructuradas; normalizar antes de reutilizar.",
    "Se evita transferir conclusiones especificas y bibliografia exclusiva de un hermano a otro."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear toda entrega a Licenciatura en Derecho, asignatura Filosofia del Derecho.",
    "Referir ubicacion curricular solo con dato verificado: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar regla de no regresion: no eliminar reglas utiles previas."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de memoria editorial.",
    "Usar exactamente el esquema solicitado, sin claves extra.",
    "Estructurar productos academicos con: problema, marco conceptual o normativo, desarrollo, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Cerrar con conclusion juridica derivada del analisis y transferible a la practica.",
    "Alinear formato final al producto pedido por la planeacion semanal."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Delimitar el problema juridico o social desde el inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir sintesis de fuentes frente a postura propia.",
    "Evitar entregas solo descriptivas o sin criterio juridico.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir que bibliografia de otra semana aplica automaticamente a Actividad 6."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de propagar.",
    "Separar reglas confirmadas de supuestos marcados.",
    "Comprobar trazabilidad de afirmaciones relevantes a fuente o supuesto.",
    "Validar correspondencia del producto con la consigna de Actividad 6.",
    "Validar consistencia entre citas en texto y archivo .bib activo.",
    "Aplicar deduplicacion por union sin perdida de reglas vigentes."
  ],
  "latex_rules": [
    "Usar codificacion en español y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrarlas sin necesidad.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Marcar como supuesto el nombre canónico del .bib mientras haya ambiguedad local."
  ],
  "bibliography_rules": [
    "No inventar fuentes ni metadatos.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar fuentes especificas de la actividad en el .bib de la asignatura.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Conservar campos minimos: autor, titulo, año, editorial o nota, URL cuando exista.",
    "No trasladar bibliografia exclusiva de un hermano sin evidencia de uso local.",
    "Marcar como supuesto cualquier dato bibliografico incompleto hasta verificarlo."
  ],
  "propagation_hints": [
    "Propagar solo patrones reutilizables: identidad, estructura, calidad y relaciones conceptuales.",
    "No propagar redaccion literal ni conclusiones especificas entre actividades hermanas.",
    "Mantener advertencia historica de salidas no estructuradas en linaje Codex/GPT-Pro.",
    "Aplicar normalizacion manual al detectar respuesta no estructurada.",
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Preservar mejoras verificables locales del destino al consolidar."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual completa de Actividad 6; confirmar producto exacto solicitado.",
    "Confirmar rubrica de evaluacion especifica para calibrar profundidad argumentativa.",
    "Confirmar nombre canonico final del .bib por coexistencia de filosofia-del-derecho.bib y filosofia-del-derecho-clean.bib.",
    "Confirmar si Actividad 6 exige formato de citacion juridica adicional a BibTeX.",
    "Supuesto: uso de clean.bib depende de que la consigna de Actividad 6 trate interpretacion juridica."
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
      "Convertir consignas semanales en productos academicos con fundamento juridico, evidencia y criterio propio.",
      "Asegurar consistencia editorial institucional y trazabilidad de fuentes.",
      "Permitir propagacion segura entre nodos sin perdida de reglas utiles."
    ],
    "style_markers": [
      "Apertura con encuadre del problema.",
      "Secciones explicitas y ordenadas.",
      "Postura personal diferenciada de la sintesis.",
      "Cierre con utilidad profesional juridica.",
      "Supuestos marcados de forma visible."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual o normativo.",
      "Relacionar evidencia con el caso o pregunta.",
      "Defender postura propia con soporte.",
      "Derivar conclusion del analisis."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Analisis propio",
        "Conclusion transferible",
        "Hermeneutica juridica [supuesto condicionado por consigna]",
        "Argumentacion juridica [supuesto condicionado por consigna]"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
        "README.md de asignatura",
        "programa-analitico-filosofia-del-derecho.md"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta editorial exige citas verificables y formato institucional."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere delimitacion previa del problema."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida deriva del desarrollo argumentativo."
        },
        {
          "source": "Hermeneutica juridica [supuesto condicionado por consigna]",
          "target": "Argumentacion juridica [supuesto condicionado por consigna]",
          "kind": "supports",
          "justification": "Si la actividad trata interpretacion, la hermeneutica fundamenta la argumentacion."
        }
      ],
      "evidence": [
        "README: identidad UnADM, ubicacion curricular y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo.",
        "Historial de calidad: bloqueo por salida no JSON parseable y necesidad de normalizacion."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin recorte semantico.",
      "Se mantuvieron reglas de calidad heredadas y se alinearon al destino.",
      "Se excluyo transferencia de conclusiones y bibliografia exclusiva de Actividad 1.",
      "Se conservaron supuestos abiertos en ausencia de consigna local completa."
    ]
  }
}