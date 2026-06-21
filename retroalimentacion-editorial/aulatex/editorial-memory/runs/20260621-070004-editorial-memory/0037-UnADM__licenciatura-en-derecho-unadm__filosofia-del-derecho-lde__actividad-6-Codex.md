{
  "summary": [
    "Se consolida memoria lateral entre actividades hermanas con union y deduplicacion sin perdida.",
    "Se preserva ADN institucional UnADM y encuadre curricular verificado de Filosofia del Derecho.",
    "Se refuerza regla critica: no propagar contenido no estructurado; normalizar antes de reutilizar.",
    "Se mantienen ejes editoriales estables: problema, conceptos o normas, producto, analisis propio y conclusion transferible.",
    "Se mantiene separacion entre reglas confirmadas y supuestos marcados."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y trazabilidad academica.",
    "Alinear toda entrega a Licenciatura en Derecho, asignatura Filosofia del Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Citar la malla curricular de Derecho UnADM cuando se declare ubicacion curricular."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido, sin claves extra.",
    "Estructurar productos academicos en: problema, marco conceptual-normativo, desarrollo, analisis propio y conclusion.",
    "Definir objetivo puntual antes del desarrollo.",
    "Cerrar con conclusion juridica derivada del analisis y transferible a la practica."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base de la asignatura.",
    "Explicitar el problema juridico o social que activa la respuesta.",
    "Relacionar conceptos, normas, doctrina o datos con el problema planteado.",
    "Distinguir sintesis de fuentes y postura propia.",
    "Evitar entregas solo descriptivas o generalizaciones sin anclaje juridico.",
    "Sustentar afirmaciones relevantes con fuentes verificables y cita explicita."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Separar afirmaciones respaldadas de supuestos marcados.",
    "No eliminar reglas utiles previas durante consolidacion.",
    "Aplicar compresion lossless por union y deduplicacion."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en archivos .tex.",
    "Verificar que toda clave citada exista en el .bib activo.",
    "Usar acentos y codificacion correcta en español en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y documentos operativos.",
    "Marcar como supuesto el nombre canonico del .bib si persiste ambiguedad."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y juridicas oficiales o academicas.",
    "Registrar fuentes especificas de actividad en el .bib de la asignatura.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No asumir que un .bib tematico de otra semana aplica automaticamente a Actividad 6."
  ],
  "propagation_hints": [
    "Propagar a nodos hermanos solo reglas reutilizables de identidad, estructura, calidad y metodo.",
    "No transferir redaccion literal ni conclusiones especificas entre hermanos.",
    "Mantener advertencias historicas sobre salidas no estructuradas heredadas.",
    "Propagar supuestos como supuestos, no como hechos confirmados.",
    "Aplicar normalizacion manual cuando haya herencia de ciclos con baja confianza."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual completa de Actividad 6; confirmar producto exacto solicitado.",
    "Confirmar rubrica especifica de evaluacion para calibrar profundidad argumentativa.",
    "Confirmar si Actividad 6 exige formato de citacion juridica adicional a BibTeX.",
    "Confirmar nombre canonico final del .bib de asignatura por coexistencia de archivos y token Slug sin resolver.",
    "Supuesto: si el foco es interpretacion juridica, confirmar obligatoriedad de corpus de hermeneutica y tesis SCJN."
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
      "Base conceptual y normativa pertinente.",
      "Producto alineado a planeacion.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico, evidencia y criterio propio.",
      "Garantizar consistencia institucional y tecnica en memoria editorial reutilizable."
    ],
    "style_markers": [
      "Apertura con encuadre breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Citas verificables con postura personal diferenciada.",
      "Cierre aplicable a practica profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco conceptual-normativo.",
      "Contrastar fuentes pertinentes.",
      "Tomar postura razonada.",
      "Derivar conclusion del analisis."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion estructurada",
        "Hermeneutica juridica [supuesto condicionado]"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "programa-analitico-filosofia-del-derecho.md",
        "README.md"
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
          "justification": "No hay analisis valido sin delimitacion previa del problema."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion debe derivar del razonamiento y evidencia."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita propagacion de errores y conserva trazabilidad editorial."
        }
      ],
      "evidence": [
        "README: identidad UnADM, ubicacion curricular y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo.",
        "Historial de ciclos: incidentes de salida no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 37: deduplicacion completa de reglas repetidas en origen y destino.",
      "Ciclo 37: se conserva regla de no regresion y no eliminacion de reglas utiles.",
      "Ciclo 37: se refuerza control de supuestos ante falta de consigna local completa.",
      "Ciclo 37: se mantiene transferencia lateral solo de patrones reutilizables."
    ]
  }
}