{
  "summary": [
    "Memoria lateral consolidada de Actividad 1 a Actividad 6 con union y deduplicacion lossless.",
    "Se preserva identidad UnADM y ubicacion curricular verificada: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se mantienen ejes editoriales estables: problema, conceptos o normas, producto, analisis propio y conclusion juridica transferible.",
    "Se refuerza regla critica: no propagar salidas no estructuradas; normalizar antes de reutilizar.",
    "Se conserva traza de fuentes provisionales heredadas y su estado de verificacion pendiente."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y criterios de integridad academica.",
    "Vincular toda entrega a Licenciatura en Derecho, asignatura Filosofia del Derecho.",
    "Citar ubicacion curricular al contextualizar: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar toda fuente heredada no verificada como provisional hasta confirmacion local.",
    "Conservar regla de no regresion: no eliminar reglas utiles previas."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion de memoria.",
    "Usar exactamente el esquema requerido, sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el producto final al formato pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Adaptar la redaccion al objetivo especifico de Actividad 6 sin romper ejes base de la asignatura.",
    "Distinguir de forma explicita sintesis de fuentes y postura propia.",
    "Sustentar afirmaciones relevantes con fuentes verificables disponibles.",
    "Evitar entregas solo descriptivas o sin criterio juridico propio.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Relacionar conceptos, normas y doctrina con el problema delimitado.",
    "Supuesto: si la consigna de Actividad 6 aborda interpretacion juridica, articular hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar aguas abajo.",
    "Separar reglas verificadas de supuestos marcados.",
    "Confirmar trazabilidad minima de afirmaciones relevantes a fuente o supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib activo.",
    "Revisar que la conclusion derive del desarrollo y no sea decorativa.",
    "Aplicar deduplicacion por union sin perdida de reglas vigentes."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en archivos .tex.",
    "Comprobar que toda clave citada exista en el archivo bibliografico activo.",
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico antes de fijar nombres canonicos.",
    "Marcar como supuesto cualquier nombre canonico ambiguo de archivo hasta confirmacion."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar fuentes especificas de actividad en el .bib de la asignatura.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No asumir que bibliografia de otra semana aplica automaticamente a Actividad 6.",
    "Marcar como supuesto todo dato bibliografico incompleto hasta verificarlo."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones reutilizables: identidad, estructura, calidad, conceptos y relaciones recurrentes.",
    "No propagar redaccion literal ni conclusiones especificas entre actividades hermanas.",
    "Mantener advertencias historicas de salidas no estructuradas en nodos con herencia de baja confianza.",
    "Normalizar manualmente ciclos tempranos si reaparecen artefactos no parseables.",
    "Propagar supuestos como supuestos, nunca como hechos confirmados."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual completa de Actividad 6; confirmar producto exacto solicitado.",
    "Confirmar rubrica de evaluacion especifica para ajustar profundidad argumentativa.",
    "Confirmar si Actividad 6 exige reporte, presentacion o ambos.",
    "Confirmar nombre canonico final del .bib por coexistencia de filosofia-del-derecho.bib y filosofia-del-derecho-clean.bib.",
    "Confirmar si se requiere formato de citacion juridica adicional a BibTeX institucional.",
    "Confirmar si las fuentes de interpretacion juridica de clean.bib son obligatorias o solo opcionales en Actividad 6."
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
      "Problema juridico o social delimitado.",
      "Marco conceptual y normativo pertinente.",
      "Producto alineado a planeacion semanal.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, verificables y utiles para la practica juridica.",
      "Preservar continuidad editorial entre actividades sin perder especificidad local.",
      "Asegurar calidad tecnica, argumentativa y bibliografica en cada entrega."
    ],
    "style_markers": [
      "Inicio con encuadre del problema.",
      "Secciones explicitas y ordenadas.",
      "Postura propia diferenciada de la sintesis de fuentes.",
      "Citas verificables y trazables.",
      "Cierre con criterio juridico aplicable."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer conceptos y normas aplicables.",
      "Contrastar fuentes relevantes.",
      "Desarrollar postura propia fundada.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco normativo y doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Hermenutica juridica [supuesto condicionado por consigna]",
        "Argumentacion juridica [supuesto condicionado por consigna]"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
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
          "justification": "La argumentacion requiere un problema delimitado."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida debe derivar del desarrollo."
        },
        {
          "source": "Marco normativo y doctrinal",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "El analisis gana solidez cuando se ancla en normas y doctrina."
        },
        {
          "source": "Hermenutica juridica [supuesto condicionado por consigna]",
          "target": "Argumentacion juridica [supuesto condicionado por consigna]",
          "kind": "supports",
          "justification": "Si la actividad trata interpretacion, la hermeneutica sustenta la argumentacion."
        }
      ],
      "evidence": [
        "README confirma identidad UnADM, ubicacion curricular y pauta editorial.",
        "Programa analitico fija cinco ejes de trabajo recurrentes.",
        "Existe historial de salida no parseable; se mantiene gate de normalizacion.",
        "Coexisten dos .bib locales; se requiere confirmacion de canonico."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin perdida semantica.",
      "Se preservaron reglas utiles previas de identidad, estructura, calidad y LaTeX.",
      "Se evitaron conclusiones especificas de Actividad 1 por ser nodo hermano.",
      "Se anadieron solo refuerzos verificables desde README, programa analitico y estado de archivos.",
      "Se marcaron supuestos donde faltan datos locales de consigna."
    ]
  }
}