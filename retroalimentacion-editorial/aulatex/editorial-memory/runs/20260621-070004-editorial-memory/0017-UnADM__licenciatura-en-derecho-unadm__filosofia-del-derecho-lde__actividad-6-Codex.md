{
  "summary": [
    "Se consolida refuerzo lateral lossless entre actividades hermanas.",
    "Se preserva identidad UnADM y ubicacion curricular verificada.",
    "Se mantiene normalizacion obligatoria antes de toda propagacion.",
    "Se refuerzan ejes editoriales estables: problema, conceptos, producto, analisis, conclusion.",
    "Se evita traslado de conclusiones o bibliografia exclusiva de una actividad hermana.",
    "Se mantiene trazabilidad de supuestos y fuentes provisionales."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear cada entrega a Licenciatura en Derecho y asignatura Filosofia del Derecho.",
    "Reconocer ubicacion curricular al contextualizar: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Conservar regla de no regresion editorial en consolidaciones."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de memoria editorial.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar desarrollo en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Alinear formato final al producto solicitado por planeacion semanal."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Distinguir sintesis de fuente y postura propia en bloques separados.",
    "Sustentar afirmaciones relevantes con fuentes verificables.",
    "Evitar desarrollo solo descriptivo o de resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir que fuentes de otras semanas aplican automaticamente a Actividad 6.",
    "Supuesto: si la consigna trata interpretacion juridica, vincular hermeneutica con argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar.",
    "Confirmar que cada afirmacion relevante tenga fuente o supuesto marcado.",
    "Separar reglas verificadas de supuestos.",
    "Validar consistencia entre citas en texto y archivo .bib activo.",
    "No eliminar reglas utiles previas durante consolidacion.",
    "Revisar que la conclusion derive del analisis y no sea decorativa."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en .tex.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Usar acentos y codificacion correcta en español en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Marcar como supuesto cualquier nombre canonico ambiguo de archivo hasta confirmacion."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas oficiales o academicas.",
    "Registrar fuentes especificas de actividad en el .bib de la asignatura.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Marcar como supuesto datos bibliograficos incompletos hasta verificacion.",
    "No transferir bibliografia exclusiva de actividad hermana sin evidencia de uso local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Aplicar union-dedupe lossless y conservar reglas historicas utiles.",
    "Propagar solo patrones reutilizables: identidad, estructura, calidad, conceptos recurrentes.",
    "No propagar supuestos como hechos confirmados.",
    "Mantener advertencia historica sobre salidas no estructuradas en ciclos tempranos.",
    "Si falta consigna local, propagar plantilla base y abrir preguntas."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 6; confirmar producto exacto solicitado.",
    "Confirmar rubrica especifica de evaluacion para Actividad 6.",
    "Confirmar si Actividad 6 exige reporte, presentacion o ambos.",
    "Confirmar nombre canonico final del .bib por token Slug sin resolver.",
    "Confirmar si filosofia-del-derecho-clean.bib aplica a Actividad 6 o solo a Semana 7.",
    "Confirmar formato de citacion juridica adicional, si existe."
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
      "Conceptos y marco normativo pertinentes.",
      "Producto alineado a planeacion semanal.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos argumentados y verificables.",
      "Sostener continuidad editorial entre actividades sin perder especificidad local."
    ],
    "style_markers": [
      "Inicio con encuadre breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Postura personal diferenciada de la sintesis.",
      "Citas verificables y trazables.",
      "Cierre con utilidad profesional juridica."
    ],
    "argumentative_patterns": [
      "Delimitar problema antes de exponer teoria.",
      "Relacionar conceptos con normas y hechos.",
      "Contrastar fuentes antes de concluir.",
      "Derivar conclusion del analisis propio.",
      "Explicitar limites y supuestos cuando falten datos."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco conceptual-normativo",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion JSON previa a propagacion",
        "Supuestos marcados"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/programa-analitico-filosofia-del-derecho.md"
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
          "justification": "El analisis requiere un problema previamente delimitado."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida debe derivar del razonamiento expuesto."
        },
        {
          "source": "Normalizacion JSON previa a propagacion",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita reutilizar salidas no estructuradas y reduce errores editoriales."
        }
      ],
      "evidence": [
        "README define identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico fija proposito y cinco ejes de trabajo.",
        "Historial de ciclos reporta incidentes de salida no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 17: se refuerza transferencia lateral por patrones reutilizables, sin copiar redaccion literal de hermano.",
      "Ciclo 17: se conserva regla critica de normalizacion estructurada antes de propagar.",
      "Ciclo 17: se mantiene separacion estricta entre hechos verificados y supuestos.",
      "Ciclo 17: se protege compatibilidad LaTeX-BibTeX y estabilidad de claves citadas."
    ]
  }
}