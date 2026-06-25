{
  "summary": [
    "Se refuerza transferencia lateral desde Filosofia del Derecho a Etica y Moral juridica con patrones reutilizables.",
    "Se preserva identidad UnADM, estructura editorial comun y compresion lossless por deduplicacion.",
    "Se mantiene bloqueo de propagacion para salidas no JSON parseables.",
    "Se confirma regla de marcar supuestos cuando falte consigna local.",
    "Se evita copiar conclusiones tematicas o bibliografia exclusiva del nodo origen.",
    "Se agregan mejoras verificables locales: token Slug sin expandir y .bib truncado [supuesto]."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Alinear la actividad a la asignatura Etica y Moral juridica.",
    "Registrar origen y destino de cada injerto de memoria.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion manual."
  ],
  "structure_rules": [
    "Responder en JSON valido y parseable segun esquema requerido.",
    "Usar frases cortas, accionables y sin duplicados.",
    "Conservar reglas utiles previas; agregar solo mejoras verificables.",
    "Aplicar compresion lossless por union y deduplicacion, sin recorte.",
    "Definir objetivo puntual antes del desarrollo.",
    "Mantener secciones: problema, conceptos, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por la planeacion semanal."
  ],
  "activity_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar resumen solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "No arrastrar contenido tematico especifico de Filosofia del Derecho sin justificacion local.",
    "Verificar consigna textual exacta de Actividad 5 antes de redactar."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de propagar.",
    "Confirmar que no se eliminen reglas utiles previas al fusionar.",
    "Validar ausencia de duplicados semanticos tras la fusion.",
    "Confirmar respaldo o marca de supuesto en afirmaciones no evidentes.",
    "Validar correspondencia entre citas en texto y archivo .bib.",
    "Normalizar incidencias por ciclo con plantilla unica."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Evitar comandos o paquetes no estandar sin justificacion editorial.",
    "Corregir rutas y nombres con caracteres anomalos antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Verificar nombres canonicos de archivos antes de referenciarlos."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de actividad en etica-y-moral-juridica.bib.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor o editor, titulo, anio, editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Marcar para revision manual entradas potencialmente duplicadas por autor+titulo+anio.",
    "Marcar [supuesto] si el truncamiento del .bib no fue validado en archivo real."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones generales reutilizables entre materias hermanas.",
    "No transferir redaccion literal ni conclusiones especificas del nodo origen.",
    "Mantener trazabilidad de ciclo y estado de validacion por regla.",
    "Si falta consigna local, propagar estructura base y preguntas abiertas.",
    "Evitar regresiones: conservar reglas institucionales y de calidad ya vigentes."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 5.",
    "Confirmar rubrica de evaluacion especifica para calibrar profundidad argumentativa.",
    "Confirmar tipo de producto final solicitado en Actividad 5.",
    "Confirmar politica local para depurar claves BibTeX duplicadas sin perder trazabilidad.",
    "Confirmar si el truncamiento en etica-y-moral-juridica.bib existe en archivo real [supuesto].",
    "Confirmar si se aplica bloqueo automatico tras N fallos consecutivos de parseo JSON."
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
      "Conceptos, normas y doctrina pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en producto academico evaluable.",
      "Sostener rigor juridico con claridad expositiva.",
      "Asegurar continuidad editorial entre actividades sin perder contexto local."
    ],
    "style_markers": [
      "Objetivo puntual al inicio.",
      "Secciones explicitas y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Cierre con criterio juridico propio."
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
        "Deduplicacion lossless",
        "Consigna local de Actividad 5"
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
          "justification": "La pauta institucional exige citas verificables y trazabilidad."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura del estudiante requiere sustento comprobable."
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
          "justification": "Sin estructura parseable no hay fusion confiable."
        },
        {
          "source": "Consigna local de Actividad 5",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El alcance argumentativo depende del producto y rubrica solicitados."
        }
      ],
      "evidence": [
        "README confirma identidad UnADM y ubicacion curricular.",
        "Programa analitico confirma ejes problema-conceptos-producto-analisis-conclusion.",
        "README y programa muestran token Slug sin expandir.",
        "Archivo .bib presenta duplicados por claves paralelas.",
        "Archivo .bib aparece truncado en contexto capturado [supuesto]."
      ]
    },
    "reinforcement_log": [
      "Ciclo 8: se consolidan reglas transversales reutilizables sin copiar contenido tematico del origen.",
      "Ciclo 8: se preserva bloqueo por no-JSON parseable como compuerta de calidad principal.",
      "Ciclo 8: se refuerza control de supuestos ante datos locales faltantes.",
      "Ciclo 8: se mantiene deduplicacion semantica y compresion lossless."
    ]
  }
}