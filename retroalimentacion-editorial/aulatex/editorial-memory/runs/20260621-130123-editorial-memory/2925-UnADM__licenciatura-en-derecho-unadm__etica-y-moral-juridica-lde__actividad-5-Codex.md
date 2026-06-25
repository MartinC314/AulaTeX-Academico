{
  "summary": [
    "Se refuerza transferencia lateral desde Filosofia del Derecho hacia Etica y Moral juridica con patrones reutilizables.",
    "Se preserva identidad UnADM, estructura editorial base y controles de calidad sin copiar contenido tematico especifico.",
    "Se mantiene normalizacion obligatoria: salida JSON parseable antes de cualquier propagacion recursiva.",
    "Se consolida compresion lossless por union y deduplicacion semantica, sin recorte de reglas utiles.",
    "Se agregan mejoras verificables locales: manejo de tokens Slug sin expandir y control de .bib potencialmente truncado [supuesto]."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y trazabilidad.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Alinear la actividad al nodo destino: Etica y Moral juridica, Actividad 5.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Registrar origen y destino de cada injerto de memoria editorial."
  ],
  "structure_rules": [
    "Responder siempre en JSON valido y parseable segun el esquema requerido.",
    "Usar frases cortas, accionables y sin duplicados.",
    "Conservar secciones existentes y agregar solo mejoras verificables.",
    "Definir objetivo puntual antes del desarrollo.",
    "Mantener secuencia editorial: problema, conceptos, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto solicitado por la planeacion semanal."
  ],
  "activity_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante y evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "No arrastrar conclusiones tematicas de otra asignatura sin justificacion local.",
    "Verificar consigna textual exacta de Actividad 5 antes de redactar contenido final."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no se eliminen reglas utiles previas al fusionar.",
    "Validar ausencia de duplicados semanticos tras la fusion.",
    "Confirmar respaldo o marca de supuesto en cada afirmacion no evidente.",
    "Validar correspondencia entre citas en texto y archivo .bib.",
    "Normalizar manualmente respuestas no estructuradas antes de consolidar memoria."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Evitar comandos o paquetes no estandar sin justificacion editorial.",
    "Corregir rutas o nombres con caracteres anomalos antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "No copiar bloques LaTeX completos entre asignaturas; transferir solo patrones estructurales."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de actividad en etica-y-moral-juridica.bib.",
    "No inventar referencias ni metadatos bibliograficos.",
    "Conservar metadatos minimos: autor o editor, titulo, año, editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Marcar para revision manual entradas potencialmente duplicadas por autor+titulo+año.",
    "Verificar cierre correcto de cada entrada BibTeX y ausencia de truncamientos antes de compilar [supuesto]."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura minima.",
    "Transferir a nodos laterales solo reglas generales reutilizables.",
    "Evitar copiar redaccion literal, conclusiones especificas o bibliografia exclusiva.",
    "Aplicar analogia controlada: identidad, estructura, calidad, conceptos y relaciones recurrentes.",
    "Mantener bitacora por ciclo con estado de parseo y acciones de normalizacion.",
    "Si falta consigna local, propagar plantilla base y abrir preguntas en lugar de inventar contenido."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 5 para fijar tipo de producto final.",
    "Confirmar rubrica especifica de evaluacion para calibrar profundidad argumentativa.",
    "Confirmar si el .bib local esta truncado en archivo real o solo en captura [supuesto].",
    "Confirmar politica local para depuracion de claves BibTeX duplicadas sin perder trazabilidad.",
    "Confirmar fuentes obligatorias de la semana correspondiente en Etica y Moral juridica."
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
      "Problema juridico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion transferible a la practica juridica."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos con fundamento juridico y evidencia.",
      "Asegurar continuidad editorial entre actividades sin perder especificidad local.",
      "Garantizar calidad estructural y trazabilidad para propagacion recursiva confiable."
    ],
    "style_markers": [
      "Objetivo puntual al inicio.",
      "Secciones explicitas y ordenadas.",
      "Afirmaciones sustantivas con cita verificable.",
      "Marcado explicito de supuestos.",
      "Cierre con criterio juridico propio y aplicable."
    ],
    "argumentative_patterns": [
      "Plantear problema y alcance.",
      "Definir conceptos operativos.",
      "Vincular marco normativo o doctrinal pertinente.",
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
        "Deduplicacion lossless",
        "Analogia controlada lateral-transversal"
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
          "justification": "La postura argumentada debe sostenerse en fuentes consultables."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion profesional deriva del razonamiento critico."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Analogia controlada lateral-transversal",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia confiable entre nodos."
        }
      ],
      "evidence": [
        "README de destino: identidad UnADM, integridad academica y conclusion juridica.",
        "Programa analitico: ejes problema-conceptos-producto-analisis-conclusion.",
        "README y programa muestran token Slug sin expandir.",
        "Archivo .bib local exhibe duplicados de claves para obras equivalentes y posible truncamiento final [supuesto]."
      ]
    },
    "reinforcement_log": [
      "Ciclo 6: se transfieren patrones nucleares reutilizables desde Filosofia del Derecho sin copiar contenido especifico.",
      "Ciclo 6: se preservan reglas utiles previas y se deduplican variantes redaccionales equivalentes.",
      "Ciclo 6: se refuerza gate de JSON parseable como precondicion de propagacion recursiva.",
      "Ciclo 6: se añade control local de token Slug sin expandir y revision de integridad BibTeX [supuesto]."
    ]
  }
}