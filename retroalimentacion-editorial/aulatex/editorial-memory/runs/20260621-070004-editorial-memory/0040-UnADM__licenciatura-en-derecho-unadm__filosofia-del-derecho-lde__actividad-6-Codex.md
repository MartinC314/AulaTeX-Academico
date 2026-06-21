{
  "summary": [
    "Se consolida memoria lateral de Actividad 1 a Actividad 6 con union-dedupe sin perdida.",
    "Se preserva identidad institucional UnADM y ubicacion curricular verificada.",
    "Se refuerza regla critica: normalizar antes de propagar y bloquear salida no JSON parseable.",
    "Se mantienen ejes editoriales estables: problema, conceptos o normas, producto, analisis propio y conclusion juridica.",
    "Se incorpora control de supuestos cuando la consigna local no sea visible."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear contenido a Licenciatura en Derecho, Filosofia del Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar regla de no regresion en consolidaciones."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido y sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear el producto al formato pedido por la planeacion semanal."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Sostener afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir sintesis de fuente y postura propia.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No transferir conclusiones especificas de Actividad 1 a Actividad 6.",
    "Supuesto: si Actividad 6 es de interpretacion juridica, vincular hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar aguas abajo.",
    "Separar reglas confirmadas de supuestos marcados.",
    "Validar trazabilidad de afirmaciones relevantes a fuente o supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No eliminar reglas utiles previas durante consolidacion."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Marcar como supuesto el nombre canonico del .bib mientras exista ambiguedad local."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Registrar fuentes especificas de actividad en el .bib de la asignatura.",
    "Mantener metadatos minimos: autor, titulo, ano, editorial o nota, URL cuando exista.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No asumir que filosofia-del-derecho-clean.bib aplica a toda actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib esta orientado a interpretacion juridica (Semana 7)."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir solo patrones reutilizables de identidad, estructura, calidad y relaciones conceptuales.",
    "No propagar redaccion literal ni bibliografia exclusiva entre hermanos.",
    "Aplicar union-dedupe lossless para evitar duplicados y preservar reglas utiles.",
    "Mantener advertencias historicas sobre salidas no estructuradas heredadas.",
    "Cuando falten datos locales, propagar plantilla base y abrir preguntas."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 6.",
    "Confirmar rubrica especifica de evaluacion para Actividad 6.",
    "Confirmar formato principal requerido: reporte, presentacion u otro.",
    "Confirmar nombre canonico final del archivo .bib por token Slug sin resolver.",
    "Confirmar si Actividad 6 requiere corpus de interpretacion juridica o uno distinto."
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
      "Problema juridico o social delimitado.",
      "Conceptos, normas y doctrina pertinentes.",
      "Producto alineado a planeacion semanal.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico.",
      "Asegurar coherencia entre evidencia, analisis y conclusion.",
      "Preservar identidad UnADM en cada entrega."
    ],
    "style_markers": [
      "Inicio con encuadre del problema.",
      "Secciones explicitas y ordenadas.",
      "Diferenciacion clara entre fuente y postura propia.",
      "Cierre con utilidad profesional juridica.",
      "Supuestos marcados cuando falte dato local."
    ],
    "argumentative_patterns": [
      "Delimitacion del problema.",
      "Marco conceptual y normativo.",
      "Analisis critico con soporte de fuentes.",
      "Postura propia argumentada.",
      "Conclusion derivada del desarrollo."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion estructurada",
        "Hermeneutica juridica [supuesto condicionado]"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "README.md de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "filosofia-del-derecho-clean.bib [uso condicionado por consigna]"
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
          "justification": "El analisis requiere un problema delimitado."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida deriva del desarrollo argumentativo."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "supports",
          "justification": "Sin JSON parseable no hay transferencia confiable."
        }
      ],
      "evidence": [
        "README: identidad UnADM, ubicacion curricular y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo.",
        "Memoria origen: regla de bloqueo por salida no estructurada.",
        "Contexto local: coexistencia de .bib canonico y clean.bib."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin recortar contenido util.",
      "Se reforzo compatibilidad lateral entre actividades hermanas.",
      "Se retiro transferencia de contenido especifico no reusable y se mantuvieron patrones.",
      "Se marcaron supuestos donde falta consigna local verificable."
    ]
  }
}