{
  "summary": [
    "Se consolida memoria lateral de Actividad 1 a Actividad 6 con union y deduplicacion sin perdida.",
    "Se preserva identidad UnADM y ubicacion curricular verificada: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se refuerzan ejes editoriales estables: problema, conceptos o normas, producto, analisis propio y conclusion juridica transferible.",
    "Se mantiene regla critica de normalizacion: no propagar contenido no estructurado ni JSON invalido.",
    "Se agregan mejoras verificables: marcar supuestos, separar reglas confirmadas y controlar trazabilidad de fuentes."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear toda entrega a Licenciatura en Derecho y asignatura Filosofia del Derecho.",
    "Usar ubicacion curricular verificada: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar toda fuente heredada no verificada como provisional hasta confirmacion local.",
    "Conservar no regresion: no eliminar reglas utiles previas."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el producto final a la consigna semanal real.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Explicitar problema juridico o social desde el inicio.",
    "Relacionar conceptos, normas y doctrina con el problema planteado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir sintesis de fuentes y postura propia.",
    "Evitar entregas solo descriptivas.",
    "No asumir automaticamente que bibliografia de otra semana aplica a Actividad 6.",
    "Supuesto: si la consigna trata interpretacion juridica, articular hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de propagar.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Validar consistencia entre citas en texto y archivo .bib activo.",
    "Verificar que el producto corresponda a la consigna local de Actividad 6.",
    "Aplicar deduplicacion por union sin perdida de reglas vigentes."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Corregir caracteres anomalos en rutas y nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: el .bib canonico esperado es filosofia-del-derecho.bib, confirmar localmente."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas oficiales o academicas.",
    "Registrar fuentes especificas de actividad en el .bib de la asignatura.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Mantener metadatos minimos: autor, titulo, ano, editor o nota, URL cuando exista.",
    "Marcar como supuesto todo dato bibliografico incompleto.",
    "No asumir que filosofia-del-derecho-clean.bib aplica automaticamente a Actividad 6."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones reutilizables; no copiar conclusiones ni redaccion literal.",
    "Mantener advertencia historica sobre salidas no estructuradas en ciclos previos.",
    "Etiquetar reglas de baja confianza como provisionales.",
    "Propagar identidad curricular verificada a nodos hermanos.",
    "Aplicar analogia controlada: conservar ADN editorial y ajustar solo al objetivo local."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual completa de Actividad 6; confirmar producto exacto.",
    "Confirmar rubrica especifica de evaluacion para calibrar profundidad argumentativa.",
    "Confirmar si Actividad 6 exige reporte, presentacion u otro formato principal.",
    "Confirmar nombre canonico final del .bib por token Slug sin resolver en README.",
    "Confirmar si se requiere formato de citacion juridica adicional a BibTeX.",
    "Confirmar si las fuentes de interpretacion juridica de clean.bib son obligatorias o solo opcionales."
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
      "Transformar planeacion semanal en productos academicos solidos.",
      "Garantizar fundamento juridico, evidencia verificable y utilidad profesional.",
      "Preservar continuidad editorial entre actividades hermanas."
    ],
    "style_markers": [
      "Inicio con encuadre breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Postura propia diferenciada de la sintesis.",
      "Cierre con aplicacion juridica concreta.",
      "Supuestos marcados de forma visible."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual y normativo.",
      "Contrastar fuentes verificables.",
      "Sostener postura propia argumentada.",
      "Derivar conclusion desde el analisis."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Analisis propio",
        "Conclusion transferible",
        "Hermeneutica juridica",
        "Argumentacion juridica",
        "Normalizacion JSON"
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
          "justification": "La pauta institucional exige evidencia verificable y formato consistente."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin problema delimitado no hay argumentacion juridica valida."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion debe derivar del desarrollo y no ser decorativa."
        },
        {
          "source": "Hermeneutica juridica",
          "target": "Argumentacion juridica",
          "kind": "supports",
          "justification": "En actividades de interpretacion, la hermeneutica fundamenta la justificacion."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Integridad academica",
          "kind": "depends_on",
          "justification": "La memoria solo es propagable si es estructurada y verificable."
        }
      ],
      "evidence": [
        "README de asignatura: identidad y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo.",
        "Regla historica: bloquear propagacion de salidas no parseables.",
        "Existencia local de clean.bib para interpretacion juridica con uso condicionado por consigna."
      ]
    },
    "reinforcement_log": [
      "Ciclo 22: deduplicacion lossless aplicada sin recorte.",
      "Ciclo 22: se preservan reglas de calidad de Actividad 1 y se adaptan lateralmente a Actividad 6.",
      "Ciclo 22: se mantienen supuestos abiertos donde falta dato local verificable."
    ]
  }
}