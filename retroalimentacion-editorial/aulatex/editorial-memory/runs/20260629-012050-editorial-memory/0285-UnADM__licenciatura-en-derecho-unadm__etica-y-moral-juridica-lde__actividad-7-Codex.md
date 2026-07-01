{
  "summary": [
    "Se realiza refuerzo lateral desde Filosofia del Derecho hacia Etica y Moral juridica con deduplicacion lossless.",
    "Se preservan reglas utiles previas del destino y se agregan solo patrones reutilizables verificados.",
    "Se consolida eje comun de actividad: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene normalizacion obligatoria: propagar solo con JSON parseable y esquema completo.",
    "Se mantiene trazabilidad de supuestos cuando falte consigna local de Actividad 7."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado en la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante y evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No trasladar redaccion literal ni conclusiones especificas de actividades hermanas.",
    "Si falta consigna local, usar estructura base y abrir preguntas en lugar de inventar contenido."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema requerido completo antes de guardar memoria.",
    "Confirmar no eliminacion de reglas utiles previas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Verificar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna especifica de Actividad 7."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correctos en espanol en .tex y .bib.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Mantener claves BibTeX estables y mapear alias sin romper citas existentes.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico antes de nuevas referencias.",
    "Verificar rutas y nombres canonicos antes de referenciarlos."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de Actividad 7 en etica-y-moral-juridica.bib.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor o editor, titulo, anio, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Deduplicar entradas equivalentes sin perdida de trazabilidad.",
    "[Supuesto] Si el .bib esta truncado, bloquear normalizacion profunda y abrir incidencia tecnica primero."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones generales reutilizables cuando falte consigna textual.",
    "Evitar regresiones de reglas de calidad institucional ya consolidadas.",
    "Aplicar normalizacion manual en ciclos con entradas no parseables.",
    "Mantener refuerzo lateral por analogia controlada sin contaminar contenido especifico entre materias."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 7.",
    "Confirmar tipo de producto requerido en la semana: reporte, presentacion u otro.",
    "Confirmar rubrica de evaluacion para ajustar profundidad argumentativa.",
    "Confirmar politica local de clave canonica y alias en BibTeX.",
    "[Supuesto] Confirmar reparacion completa del .bib truncado antes de nuevas deduplicaciones."
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
        "Asignatura destino: Etica y Moral juridica."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir la planeacion semanal en entregables academicos solidos y verificables.",
      "Asegurar continuidad editorial institucional entre actividades y materias afines.",
      "Preservar memoria util sin perdida mediante deduplicacion lossless."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Supuestos marcados de forma explicita.",
      "Separacion clara entre concepto, evidencia y postura.",
      "Trazabilidad de decisiones editoriales."
    ],
    "argumentative_patterns": [
      "Problematizar, definir, sustentar, argumentar, concluir.",
      "Conectar doctrina o norma con implicacion practica.",
      "Evitar resumen pasivo y sostener postura propia."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Estructura minima de actividad",
        "Analisis propio",
        "Conclusion juridica",
        "JSON parseable",
        "Deduplicacion lossless",
        "Consistencia bibliografica"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
        "etica-y-moral-juridica.bib"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Estructura minima de actividad",
          "kind": "supports",
          "justification": "La identidad institucional exige forma academica consistente."
        },
        {
          "source": "Estructura minima de actividad",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La estructura obliga a pasar de descripcion a argumentacion."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica",
          "kind": "develops",
          "justification": "La conclusion debe derivar de argumentos y evidencia."
        },
        {
          "source": "JSON parseable",
          "target": "Deduplicacion lossless",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay consolidacion segura."
        },
        {
          "source": "Consistencia bibliografica",
          "target": "Conclusion juridica",
          "kind": "supports",
          "justification": "La conclusion valida depende de evidencia trazable."
        }
      ],
      "evidence": [
        "README local confirma semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Programa analitico local confirma ejes de trabajo compartidos.",
        "README y programa analitico muestran token Slug sin expandir.",
        "[Supuesto] El .bib local visible termina truncado en la ultima entrada mostrada."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: se consolidan patrones transversales reutilizables sin copiar contenido especifico del origen.",
      "Ciclo 2: se refuerza control de calidad por JSON estricto y esquema completo.",
      "Ciclo 2: se mantiene ADN editorial institucional y se reducen duplicados semanticos."
    ]
  }
}