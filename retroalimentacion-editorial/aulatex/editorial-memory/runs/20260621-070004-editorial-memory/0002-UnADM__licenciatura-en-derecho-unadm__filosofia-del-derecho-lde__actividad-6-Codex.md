{
  "summary": [
    "Se consolida memoria lateral A1->A6 con union-dedupe sin perdida.",
    "Se preserva identidad UnADM y ubicacion curricular verificada.",
    "Se mantienen ejes editoriales estables: problema, conceptos, producto, analisis propio y conclusion juridica.",
    "Se refuerza regla critica: no propagar contenido no estructurado sin normalizacion.",
    "Se conserva trazabilidad de fuentes y marcacion de supuestos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear toda actividad a Licenciatura en Derecho, Filosofia del Derecho.",
    "Contextualizar con semestre 1, bloque 2, obligatoria, 8 creditos cuando aplique.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Conservar regla de no regresion editorial en consolidaciones."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Definir objetivo puntual de la actividad antes del desarrollo.",
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir sintesis de fuentes y postura propia del estudiante.",
    "Evitar entregas solo descriptivas o generalizaciones sin anclaje juridico.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Supuesto: si la consigna aborda interpretacion juridica, vincular hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de propagar.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que toda afirmacion relevante tenga fuente o supuesto marcado.",
    "Validar consistencia entre citas en texto y archivo .bib activo.",
    "No eliminar reglas utiles previas durante la consolidacion.",
    "Separar reglas confirmadas de supuestos editoriales."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener compatibilidad .tex/.bib sin romper claves citadas.",
    "No cambiar claves BibTeX ya usadas en archivos .tex.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir caracteres anomalos en rutas o nombres antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar fuentes especificas de cada actividad en el .bib de la asignatura.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Marcar como supuesto cualquier dato bibliografico incompleto.",
    "No asumir que un .bib depurado de otra semana aplica automaticamente a Actividad 6."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir a nodos hermanos solo patrones reutilizables, no contenido puntual.",
    "Conservar advertencias historicas de salidas no parseables para prevenir regresiones.",
    "Aplicar union-dedupe lossless en cada ciclo.",
    "Cuando falte consigna local, propagar estructura base y abrir preguntas.",
    "Etiquetar como provisionales reglas de baja confianza hasta confirmacion local."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 6.",
    "Confirmar rubrica de evaluacion especifica de Actividad 6.",
    "Confirmar si el producto requerido es reporte, presentacion u otro formato.",
    "Confirmar nombre canonico final del .bib de la asignatura por token Slug sin resolver.",
    "Confirmar si se reutiliza filosofia-del-derecho-clean.bib o se usa .bib general.",
    "Supuesto: verificar si Actividad 6 corresponde formalmente a interpretacion juridica."
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
        "Filosofia del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social bien delimitado.",
      "Uso de conceptos y marco normativo pertinente.",
      "Producto alineado a planeacion semanal.",
      "Analisis propio diferenciado de la fuente.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables.",
      "Sostener decisiones editoriales con evidencia verificable.",
      "Garantizar consistencia institucional y calidad tecnica en LaTeX."
    ],
    "style_markers": [
      "Inicio con encuadre breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Citas verificables con postura personal diferenciada.",
      "Cierre con utilidad profesional juridica.",
      "Marcacion explicita de supuestos."
    ],
    "argumentative_patterns": [
      "Delimitar problema -> definir objetivo.",
      "Construir marco conceptual-normativo -> contrastar fuentes.",
      "Desarrollar postura propia -> justificar con evidencia.",
      "Derivar conclusion desde el analisis, no decorativa."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco normativo/doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion de salida estructurada",
        "Hermeneutica juridica [supuesto condicionado por consigna]",
        "Argumentacion juridica [supuesto condicionado por consigna]"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "programa-analitico-filosofia-del-derecho.md",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y formato consistente."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "No hay analisis solido sin delimitacion previa del problema."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion debe derivar del desarrollo argumentativo."
        },
        {
          "source": "Normalizacion de salida estructurada",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La trazabilidad editorial depende de salidas parseables y auditables."
        }
      ],
      "evidence": [
        "README: identidad UnADM, ubicacion curricular y pauta editorial.",
        "Programa analitico: ejes de trabajo en cinco pasos.",
        "Memoria origen y destino: regla persistente de JSON parseable y normalizacion.",
        "Coexistencia de .bib general y clean.bib: requiere confirmacion local por actividad."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: se mantuvo union-dedupe lossless sin eliminar reglas utiles previas.",
      "Ciclo 2: se reforzo bloqueo por JSON no parseable y normalizacion obligatoria.",
      "Ciclo 2: se preservaron ejes editoriales nucleares compartidos entre actividades hermanas.",
      "Ciclo 2: se evitó transferir conclusiones o bibliografia exclusiva no confirmada para A6."
    ]
  }
}