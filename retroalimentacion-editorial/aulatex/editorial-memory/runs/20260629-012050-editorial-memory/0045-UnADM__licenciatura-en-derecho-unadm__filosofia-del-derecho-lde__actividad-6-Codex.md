{
  "summary": [
    "Se consolida refuerzo lateral entre actividades hermanas sin copiar contenido especifico.",
    "Se preserva identidad UnADM y ubicacion curricular verificada: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se mantienen ejes editoriales estables: problema, conceptos o normas, producto, analisis propio, conclusion juridica.",
    "Se refuerza regla critica: no propagar salidas no estructuradas; normalizar antes de reutilizar.",
    "Se conserva compresion lossless por union y deduplicacion de reglas vigentes.",
    "Supuesto: falta consigna textual de Actividad 6; se transfiere estructura base reusable."
  ],
  "identity_rules": [
    "Mantener tono institucional UnADM en toda entrega.",
    "Alinear cada producto a Licenciatura en Derecho y asignatura Filosofia del Derecho.",
    "Citar contexto curricular cuando aplique: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar como provisionales las fuentes heredadas no verificadas localmente.",
    "Conservar regla de no regresion editorial en cada ciclo de consolidacion."
  ],
  "structure_rules": [
    "Entregar JSON parseable en tareas de memoria editorial.",
    "Usar exactamente el esquema requerido, sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual de la actividad antes del desarrollo.",
    "Alinear formato final al producto pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Distinguir con claridad sintesis de fuentes y postura propia.",
    "Sustentar afirmaciones relevantes con fuentes verificables.",
    "Evitar entregas solo descriptivas sin criterio juridico.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Relacionar conceptos y normas con el problema delimitado.",
    "Supuesto: si la consigna aborda interpretacion juridica, articular hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de propagar.",
    "Separar reglas verificadas de supuestos marcados.",
    "No eliminar reglas utiles previas durante consolidacion.",
    "Validar trazabilidad de afirmaciones a fuente o supuesto.",
    "Comprobar consistencia entre citas en texto y archivo .bib activo.",
    "Revisar que la conclusion derive del analisis y no sea decorativa."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en .tex.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Usar acentos y codificacion correcta en espanol.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Marcar como supuesto el nombre canonico de .bib hasta confirmacion final."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo fuentes consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y juridicas oficiales o academicas.",
    "Registrar nuevas fuentes en el .bib de la asignatura.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No transferir bibliografia exclusiva de una actividad hermana como obligatoria en otra.",
    "Supuesto: filosofia-del-derecho-clean.bib puede ser corpus tematico puntual y no canon general."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas reutilizables de identidad, estructura y calidad.",
    "Aplicar union-dedupe lossless en cada salto lateral.",
    "No copiar conclusiones ni redaccion literal entre actividades hermanas.",
    "Conservar advertencias historicas sobre salidas no estructuradas.",
    "Elevar a verificado solo lo confirmado por documentos locales.",
    "Cuando falte consigna local, propagar plantilla base y abrir preguntas."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 6.",
    "Confirmar rubrica especifica de evaluacion para calibrar profundidad argumentativa.",
    "Confirmar producto principal exigido: reporte, presentacion u otro.",
    "Confirmar nombre canonico final del archivo .bib por token Slug sin resolver.",
    "Confirmar si se exige formato de citacion juridica adicional a BibTeX.",
    "Confirmar si el corpus de interpretacion juridica aplica formalmente a Actividad 6."
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
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos consistentes y verificables.",
      "Preservar continuidad editorial entre actividades sin perder especificidad local."
    ],
    "style_markers": [
      "Inicio con encuadre breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Postura propia diferenciada de la fuente.",
      "Cierre con utilidad profesional juridica.",
      "Marcado explicito de supuestos."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Definir marco conceptual y normativo.",
      "Contrastar fuentes relevantes.",
      "Tomar postura fundamentada.",
      "Concluir con criterio aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Hermeneutica juridica",
        "Argumentacion juridica",
        "Normalizacion JSON"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "README.md de la asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "filosofia-del-derecho-clean.bib",
        "filosofia-del-derecho.bib"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y forma academica."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "La argumentacion valida parte de un problema delimitado."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion debe derivar del desarrollo, no de afirmaciones aisladas."
        },
        {
          "source": "Hermeneutica juridica",
          "target": "Argumentacion juridica",
          "kind": "supports",
          "justification": "En actividades de interpretacion, la hermeneutica fundamenta la argumentacion."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia confiable."
        }
      ],
      "evidence": [
        "README confirma identidad UnADM y pauta editorial.",
        "Programa analitico define cinco ejes de trabajo.",
        "Malla curricular respalda ubicacion: semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Coexistencia de .bib y clean.bib exige validacion local por actividad.",
        "Historial de salida no parseable justifica puerta de calidad JSON."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: se mantiene union-dedupe lossless sin recorte de reglas utiles.",
      "Ciclo 2: se transfiere solo patron reusable; no se copia bibliografia exclusiva ni conclusiones del hermano.",
      "Ciclo 2: se refuerza marcado de supuestos por falta de consigna local completa.",
      "Ciclo 2: se conserva alerta sobre token Slug sin resolver y validacion de .bib canonico."
    ]
  }
}