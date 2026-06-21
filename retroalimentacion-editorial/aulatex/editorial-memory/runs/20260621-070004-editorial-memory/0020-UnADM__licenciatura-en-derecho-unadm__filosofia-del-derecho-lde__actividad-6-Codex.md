{
  "summary": [
    "Se consolida refuerzo lateral entre actividades hermanas sin copiar redaccion literal.",
    "Se preserva identidad UnADM y ubicacion curricular verificada: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se mantienen ejes editoriales estables: problema, conceptos o normas, producto, analisis propio y conclusion juridica transferible.",
    "Se refuerza regla critica: no propagar contenido no estructurado sin normalizacion JSON.",
    "Se conserva compresion lossless por union y deduplicacion de reglas validas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear toda entrega a Licenciatura en Derecho y asignatura Filosofia del Derecho.",
    "Citar ubicacion curricular al contextualizar: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Conservar regla de no regresion editorial en consolidaciones."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de memoria editorial.",
    "Usar exactamente el esquema solicitado y sin claves extra.",
    "Estructurar producto academico en: problema, marco conceptual-normativo, desarrollo, analisis propio y conclusion.",
    "Definir objetivo puntual antes del desarrollo.",
    "Cerrar con conclusion juridica derivada del analisis y transferible a practica."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Explicitar problema juridico o social desde el inicio.",
    "Relacionar conceptos, normas o doctrina con el problema planteado.",
    "Sostener afirmaciones relevantes con fuentes verificables.",
    "Distinguir sintesis de fuentes y postura propia.",
    "Evitar entregas solo descriptivas.",
    "No trasladar conclusiones especificas de actividad hermana."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar.",
    "Separar reglas confirmadas de supuestos marcados.",
    "Verificar trazabilidad de afirmaciones a fuente o supuesto.",
    "Validar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No eliminar reglas utiles previas durante consolidacion.",
    "Validar consistencia entre citas en texto y .bib activo."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre .tex y .bib.",
    "No cambiar claves BibTeX ya citadas.",
    "Comprobar que toda clave citada exista en el archivo bibliografico activo.",
    "Usar acentos y codificacion correcta en espanol.",
    "Evitar comandos no estandar sin justificacion.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: archivo .bib canonico esperado es filosofia-del-derecho.bib hasta confirmacion."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Registrar fuentes especificas de cada actividad en el .bib de asignatura.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener metadatos minimos: autor, titulo, ano, editor o nota, URL cuando exista.",
    "Marcar como supuesto todo dato bibliografico incompleto.",
    "No asumir que clean.bib aplica automaticamente a toda actividad."
  ],
  "propagation_hints": [
    "Propagar solo patrones reutilizables: identidad, estructura, calidad y relaciones conceptuales.",
    "No propagar redaccion literal ni bibliografia exclusiva de otra actividad.",
    "Aplicar union-dedupe lossless en cada ciclo recursivo.",
    "Mantener advertencias historicas de salidas no estructuradas.",
    "Propagar supuestos como supuestos, nunca como hechos confirmados.",
    "Si falta consigna local, transferir estructura base y abrir preguntas."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 6; confirmar producto exacto solicitado.",
    "Confirmar rubrica especifica de evaluacion de Actividad 6.",
    "Confirmar si Actividad 6 exige reporte, presentacion o ambos.",
    "Confirmar nombre canonico final del .bib por token Slug sin resolver.",
    "Confirmar si las fuentes de interpretacion juridica de clean.bib son obligatorias o solo opcionales para Actividad 6."
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
      "Marco conceptual y normativo pertinente.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible.",
      "Normalizacion estructurada antes de propagar."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos consistentes.",
      "Asegurar fundamento juridico y evidencia verificable.",
      "Evitar regresiones de calidad editorial entre actividades hermanas."
    ],
    "style_markers": [
      "Inicio con encuadre breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Postura personal diferenciada de la sintesis.",
      "Cierre con utilidad profesional juridica.",
      "Supuestos marcados de forma visible."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual-normativo.",
      "Contrastar fuentes pertinentes.",
      "Sostener postura propia con evidencia.",
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
        "Hermeneutica juridica [supuesto condicionado a consigna]",
        "Argumentacion juridica [supuesto condicionado a consigna]"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
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
          "justification": "Sin delimitacion del problema no hay argumentacion focalizada."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida debe derivar del desarrollo."
        },
        {
          "source": "Hermeneutica juridica [supuesto condicionado a consigna]",
          "target": "Argumentacion juridica [supuesto condicionado a consigna]",
          "kind": "supports",
          "justification": "Si la actividad trata interpretacion, la hermeneutica fundamenta la argumentacion."
        }
      ],
      "evidence": [
        "README: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo.",
        "Historial de calidad: bloqueo por salidas no JSON parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 20: deduplicadas reglas repetidas y preservadas reglas utiles previas.",
      "Ciclo 20: reforzada compatibilidad estructural JSON para propagacion recursiva.",
      "Ciclo 20: mantenida separacion entre hechos confirmados y supuestos.",
      "Ciclo 20: transferidos solo patrones reutilizables entre hermanos."
    ]
  }
}