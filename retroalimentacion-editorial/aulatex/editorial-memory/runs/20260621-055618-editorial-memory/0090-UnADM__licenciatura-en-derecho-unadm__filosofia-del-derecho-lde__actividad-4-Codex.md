{
  "summary": [
    "Se consolida memoria lateral para Actividad 4 con deduplicacion lossless y sin recorte util.",
    "Se preserva identidad UnADM, contexto curricular y pauta editorial canonica de la asignatura.",
    "Se refuerza normalizacion estructurada y bloqueo por JSON no parseable antes de propagar.",
    "Se transfieren patrones reutilizables de estructura, calidad y argumentacion desde Actividad 1 sin copiar contenido especifico.",
    "Supuesto: la consigna puntual de Actividad 4 no esta visible; se mantiene plantilla base verificable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono formal academico y precision juridica.",
    "Alinear la actividad a Licenciatura en Derecho, asignatura Filosofia del Derecho.",
    "Conservar ubicacion curricular: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica documental.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Referenciar malla-curricular-derecho-unadm.pdf para sustento de ubicacion curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Separar hechos, conceptos, argumentos y postura personal.",
    "Alinear el producto final a la planeacion semanal y a la consigna de la actividad.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Incluir explicitamente problema, conceptos, evidencia y analisis propio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Confirmar que el formato de entrega solicitado coincida con el artefacto generado.",
    "No asumir que bibliografia de otra semana aplica automaticamente a Actividad 4."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregable y consigna local."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correctos en espanol en .tex y .bib.",
    "Citar en .tex solo claves existentes en .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Verificar nombres reales de archivo cuando README tenga tokens sin resolver tipo $(@{...}.Slug).",
    "Corregir rutas o nombres con caracteres anomalos antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables: UnADM, SCJN, UNAM-IIJ.",
    "Registrar fuentes especificas de Actividad 4 en el .bib canonico de la asignatura.",
    "No inventar referencias ni metadatos faltantes.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a interpretacion juridica de otra semana; verificar aplicabilidad local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura completa.",
    "Propagar a nodos hermanos solo reglas generales reutilizables, no contenido especifico.",
    "Preservar reglas utiles previas y agregar solo mejoras verificables.",
    "Aplicar union-dedupe para compresion lossless en cada ciclo.",
    "Mantener bandera de normalizacion manual cuando existan antecedentes de salida no estructurada."
  ],
  "open_questions": [
    "Confirmar consigna textual de Actividad 4: producto, extension y criterios de evaluacion.",
    "Confirmar si Actividad 4 exige reporte, presentacion u otro formato.",
    "Confirmar rubrica docente especifica para calibrar profundidad argumentativa.",
    "Confirmar nombre canonico final del archivo .bib si el README mantiene plantilla sin resolver.",
    "Confirmar si la bibliografia limpia de Semana 7 aplica o si se requiere seleccion nueva para Actividad 4."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro.",
        "Juridicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Entrada canonica en carpeta de asignatura.",
        "Normalizacion obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Filosofia del Derecho.",
        "Semestre 1, bloque 2.",
        "Obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social que activa la actividad.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion transferible a la practica juridica."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en producto academico verificable y util profesionalmente.",
      "Asegurar coherencia entre fundamento juridico, evidencia y postura propia.",
      "Mantener trazabilidad editorial y tecnica en todo el flujo LaTeX."
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
        "Ejes editoriales de Filosofia del Derecho",
        "Normalizacion estructurada",
        "Validacion JSON estricta",
        "Integridad academica y verificabilidad",
        "Relacion problema-evidencia-conclusion"
      ],
      "citations": [
        "README de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
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
          "justification": "Los ejes ordenan problema, conceptos, analisis y cierre."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva segura",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay reutilizacion confiable."
        },
        {
          "source": "Integridad academica y verificabilidad",
          "target": "Conclusion juridica propia",
          "kind": "supports",
          "justification": "La conclusion valida depende de evidencia trazable."
        }
      ],
      "evidence": [
        "README define identidad UnADM, integridad academica, citas verificables y conclusion juridica propia.",
        "Programa analitico define cinco ejes de trabajo reutilizables.",
        "Antecedentes registran salidas no parseables; se justifica gate JSON estricto."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas por acento, variante y redaccion equivalente.",
      "Se preservaron reglas tecnicas y editoriales utiles previas sin eliminacion regresiva.",
      "Se removio transferencia de conclusiones especificas de Actividad 1 por regla de salto entre hermanos.",
      "Se mantuvieron supuestos explicitos donde falta consigna local verificable."
    ]
  }
}