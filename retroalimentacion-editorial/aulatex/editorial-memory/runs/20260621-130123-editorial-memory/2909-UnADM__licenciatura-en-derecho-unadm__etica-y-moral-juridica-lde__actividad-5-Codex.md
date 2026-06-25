{
  "summary": [
    "Se consolida transferencia lateral desde Filosofia del Derecho hacia Etica y Moral juridica con analogia controlada.",
    "Se preservan reglas institucionales, estructurales y de calidad ya validas en destino.",
    "Se refuerza normalizacion obligatoria: solo JSON parseable antes de propagacion recursiva.",
    "Se mantiene compresion lossless por union y deduplicacion, sin recorte.",
    "Se agregan mejoras verificables del contexto local: token Slug sin expandir y .bib posiblemente truncado [supuesto]."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Alinear la actividad a Etica y Moral juridica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Registrar trazabilidad de injertos con origen y destino."
  ],
  "structure_rules": [
    "Responder en JSON valido y parseable segun el esquema requerido.",
    "Usar frases cortas, accionables y sin duplicados.",
    "Conservar secciones existentes y agregar solo mejoras verificables.",
    "Definir objetivo puntual antes del desarrollo.",
    "Mantener secuencia base: problema, conceptos, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto solicitado por la planeacion semanal."
  ],
  "activity_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "No trasladar conclusiones tematicas de otra asignatura sin justificacion local.",
    "Confirmar consigna textual exacta de Actividad 5 antes de cerrar contenido."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de propagar.",
    "Confirmar que no se eliminen reglas utiles previas al fusionar.",
    "Validar ausencia de duplicados semanticos tras la fusion.",
    "Confirmar respaldo o marca de supuesto en cada afirmacion no evidente.",
    "Validar correspondencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Evitar comandos o paquetes no estandar sin justificacion editorial.",
    "Corregir nombres y rutas con caracteres anommalos antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de actividad en etica-y-moral-juridica.bib.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor o editor, titulo, anio, editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Marcar para revision manual entradas potencialmente duplicadas por autor+titulo+anio."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones reutilizables, no redaccion literal ni conclusiones especificas.",
    "Mantener analogia controlada entre nodos laterales.",
    "Unificar incidencias por ciclo en plantilla unica para evitar repeticion.",
    "Preservar reglas utiles previas y evitar regresiones."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 5.",
    "Confirmar rubrica especifica para calibrar profundidad argumentativa.",
    "Confirmar si el .bib local esta truncado en archivo real [supuesto].",
    "Confirmar politica local para depuracion de claves BibTeX duplicadas sin perder trazabilidad.",
    "Confirmar si existe listado de fuentes obligatorias de la semana correspondiente."
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
      "Conceptos y marco normativo o doctrinal.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar la planeacion semanal en productos academicos claros, fundamentados y aplicables.",
      "Asegurar trazabilidad editorial y tecnica en todo ciclo de memoria."
    ],
    "style_markers": [
      "Objetivo puntual al inicio.",
      "Secciones explicitas y ordenadas.",
      "Marcado explicito de supuestos.",
      "Cierre con implicacion juridica practica."
    ],
    "argumentative_patterns": [
      "Plantear problema y alcance.",
      "Definir conceptos operativos.",
      "Conectar con marco normativo o doctrinal.",
      "Desarrollar postura propia sustentada.",
      "Concluir con transferencia a practica profesional."
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
        "malla-curricular-derecho-unadm.pdf",
        "etica-y-moral-juridica.bib"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige trazabilidad y verificacion."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura academica requiere respaldo consultable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion practica deriva del razonamiento argumentado."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Deduplicacion lossless",
          "kind": "depends_on",
          "justification": "La compresion segura exige estructura valida."
        }
      ],
      "evidence": [
        "README local confirma identidad UnADM y ubicacion curricular.",
        "Programa analitico local confirma ejes problema-conceptos-producto-analisis-conclusion.",
        "README y programa muestran token Slug sin expandir, requiere normalizacion tecnica.",
        "Archivo .bib visible termina incompleto [supuesto: truncamiento de captura o archivo]."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: se refuerza transferencia lateral de patrones comunes sin copiar contenido especifico de Filosofia del Derecho.",
      "Ciclo 2: se mantiene regla dura de bloqueo por JSON no parseable.",
      "Ciclo 2: se conserva y limpia deduplicacion semantica en reglas troncales.",
      "Ciclo 2: se agregan incidencias tecnicas locales verificables con marcado de supuesto."
    ]
  }
}