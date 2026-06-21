{
  "summary": [
    "Se consolida memoria lateral A1->A6 con union-dedupe sin perdida.",
    "Se mantiene ADN UnADM: identidad institucional, integridad academica y cierre juridico propio.",
    "Se preservan cinco ejes editoriales: problema, conceptos/normas, producto, analisis propio y conclusion transferible.",
    "Se refuerza regla critica: no propagar contenido no estructurado sin normalizacion.",
    "Se mantiene ubicacion curricular verificada: Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se marca como supuesto todo dato no visible en consigna local de actividad 6."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear la actividad a Licenciatura en Derecho y asignatura Filosofia del Derecho.",
    "Citar ubicacion curricular cuando contextualice: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como provisional toda fuente heredada no verificada localmente.",
    "Marcar como supuesto cualquier dato no visible en la consigna."
  ],
  "structure_rules": [
    "Entregar JSON valido cuando la tarea sea consolidacion de memoria.",
    "Usar exactamente el esquema requerido y sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar en bloques: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear el producto final a la planeacion semanal de actividad 6.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Definir objetivo puntual de actividad 6 antes del desarrollo.",
    "Relacionar conceptos, normas y doctrina con el problema delimitado.",
    "Distinguir sintesis de fuentes y postura propia.",
    "Evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Supuesto: si A6 trata interpretacion juridica, integrar hermeneutica y argumentacion con aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si salida no es JSON parseable.",
    "Validar estructura minima completa antes de propagar.",
    "No eliminar reglas utiles previas durante consolidacion.",
    "Separar reglas confirmadas de supuestos marcados.",
    "Confirmar trazabilidad de afirmaciones relevantes a fuente o supuesto.",
    "Validar consistencia entre citas en texto y .bib activo.",
    "Revisar que conclusion derive del analisis y no sea decorativa."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correctos en .tex y .bib.",
    "Mantener claves BibTeX estables ya citadas.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: .bib canonico esperado por Slug es filosofia-del-derecho.bib hasta confirmacion."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Registrar fuentes de actividad 6 en .bib de asignatura.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Marcar como supuesto datos bibliograficos incompletos.",
    "No asumir que clean.bib aplica a A6 si la consigna no lo confirma."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir a hermanos solo patrones reutilizables, no conclusiones especificas.",
    "Mantener union-dedupe lossless para evitar regresiones.",
    "Conservar advertencia historica de salidas no estructuradas en ciclos tempranos.",
    "Cuando falte consigna local, propagar plantilla base y preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad 6.",
    "Confirmar formato exigido en A6: reporte, presentacion u otro.",
    "Confirmar rubrica especifica de evaluacion de A6.",
    "Confirmar si A6 es de interpretacion juridica o de otro eje.",
    "Confirmar nombre canonico final del .bib por token Slug sin resolver.",
    "Confirmar si clean.bib se reutiliza en A6 o si requiere seleccion nueva."
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
        "Asignatura: Filosofia del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Conceptos y normas pertinentes.",
      "Producto alineado a planeacion.",
      "Analisis propio fundamentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico, evidencia y criterio propio."
    ],
    "style_markers": [
      "Inicio con encuadre breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Postura personal diferenciada de la sintesis.",
      "Cierre con utilidad profesional juridica.",
      "Supuestos marcados de forma visible."
    ],
    "argumentative_patterns": [
      "Delimitar problema -> definir objetivo puntual.",
      "Exponer marco conceptual/normativo -> vincular fuentes.",
      "Analizar caso o tema -> contrastar posturas.",
      "Fijar postura propia -> justificar con evidencia.",
      "Cerrar con conclusion derivada del desarrollo."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco normativo/doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Hermeneutica juridica [supuesto condicionado a consigna]",
        "Argumentacion juridica [supuesto condicionado a consigna]"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
        "README.md de asignatura",
        "programa-analitico-filosofia-del-derecho.md"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta editorial exige citas verificables y rigor formal."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere un problema delimitado."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida debe derivar del desarrollo argumentativo."
        },
        {
          "source": "Hermeneutica juridica [supuesto condicionado a consigna]",
          "target": "Argumentacion juridica [supuesto condicionado a consigna]",
          "kind": "supports",
          "justification": "Si A6 aborda interpretacion, la hermeneutica fundamenta la argumentacion."
        }
      ],
      "evidence": [
        "Pauta editorial del README: identidad, citas verificables y conclusion juridica propia.",
        "Programa analitico: cinco ejes estables de trabajo.",
        "Regla consolidada: normalizar antes de propagar contenido heredado."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin recortar contenido util.",
      "Se conservaron controles de calidad y no regresion.",
      "Se reforzo separacion entre hechos verificados y supuestos.",
      "Se evito transferir redaccion literal y conclusiones especificas de A1."
    ]
  }
}