{
  "summary": [
    "Se consolida refuerzo lateral desde actividad 1 hacia actividad 6 con deduplicacion sin perdida.",
    "Se preserva identidad UnADM y contexto curricular verificado: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se mantienen ejes editoriales estables: problema, conceptos o normas, producto, analisis propio y conclusion juridica transferible.",
    "Se conserva regla critica: no propagar contenido no estructurado sin normalizacion previa.",
    "Se mantiene trazabilidad de supuestos cuando falte consigna local de actividad 6."
  ],
  "identity_rules": [
    "Mantener tono institucional UnADM en toda entrega.",
    "Alinear toda actividad a Licenciatura en Derecho y asignatura Filosofia del Derecho.",
    "Citar ubicacion curricular solo con fuente institucional verificada.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar regla de no regresion en consolidaciones."
  ],
  "structure_rules": [
    "Entregar JSON valido cuando la tarea sea consolidacion de memoria.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Estructurar producto academico en: problema, marco conceptual-normativo, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Cerrar con conclusion juridica aplicable a practica profesional.",
    "Alinear formato final al producto exigido por planeacion semanal."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de actividad 6 sin romper ejes base.",
    "Explicitar problema juridico o social que activa la respuesta.",
    "Relacionar conceptos y normas con el problema planteado.",
    "Distinguir sintesis de fuentes y postura propia.",
    "Evitar entregas solo descriptivas.",
    "Sustentar afirmaciones relevantes con fuentes verificables.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar.",
    "Separar reglas confirmadas de supuestos marcados.",
    "No eliminar reglas utiles previas durante consolidacion.",
    "Validar correspondencia entre producto y consigna local de actividad 6.",
    "Revisar que conclusion derive del analisis y no sea decorativa.",
    "Validar consistencia entre citas en texto y archivo .bib activo."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre archivos .tex y .bib.",
    "No cambiar claves BibTeX ya citadas.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Usar codificacion y acentos correctos en español.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y referencias internas.",
    "Supuesto: archivo .bib canonico esperado es filosofia-del-derecho.bib hasta confirmacion local."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Registrar nuevas fuentes en el .bib de la asignatura.",
    "Mantener metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Marcar como supuesto datos bibliograficos incompletos.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No asumir que clean.bib aplica a actividad 6 sin confirmacion de consigna."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir a nodos hermanos solo patrones reutilizables, no conclusiones especificas.",
    "Conservar advertencias historicas de salidas no estructuradas en nodos con herencia provisional.",
    "Aplicar union-dedupe lossless en cada ciclo.",
    "Cuando falte dato local, propagar estructura base y pregunta abierta."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de actividad 6; confirmar producto exacto solicitado.",
    "Confirmar rubrica especifica de evaluacion de actividad 6.",
    "Confirmar si actividad 6 exige reporte, presentacion u otro formato principal.",
    "Confirmar nombre canonico final del .bib por coexistencia de filosofia-del-derecho.bib y filosofia-del-derecho-clean.bib.",
    "Confirmar si tema local de actividad 6 corresponde a interpretacion juridica o a otro eje.",
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
        "Carpeta de asignatura como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura Filosofia del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Conceptos y normas pertinentes.",
      "Producto alineado a planeacion.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, fundados y utiles para practica juridica."
    ],
    "style_markers": [
      "Encuadre inicial breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Citas verificables con postura personal diferenciada.",
      "Cierre con criterio juridico aplicable."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Construir marco conceptual-normativo.",
      "Contrastar fuentes relevantes.",
      "Fijar postura propia argumentada.",
      "Derivar conclusion desde el analisis."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco conceptual-normativo",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion estructurada",
        "Trazabilidad bibliografica"
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
          "justification": "La pauta editorial exige citas verificables y consistencia institucional."
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
          "justification": "La conclusion valida se deriva del razonamiento expuesto."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "supports",
          "justification": "Se evita arrastre de salidas no parseables."
        }
      ],
      "evidence": [
        "README confirma identidad UnADM y ubicacion curricular.",
        "Programa analitico fija cinco ejes de trabajo recurrentes.",
        "Memoria origen confirma regla de normalizacion previa y deduplicacion lossless."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas de identidad, estructura y calidad.",
      "Se reforzo separacion entre hechos verificados y supuestos.",
      "Se retiro transferencia de contenido especifico de actividad 1 no reutilizable.",
      "Se mantuvieron reglas tecnicas de JSON parseable y trazabilidad .tex/.bib.",
      "Se preservo ADN editorial sin recorte de patrones utiles."
    ]
  }
}