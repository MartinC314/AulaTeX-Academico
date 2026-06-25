{
  "summary": [
    "Se consolida refuerzo lateral desde Actividad 1 hacia Actividad 6 con union-dedupe lossless.",
    "Se preserva identidad UnADM y ubicacion curricular verificada: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se mantienen ejes editoriales estables: problema, conceptos o normas, producto, analisis propio y conclusion juridica transferible.",
    "Se refuerza regla critica: no propagar contenido no estructurado; normalizar antes de reutilizar.",
    "Se mantiene traza de fuentes provisionales heredadas hasta validacion local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear cada entrega a Licenciatura en Derecho y asignatura Filosofia del Derecho.",
    "Reconocer al contextualizar: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar regla de no regresion: no eliminar reglas utiles previas."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el producto al formato exigido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Explicitar problema, no solo tema general.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Diferenciar sintesis de fuente y postura propia.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Supuesto: si la consigna es de interpretacion juridica, vincular hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de propagar.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar trazabilidad de afirmaciones relevantes a fuente o supuesto marcado.",
    "Validar consistencia entre citas en texto y archivo .bib activo.",
    "No eliminar reglas utiles previas durante consolidacion.",
    "Separar reglas confirmadas de supuestos editoriales."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Marcar como supuesto el nombre canonico de .bib mientras exista ambiguedad."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar fuentes especificas de la actividad en el .bib de la asignatura.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Supuesto: filosofia-del-derecho-clean.bib esta orientado a actividad de interpretacion juridica y no aplica por defecto a toda actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones reutilizables, no redaccion literal ni conclusiones especificas.",
    "Propagar identidad curricular verificada a nodos hermanos.",
    "Mantener advertencias historicas de salidas no parseables en nodos con herencia dudosa.",
    "Aplicar union-dedupe lossless y evitar recorte de reglas vigentes.",
    "Cuando falte consigna local, propagar estructura base y abrir preguntas."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 6.",
    "Confirmar rubrica especifica de evaluacion de Actividad 6.",
    "Confirmar si Actividad 6 exige reporte, presentacion u otro producto principal.",
    "Confirmar nombre canonico final del .bib de la asignatura por token Slug sin resolver.",
    "Confirmar si se exige formato juridico de citacion adicional a BibTeX.",
    "Confirmar si las fuentes de hermeneutica/SCJN son obligatorias o solo opcionales para Actividad 6."
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
      "Problema juridico o social como punto de partida.",
      "Marco conceptual y normativo pertinente.",
      "Producto alineado a planeacion.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos con fundamento juridico, evidencia y utilidad profesional.",
      "Asegurar consistencia editorial institucional entre actividades hermanas."
    ],
    "style_markers": [
      "Inicio con encuadre breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Citas verificables con diferenciacion de voz propia.",
      "Cierre con criterio juridico aplicable."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Presentar conceptos y normas aplicables.",
      "Contrastar fuentes.",
      "Sostener postura propia.",
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
        "Hermeneutica juridica [supuesto condicionado por consigna]",
        "Argumentacion juridica [supuesto condicionado por consigna]"
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
          "justification": "La conclusion debe derivar del razonamiento expuesto."
        },
        {
          "source": "Hermeneutica juridica [supuesto]",
          "target": "Argumentacion juridica [supuesto]",
          "kind": "supports",
          "justification": "Si la actividad trata interpretacion, la hermeneutica fundamenta la argumentacion."
        }
      ],
      "evidence": [
        "README de asignatura: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo.",
        "Regla historica consolidada: normalizar antes de propagar.",
        "Existencia de clean.bib orientado a interpretacion juridica (uso condicionado por consigna)."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin perdida semantica.",
      "Se conservaron reglas utiles previas y se eliminaron solo duplicados literales.",
      "Se marco explicitamente el uso de supuestos cuando faltan datos locales.",
      "Se evitaron traslados de conclusiones especificas de Actividad 1 hacia Actividad 6."
    ]
  }
}