{
  "summary": [
    "Se consolida memoria lateral de Actividad 1 hacia Actividad 6 con union y deduplicacion sin perdida.",
    "Se preserva identidad institucional UnADM y ubicacion curricular verificada.",
    "Se mantienen ejes editoriales estables: problema, conceptos, producto, analisis propio y conclusion transferible.",
    "Se refuerza regla critica: no propagar salidas no estructuradas; normalizar antes de reutilizar.",
    "Se conserva separacion entre reglas confirmadas y supuestos marcados."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear toda actividad a Licenciatura en Derecho y asignatura Filosofia del Derecho.",
    "Citar ubicacion curricular cuando aplique: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar regla de no regresion editorial en consolidaciones."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de memoria.",
    "Usar exactamente el esquema requerido y sin claves extra.",
    "Estructurar productos academicos con: problema, marco conceptual-normativo, desarrollo, analisis propio y conclusion.",
    "Definir objetivo puntual antes del desarrollo.",
    "Cerrar con conclusion juridica derivada del analisis y transferible a practica profesional.",
    "Alinear formato final al producto pedido por la planeacion semanal."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Delimitar problema juridico o social desde el inicio.",
    "Relacionar conceptos, normas, doctrina o datos con el problema planteado.",
    "Distinguir sintesis de fuentes y postura propia.",
    "Sustentar afirmaciones relevantes con fuentes verificables.",
    "Evitar desarrollo solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Supuesto: si la consigna trata interpretacion juridica, vincular hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar aguas abajo.",
    "Revisar que no haya contenido no estructurado sin normalizar.",
    "Confirmar trazabilidad de afirmaciones a fuente o supuesto marcado.",
    "Validar consistencia entre citas en texto y archivo .bib activo.",
    "No eliminar reglas utiles previas durante consolidacion.",
    "Aplicar compresion lossless por union y deduplicacion."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en .tex.",
    "Comprobar que toda clave citada exista en el .bib usado.",
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico antes de fijar nombres canonicos.",
    "Marcar como supuesto cualquier nombre de archivo ambiguo hasta confirmacion."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Registrar fuentes especificas de actividad en el .bib de la asignatura.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No asumir que clean.bib aplica automaticamente a Actividad 6 sin consigna local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones reutilizables; no transferir conclusiones especificas de un hermano.",
    "Conservar advertencias historicas sobre salidas no parseables en nodos con herencia similar.",
    "Propagar identidad curricular verificada a actividades hermanas de la misma asignatura.",
    "Si falta consigna local, propagar estructura base y preguntas abiertas.",
    "Mantener union-dedupe lossless en cada ciclo."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual completa de Actividad 6; confirmar producto exacto solicitado.",
    "Confirmar rubrica especifica de evaluacion de Actividad 6.",
    "Confirmar si Actividad 6 exige reporte, presentacion o ambos.",
    "Confirmar si se requiere formato de citacion juridica adicional a BibTeX.",
    "Confirmar nombre canonico final del .bib de asignatura por token Slug sin resolver.",
    "Confirmar si filosofia-del-derecho-clean.bib se usa en Actividad 6 o solo en Semana 7."
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
      "Producto alineado a planeacion.",
      "Analisis propio con postura.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Estandarizar productos academicos con identidad UnADM y calidad verificable.",
      "Convertir planeacion semanal en entregables argumentados y trazables.",
      "Asegurar continuidad editorial entre actividades hermanas sin perder contexto."
    ],
    "style_markers": [
      "Apertura con encuadre breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Citas verificables con postura personal diferenciada.",
      "Cierre con utilidad juridica profesional.",
      "Marcado explicito de supuestos."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Construir marco conceptual-normativo.",
      "Contrastar fuentes.",
      "Sostener postura propia.",
      "Concluir desde evidencia y analisis."
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
        "Hermeneutica juridica [supuesto condicionado a consigna]",
        "Argumentacion juridica [supuesto condicionado a consigna]"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
        "README.md de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib [uso condicionado]"
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
          "justification": "El analisis requiere delimitacion previa del problema."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida deriva del desarrollo argumentativo."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "supports",
          "justification": "Sin JSON valido no hay transferencia segura entre nodos."
        },
        {
          "source": "Hermeneutica juridica [supuesto condicionado a consigna]",
          "target": "Argumentacion juridica [supuesto condicionado a consigna]",
          "kind": "supports",
          "justification": "En actividades de interpretacion, la hermeneutica fundamenta la argumentacion."
        }
      ],
      "evidence": [
        "README confirma identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico confirma cinco ejes de trabajo.",
        "Memoria de origen confirma regla de no propagar salidas no estructuradas.",
        "Contexto local confirma coexistencia de .bib canonico y clean.bib con uso distinto."
      ]
    },
    "reinforcement_log": [
      "Ciclo 44: deduplicacion completa de reglas repetidas y variantes ortograficas.",
      "Ciclo 44: se mantiene advertencia de fuentes provisionales heredadas.",
      "Ciclo 44: se refuerza transferencia por patrones y no por contenido especifico entre hermanos.",
      "Ciclo 44: se conserva criterio lossless sin recorte de reglas utiles previas."
    ]
  }
}