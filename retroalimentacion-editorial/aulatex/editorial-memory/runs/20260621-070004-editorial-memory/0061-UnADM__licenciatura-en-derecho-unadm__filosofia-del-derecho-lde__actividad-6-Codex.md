{
  "summary": [
    "Se consolida memoria lateral de actividad 1 hacia actividad 6 con union y deduplicacion sin perdida.",
    "Se preserva identidad UnADM, ubicacion curricular y ejes editoriales base de Filosofia del Derecho.",
    "Se mantiene regla critica: no propagar contenido no estructurado sin normalizacion previa.",
    "Se refuerza uso de supuestos marcados cuando falte consigna local verificable.",
    "Se conserva separacion entre reglas generales reutilizables y contenido especifico no transferible entre hermanos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar regla de no regresion: no eliminar reglas utiles previas."
  ],
  "structure_rules": [
    "Entregar consolidaciones en JSON valido y parseable.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el producto al formato solicitado por la planeacion semanal."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes de asignatura.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir sintesis de fuentes y postura propia del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Supuesto: si la consigna aborda interpretacion juridica, vincular hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Separar reglas confirmadas de supuestos marcados.",
    "Validar trazabilidad de afirmaciones relevantes a fuente o supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No eliminar reglas utiles previas durante consolidacion."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener compatibilidad entre .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en .tex.",
    "Comprobar que toda clave citada exista en el archivo bibliografico activo.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico antes de fijar nombres canonicos."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar fuentes especificas de la actividad en el .bib de la asignatura.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Marcar como supuesto todo dato bibliografico incompleto hasta verificarlo.",
    "Supuesto: filosofia-del-derecho-clean.bib puede corresponder a semana tematica especifica y no reemplaza automaticamente el .bib canonico de materia."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones reutilizables: identidad, estructura, calidad, conceptos y relaciones recurrentes.",
    "No transferir redaccion literal ni conclusiones especificas entre actividades hermanas.",
    "Propagar reglas generales cuando falte consigna textual local.",
    "Mantener advertencias historicas de salidas no parseables para prevenir regresiones.",
    "Aplicar union-dedupe lossless en cada ciclo."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 6.",
    "Confirmar rubrica de evaluacion especifica de Actividad 6.",
    "Confirmar si el producto principal es reporte, presentacion u otro formato.",
    "Confirmar nombre canonico final del archivo .bib de la asignatura.",
    "Confirmar si Actividad 6 exige formato de citacion juridica adicional a BibTeX.",
    "Confirmar si las fuentes de interpretacion juridica de clean.bib aplican formalmente a Actividad 6."
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
      "Conceptos, normas o doctrina pertinente.",
      "Producto segun planeacion.",
      "Analisis propio con postura.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico y utilidad profesional.",
      "Sostener aprendizaje argumentativo con evidencia verificable."
    ],
    "style_markers": [
      "Inicio con encuadre breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Diferenciacion visible entre fuente y postura propia.",
      "Cierre con criterio juridico aplicable."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Construir marco conceptual-normativo.",
      "Relacionar evidencia con el caso o pregunta.",
      "Tomar postura fundamentada.",
      "Derivar conclusion del analisis."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Analisis propio",
        "Conclusion transferible",
        "Hermeneutica juridica [supuesto condicionado a consigna]",
        "Argumentacion juridica [supuesto condicionado a consigna]"
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
          "justification": "La pauta institucional exige citas verificables y consistencia formal."
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
          "justification": "La conclusion valida debe derivar del razonamiento expuesto."
        },
        {
          "source": "Hermeneutica juridica [supuesto condicionado a consigna]",
          "target": "Argumentacion juridica [supuesto condicionado a consigna]",
          "kind": "supports",
          "justification": "En actividades de interpretacion, la hermeneutica fundamenta la argumentacion."
        }
      ],
      "evidence": [
        "README de asignatura: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo estables.",
        "Regla historica consolidada: normalizar antes de propagar contenido no estructurado."
      ]
    },
    "reinforcement_log": [
      "Ciclo 61: se reforzo ADN institucional y estructura argumentativa comun sin copiar contenido especifico de Actividad 1.",
      "Ciclo 61: se mantuvo compresion lossless por deduplicacion y no por recorte.",
      "Ciclo 61: se agregaron supuestos marcados solo donde faltan datos locales verificables."
    ]
  }
}