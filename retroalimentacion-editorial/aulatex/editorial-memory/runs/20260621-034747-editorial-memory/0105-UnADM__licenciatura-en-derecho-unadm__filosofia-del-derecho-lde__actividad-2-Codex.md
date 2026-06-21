{
  "summary": [
    "Se consolida actividad-2 con transferencia lateral controlada desde actividad-1.",
    "Se preservan reglas validas previas por union-dedupe lossless.",
    "Se refuerza normalizacion obligatoria antes de propagacion recursiva.",
    "Se mantienen ejes troncales: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se evita copiar contenido exclusivo de un nodo hermano; solo patrones reutilizables."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Redactar con enfoque academico-juridico y transferencia profesional.",
    "Marcar como supuesto todo dato no confirmado por consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato al producto pedido en la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica.",
    "Mantener trazabilidad entre afirmaciones, citas y bibliografia."
  ],
  "activity_rules": [
    "Ajustar actividad-2 a la consigna docente local.",
    "Incluir postura argumentada del estudiante; evitar solo descripcion.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "No asumir tema, semana o formato sin evidencia local.",
    "Diferenciar postura propia, cita textual y parafrasis.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar.",
    "Normalizar respuestas no estructuradas heredadas antes de aplicar aguas abajo.",
    "Confirmar que cada afirmacion sustantiva tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No eliminar reglas utiles previas; solo unir y deduplicar."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Verificar rutas y nombres canonicos de archivos antes de referenciar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Agregar fuentes especificas de actividad en el .bib canonico de la asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Tratar filosofia-del-derecho-clean.bib como complemento tematico, no reemplazo automatico [supuesto]."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir entre hermanos solo identidad, estructura, calidad y patrones argumentativos.",
    "Evitar mover conclusiones especificas o bibliografia exclusiva de otra actividad.",
    "Mantener registro de fuentes provisionales como antecedente historico.",
    "Aplicar normalizacion manual cuando reaparezcan salidas no estructuradas.",
    "Reforzar sin regresion las reglas institucionales ya validadas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-2: tema, semana y producto.",
    "Confirmar si el producto requerido es reporte, presentacion u otro formato.",
    "Confirmar rubrica de evaluacion especifica para calibrar profundidad.",
    "Confirmar nombre canonico final del .bib de asignatura.",
    "Confirmar si existe estilo de citacion institucional obligatorio [supuesto: no confirmado].",
    "Confirmar si fuentes de interpretacion juridica (Semana 7) aplican a actividad-2 [supuesto]."
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
      "Problema juridico o social como disparador.",
      "Conceptos y normas con respaldo verificable.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible.",
      "Normalizacion estructurada antes de propagar."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables.",
      "Garantizar calidad juridica, evidencia y claridad argumentativa.",
      "Sostener continuidad editorial entre actividades sin contaminar contenidos especificos."
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
      "Consigna local -> adecuacion de formato -> verificacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales troncales",
        "Integridad academica",
        "Normalizacion de salidas",
        "Trazabilidad cita-bibliografia",
        "Transferencia lateral controlada"
      ],
      "citations": [
        "README.md de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Ejes editoriales troncales",
          "kind": "supports",
          "justification": "Define tono, formato y proposito comun."
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
          "target": "Actividad 2",
          "kind": "develops",
          "justification": "Son patrones reutilizables entre nodos hermanos."
        }
      ],
      "evidence": [
        "README fija identidad UnADM, integridad academica y cierre juridico.",
        "Programa analitico fija proposito y ejes transferibles.",
        "Regla valida: bloquear propagacion sin JSON parseable.",
        "Transferencia entre hermanos limitada a patrones reutilizables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 5: deduplicacion completa de reglas repetidas.",
      "Ciclo 5: refuerzo de regla de supuestos para datos no visibles.",
      "Ciclo 5: refuerzo de no copiar contenido exclusivo entre hermanos.",
      "Ciclo 5: mantenimiento de compatibilidad LaTeX-BibTeX y control de tokens Slug.",
      "Ciclo 5: preservacion de ADN institucional sin recorte semantico."
    ]
  }
}