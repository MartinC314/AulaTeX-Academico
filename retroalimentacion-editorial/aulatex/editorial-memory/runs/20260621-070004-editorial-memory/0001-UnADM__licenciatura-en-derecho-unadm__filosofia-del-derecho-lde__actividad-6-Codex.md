{
  "summary": [
    "Se consolida memoria lateral de Actividad 1 a Actividad 6 con union y deduplicacion sin perdida.",
    "Se preserva identidad UnADM y ubicacion curricular verificada: Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se refuerzan ejes editoriales estables: problema, conceptos o normas, producto, analisis propio, conclusion juridica transferible.",
    "Se mantiene regla critica: no propagar contenido no estructurado; normalizar antes de reutilizar.",
    "Se incorporan pistas locales verificables: token Slug sin resolver en README y coexistencia de filosofia-del-derecho.bib y filosofia-del-derecho-clean.bib."
  ],
  "identity_rules": [
    "Mantener tono institucional UnADM en toda entrega.",
    "Alinear contenido a Filosofia del Derecho de la Licenciatura en Derecho.",
    "Citar ubicacion curricular al contextualizar: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Entregar salida en JSON valido cuando la tarea sea de consolidacion.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio, cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Cerrar con conclusion juridica aplicable a practica profesional.",
    "Alinear formato final al producto exigido por la planeacion semanal."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Distinguir de forma explicita sintesis de fuentes y postura propia.",
    "Sustentar afirmaciones relevantes con fuentes verificables.",
    "Evitar texto solo descriptivo o de resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Relacionar conceptos y normas con el problema planteado.",
    "Supuesto: si la consigna trata interpretacion juridica, articular hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de propagar.",
    "Separar reglas confirmadas de supuestos marcados.",
    "No eliminar reglas utiles previas durante consolidacion.",
    "Verificar trazabilidad de afirmaciones a fuente o supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib activo.",
    "Revisar que la conclusion derive del desarrollo."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre .tex y .bib.",
    "No cambiar claves BibTeX ya citadas.",
    "Comprobar que cada clave citada exista en el .bib usado.",
    "Usar acentos y codificacion correctos en espanol.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) antes de fijar nombres canonicos."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y juridicas oficiales o academicas.",
    "Registrar fuentes de actividad en el .bib de la asignatura.",
    "Conservar metadatos minimos: autor, titulo, ano, editor o nota, URL cuando exista.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Tratar filosofia-del-derecho-clean.bib como archivo tematico depurado, no automaticamente canonico para toda actividad."
  ],
  "propagation_hints": [
    "Propagar lateral y recursivo solo tras validacion JSON y estructura.",
    "Transferir solo patrones reutilizables, no conclusiones especificas de Actividad 1.",
    "Aplicar union-dedupe lossless en cada ciclo.",
    "Mantener advertencias historicas de baja confianza hasta verificacion local.",
    "No convertir supuestos en hechos durante saltos entre hermanos.",
    "Usar preguntas abiertas cuando falte consigna textual de Actividad 6."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 6.",
    "Confirmar producto requerido en Actividad 6: reporte, presentacion u otro.",
    "Confirmar rubrica de evaluacion especifica para ajustar profundidad argumentativa.",
    "Confirmar nombre canonico final del .bib por token Slug no resuelto en README.",
    "Confirmar si Actividad 6 reutiliza bibliografia de interpretacion juridica o requiere corpus propio.",
    "Confirmar si se exige formato de citacion juridica adicional a BibTeX."
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
      "Problema juridico o social.",
      "Conceptos, normas o doctrina pertinentes.",
      "Producto segun planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico y criterio propio.",
      "Asegurar trazabilidad entre problema, evidencia, analisis y cierre."
    ],
    "style_markers": [
      "Inicio con encuadre breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Citas verificables y postura personal diferenciada.",
      "Cierre con utilidad profesional juridica."
    ],
    "argumentative_patterns": [
      "Delimitacion del problema.",
      "Marco conceptual y normativo.",
      "Contraste de fuentes.",
      "Toma de postura fundamentada.",
      "Conclusion derivada del analisis."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Analisis propio",
        "Conclusion transferible",
        "Hermeneutica juridica",
        "Argumentacion juridica"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
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
          "justification": "La pauta editorial exige citas verificables y formato institucional."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis se construye sobre un problema delimitado."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida debe derivar del desarrollo argumentativo."
        },
        {
          "source": "Hermeneutica juridica",
          "target": "Argumentacion juridica",
          "kind": "supports",
          "justification": "Si la actividad aborda interpretacion, la hermeneutica fundamenta la argumentacion."
        }
      ],
      "evidence": [
        "README de asignatura: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo.",
        "clean.bib: existencia de corpus sobre interpretacion juridica para uso condicionado por consigna."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas conservando contenido normativo.",
      "Se reforzo control de supuestos por falta de consigna local de Actividad 6.",
      "Se mantuvo advertencia sobre salidas no estructuradas en ciclos previos.",
      "Se anclo la memoria a evidencia local verificable sin inventar fuentes."
    ]
  }
}