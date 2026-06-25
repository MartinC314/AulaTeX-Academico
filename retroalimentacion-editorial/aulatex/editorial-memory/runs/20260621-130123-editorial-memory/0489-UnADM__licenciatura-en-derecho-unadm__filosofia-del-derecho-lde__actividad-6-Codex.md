{
  "summary": [
    "Se consolida refuerzo lateral entre actividades hermanas con deduplicacion sin perdida.",
    "Se preserva ADN UnADM: identidad institucional, integridad academica, citas verificables y conclusion juridica propia.",
    "Se mantiene ubicacion curricular verificada: Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se refuerzan ejes estables: problema, conceptos o normas, producto, analisis propio y conclusion transferible.",
    "Se conserva regla critica: no propagar contenido no estructurado; normalizar antes de reutilizar."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en toda entrega.",
    "Alinear toda actividad a Filosofia del Derecho de la Licenciatura en Derecho.",
    "Citar ubicacion curricular cuando aplique: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Conservar regla de no regresion en consolidaciones editoriales."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de memoria.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear formato final al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Distinguir sintesis de fuentes y postura propia.",
    "Sustentar afirmaciones relevantes con fuentes verificables.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Relacionar conceptos y normas con el problema planteado.",
    "Supuesto: si la consigna de Actividad 6 aborda interpretacion juridica, usar hermeneutica y argumentacion como marco."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de propagar.",
    "Separar reglas confirmadas de supuestos marcados.",
    "No eliminar reglas utiles previas durante consolidacion.",
    "Validar trazabilidad de afirmaciones a fuente o supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar que la conclusion derive del analisis."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre .tex y .bib.",
    "No cambiar claves BibTeX ya citadas.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Usar acentos y codificacion correcta en español.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: nombre canónico esperado del .bib es filosofia-del-derecho.bib hasta confirmacion final."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo fuentes consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y juridicas oficiales o academicas.",
    "Registrar fuentes especificas por actividad en el .bib de asignatura.",
    "Mantener metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No asumir que filosofia-del-derecho-clean.bib aplica a toda actividad; validar por consigna."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir solo patrones reutilizables, no conclusiones especificas.",
    "Aplicar union-dedupe lossless en nodos hermanos.",
    "Conservar advertencias historicas de fuentes provisionales.",
    "No propagar supuestos como hechos confirmados.",
    "Si falta consigna local, propagar estructura base y abrir preguntas."
  ],
  "open_questions": [
    "Confirmar consigna exacta y rubrica de Actividad 6.",
    "Confirmar producto principal requerido: reporte, presentacion u otro.",
    "Confirmar si Actividad 6 corresponde formalmente a interpretacion juridica.",
    "Confirmar nombre canonico final del archivo .bib de la asignatura.",
    "Confirmar si se exige formato de citacion juridica adicional a BibTeX institucional."
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
      "Conceptos, normas y doctrina pertinentes.",
      "Producto alineado a planeacion.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico y postura propia.",
      "Estandarizar calidad editorial reusable entre actividades hermanas sin perder contexto."
    ],
    "style_markers": [
      "Inicio con encuadre breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Fuentes verificables con postura personal diferenciada.",
      "Cierre con utilidad profesional juridica."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Establecer marco conceptual y normativo.",
      "Contrastar fuentes.",
      "Sostener postura propia argumentada.",
      "Concluir con criterio juridico aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Analisis propio",
        "Conclusion transferible",
        "Hermeneutica juridica",
        "Argumentacion juridica",
        "Normalizacion de salidas estructuradas"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "hernandezManriquezHermeneutica2019",
        "scjnMemoriaArgumentacion2008",
        "scjnViolenciaFisica2022",
        "scjnIncapacidadResistencia2019"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y rigor."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere delimitacion previa del problema."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida deriva del desarrollo argumentativo."
        },
        {
          "source": "Hermeneutica juridica",
          "target": "Argumentacion juridica",
          "kind": "supports",
          "justification": "En actividades de interpretacion, la hermeneutica fundamenta la argumentacion."
        },
        {
          "source": "Normalizacion de salidas estructuradas",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita propagar errores y preserva trazabilidad editorial."
        }
      ],
      "evidence": [
        "README de asignatura: identidad y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo.",
        "Regla historica consolidada: bloquear propagacion sin JSON parseable.",
        "Supuesto marcado: aplicacion de clean.bib depende de consigna local."
      ]
    },
    "reinforcement_log": [
      "Ciclo 13: deduplicacion completa de reglas repetidas en origen y destino.",
      "Ciclo 13: se preservan reglas utiles previas sin recorte semantico.",
      "Ciclo 13: se refuerza control de supuestos y fuentes provisionales.",
      "Ciclo 13: se mantiene separacion entre patrones reutilizables y contenido especifico de actividad."
    ]
  }
}