{
  "summary": [
    "Se refuerza transferencia lateral desde Filosofia del Derecho hacia Etica y Moral juridica con patrones reutilizables.",
    "Se preserva identidad UnADM, estructura argumentativa y control de calidad sin copiar contenido tematico especifico.",
    "Se mantiene compresion lossless por deduplicacion semantica y union de reglas utiles.",
    "Se incorpora incidencia local verificable: archivo .bib truncado en entrada final [supuesto hasta verificacion de archivo completo].",
    "Se conserva regla de bloqueo de propagacion cuando no haya JSON parseable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y trazabilidad.",
    "Vincular cada entrega a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Registrar origen-destino de cada injerto de memoria editorial."
  ],
  "structure_rules": [
    "Responder siempre en JSON parseable y valido contra el esquema requerido.",
    "Usar frases cortas, accionables y sin duplicados.",
    "Conservar reglas utiles previas; agregar solo mejoras verificables.",
    "Organizar contenidos en: problema, conceptos, marco normativo/doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el formato final al producto solicitado por la consigna semanal."
  ],
  "activity_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar resumen solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "No trasladar conclusiones de otra asignatura sin justificacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de propagar.",
    "Confirmar que no se eliminen reglas utiles previas al fusionar.",
    "Validar ausencia de duplicados semanticos tras la fusion.",
    "Confirmar respaldo o marca [supuesto] en toda afirmacion no evidente.",
    "Validar correspondencia entre citas en texto y archivo .bib.",
    "Validar integridad sintactica del .bib antes de compilar."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar paquetes o comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni citas rotas.",
    "Corregir caracteres anomalos en rutas y nombres de archivo.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "bibliography_rules": [
    "No inventar referencias ni metadatos.",
    "Usar solo obras realmente consultables.",
    "Conservar metadatos minimos: autor/editor, titulo, anio, editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Registrar fuentes de actividad en etica-y-moral-juridica.bib.",
    "Marcar para revision manual duplicados potenciales por autor+titulo+anio.",
    "Revisar y cerrar entradas truncadas del .bib antes de uso [supuesto]."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones generales reutilizables; no texto literal entre actividades hermanas.",
    "Priorizar identidad institucional, estructura, calidad y patrones argumentativos comunes.",
    "Si falta consigna local, propagar plantilla base y dejar preguntas abiertas.",
    "Mantener bitacora de incidencias por ciclo con una sola regla plantilla deduplicada."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 5.",
    "Confirmar rubrica especifica de evaluacion para calibrar profundidad argumentativa.",
    "Confirmar tipo de producto final solicitado (reporte, presentacion u otro).",
    "Confirmar si el truncamiento en etica-y-moral-juridica.bib existe en archivo real completo [supuesto].",
    "Confirmar politica local para depuracion de claves BibTeX duplicadas sin perder trazabilidad."
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
        "Trazabilidad de memoria editorial."
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
      "Conceptos y marco normativo o doctrinal.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos solidos y trazables.",
      "Sostener una voz institucional consistente entre actividades.",
      "Garantizar calidad tecnica y argumentativa en LaTeX y bibliografia."
    ],
    "style_markers": [
      "Objetivo puntual al inicio.",
      "Secciones explicitas y ordenadas.",
      "Marcado explicito de [supuesto] cuando falte evidencia local.",
      "Cierre con implicacion profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema y alcance.",
      "Definir conceptos operativos.",
      "Anclar en marco normativo/doctrinal pertinente.",
      "Desarrollar postura critica propia.",
      "Concluir con transferencia practica."
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
        "Control de calidad editorial"
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
          "justification": "La postura requiere respaldo en fuentes consultables."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion profesional deriva del razonamiento argumentado."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Control de calidad editorial",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay fusion ni propagacion confiable."
        }
      ],
      "evidence": [
        "README confirma identidad UnADM y pauta editorial.",
        "Programa analitico confirma ejes problema-conceptos-producto-analisis-conclusion.",
        "README y programa muestran token Slug sin expandir.",
        "Bib local muestra duplicados de claves para obras equivalentes.",
        "Bib local presenta entrada final truncada [supuesto]."
      ]
    },
    "reinforcement_log": [
      "Ciclo 14: se consolidan reglas transversales reutilizables sin copiar conclusiones del nodo origen.",
      "Ciclo 14: se mantiene bloqueo por no-JSON parseable y normalizacion obligatoria.",
      "Ciclo 14: se refuerza control bibliografico por duplicados y truncamientos locales [supuesto]."
    ]
  }
}