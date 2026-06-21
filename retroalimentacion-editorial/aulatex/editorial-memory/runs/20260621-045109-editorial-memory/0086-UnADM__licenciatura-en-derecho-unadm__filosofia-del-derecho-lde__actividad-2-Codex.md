{
  "summary": [
    "Se refuerza actividad-2 con patrones reutilizables de actividad-1 sin copiar contenido especifico.",
    "Se mantiene compresion lossless por union y deduplicacion, sin eliminar reglas utiles.",
    "Se consolida ADN editorial UnADM con foco en problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se conserva normalizacion obligatoria de salidas no estructuradas antes de propagacion recursiva.",
    "Supuesto: la consigna local de actividad-2 no esta completamente visible."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y cierre.",
    "Anclar contexto curricular: Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no confirmado por consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Conservar integridad academica con citas verificables."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto pedido en planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener trazabilidad entre afirmaciones, citas y bibliografia."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Sustentar cada afirmacion sustantiva con fuente verificable o marca de supuesto.",
    "Diferenciar postura propia, cita textual y parafrasis.",
    "No asumir tema, semana o formato de actividad-2 sin evidencia local.",
    "No trasladar conclusiones ni bibliografia exclusiva de actividad-1.",
    "Usar patrones comunes entre actividades hermanas: problema, evidencia, analisis y cierre."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas heredadas no estructuradas antes de reutilizar.",
    "Verificar consistencia entre texto, citas y archivo .bib.",
    "Confirmar correspondencia entre producto entregable y consigna local.",
    "Aplicar solo union-dedupe lossless; prohibido recorte destructivo."
  ],
  "latex_rules": [
    "Usar espanol con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables y compatibles con citas en .tex.",
    "No renombrar claves ya citadas sin migracion completa.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y rutas.",
    "Supuesto: .bib canonico esperado es filosofia-del-derecho.bib por Slug."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y documentos juridicos verificables.",
    "Agregar al .bib canonico solo fuentes realmente consultables.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Tratar filosofia-del-derecho-clean.bib como complemento tematico, no reemplazo automatico.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a Semana 7 y aplica solo si la consigna lo pide."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir entre hermanos solo patrones reutilizables, no contenidos cerrados.",
    "Mantener historial de fuentes provisionales como antecedente, no como verdad final.",
    "Evitar regresiones sobre reglas institucionales ya validadas.",
    "Cuando falte consigna local, propagar plantilla base y abrir preguntas.",
    "Registrar reforzamientos por analogia controlada en cada ciclo."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-2: tema, semana y producto.",
    "Confirmar plantilla obligatoria de secciones definida por docente.",
    "Confirmar estilo de citacion obligatorio institucional.",
    "Confirmar nombre canonico final del .bib de asignatura.",
    "Confirmar si actividad-2 requiere reporte, presentacion u otro formato.",
    "Confirmar si fuentes de hermeneutica/argumentacion son obligatorias en esta actividad."
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
        "Integridad academica y citas verificables.",
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
      "Conceptos y fuentes pertinentes.",
      "Analisis propio con postura academica.",
      "Evidencia verificable.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en producto academico util y verificable.",
      "Garantizar coherencia entre consigna, desarrollo y cierre.",
      "Sostener calidad editorial institucional en cada actividad."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales y trazables.",
      "Marcado explicito de supuestos.",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> analisis -> conclusion.",
      "Afirmacion juridica -> evidencia -> interpretacion propia.",
      "Consigna local -> formato solicitado -> verificacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion de salidas",
        "Integridad academica",
        "Trazabilidad cita-bibliografia",
        "Ejes editoriales troncales",
        "Transferencia lateral controlada"
      ],
      "citations": [
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/programa-analitico-filosofia-del-derecho.md",
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Ejes editoriales troncales",
          "kind": "supports",
          "justification": "Define tono, formato y finalidad comun."
        },
        {
          "source": "Normalizacion de salidas",
          "target": "Transferencia lateral controlada",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay propagacion segura."
        },
        {
          "source": "Trazabilidad cita-bibliografia",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Permite verificar respaldo de afirmaciones."
        },
        {
          "source": "Ejes editoriales troncales",
          "target": "Actividad-2",
          "kind": "develops",
          "justification": "Son patrones reutilizables entre nodos hermanos."
        }
      ],
      "evidence": [
        "README fija identidad UnADM, integridad academica y conclusion juridica.",
        "Programa analitico fija proposito y ejes transferibles.",
        "Regla estable: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 86: refuerzo lateral desde actividad-1 aplicado por analogia controlada.",
      "Se preservaron reglas validas previas sin eliminacion.",
      "Se deduplicaron duplicados semanticos y formales.",
      "Se evitaron traslados de contenido exclusivo del hermano origen.",
      "Se mantuvo pendiente de confirmacion todo dato sin consigna local."
    ]
  }
}