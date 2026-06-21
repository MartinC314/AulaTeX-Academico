{
  "summary": [
    "Se consolida memoria lateral para Actividad 6 con deduplicacion lossless y sin recorte de reglas utiles.",
    "Se preserva identidad UnADM y contexto curricular verificado: Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se mantienen ejes editoriales estables: problema, conceptos o normas, producto, analisis propio y conclusion juridica transferible.",
    "Se refuerza regla critica: no propagar salidas no estructuradas; normalizar antes de reutilizar.",
    "Se mantiene separacion entre reglas confirmadas y supuestos marcados."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear la actividad a Licenciatura en Derecho y asignatura Filosofia del Derecho.",
    "Contextualizar ubicacion curricular al citar la materia: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Conservar regla de no regresion editorial en consolidaciones."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el producto al formato exigido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Relacionar conceptos, normas o doctrina con el problema planteado.",
    "Sustentar afirmaciones relevantes con fuentes verificables.",
    "Distinguir sintesis de fuentes y postura propia.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Supuesto: si la consigna trata interpretacion juridica, articular hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de propagar.",
    "Revisar que no exista respuesta no estructurada reutilizada.",
    "Confirmar trazabilidad de afirmaciones a fuente o supuesto marcado.",
    "Validar consistencia entre citas en texto y archivo .bib activo.",
    "Separar reglas verificadas de supuestos.",
    "No eliminar reglas utiles previas durante consolidacion."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener compatibilidad .tex/.bib sin cambiar claves citadas existentes.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico antes de fijar nombres canonicos.",
    "Marcar como supuesto cualquier nombre de archivo ambiguo hasta confirmacion."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y juridicas oficiales o academicas.",
    "Registrar fuentes especificas de actividad en el .bib de la asignatura.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No asumir que el clean.bib de Semana 7 aplica automaticamente a Actividad 6."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir a nodos hermanos solo patrones reutilizables, no redaccion literal ni conclusiones locales.",
    "Aplicar union-dedupe lossless en cada ciclo.",
    "Conservar advertencias historicas sobre salidas no parseables en linajes con herencia Codex/GPT-Pro.",
    "Propagar identidad curricular verificada y gates de calidad como base comun.",
    "Cuando falte consigna local, propagar estructura base y abrir preguntas en lugar de inventar contenido."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual completa de Actividad 6; confirmar producto exacto solicitado.",
    "Confirmar rubrica de evaluacion especifica para ajustar profundidad argumentativa.",
    "Confirmar si Actividad 6 exige formato adicional de citacion juridica ademas de BibTeX.",
    "Confirmar nombre canonico final del .bib por token Slug no resuelto y coexistencia de filosofia-del-derecho.bib y filosofia-del-derecho-clean.bib.",
    "Confirmar si las fuentes de interpretacion juridica de clean.bib son obligatorias u opcionales para Actividad 6."
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
        "Asignatura Filosofia del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social delimitado.",
      "Conceptos, normas y doctrina pertinentes.",
      "Producto alineado a planeacion.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir la planeacion semanal en productos academicos con fundamento juridico y utilidad profesional.",
      "Garantizar consistencia editorial institucional entre actividades hermanas.",
      "Sostener calidad tecnica en estructura, citas y compilacion."
    ],
    "style_markers": [
      "Inicio con encuadre del problema.",
      "Secciones explicitas y ordenadas.",
      "Diferenciacion visible entre fuente y postura propia.",
      "Cierre con criterio juridico aplicable."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Construir marco conceptual-normativo.",
      "Contrastar fuentes verificables.",
      "Emitir postura propia fundamentada.",
      "Derivar conclusion del analisis."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Analisis propio",
        "Conclusion transferible",
        "Hermeneutica juridica [supuesto condicionado]",
        "Argumentacion juridica [supuesto condicionado]"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
        "README.md de asignatura",
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
          "justification": "El analisis requiere un problema delimitado para ser evaluable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion debe derivar del desarrollo argumentativo."
        },
        {
          "source": "Hermeneutica juridica [supuesto condicionado]",
          "target": "Argumentacion juridica [supuesto condicionado]",
          "kind": "supports",
          "justification": "Si la consigna aborda interpretacion, la hermeneutica sustenta la argumentacion."
        }
      ],
      "evidence": [
        "README: identidad UnADM, ubicacion curricular y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo recurrentes.",
        "Regla historica: normalizar salida no estructurada antes de propagar.",
        "Contexto local: token Slug sin resolver para nombre de .bib."
      ]
    },
    "reinforcement_log": [
      "Ciclo 29: deduplicacion de reglas repetidas en identidad, estructura, calidad y latex.",
      "Ciclo 29: preservada advertencia de fuentes heredadas provisionales.",
      "Ciclo 29: reforzada separacion entre hechos verificados y supuestos.",
      "Ciclo 29: mantenido patron argumentativo comun para nodos hermanos sin copiar contenido especifico."
    ]
  }
}