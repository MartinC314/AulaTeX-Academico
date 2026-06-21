{
  "summary": [
    "Se consolida memoria lateral de actividad 1 hacia actividad 6 con union y deduplicacion sin perdida.",
    "Se preserva identidad UnADM y ubicacion curricular verificada: Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se refuerzan ejes editoriales estables: problema, conceptos o normas, producto, analisis propio y conclusion juridica transferible.",
    "Se mantiene regla critica: no propagar contenido no estructurado; normalizar antes de reutilizar.",
    "Se conserva trazabilidad de fuentes provisionales heredadas hasta validacion local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear la actividad a Licenciatura en Derecho y asignatura Filosofia del Derecho.",
    "Citar ubicacion curricular al contextualizar: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar toda fuente heredada no verificada como provisional hasta confirmacion local.",
    "Conservar regla de no regresion: no eliminar reglas utiles previas."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el producto al formato solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de actividad 6 sin romper ejes base de la asignatura.",
    "Explicitar el problema juridico o social que activa la respuesta.",
    "Relacionar conceptos, normas, doctrina o datos con el problema planteado.",
    "Distinguir sintesis de fuentes y postura propia del estudiante.",
    "Sustentar afirmaciones relevantes con fuentes verificables.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Supuesto: si actividad 6 aborda interpretacion juridica, integrar hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de propagar.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Separar reglas verificadas de supuestos marcados.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar que la conclusion derive del analisis y no sea decorativa.",
    "No eliminar reglas utiles previas durante consolidacion."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener compatibilidad entre .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en .tex.",
    "Comprobar que toda clave citada exista en el archivo bibliografico activo.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Verificar nombres de archivo antes de referenciarlos.",
    "Corregir caracteres anomalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: el .bib canonico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar fuentes especificas de la actividad en el .bib de la asignatura.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Marcar como supuesto todo dato bibliografico incompleto hasta verificarlo.",
    "No asumir que un .bib depurado de otra semana aplica automaticamente a actividad 6."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Propagar solo patrones reutilizables: identidad, estructura, calidad, conceptos recurrentes y relaciones estables.",
    "No propagar redaccion literal, conclusiones especificas ni bibliografia exclusiva de un hermano.",
    "Aplicar union-dedupe lossless en cada ciclo para evitar regresiones.",
    "Mantener advertencias historicas de salidas no estructuradas en nodos con herencia provisional.",
    "Si falta consigna local, propagar plantilla base y abrir preguntas en lugar de inventar contenido."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual completa de actividad 6; confirmar producto exacto solicitado.",
    "Confirmar rubrica especifica de evaluacion para ajustar profundidad argumentativa.",
    "Confirmar si actividad 6 exige reporte, presentacion u otro formato principal.",
    "Confirmar nombre canonico final del archivo .bib de la asignatura.",
    "Confirmar si actividad 6 requiere fuentes obligatorias de semana especifica.",
    "Confirmar si la memoria provisional heredada ya fue validada localmente."
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
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto segun planeacion.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos con fundamento juridico, evidencia y criterio propio.",
      "Garantizar coherencia entre identidad institucional, estructura argumentativa y calidad verificable."
    ],
    "style_markers": [
      "Encuadre inicial breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Postura propia diferenciada de la sintesis de fuentes.",
      "Cierre con utilidad profesional juridica.",
      "Supuestos marcados cuando falten datos."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Desarrollar marco conceptual y normativo.",
      "Contrastar fuentes verificables.",
      "Sostener postura propia fundada.",
      "Concluir con criterio juridico aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco conceptual-normativo",
        "Analisis propio",
        "Conclusion transferible",
        "Hermenautica juridica [supuesto condicional]",
        "Argumentacion juridica [supuesto condicional]"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "README.md de la asignatura",
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
          "justification": "La conclusion valida debe derivar del desarrollo argumentativo."
        },
        {
          "source": "Hermenautica juridica [supuesto condicional]",
          "target": "Argumentacion juridica [supuesto condicional]",
          "kind": "supports",
          "justification": "Si la consigna trata interpretacion, la hermeneutica fortalece la justificacion argumentativa."
        }
      ],
      "evidence": [
        "Pauta editorial en README: identidad UnADM, integridad academica, citas verificables y conclusion juridica propia.",
        "Programa analitico: cinco ejes de trabajo recurrentes.",
        "Regla tecnica consolidada: bloquear propagacion de salida no JSON parseable.",
        "Coexistencia de filosofia-del-derecho.bib y filosofia-del-derecho-clean.bib; requiere confirmacion canonica."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin perdida semantica.",
      "Se mantuvieron reglas utiles previas y se eliminaron redundancias literales.",
      "Se reforzo separacion entre hechos verificados y supuestos.",
      "Se preservaron conexiones argumentativas reutilizables para nodos hermanos."
    ]
  }
}