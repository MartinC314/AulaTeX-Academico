{
  "summary": [
    "Se consolida memoria lateral de actividad 1 a actividad 6 con union y deduplicacion sin perdida.",
    "Se preserva identidad UnADM y ubicacion curricular verificada: Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se refuerzan ejes editoriales recurrentes: problema, conceptos o normas, producto, analisis propio y conclusion juridica transferible.",
    "Se mantiene regla critica: no propagar contenido no estructurado; normalizar antes de reutilizar.",
    "Se mantiene traza de riesgo historico: hubo salidas no JSON parseables en ciclos previos.",
    "Se evita transferir conclusiones especificas o bibliografia exclusiva de actividad 1."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear la actividad a Filosofia del Derecho de la Licenciatura en Derecho.",
    "Citar ubicacion curricular solo con dato verificado: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local de actividad 6.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar regla de no regresion: no eliminar reglas utiles previas."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual de la actividad antes del desarrollo.",
    "Alinear el producto al formato solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de actividad 6 sin romper ejes base.",
    "Distinguir sintesis de fuente y postura propia en forma explicita.",
    "Sustentar afirmaciones relevantes con fuentes verificables.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Relacionar conceptos, normas o doctrina con el problema planteado.",
    "Supuesto: si actividad 6 aborda interpretacion juridica, integrar hermeneutica y argumentacion juridica."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de propagar.",
    "Revisar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Separar reglas confirmadas de supuestos editoriales.",
    "Validar que la conclusion derive del analisis.",
    "Validar consistencia entre citas en texto y archivo .bib activo.",
    "Aplicar deduplicacion por union sin perdida de reglas vigentes."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre .tex y .bib.",
    "No cambiar claves BibTeX ya citadas sin necesidad justificada.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Usar acentos y codificacion correctos en espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico antes de fijar nombres canonicos.",
    "Supuesto: el .bib canonico esperado por Slug es filosofia-del-derecho.bib; confirmar localmente."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y juridicas oficiales o academicas.",
    "Registrar fuentes especificas de actividad en el .bib de la asignatura.",
    "Conservar metadatos minimos: autor, titulo, ano, editorial o nota, URL cuando exista.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No asumir que filosofia-del-derecho-clean.bib aplica a toda actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib esta orientado a interpretacion juridica (Semana 7) y su uso en actividad 6 depende de consigna."
  ],
  "propagation_hints": [
    "Propagar a nodos hermanos solo reglas reutilizables y verificadas.",
    "No transferir redaccion literal ni conclusiones especificas entre actividades hermanas.",
    "Conservar advertencias historicas de calidad sobre JSON no parseable.",
    "Aplicar normalizacion manual cuando reaparezca salida no estructurada.",
    "Propagar identidad curricular y compuertas de calidad como nucleo estable.",
    "Cuando falte consigna local, propagar estructura base y abrir preguntas."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad 6.",
    "Confirmar producto principal requerido en actividad 6: reporte, presentacion u otro.",
    "Confirmar rubrica especifica de evaluacion para actividad 6.",
    "Confirmar si actividad 6 exige formato de citacion juridica adicional a BibTeX.",
    "Confirmar nombre canonico final del archivo .bib por token Slug sin resolver en README.",
    "Confirmar si la fuente provisional heredada debe reemplazarse por validacion local."
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
      "Problema juridico o social como punto de partida.",
      "Marco conceptual y normativo pertinente.",
      "Producto alineado a planeacion semanal.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos con fundamento juridico, evidencia y criterio propio.",
      "Asegurar consistencia institucional y calidad tecnica en contenidos y formato."
    ],
    "style_markers": [
      "Encuadre inicial breve y focalizado.",
      "Secciones explicitas y ordenadas.",
      "Postura propia diferenciada de la fuente.",
      "Cierre aplicado a practica juridica.",
      "Supuestos marcados cuando falten datos."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Definir conceptos y marco normativo.",
      "Contrastar fuentes relevantes.",
      "Sostener postura propia con evidencia.",
      "Cerrar con conclusion derivada del analisis."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion estructurada",
        "JSON parseable",
        "Hermeneutica juridica [supuesto condicionado]"
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
          "justification": "El analisis debe construirse sobre un problema delimitado."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida deriva del desarrollo argumentativo."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "JSON parseable",
          "kind": "supports",
          "justification": "La propagacion segura depende de salidas estructuradas."
        },
        {
          "source": "Hermeneutica juridica [supuesto condicionado]",
          "target": "Marco normativo o doctrinal",
          "kind": "develops",
          "justification": "Aplica solo si la consigna de actividad 6 trata interpretacion juridica."
        }
      ],
      "evidence": [
        "README: identidad UnADM, entrada canonica, pauta editorial y ubicacion curricular.",
        "Programa analitico: cinco ejes de trabajo recurrentes.",
        "Historial de ciclos: incidencias de salida no JSON parseable y necesidad de normalizacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 3: se consolidan reglas comunes de hermano sin copiar contenido especifico.",
      "Ciclo 3: se preservan reglas de calidad y no regresion.",
      "Ciclo 3: se refuerza manejo de supuestos por falta de consigna local.",
      "Ciclo 3: se mantiene advertencia sobre tokens Slug sin resolver en documentos base."
    ]
  }
}