{
  "summary": [
    "Se consolida refuerzo lateral de Actividad 1 a Actividad 6 con union y deduplicacion sin perdida.",
    "Se preserva identidad UnADM y ubicacion curricular verificada: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se mantiene regla critica: no propagar contenido no estructurado sin normalizacion previa.",
    "Se refuerzan ejes estables: problema, conceptos o normas, producto, analisis propio y conclusion juridica.",
    "Se conserva separacion entre reglas verificadas y supuestos marcados."
  ],
  "identity_rules": [
    "Mantener tono institucional UnADM en toda entrega.",
    "Alinear contenido a Licenciatura en Derecho, asignatura Filosofia del Derecho.",
    "Citar ubicacion curricular al contextualizar: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar regla de no regresion editorial en consolidaciones."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual de la actividad antes del desarrollo.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Alinear formato final al producto pedido por la planeacion semanal."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Explicitar problema juridico o social que guia la respuesta.",
    "Relacionar conceptos y normas con el problema delimitado.",
    "Sostener afirmaciones relevantes con fuentes verificables disponibles.",
    "Distinguir sintesis de fuentes y postura propia del estudiante.",
    "Evitar desarrollo solo descriptivo o de resumen.",
    "Supuesto: si la consigna aborda interpretacion juridica, vincular hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Verificar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Confirmar trazabilidad: cada afirmacion relevante con fuente o supuesto marcado.",
    "Validar consistencia entre citas en texto y archivo .bib activo.",
    "No eliminar reglas utiles previas durante consolidacion.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en .tex.",
    "Comprobar que toda clave citada exista en el .bib usado.",
    "Usar acentos y codificacion correctos en espanol.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y documentos de control.",
    "Supuesto: el .bib canonico esperado por Slug es filosofia-del-derecho.bib hasta confirmacion local."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Registrar fuentes especificas de actividad en el .bib de la asignatura.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Mantener metadatos minimos: autor, titulo, ano y fuente editorial o URL.",
    "Marcar como supuesto todo dato bibliografico incompleto.",
    "No asumir que clean.bib aplica a toda actividad; validar por consigna."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones reutilizables, no conclusiones especificas de actividades hermanas.",
    "Mantener union-dedupe lossless en cada ciclo.",
    "Etiquetar reglas de baja confianza como provisionales.",
    "Conservar advertencia historica sobre salidas no parseables en herencias previas.",
    "Si falta consigna local, propagar estructura base y abrir preguntas en vez de inventar contenido."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 6.",
    "Confirmar rubrica de evaluacion especifica para ajustar profundidad argumentativa.",
    "Confirmar si el producto requerido es reporte, presentacion u otro formato.",
    "Confirmar nombre canonico final del .bib por coexistencia con clean.bib y token Slug sin resolver.",
    "Confirmar si se exige formato de citacion juridica adicional a BibTeX.",
    "Supuesto: verificar si fuentes de interpretacion juridica de clean.bib son obligatorias en Actividad 6."
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
      "Problema juridico o social como detonador.",
      "Conceptos, normas y doctrina pertinentes.",
      "Producto alineado a planeacion semanal.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico y utilidad profesional.",
      "Sostener integridad editorial mediante estructura, evidencia y criterio propio."
    ],
    "style_markers": [
      "Inicio breve con encuadre del problema.",
      "Secciones explicitas y ordenadas.",
      "Diferenciacion visible entre fuente y postura propia.",
      "Cierre con aplicabilidad juridica.",
      "Marcado explicito de supuestos."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Construir marco conceptual y normativo.",
      "Contrastar fuentes verificables.",
      "Defender postura propia fundamentada.",
      "Derivar conclusion del analisis."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco conceptual y normativo",
        "Analisis propio",
        "Conclusion transferible",
        "Hermeneutica juridica",
        "Argumentacion juridica"
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
          "justification": "Sin delimitacion del problema no hay argumentacion valida."
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
          "justification": "En actividades de interpretacion, la hermeneutica fundamenta la justificacion normativa."
        }
      ],
      "evidence": [
        "README: identidad, pauta editorial y ubicacion curricular.",
        "Programa analitico: cinco ejes de trabajo estables.",
        "Regla transversal: normalizar antes de propagar si hay salida no estructurada.",
        "Supuesto marcado sobre uso condicionado de clean.bib por consigna."
      ]
    },
    "reinforcement_log": [
      "Ciclo 16: se reforzo identidad institucional y estructura argumentativa reusable entre hermanos.",
      "Ciclo 16: se depuraron duplicados semanticos y se mantuvieron reglas utiles previas.",
      "Ciclo 16: se mantuvo separacion entre hechos verificados y supuestos.",
      "Ciclo 16: se evito transferir conclusiones o bibliografia exclusiva no confirmada localmente."
    ]
  }
}