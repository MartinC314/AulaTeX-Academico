{
  "summary": [
    "Se consolida memoria lateral de Actividad 1 hacia Actividad 6 con union-dedupe sin perdida.",
    "Se preserva identidad UnADM y ubicacion curricular verificada: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se mantienen ejes editoriales base: problema, conceptos o normas, producto, analisis propio y conclusion juridica transferible.",
    "Se refuerza regla critica: no propagar salidas no estructuradas; normalizar antes de reutilizar.",
    "Se mantiene trazabilidad de fuentes y marcacion explicita de supuestos cuando falte consigna local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear contenido a Licenciatura en Derecho, asignatura Filosofia del Derecho.",
    "Reconocer ubicacion curricular al contextualizar: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar regla de no regresion: no eliminar reglas utiles previas."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion de memoria.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual de la actividad antes del desarrollo.",
    "Alinear el producto final a la planeacion semanal de la actividad 6.",
    "Cerrar con conclusion juridica derivada del analisis y transferible a la practica."
  ],
  "activity_rules": [
    "Adaptar la redaccion al objetivo especifico de actividad 6 sin romper ejes base.",
    "Distinguir con claridad sintesis de fuentes y postura propia.",
    "Sustentar afirmaciones relevantes con fuentes verificables.",
    "Evitar entregas solo descriptivas o sin argumentacion juridica.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir automaticamente que bibliografia de otra semana aplica a actividad 6.",
    "Supuesto: si la consigna trata interpretacion juridica, articular hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar cualquier respuesta no estructurada antes de reutilizar.",
    "Confirmar que cada afirmacion relevante tenga fuente o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib activo.",
    "Verificar que la conclusion derive del desarrollo y no sea decorativa.",
    "Separar reglas verificadas de supuestos editoriales."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Comprobar que toda clave citada exista en el .bib usado.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Marcar como supuesto el nombre canonico del .bib mientras exista ambiguedad por token no resuelto."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos oficiales o academicos.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Registrar fuentes de actividad en el .bib de la asignatura.",
    "Conservar metadatos minimos: autor, titulo, ano, editorial o nota, URL cuando exista.",
    "Supuesto: filosofia-del-derecho-clean.bib parece orientado a interpretacion juridica de semana especifica; confirmar aplicacion a actividad 6."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Aplicar union-dedupe lossless en nodos hermanos para evitar regresiones.",
    "Transferir solo patrones reutilizables: identidad, estructura, calidad, conceptos y relaciones recurrentes.",
    "No copiar conclusiones especificas ni bibliografia exclusiva entre hermanos sin validacion local.",
    "Mantener advertencia historica sobre salidas no parseables en ciclos tempranos.",
    "Cuando falte consigna local, propagar plantilla base y abrir preguntas, no inventar contenido."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de actividad 6; confirmar producto exacto solicitado.",
    "Confirmar rubrica de evaluacion especifica para ajustar profundidad argumentativa.",
    "Confirmar si actividad 6 exige reporte, presentacion u otro formato principal.",
    "Confirmar nombre canonico final del archivo .bib por token Slug sin resolver en README.",
    "Confirmar si se requiere formato de citacion juridica adicional a BibTeX.",
    "Confirmar si las fuentes de hermeneutica y tesis SCJN son obligatorias o solo opcionales para actividad 6."
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
      "Analisis propio con postura argumentada.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos utiles y verificables.",
      "Sostener decisiones editoriales con estructura, evidencia y criterio juridico propio."
    ],
    "style_markers": [
      "Inicio con encuadre del problema.",
      "Secciones explicitas y ordenadas.",
      "Diferenciacion entre fuente y postura personal.",
      "Cierre con utilidad profesional juridica.",
      "Marcacion transparente de supuestos."
    ],
    "argumentative_patterns": [
      "Delimitar problema antes de definir tesis.",
      "Conectar conceptos y normas con hechos o pregunta guia.",
      "Contrastar fuentes y justificar seleccion.",
      "Desarrollar postura propia sustentada.",
      "Derivar conclusion del analisis previo."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco conceptual-normativo",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion de salidas",
        "Trazabilidad de fuentes",
        "Hermeneutica juridica [supuesto condicionado a consigna]",
        "Argumentacion juridica [supuesto condicionado a consigna]"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/programa-analitico-filosofia-del-derecho.md",
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
          "justification": "El analisis requiere un problema delimitado para ser evaluable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida debe derivar del desarrollo argumentativo."
        },
        {
          "source": "Normalizacion de salidas",
          "target": "Trazabilidad de fuentes",
          "kind": "supports",
          "justification": "La estructura valida facilita control de citas y supuestos."
        },
        {
          "source": "Hermeneutica juridica [supuesto condicionado a consigna]",
          "target": "Argumentacion juridica [supuesto condicionado a consigna]",
          "kind": "supports",
          "justification": "Si la actividad trata interpretacion, la hermeneutica fundamenta la argumentacion."
        }
      ],
      "evidence": [
        "README confirma identidad UnADM, ubicacion curricular y pauta editorial.",
        "Programa analitico confirma cinco ejes de trabajo recurrentes.",
        "Historial confirma necesidad de bloquear salidas no JSON parseables.",
        "Coexistencia de filosofia-del-derecho.bib y filosofia-del-derecho-clean.bib exige validacion local por actividad."
      ]
    },
    "reinforcement_log": [
      "Ciclo 52: se refuerza transferencia lateral por patrones, sin copiar contenido especifico.",
      "Ciclo 52: se conserva regla de normalizacion obligatoria antes de propagacion recursiva.",
      "Ciclo 52: se mantiene compresion lossless por deduplicacion semantica.",
      "Ciclo 52: se consolidan preguntas abiertas donde falta evidencia local de consigna."
    ]
  }
}