{
  "summary": [
    "Se consolida refuerzo lateral para actividad-3 con reglas reutilizables de actividad-1.",
    "Se preserva identidad UnADM, contexto curricular y ejes editoriales sin recorte.",
    "Se mantiene deduplicacion lossless y control de no regresion.",
    "Se refuerza normalizacion JSON obligatoria antes de propagacion recursiva.",
    "Se transfieren patrones, no redacciones ni conclusiones especificas entre hermanos.",
    "Se mantienen supuestos explicitos donde falta consigna local de actividad-3."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular actividad con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no confirmado en consigna local.",
    "Tratar memorias editoriales Codex o GPT-Pro como antecedente provisional, no como fuente academica.",
    "Registrar incidencias de parseo como metadato tecnico, no como evidencia disciplinar.",
    "Usar malla-curricular-derecho-unadm.pdf solo para ubicacion curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear estructura al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Si falta consigna local, usar estructura base y marcar supuestos."
  ],
  "activity_rules": [
    "Heredar reglas validas de actividad-1 sin eliminar reglas utiles previas.",
    "No copiar redaccion literal ni conclusiones especificas entre actividades hermanas.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir semana, formato o tema de actividad-3 sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado o propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad entre afirmaciones y fuentes citadas.",
    "Confirmar consistencia entre citas en texto y archivo .bib.",
    "Aplicar no regresion: no eliminar reglas utiles previas.",
    "Normalizar manualmente memorias con incidencias de parseo antes de reutilizarlas."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Verificar rutas y nombres de archivo contra README antes de referenciar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: archivo .bib canonico esperado es filosofia-del-derecho.bib por Slug."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Registrar en .bib solo entradas efectivamente citadas por la actividad.",
    "Conservar metadatos minimos: autor, titulo, año, fuente editorial o URL.",
    "No asumir que filosofia-del-derecho-clean.bib aplica a actividad-3; marcar como supuesto hasta confirmar consigna."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Propagar a nodos hermanos solo patrones generales reutilizables.",
    "No propagar supuestos como hechos confirmados.",
    "Aplicar compresion por union y deduplicacion lossless en cada ciclo.",
    "Conservar bandera de riesgo tecnico si hubo salida no estructurada en ciclos previos.",
    "Mantener especificidad local del nodo destino sin contaminar con bibliografia exclusiva de otro hermano."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-3.",
    "Confirmar formato de entrega requerido en actividad-3 (reporte, presentacion u otro).",
    "Confirmar rubrica de evaluacion especifica para actividad-3.",
    "Confirmar fuentes obligatorias de la semana correspondiente a actividad-3.",
    "Confirmar si actividad-3 reutiliza bibliografia existente o requiere .bib propio.",
    "Confirmar archivo .tex principal canonico para actividad-3."
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
        "Asignatura: Filosofia del Derecho."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos con claridad, fundamento juridico y evidencia.",
      "Garantizar coherencia entre estructura, citas y cierre argumentativo.",
      "Sostener continuidad editorial entre actividades sin copiar contenido especifico."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explicitas con orden logico.",
      "Afirmaciones con cita verificable.",
      "Supuestos etiquetados cuando falte evidencia local.",
      "Cierre juridico aplicable a practica profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos y marco -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> postura propia.",
      "Objetivo declarado -> desarrollo coherente -> cierre verificable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad academica",
        "Normalizacion JSON",
        "Problema juridico",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Bibliografia verificable",
        "Supuestos controlados"
      ],
      "citations": [
        "README.md de la asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib [supuesto de aplicacion condicionada]"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y criterio propio."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay transferencia confiable."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El analisis parte de una delimitacion clara del problema."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion depende de argumentacion sustentada."
        },
        {
          "source": "Supuestos controlados",
          "target": "Bibliografia verificable",
          "kind": "supports",
          "justification": "Evita inventar fuentes y obliga verificacion local."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad academica, conclusion juridica propia.",
        "Programa analitico: ejes problema, conceptos, producto, analisis y conclusion.",
        "Regla persistente: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 44: deduplicacion de reglas duplicadas por acento y variante lexical.",
      "Ciclo 44: refuerzo de transferencia lateral por patrones reutilizables.",
      "Ciclo 44: preservacion de no regresion y normalizacion estructurada obligatoria.",
      "Ciclo 44: mantenimiento de supuestos abiertos por falta de consigna local."
    ]
  }
}