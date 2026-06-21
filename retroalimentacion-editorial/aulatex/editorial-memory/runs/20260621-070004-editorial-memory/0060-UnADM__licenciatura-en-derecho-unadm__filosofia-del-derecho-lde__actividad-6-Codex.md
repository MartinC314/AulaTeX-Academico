{
  "summary": [
    "Se consolida memoria lateral de Actividad 1 a Actividad 6 con union y deduplicacion lossless.",
    "Se preserva identidad UnADM y ubicacion curricular verificada: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se refuerzan ejes editoriales estables: problema, conceptos o normas, producto, analisis propio y conclusion juridica transferible.",
    "Se mantiene regla critica de normalizar salidas no estructuradas antes de propagar.",
    "Se agrega control de transferencia entre hermanos: solo patrones reutilizables, sin copiar conclusiones ni bibliografia exclusiva."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear toda actividad a Licenciatura en Derecho y asignatura Filosofia del Derecho.",
    "Contextualizar con ubicacion curricular: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar regla de no regresion: no eliminar reglas utiles previas."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual de la actividad antes del desarrollo.",
    "Alinear el formato final al producto pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Distinguir con claridad sintesis de fuentes y postura propia.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sostener afirmaciones con fuentes verificables y cita explicita.",
    "Relacionar conceptos y normas con el problema planteado.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir automaticamente que bibliografia de otra semana aplica a Actividad 6 [supuesto]."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib activo.",
    "Verificar correspondencia entre producto entregado y consigna local de Actividad 6.",
    "Aplicar deduplicacion por union sin perdida de reglas vigentes."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Marcar como supuesto el nombre canonico del .bib si persiste ambiguedad."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Registrar fuentes de la actividad en el .bib de la asignatura.",
    "Conservar metadatos minimos: autor, titulo, ano, editorial o nota, URL cuando exista.",
    "No trasladar bibliografia exclusiva de un hermano a otro sin evidencia de uso local.",
    "Si se usa corpus de interpretacion juridica de clean.bib, condicionarlo a consigna confirmada [supuesto]."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir entre hermanos solo patrones generales reutilizables.",
    "No copiar redaccion literal, conclusiones especificas ni citas exclusivas de otro nodo.",
    "Mantener advertencias historicas sobre salidas no parseables de ciclos previos.",
    "Separar reglas confirmadas de supuestos antes de propagar.",
    "Reforzar identidad curricular y gates de calidad como nucleo comun lateral."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 6.",
    "Confirmar rubrica especifica de evaluacion para Actividad 6.",
    "Confirmar si el producto principal es reporte, presentacion u otro formato.",
    "Confirmar nombre canonico final del .bib de la asignatura por token Slug sin resolver.",
    "Confirmar si bibliografia de interpretacion juridica (Semana 7) aplica formalmente a Actividad 6.",
    "Confirmar si existe formato de citacion juridica adicional a BibTeX."
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
      "Conceptos, normas o doctrina pertinentes.",
      "Producto alineado a planeacion.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables academicos solidos.",
      "Asegurar fundamento juridico, evidencia verificable y cierre argumentativo util.",
      "Preservar trazabilidad editorial y tecnica en todo el flujo LaTeX."
    ],
    "style_markers": [
      "Inicio con delimitacion del problema.",
      "Secciones explicitas y ordenadas.",
      "Diferenciacion visible entre fuente y postura propia.",
      "Uso prudente de supuestos marcados.",
      "Cierre con aplicacion profesional juridica."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual-normativo -> analisis propio -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> postura.",
      "Coherencia entre pregunta guia, desarrollo y cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion de salida estructurada",
        "Trazabilidad bibliografica"
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
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige evidencia verificable y formato consistente."
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
          "justification": "La conclusion valida debe derivar del razonamiento previo."
        },
        {
          "source": "Normalizacion de salida estructurada",
          "target": "Trazabilidad bibliografica",
          "kind": "supports",
          "justification": "Sin estructura parseable no hay control fiable de citas y reglas."
        }
      ],
      "evidence": [
        "README: identidad institucional y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo.",
        "Memoria origen: regla de no propagar contenido no estructurado.",
        "Contexto local: coexistencia de .bib y clean.bib con token Slug sin resolver."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas conservando cobertura completa.",
      "Se preservaron reglas utiles previas sin recorte semantico.",
      "Se reforzo control lateral entre nodos hermanos para evitar fuga de contenido especifico.",
      "Se mantuvieron supuestos abiertos donde falta consigna local verificable."
    ]
  }
}