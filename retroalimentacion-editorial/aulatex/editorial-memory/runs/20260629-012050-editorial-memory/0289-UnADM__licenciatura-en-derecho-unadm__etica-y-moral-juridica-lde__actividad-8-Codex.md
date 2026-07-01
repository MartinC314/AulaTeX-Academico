{
  "summary": [
    "Se transfiere ADN editorial reutilizable desde Filosofia del Derecho a Etica y Moral juridica por analogia controlada.",
    "Se preserva identidad UnADM, estructura canonica y control de calidad sin copiar contenido especifico del hermano.",
    "Se mantiene regla de normalizacion obligatoria: no propagar salidas no estructuradas.",
    "Se refuerzan los cinco ejes editoriales comunes del programa analitico local.",
    "Se agrega mejora verificable: resolver tokens Slug sin expandir en README y programa analitico del destino.",
    "Se agrega mejora verificable: corregir artefactos de ruta con caracteres truncados en README del destino.",
    "Se mantiene compresion lossless por union y deduplicacion semantica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y cierre juridico.",
    "Vincular toda actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Registrar trazabilidad de fusion con origen, destino, ciclo y tipo de relacion lateral-transversal."
  ],
  "structure_rules": [
    "Responder siempre en JSON valido y parseable para memoria.",
    "Usar esquema canonico completo sin omitir secciones.",
    "Iniciar producto con encuadre breve del problema juridico o social.",
    "Separar desarrollo en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear formato final al producto solicitado por la planeacion semanal."
  ],
  "activity_rules": [
    "Seguir los cinco ejes de trabajo como lista de verificacion.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "No asumir fuentes de otras semanas o materias sin validacion en consigna."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No eliminar reglas utiles previas durante fusion.",
    "Aceptar solo mejoras verificables contra archivos locales o memoria valida."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables y evitar colisiones por duplicado.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo truncados en README antes de referenciar rutas de compilacion."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de actividad en etica-y-moral-juridica.bib.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Detectar y documentar duplicados historicos de claves antes de normalizar."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Reutilizar reglas institucionales comunes sin copiar conclusiones especificas.",
    "Aplicar analogia controlada: transferir patrones, no redaccion literal.",
    "Si falta consigna local, mantener estructura base y abrir preguntas.",
    "Mantener bandera de normalizacion manual mientras existan salidas no estructuradas en nodos vecinos."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 8 para fijar tipo de producto.",
    "Confirmar rubrica de evaluacion local para ajustar profundidad argumentativa.",
    "Confirmar lista canonica de claves BibTeX para resolver duplicados por obra.",
    "Supuesto: la entrada sierraUniversidadNacional1910 esta truncada en etica-y-moral-juridica.bib; validar y corregir.",
    "Confirmar si la actividad exige reporte, presentacion o producto visual."
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
      "Problema juridico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion transferible a la practica juridica."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico y evidencia.",
      "Asegurar trazabilidad editorial y consistencia institucional en cada actividad."
    ],
    "style_markers": [
      "Frases breves y accionables.",
      "Supuestos marcados de forma explicita.",
      "Citas verificables y cierre con criterio juridico propio.",
      "Estructura por secciones funcionales."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual y normativo pertinente.",
      "Analisis propio sustentado.",
      "Conclusion juridica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Cinco ejes editoriales",
        "Normalizacion estructurada",
        "Integridad academica",
        "Conclusion juridica transferible"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta editorial local exige citas verificables y formato institucional."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "El programa analitico define una secuencia de trabajo que culmina en cierre aplicable."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON parseable no hay transferencia segura entre nodos."
        }
      ],
      "evidence": [
        "README de Etica y Moral juridica: identidad UnADM, ubicacion curricular y pauta editorial.",
        "Programa analitico local: proposito y cinco ejes de trabajo.",
        "Archivo .bib local: evidencia de duplicados y entrada truncada."
      ]
    },
    "reinforcement_log": [
      "Ciclo 1: se consolida transferencia lateral de patrones comunes sin copiar contenido especifico.",
      "Ciclo 1: se refuerza regla critica de JSON parseable y normalizacion previa.",
      "Ciclo 1: se agregan mejoras verificables de higiene tecnica en README y .bib del destino."
    ]
  }
}