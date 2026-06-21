{
  "summary": [
    "Se consolida memoria lateral de Actividad 1 a Actividad 6 con union y deduplicacion sin perdida.",
    "Se preserva identidad UnADM y ubicacion curricular verificada: Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se refuerzan ejes editoriales estables: problema, conceptos o normas, producto, analisis propio y conclusion juridica transferible.",
    "Se mantiene regla critica: no propagar contenido no estructurado; normalizar antes de reutilizar.",
    "Se agrega control local verificable: resolver tokens Slug sin expandir en README y programa analitico."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear contenido a Filosofia del Derecho de la Licenciatura en Derecho.",
    "Reconocer ubicacion curricular al contextualizar: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar regla de no regresion: no eliminar reglas utiles previas."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Definir objetivo puntual antes del desarrollo de la actividad.",
    "Estructurar en bloques: problema, conceptos o marco normativo, desarrollo del producto, analisis propio y conclusion.",
    "Cerrar con conclusion juridica derivada del analisis y transferible a practica.",
    "Alinear formato final al producto pedido por la planeacion semanal."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Explicitar el problema juridico o social que activa la respuesta.",
    "Relacionar conceptos, normas, doctrina o datos con el problema planteado.",
    "Sustentar afirmaciones relevantes con fuentes verificables y cita explicita.",
    "Distinguir sintesis de fuente y postura propia.",
    "Evitar entregas solo descriptivas.",
    "Supuesto: si Actividad 6 aborda interpretacion juridica, vincular hermeneutica y argumentacion juridica."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de propagar.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Separar reglas confirmadas de supuestos marcados.",
    "Verificar trazabilidad de afirmaciones relevantes a fuente o supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Comprobar que la conclusion derive del desarrollo."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre archivos .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en .tex.",
    "Comprobar que toda clave citada exista en el archivo bibliografico activo.",
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: archivo .bib canonico esperado es filosofia-del-derecho.bib por Slug visible."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Usar solo obras realmente consultables.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar fuentes especificas de actividad en el .bib de la asignatura.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Mantener metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Marcar como supuesto todo dato bibliografico incompleto hasta verificarlo.",
    "No asumir que filosofia-del-derecho-clean.bib aplica automaticamente a Actividad 6."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Aplicar union-dedupe lossless y evitar recorte semantico.",
    "Transferir a hermanos solo patrones reutilizables, no redaccion literal ni conclusiones puntuales.",
    "No propagar supuestos como hechos confirmados.",
    "Mantener advertencia historica de salidas no estructuradas en nodos con herencia Codex o GPT-Pro provisional.",
    "Cuando falte consigna local, propagar estructura base y preguntas abiertas."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual completa de Actividad 6; confirmar producto exacto solicitado.",
    "Confirmar rubrica especifica de evaluacion para ajustar profundidad argumentativa.",
    "Confirmar si Actividad 6 exige reporte, presentacion o ambos.",
    "Confirmar nombre canonico final del .bib de la asignatura por token Slug sin resolver.",
    "Confirmar si debe usarse bibliografia de interpretacion juridica de clean.bib en esta actividad.",
    "Confirmar si existe formato juridico de citacion adicional a BibTeX institucional."
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
      "Problema juridico o social.",
      "Conceptos y marco normativo o doctrinal.",
      "Producto de planeacion semanal.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos estructurados.",
      "Asegurar fundamento juridico, evidencia verificable y utilidad profesional."
    ],
    "style_markers": [
      "Inicio con encuadre breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Diferenciacion visible entre fuente y postura propia.",
      "Cierre con criterio juridico aplicable."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer conceptos y marco normativo.",
      "Analizar evidencia y contrastar fuentes.",
      "Fijar postura propia argumentada.",
      "Concluir con derivacion logica y transferencia practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco conceptual y normativo",
        "Analisis propio",
        "Conclusion transferible",
        "Hermenutica juridica",
        "Argumentacion juridica"
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
          "justification": "La pauta exige citas verificables y formato institucional."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "No hay analisis solido sin delimitacion del problema."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida debe derivar del desarrollo."
        },
        {
          "source": "Hermenutica juridica",
          "target": "Argumentacion juridica",
          "kind": "supports",
          "justification": "En actividades de interpretacion, la hermeneutica fundamenta la argumentacion."
        }
      ],
      "evidence": [
        "README: identidad UnADM, ubicacion curricular y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo.",
        "Regla transversal heredada: normalizar antes de propagar.",
        "Contexto local: coexisten filosofia-del-derecho.bib y filosofia-del-derecho-clean.bib."
      ]
    },
    "reinforcement_log": [
      "Ciclo 11: refuerzo lateral aplicado con analogia controlada entre hermanos.",
      "Se deduplicaron reglas repetidas manteniendo cobertura semantica.",
      "Se conservaron advertencias de fuentes provisionales y de JSON no parseable historico.",
      "Se anclaron mejoras verificables al contexto local: token Slug sin resolver y gestion de .bib."
    ]
  }
}