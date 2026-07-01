{
  "summary": [
    "Se refuerza transferencia lateral desde Filosofia del Derecho hacia Etica y Moral juridica con solo patrones reutilizables.",
    "Se preserva normalizacion obligatoria: no propagar contenido no parseable.",
    "Se consolidan ejes comunes: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se agrega mejora verificable local: resolver tokens Slug sin expandir en README y programa analitico.",
    "Se agrega mejora verificable local: corregir nombres de archivo truncados en README.",
    "Se mantiene compresion lossless por union y deduplicacion semantica sin recorte."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y cierre juridico.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como punto de entrada canonico.",
    "Mantener referencia explicita a Etica y Moral juridica en cada producto.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Registrar ruta origen-destino y ciclo en cada fusion."
  ],
  "structure_rules": [
    "Responder en JSON valido y parseable.",
    "Usar esquema canonico completo sin omisiones.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar desarrollo en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por la planeacion semanal.",
    "Mantener trazabilidad de cambios por ciclo en frases breves."
  ],
  "activity_rules": [
    "Alinear la entrega al problema juridico o social de la actividad.",
    "Integrar conceptos, normas o doctrina pertinentes antes de concluir.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "No asumir fuentes de otras semanas o materias sin validacion en consigna."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar deduplicacion semantica antes de guardar memoria.",
    "No eliminar reglas utiles previas durante fusion.",
    "Aceptar solo mejoras verificables contra archivos locales o memoria valida.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables y evitar colisiones.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo truncados en README antes de referenciar rutas."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de actividad en etica-y-moral-juridica.bib.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Marcar duplicados historicos como pendientes de normalizacion sin perder trazabilidad.",
    "Supuesto: la entrada sierraUniversidadNacional1910 esta truncada y requiere correccion previa a compilacion."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones generales reutilizables entre materias hermanas.",
    "No copiar redaccion literal ni conclusiones especificas del nodo origen.",
    "Mantener bandera de normalizacion manual mientras persistan salidas no estructuradas.",
    "Aplicar analogia controlada: conservar identidad, estructura, calidad y relaciones nucleares."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 8 para fijar tipo de producto final.",
    "Confirmar rubrica de evaluacion local para ajustar profundidad argumentativa.",
    "Confirmar criterio canonico para resolver claves BibTeX duplicadas con alias trazables.",
    "Confirmar correccion completa de la entrada truncada sierraUniversidadNacional1910.",
    "Supuesto: la Actividad 8 mantiene formato reporte; validar si tambien admite presentacion o producto visual."
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
        "Asignatura: Etica y Moral juridica."
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
      "Transformar planeacion semanal en productos academicos con fundamento juridico y utilidad profesional.",
      "Preservar memoria editorial estable, verificable y reutilizable entre nodos relacionados."
    ],
    "style_markers": [
      "Frases breves y accionables.",
      "Supuestos marcados de forma explicita.",
      "Estructura funcional por secciones.",
      "Cierre juridico con criterio propio."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual y normativo pertinente.",
      "Analisis propio sustentado en evidencia.",
      "Conclusion juridica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Cinco ejes editoriales",
        "Integridad academica",
        "Conclusion juridica transferible"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
        "etica-y-moral-juridica.bib"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta local exige citas verificables y formato institucional."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON parseable no hay transferencia segura."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La secuencia de trabajo culmina en cierre aplicable."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Etica y Moral juridica",
          "kind": "supports",
          "justification": "Comparte patrones editoriales nucleares transferibles por analogia controlada."
        }
      ],
      "evidence": [
        "README local confirma identidad UnADM y ubicacion curricular.",
        "Programa analitico local define cinco ejes de trabajo.",
        "README y programa analitico muestran token Slug sin expandir.",
        "README local muestra nombres de archivo truncados.",
        "Archivo .bib local evidencia duplicados y entrada final truncada."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: se preservan reglas utiles previas sin eliminacion.",
      "Ciclo 2: se deduplican reglas repetidas por equivalencia semantica.",
      "Ciclo 2: se incorpora mejora verificable de higiene de rutas y tokens.",
      "Ciclo 2: se mantiene separacion entre patrones transferibles y contenido especifico no transferible."
    ]
  }
}