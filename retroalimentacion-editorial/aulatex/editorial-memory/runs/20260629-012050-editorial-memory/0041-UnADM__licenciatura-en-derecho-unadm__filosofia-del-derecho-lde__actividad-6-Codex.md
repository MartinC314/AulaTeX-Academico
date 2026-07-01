{
  "summary": [
    "Se consolida refuerzo lateral desde Actividad 1 a Actividad 6 con union-dedupe sin perdida.",
    "Se preserva identidad UnADM, ubicacion curricular y ejes editoriales de la asignatura.",
    "Se mantiene regla critica de normalizar salidas no estructuradas antes de propagar.",
    "Se transfieren solo patrones reutilizables y no contenido conclusivo especifico de un hermano.",
    "Supuesto: falta consigna textual de Actividad 6; se conserva estructura base verificable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear toda entrega a Licenciatura en Derecho, Filosofia del Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar como provisionales las fuentes heredadas no verificadas localmente.",
    "Conservar regla de no regresion en consolidaciones editoriales."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de memoria editorial.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Estructurar actividades con: problema, conceptos o marco normativo, desarrollo del producto, analisis propio y conclusion.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Cerrar con conclusion juridica derivada del desarrollo y transferible a practica.",
    "Alinear formato final al producto solicitado en la planeacion semanal."
  ],
  "activity_rules": [
    "Definir objetivo puntual de la actividad antes del desarrollo.",
    "Relacionar conceptos, normas, doctrina o datos con el problema planteado.",
    "Sustentar afirmaciones relevantes con fuentes verificables y cita explicita.",
    "Distinguir sintesis de fuentes y postura propia.",
    "Evitar entregas solo descriptivas o sin anclaje juridico.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Supuesto: si Actividad 6 aborda interpretacion juridica, integrar hermeneutica y argumentacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar aguas abajo.",
    "Separar reglas verificadas de supuestos marcados.",
    "No eliminar reglas utiles previas durante consolidacion.",
    "Confirmar trazabilidad de afirmaciones a fuente o supuesto marcado.",
    "Validar consistencia entre citas en texto y archivo .bib activo.",
    "Revisar que la conclusion no sea decorativa y derive del analisis."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre archivos .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en .tex.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Usar acentos y codificacion correctos en espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, citas rotas ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico antes de fijar nombres canonicos.",
    "Supuesto: el .bib canonico esperado es filosofia-del-derecho.bib hasta confirmacion local."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Usar solo obras consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y juridicas oficiales o academicas.",
    "Registrar fuentes especificas de la actividad en el .bib de la asignatura.",
    "Conservar metadatos minimos: autor, titulo, ano, editor o nota, URL cuando exista.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No asumir que filosofia-del-derecho-clean.bib aplica a todas las actividades.",
    "Supuesto: clean.bib esta orientado a interpretacion juridica (Semana 7) salvo confirmacion distinta."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir a nodos hermanos solo identidad, estructura, calidad y patrones argumentativos reutilizables.",
    "No propagar redaccion literal, conclusiones especificas ni bibliografia exclusiva de otra actividad.",
    "Mantener advertencia historica sobre salidas no estructuradas heredadas.",
    "Aplicar normalizacion manual cuando aparezcan respuestas no parseables.",
    "Agregar mejoras solo si son verificables en README, programa analitico o artefactos locales."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 6 y producto requerido.",
    "Confirmar rubrica especifica de evaluacion de Actividad 6.",
    "Confirmar si se exige formato de citacion juridica adicional a BibTeX.",
    "Confirmar nombre canonico final del .bib por token Slug no resuelto en documentos base.",
    "Confirmar si las fuentes de hermeneutica y tesis SCJN son obligatorias o solo opcionales en Actividad 6."
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
      "Problema juridico o social.",
      "Conceptos y marco normativo o doctrinal.",
      "Producto alineado a planeacion.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir la planeacion semanal en productos academicos claros, fundados y utiles para practica juridica.",
      "Sostener una memoria editorial persistente, verificable y reutilizable sin perdida."
    ],
    "style_markers": [
      "Encuadre inicial breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Postura propia diferenciada de la fuente.",
      "Citas verificables y trazables.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema antes de argumentar.",
      "Construir marco conceptual y normativo pertinente.",
      "Contrastar fuentes y justificar seleccion.",
      "Presentar postura propia con razones.",
      "Derivar conclusion desde el analisis."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco conceptual-normativo",
        "Analisis propio",
        "Conclusion transferible",
        "Hermenéutica juridica",
        "Argumentacion juridica",
        "Normalizacion de salidas estructuradas"
      ],
      "citations": [
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf",
        "hernandezManriquezHermeneutica2019",
        "scjnMemoriaArgumentacion2008"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta editorial exige rigor institucional y citas verificables."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitacion del problema no hay argumentacion pertinente."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida debe derivar del razonamiento."
        },
        {
          "source": "Hermenéutica juridica",
          "target": "Argumentacion juridica",
          "kind": "supports",
          "justification": "La interpretacion sostiene la justificacion de decisiones juridicas."
        },
        {
          "source": "Normalizacion de salidas estructuradas",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita propagar errores y conserva trazabilidad editorial."
        }
      ],
      "evidence": [
        "README: identidad UnADM, ubicacion curricular y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo estables.",
        "Registro historico: salidas no JSON en ciclos previos requieren normalizacion.",
        "Existencia de clean.bib y .bib base obliga control de alcance por actividad."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin recortar contenido util.",
      "Se reforzo regla de normalizacion previa a toda propagacion.",
      "Se mantuvo distincion entre hechos verificados y supuestos.",
      "Se evito transferir conclusiones especificas de Actividad 1 hacia Actividad 6.",
      "Se consolidaron patrones argumentativos comunes de la asignatura."
    ]
  }
}