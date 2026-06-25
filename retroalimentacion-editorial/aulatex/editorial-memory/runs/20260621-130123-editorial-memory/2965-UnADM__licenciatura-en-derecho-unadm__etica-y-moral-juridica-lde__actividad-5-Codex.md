{
  "summary": [
    "Se refuerza transferencia lateral desde Filosofia del Derecho hacia Etica y Moral juridica con patrones reutilizables.",
    "Se preserva identidad UnADM y estructura editorial comun sin copiar contenido tematico especifico.",
    "Se mantiene compresion lossless por deduplicacion semantica y union de reglas validas.",
    "Se conserva regla critica: bloquear propagacion cuando no haya JSON parseable.",
    "Se integra evidencia local verificable: tokens Slug sin expandir en README/programa y truncamiento de .bib [supuesto hasta verificacion completa]."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y trazabilidad.",
    "Vincular cada entrega a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica de trabajo.",
    "Marcar como [supuesto] todo dato no visible en la consigna local.",
    "Tratar como provisional toda regla originada en salida no parseable hasta validacion manual.",
    "Registrar origen y destino de cada injerto de memoria editorial."
  ],
  "structure_rules": [
    "Responder solo en JSON valido y parseable segun esquema requerido.",
    "Usar frases cortas, accionables y sin duplicados.",
    "Conservar reglas utiles previas; agregar solo mejoras verificables.",
    "Aplicar compresion lossless por union y deduplicacion, sin recorte.",
    "Mantener secciones nucleares: problema, conceptos, marco, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo."
  ],
  "activity_rules": [
    "Alinear el producto final a la consigna textual de Actividad 5.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de propagar recursivamente.",
    "Validar que no se eliminen reglas utiles previas en cada fusion.",
    "Validar ausencia de duplicados semanticos tras deduplicacion.",
    "Exigir respaldo o marca [supuesto] en toda afirmacion no evidente.",
    "Validar correspondencia entre citas en texto y claves en .bib."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos o paquetes no estandar sin justificacion editorial.",
    "Corregir rutas o nombres con caracteres anommalos antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "bibliography_rules": [
    "No inventar referencias ni metadatos bibliograficos.",
    "Usar solo obras realmente consultables y verificables.",
    "Conservar metadatos minimos: autor o editor, titulo, anio, editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Registrar fuentes de la actividad en etica-y-moral-juridica.bib.",
    "Marcar para revision manual entradas potencialmente duplicadas por autor+titulo+anio."
  ],
  "propagation_hints": [
    "Propagar lateral y recursivo solo despues de validar JSON y estructura.",
    "Transferir solo patrones generales reutilizables, no conclusiones de otra asignatura.",
    "Mantener analogia controlada: identidad, estructura, calidad y metodo argumentativo.",
    "Si falta consigna local, preservar plantilla base y abrir preguntas en vez de inventar.",
    "Normalizar incidencias por ciclo con plantilla unica para trazabilidad."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 5 y tipo de producto final.",
    "Confirmar rubrica local de evaluacion para ajustar profundidad argumentativa.",
    "Confirmar politica local para depuracion de claves BibTeX duplicadas sin perder trazabilidad.",
    "Verificar si el truncamiento detectado en etica-y-moral-juridica.bib existe en archivo real [supuesto].",
    "Confirmar si hay fuentes obligatorias de semana para Actividad 5."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Reflexivo ante dilemas etico-juridicos."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de asignatura como entrada canonica.",
        "Trazabilidad de memoria editorial y fuentes."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura destino: Etica y Moral juridica.",
        "Actividad destino: Actividad 5."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco pertinente.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en producto academico util y verificable.",
      "Asegurar coherencia entre consigna, argumento, evidencia y cierre profesional."
    ],
    "style_markers": [
      "Objetivo puntual al inicio.",
      "Secciones explicitas y ordenadas.",
      "Citas verificables en afirmaciones sustantivas.",
      "Marcado explicito de [supuesto] cuando falten datos."
    ],
    "argumentative_patterns": [
      "Plantear problema y alcance.",
      "Definir conceptos operativos.",
      "Vincular marco normativo o doctrinal.",
      "Desarrollar analisis critico propio.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Normalizacion JSON",
        "Deduplicacion lossless"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/programa-analitico-etica-y-moral-juridica.md",
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/etica-y-moral-juridica.bib"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige trazabilidad y citas verificables."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura academica requiere respaldo documental."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion profesional deriva del razonamiento argumentado."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Deduplicacion lossless",
          "kind": "depends_on",
          "justification": "La fusion segura requiere estructura valida y comparable."
        }
      ],
      "evidence": [
        "README y programa confirman identidad UnADM y ejes editoriales comunes.",
        "README y programa muestran token Slug sin expandir en rutas bibliograficas.",
        "El .bib visible termina truncado en la entrada final [supuesto hasta verificacion de archivo completo]."
      ]
    },
    "reinforcement_log": [
      "Ciclo 16: se consolida transferencia lateral por patrones, sin copiar contenido especifico del nodo hermano.",
      "Ciclo 16: se deduplican reglas repetidas y se preservan reglas utiles previas.",
      "Ciclo 16: se fortalece gate de JSON parseable como condicion de propagacion recursiva."
    ]
  }
}