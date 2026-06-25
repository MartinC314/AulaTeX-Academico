{
  "summary": [
    "Se consolida sincronizacion transversal conservadora para materia destino con reglas estables reutilizables.",
    "Se preserva identidad UnADM, estructura base de argumentacion juridica y control de calidad por JSON parseable.",
    "Se evita transferir contenido tematico propio de Filosofia del Derecho; solo se transfieren abstracciones editoriales.",
    "Se mantiene contexto local verificado del destino: semestre 6, bloque 2, obligatoria, 8 creditos y .bib local existente.",
    "Se refuerza correccion de placeholders y nombres truncados en README/programa como deuda tecnica prioritaria."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables a Licenciatura en Derecho y a la materia destino.",
    "Conservar tono juridico-formal, claro y argumentativo.",
    "Cerrar con postura academica propia y criterio juridico.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Usar carpeta de materia como entrada canonica para README, programa, .tex y .bib.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear formato final al producto solicitado en planeacion semanal.",
    "Mantener coherencia entre pregunta guia, desarrollo y conclusion."
  ],
  "activity_rules": [
    "Contextualizar cada actividad con problema concreto y delimitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir evidencia citada de interpretacion propia.",
    "Evitar entregas solo descriptivas.",
    "Incluir conclusion juridica transferible a practica profesional.",
    "No asumir fuentes de otras semanas o materias sin validacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad entre afirmaciones y fuentes.",
    "Validar consistencia entre citas en texto y .bib.",
    "Verificar ausencia de fuentes inventadas.",
    "Verificar correccion de placeholders de slug y nombres truncados antes de compilar."
  ],
  "latex_rules": [
    "Usar espanol correcto con acentos consistentes en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir macros truncadas antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa."
  ],
  "bibliography_rules": [
    "Usar como base el .bib local confirmado de la materia destino.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Agregar al .bib solo fuentes realmente consultables.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente o URL.",
    "Agregar fecha de consulta en recursos web.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No inventar referencias."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas normalizadas, generales y sin duplicados.",
    "Mantener estrategia conservadora en saltos transversales entre nodos no equivalentes.",
    "Reutilizar gates institucionales de calidad como nucleo estable.",
    "No propagar redaccion literal ni contenido doctrinal especifico de otra materia.",
    "Mantener alerta heredada de normalizacion manual de ciclos previos hasta nueva evidencia."
  ],
  "open_questions": [
    "Confirmar si ya se corrigieron en README los nombres truncados de archivos.",
    "Confirmar resolucion final de placeholders de slug en README y programa.",
    "Confirmar plantilla oficial de presentacion para esta materia.",
    "Confirmar si la incidencia historica de salida no JSON parseable ya fue cerrada.",
    "Supuesto: macro de departamento en .tex permanece truncada; validar archivo completo."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Juridicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta canonica como punto de entrada."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 2, obligatoria, 8 creditos.",
        "Materia: Derechos de contratos mercantiles y titulos valores."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Marco conceptual y normativo verificable.",
      "Analisis propio diferenciado de la evidencia.",
      "Cierre con transferencia profesional.",
      "Normalizacion estructurada previa a propagacion."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, verificables y juridicamente utiles.",
      "Sostener continuidad editorial entre actividades sin perder contexto local de la materia."
    ],
    "style_markers": [
      "Apertura breve con problema.",
      "Secciones explicitas y ordenadas.",
      "Supuestos marcados cuando falte evidencia.",
      "Citas trazables y cierre con implicacion profesional."
    ],
    "argumentative_patterns": [
      "Problema -> marco normativo/doctrinal -> contraste de evidencia -> postura propia -> conclusion.",
      "Toda afirmacion juridica relevante exige respaldo verificable.",
      "Descripcion sola no basta; exigir analisis y justificacion."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico delimitado",
        "Marco normativo o doctrinal",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Normalizacion estructurada",
        "JSON parseable",
        "Bibliografia local valida"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad institucional exige trazabilidad y verificabilidad."
        },
        {
          "source": "Problema juridico delimitado",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitacion no hay argumentacion pertinente."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "El cierre profesional requiere fundamento juridico explicito."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "JSON parseable",
          "kind": "depends_on",
          "justification": "La propagacion recursiva segura requiere estructura valida."
        },
        {
          "source": "Bibliografia local valida",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "El .bib local es base de control de fuentes."
        }
      ],
      "evidence": [
        "README de materia con ubicacion curricular y pauta editorial.",
        "Programa analitico con ejes: problema, conceptos, producto, analisis, conclusion.",
        ".bib local con entradas institucionales unadmSitioWeb y unadmMallaDerecho2024.",
        "Regla heredada: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 12: deduplicacion integral sin recorte de reglas utiles.",
      "Ciclo 12: transferencia transversal limitada a abstracciones estables.",
      "Ciclo 12: refuerzo de gates de calidad y normalizacion previa.",
      "Ciclo 12: mantenimiento de alertas heredadas como provisionales.",
      "Ciclo 12: preservacion de identidad UnADM y patron argumentativo comun."
    ]
  }
}