{
  "summary": [
    "Se consolida memoria lateral de Actividad 4 con union-dedupe lossless.",
    "Se preserva ADN UnADM y marco curricular verificable.",
    "Se refuerza normalizacion estructurada y validacion JSON estricta.",
    "Se transfieren patrones reutilizables desde Actividad 1 sin copiar contenido especifico.",
    "Supuesto: la consigna local de Actividad 4 no esta visible completa."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato academico.",
    "Alinear contenido con Licenciatura en Derecho y Filosofia del Derecho.",
    "Vincular ubicacion curricular a semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Citar malla-curricular-derecho-unadm.pdf para datos curriculares."
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
    "Adaptar Actividad 4 a los ejes del programa analitico.",
    "Incluir problema, conceptos o normas, evidencia y analisis propio.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Confirmar formato de producto antes de redactar version final."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna local de Actividad 4."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en .tex y .bib.",
    "Citar en .tex solo claves existentes en .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo con caracteres anomalo antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables.",
    "Registrar fuentes especificas de la actividad en el .bib canonico de asignatura.",
    "No inventar referencias ni metadatos faltantes.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a Semana 7; verificar aplicabilidad a Actividad 4."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Reutilizar reglas institucionales de calidad sin perder especificidad local.",
    "Evitar regresiones y conservar reglas utiles previas.",
    "Transferir solo patrones reutilizables; no trasladar conclusiones especificas entre hermanos.",
    "Si falta consigna textual local, propagar estructura base y preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar consigna completa de Actividad 4: producto, extension y criterios.",
    "Confirmar si el producto es reporte, presentacion u otro formato.",
    "Confirmar rubrica docente especifica para profundidad argumentativa.",
    "Confirmar nombre canonico final del .bib por token Slug no resuelto.",
    "Confirmar si Actividad 4 requiere bibliografia propia o reutiliza base existente."
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
        "Normalizacion estructurada obligatoria antes de propagar.",
        "Carpeta de asignatura como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2.",
        "Asignatura obligatoria de 8 creditos.",
        "Asignatura: Filosofia del Derecho."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas o doctrina pertinente.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables.",
      "Unir fundamento juridico, evidencia y postura propia.",
      "Asegurar transferencia profesional de la conclusion."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales con logica juridica.",
      "Cita explicita para cada afirmacion relevante.",
      "Supuestos marcados cuando falte evidencia local."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Definir marco conceptual y normativo.",
      "Contrastar fuentes con analisis propio.",
      "Emitir postura justificada.",
      "Cerrar con conclusion aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales de Filosofia del Derecho",
        "Normalizacion estructurada",
        "Validacion JSON estricta",
        "Integridad academica y verificabilidad",
        "Relacion problema-evidencia-conclusion"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "README.md de asignatura",
        "programa-analitico-filosofia-del-derecho.md"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Tono y formato academico",
          "kind": "supports",
          "justification": "La pauta editorial exige alineacion institucional explicita."
        },
        {
          "source": "Ejes editoriales de Filosofia del Derecho",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Los ejes definen orden de desarrollo y cierre."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay reutilizacion segura."
        },
        {
          "source": "Integridad academica y verificabilidad",
          "target": "Conclusion juridica propia",
          "kind": "supports",
          "justification": "La conclusion valida requiere respaldo y analisis."
        }
      ],
      "evidence": [
        "README fija identidad UnADM, citas verificables y conclusion juridica propia.",
        "Programa analitico fija cinco ejes de trabajo transferibles.",
        "Antecedentes de salida no parseable justifican gate JSON estricto."
      ]
    },
    "reinforcement_log": [
      "Ciclo 16: deduplicacion de reglas repetidas por acento y variante.",
      "Ciclo 16: conservacion de reglas utiles previas sin recorte semantico.",
      "Ciclo 16: refuerzo lateral de estructura, calidad y trazabilidad.",
      "Ciclo 16: se evita copiar bibliografia exclusiva o conclusiones de Actividad 1."
    ]
  }
}