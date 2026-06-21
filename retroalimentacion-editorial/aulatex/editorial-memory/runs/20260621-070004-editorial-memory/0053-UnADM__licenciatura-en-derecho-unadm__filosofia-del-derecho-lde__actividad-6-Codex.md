{
  "summary": [
    "Se consolida memoria lateral A1->A6 con union y deduplicacion sin perdida.",
    "Se preserva identidad UnADM y ubicacion curricular verificada.",
    "Se mantiene regla critica: normalizar antes de propagar cualquier salida.",
    "Se refuerzan ejes estables: problema, conceptos, producto, analisis propio, conclusion juridica.",
    "Se evita transferir conclusiones o bibliografia exclusiva de A1 a A6."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear contenido a Licenciatura en Derecho y asignatura Filosofia del Derecho.",
    "Usar ubicacion curricular al contextualizar: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido y sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio, cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Cerrar con conclusion juridica transferible a la practica.",
    "Alinear el producto final a la consigna semanal real."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Distinguir sintesis de fuentes y postura propia.",
    "Sustentar afirmaciones relevantes con fuentes verificables.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir que fuentes de otras semanas aplican automaticamente a Actividad 6.",
    "Supuesto: si A6 trata interpretacion juridica, vincular hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar.",
    "Separar reglas confirmadas de supuestos marcados.",
    "No eliminar reglas utiles previas en consolidacion.",
    "Verificar trazabilidad de afirmaciones a fuente o supuesto.",
    "Validar consistencia entre citas en texto y .bib activo.",
    "Revisar que la conclusion derive del analisis y no sea decorativa."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre .tex y .bib.",
    "No cambiar claves BibTeX ya citadas.",
    "Comprobar que toda clave citada exista en el .bib usado.",
    "Usar acentos y codificacion correctos en espanol.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: .bib canonico esperado por Slug es filosofia-del-derecho.bib hasta confirmacion final."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar fuentes especificas de actividad en el .bib de la asignatura.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No forzar uso de filosofia-del-derecho-clean.bib fuera de su contexto si la consigna no lo exige."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir a hermanos solo patrones reutilizables, no redaccion literal.",
    "Mantener union-dedupe lossless como metodo de compresion.",
    "Conservar advertencias historicas sobre salidas no estructuradas.",
    "Si falta consigna local, propagar estructura base y abrir preguntas en lugar de inventar."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 6.",
    "Confirmar rubrica especifica de evaluacion de Actividad 6.",
    "Confirmar formato principal exigido: reporte, presentacion u otro.",
    "Confirmar nombre canonico final del .bib por coexistencia de archivos y token Slug sin resolver.",
    "Confirmar si A6 requiere corpus de interpretacion juridica o otro eje tematico."
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
        "Entrada canonica en carpeta de asignatura."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Filosofia del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social delimitado.",
      "Conceptos y normas pertinentes.",
      "Producto alineado a planeacion.",
      "Analisis propio con postura argumentada.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables.",
      "Garantizar coherencia juridica, trazabilidad de fuentes y utilidad profesional."
    ],
    "style_markers": [
      "Inicio con encuadre breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Postura propia diferenciada de la sintesis.",
      "Cierre con criterio juridico aplicable."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Construir marco conceptual y normativo.",
      "Contrastar fuentes relevantes.",
      "Sostener postura propia con evidencia.",
      "Concluir en terminos juridicos transferibles."
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
        "README.md de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "hernandezManriquezHermeneutica2019 [uso condicionado]",
        "scjnMemoriaArgumentacion2008 [uso condicionado]"
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
          "justification": "El analisis requiere un problema delimitado."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida deriva del desarrollo argumentativo."
        },
        {
          "source": "Hermeneutica juridica [supuesto condicionado a consigna]",
          "target": "Argumentacion juridica [supuesto condicionado a consigna]",
          "kind": "supports",
          "justification": "En actividades de interpretacion, la hermeneutica fundamenta la argumentacion."
        }
      ],
      "evidence": [
        "README: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo.",
        "Historial: regla de bloqueo ante salida no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 53: se refuerza normalizacion estructurada obligatoria antes de propagacion.",
      "Ciclo 53: se preserva ADN institucional y curricular sin recorte.",
      "Ciclo 53: se limita transferencia a patrones reutilizables entre hermanos.",
      "Ciclo 53: se marcan supuestos tematicos de A6 sin inventar contenido local."
    ]
  }
}