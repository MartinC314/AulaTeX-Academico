{
  "summary": [
    "Se consolida refuerzo lateral desde actividad 1 a actividad 6 con union y deduplicacion sin perdida.",
    "Se preserva identidad UnADM y ubicacion curricular verificada: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se refuerzan ejes editoriales estables: problema, conceptos o normas, producto, analisis propio y conclusion juridica transferible.",
    "Se mantiene regla critica: no propagar salidas no estructuradas; normalizar antes de reutilizar.",
    "Se mantiene uso de fuentes verificables y marcacion explicita de supuestos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear toda actividad a Licenciatura en Derecho y asignatura Filosofia del Derecho.",
    "Citar ubicacion curricular al contextualizar: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar como provisional toda fuente heredada no verificada localmente.",
    "Conservar regla de no regresion editorial en consolidaciones."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de memoria editorial.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Estructurar productos con: problema, marco conceptual o normativo, desarrollo, analisis propio y conclusion.",
    "Definir objetivo puntual antes del desarrollo.",
    "Cerrar con conclusion juridica transferible a la practica.",
    "Alinear el tipo de producto a la planeacion semanal y consigna vigente."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de actividad 6 sin romper ejes base.",
    "Explicitar el problema juridico o social que activa la respuesta.",
    "Relacionar conceptos, normas o doctrina con el problema planteado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir sintesis de fuente y postura propia.",
    "Evitar entregas solo descriptivas y generalizaciones sin anclaje juridico.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Separar reglas verificadas de supuestos marcados.",
    "Validar trazabilidad de afirmaciones relevantes a fuente o supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib activo.",
    "No eliminar reglas utiles previas durante consolidacion."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener claves BibTeX estables ya citadas.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: nombre canonico esperado del .bib es filosofia-del-derecho.bib hasta confirmacion local."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas oficiales o academicas.",
    "Registrar fuentes especificas de la actividad en el .bib de la asignatura.",
    "Conservar metadatos minimos: autor, titulo, ano, editorial o nota, URL cuando exista.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a actividad de interpretacion juridica y no sustituye automaticamente el .bib canonico."
  ],
  "propagation_hints": [
    "Propagar a nodos hermanos solo reglas reutilizables y verificadas.",
    "Aplicar union-dedupe lossless y evitar duplicados semanticos.",
    "No transferir redaccion literal ni conclusiones especificas entre hermanos.",
    "Si falta consigna local, propagar estructura base y preguntas abiertas.",
    "Mantener advertencia historica de salidas no estructuradas en ciclos tempranos.",
    "Normalizar manualmente memorias heredadas de baja confianza antes de reutilizar."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual completa de actividad 6; confirmar producto exacto solicitado.",
    "Confirmar rubrica especifica de evaluacion de actividad 6.",
    "Confirmar si actividad 6 exige reporte, presentacion o ambos.",
    "Confirmar nombre canonico final del archivo .bib por token Slug sin resolver en README.",
    "Confirmar si se requiere formato adicional de citacion juridica aparte de BibTeX.",
    "Confirmar si el corpus de hermeneutica y tesis SCJN aplica formalmente a actividad 6."
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
      "Conceptos, normas y doctrina pertinentes.",
      "Producto alineado a planeacion.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir la planeacion semanal en productos academicos con fundamento juridico y utilidad profesional.",
      "Preservar coherencia metodologica entre actividades hermanas sin perder especificidad local."
    ],
    "style_markers": [
      "Inicio con encuadre breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Citas verificables y supuestos marcados.",
      "Postura propia diferenciada de la sintesis.",
      "Cierre con criterio juridico aplicable."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Construir marco conceptual o normativo.",
      "Contrastar fuentes relevantes.",
      "Desarrollar postura propia fundamentada.",
      "Derivar conclusion desde el analisis."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion JSON",
        "Hermeneutica juridica",
        "Argumentacion juridica"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "README.md de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib"
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
          "justification": "El analisis requiere un problema delimitado."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion debe derivar del razonamiento previo."
        },
        {
          "source": "Hermeneutica juridica",
          "target": "Argumentacion juridica",
          "kind": "supports",
          "justification": "Si la consigna trata interpretacion, la hermeneutica fundamenta la argumentacion."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "No se propaga contenido no estructurado."
        }
      ],
      "evidence": [
        "README: identidad UnADM, ubicacion curricular y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo recurrentes.",
        "Memoria origen: regla de normalizacion previa y ejes editoriales estables.",
        "Contexto local: coexistencia de .bib canonico y .bib clean con uso condicionado."
      ]
    },
    "reinforcement_log": [
      "Ciclo 57: se refuerza lateralmente identidad, estructura y control de calidad sin copiar contenido especifico del hermano.",
      "Ciclo 57: se depuran duplicados y se preservan reglas utiles previas.",
      "Ciclo 57: se mantiene trazabilidad de supuestos sobre consigna y nombre canonico del .bib."
    ]
  }
}