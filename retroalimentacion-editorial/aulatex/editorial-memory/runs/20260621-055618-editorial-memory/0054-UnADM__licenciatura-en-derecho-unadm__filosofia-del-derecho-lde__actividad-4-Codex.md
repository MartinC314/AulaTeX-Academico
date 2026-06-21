{
  "summary": [
    "Se consolida memoria lateral para Actividad 4 con union y deduplicacion lossless.",
    "Se preservan reglas institucionales UnADM, estructura editorial y control de calidad.",
    "Se refuerza validacion JSON estricta por antecedentes de salidas no parseables.",
    "Se transfieren patrones reutilizables desde Actividad 1 sin copiar contenido especifico.",
    "Supuesto: la consigna textual de Actividad 4 no esta visible; se mantiene plantilla base verificable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato academico.",
    "Alinear la actividad con Licenciatura en Derecho y Filosofia del Derecho.",
    "Vincular ubicacion curricular a semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Separar hechos, conceptos, argumentos y postura personal.",
    "Alinear la entrega al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Aplicar los cinco ejes del programa analitico en cada entrega.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar asumir fuentes de otras semanas sin confirmacion de consigna.",
    "Supuesto: confirmar formato final de Actividad 4 antes de fijar maqueta definitiva."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Normalizar respuestas no estructuradas heredadas antes de reutilizar.",
    "Verificar correspondencia del producto con la consigna especifica de Actividad 4."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Citar en .tex solo claves existentes en .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y referencias.",
    "Corregir nombres de archivo con caracteres danados antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Registrar fuentes especificas de la actividad en el .bib canonico de asignatura.",
    "No inventar referencias ni metadatos faltantes.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a otra actividad; validar aplicabilidad en Actividad 4."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Reutilizar reglas institucionales de calidad sin perder especificidad local.",
    "Evitar regresiones: no eliminar reglas utiles previas ya validadas.",
    "Transferir solo patrones reutilizables entre nodos hermanos.",
    "Cuando falten datos locales, propagar estructura base y preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar consigna textual de Actividad 4.",
    "Confirmar producto solicitado: reporte, presentacion u otro formato.",
    "Confirmar rubrica de evaluacion especifica para profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana de Actividad 4.",
    "Confirmar nombre canonico final del .bib de asignatura tras resolver token Slug.",
    "Confirmar si Actividad 4 reutiliza bibliografia existente o requiere bloque bibliografico propio."
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
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Filosofia del Derecho."
      ]
    },
    "essence": [
      "Problema juridico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion transferible a la practica juridica."
    ],
    "reason_for_being": [
      "Transformar la planeacion semanal en productos academicos con fundamento juridico y evidencia.",
      "Asegurar trazabilidad editorial y tecnica para propagacion recursiva confiable."
    ],
    "style_markers": [
      "Definir objetivo antes del desarrollo.",
      "Separar secciones funcionales con logica juridica.",
      "Sostener afirmaciones con cita explicita.",
      "Marcar supuestos cuando falte evidencia local."
    ],
    "argumentative_patterns": [
      "Plantear problema inicial.",
      "Desarrollar marco conceptual y normativo.",
      "Contrastar fuentes con analisis propio.",
      "Emitir postura justificada.",
      "Cerrar con conclusion juridica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON estricta",
        "Ejes editoriales de Filosofia del Derecho",
        "Integridad academica y verificabilidad",
        "Relacion problema-evidencia-conclusion juridica"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/programa-analitico-filosofia-del-derecho.md"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Tono y formato academico",
          "kind": "supports",
          "justification": "La pauta editorial exige alineacion institucional explicita."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay reutilizacion segura."
        },
        {
          "source": "Ejes editoriales de Filosofia del Derecho",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Definen orden de problema, conceptos, analisis y cierre."
        },
        {
          "source": "Integridad academica y verificabilidad",
          "target": "Conclusion juridica propia",
          "kind": "supports",
          "justification": "La conclusion debe estar sustentada, no ser solo opinion."
        }
      ],
      "evidence": [
        "README: identidad UnADM, entrada canonica y criterio propio en conclusion.",
        "Programa analitico: cinco ejes de trabajo reutilizables.",
        "Antecedentes de ciclos previos: salida no parseable requiere gate JSON."
      ]
    },
    "reinforcement_log": [
      "Ciclo 54: deduplicacion integral de reglas repetidas en destino.",
      "Ciclo 54: refuerzo lateral de patrones estructurales y de calidad desde nodo hermano.",
      "Ciclo 54: se mantiene separacion entre reglas generales y contenido especifico de actividad.",
      "Ciclo 54: se agregan supuestos explicitos donde falta consigna local verificable."
    ]
  }
}