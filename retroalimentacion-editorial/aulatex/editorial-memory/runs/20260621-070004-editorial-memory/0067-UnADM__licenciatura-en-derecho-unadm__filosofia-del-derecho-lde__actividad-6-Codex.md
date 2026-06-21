{
  "summary": [
    "Se consolida refuerzo lateral desde actividad 1 hacia actividad 6 sin copiar contenido especifico.",
    "Se preserva identidad UnADM con ubicacion curricular verificada y tono juridico-academico.",
    "Se mantienen ejes editoriales estables: problema, conceptos o normas, producto, analisis propio y conclusion transferible.",
    "Se refuerza regla critica de normalizacion: no propagar salidas no estructuradas.",
    "Se conserva deduplicacion lossless por union de reglas utiles previas.",
    "Se mantiene trazabilidad de supuestos cuando falta consigna local de actividad 6."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear contenido a Licenciatura en Derecho, asignatura Filosofia del Derecho.",
    "Reconocer ubicacion curricular al contextualizar: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar regla de no regresion: no eliminar reglas utiles previas."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el producto al formato solicitado en la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Adaptar la redaccion al objetivo especifico de actividad 6 sin romper ejes base.",
    "Explicitar el problema que activa la respuesta.",
    "Relacionar conceptos, normas, doctrina o datos con el problema planteado.",
    "Sostener afirmaciones con fuentes verificables disponibles.",
    "Distinguir sintesis de fuente y postura propia.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Supuesto: si la consigna aborda interpretacion juridica, vincular hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que cada afirmacion relevante tenga fuente o marca de supuesto.",
    "Validar coherencia con pauta editorial de la asignatura.",
    "Validar correspondencia del producto con la consigna local de actividad 6.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar deduplicacion por union sin perdida de reglas vigentes."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener compatibilidad entre .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en .tex.",
    "Comprobar que toda clave citada exista en el archivo bibliografico activo.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Marcar como supuesto el nombre canonico de .bib mientras persista ambiguedad."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar fuentes especificas de actividad en el .bib de la asignatura.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Marcar como supuesto todo dato bibliografico incompleto hasta verificarlo.",
    "No asumir que bibliografia de otra semana aplica automaticamente a actividad 6."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir a nodos hermanos solo patrones reutilizables y no conclusiones especificas.",
    "Mantener union-dedupe lossless en cada ciclo.",
    "Conservar advertencias historicas sobre salidas no parseables.",
    "Reforzar identidad curricular verificada en actividades hermanas.",
    "No propagar supuestos como hechos confirmados.",
    "Aplicar normalizacion manual cuando reaparezcan salidas heredadas no estructuradas."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de actividad 6; confirmar producto exacto solicitado.",
    "Confirmar rubrica especifica de evaluacion para actividad 6.",
    "Confirmar si se exige formato de citacion juridica adicional a BibTeX.",
    "Confirmar nombre canonico final del archivo .bib por token Slug sin resolver en README.",
    "Confirmar si actividad 6 requiere reporte, presentacion o ambos.",
    "Confirmar si las fuentes de interpretacion juridica (Semana 7) son obligatorias o solo opcionales para actividad 6."
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
      "Marco conceptual y normativo pertinente.",
      "Producto alineado a planeacion.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables.",
      "Garantizar coherencia entre identidad institucional, metodo y evidencia.",
      "Asegurar transferencia profesional del razonamiento juridico."
    ],
    "style_markers": [
      "Inicio breve con problema.",
      "Secciones explicitas y ordenadas.",
      "Citas trazables.",
      "Postura propia diferenciada.",
      "Cierre con utilidad juridica practica."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer conceptos y normas aplicables.",
      "Contrastar fuentes relevantes.",
      "Sostener postura propia con evidencia.",
      "Concluir desde el analisis y no por formula."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco conceptual-normativo",
        "Analisis propio",
        "Conclusion transferible",
        "Hermeneutica juridica",
        "Argumentacion juridica",
        "Normalizacion estructurada"
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
          "justification": "El analisis requiere un problema delimitado."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida deriva del razonamiento previo."
        },
        {
          "source": "Hermeneutica juridica",
          "target": "Argumentacion juridica",
          "kind": "supports",
          "justification": "La interpretacion sustenta la construccion argumentativa cuando la consigna lo exige."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita propagacion de errores y mantiene trazabilidad editorial."
        }
      ],
      "evidence": [
        "README establece identidad UnADM, ubicacion curricular y pauta editorial.",
        "Programa analitico fija cinco ejes de trabajo recurrentes.",
        "Memoria previa registra riesgo de salida no JSON parseable y necesidad de normalizacion.",
        "Contexto local confirma coexistencia de dos .bib y token Slug sin resolver."
      ]
    },
    "reinforcement_log": [
      "Ciclo 67: se consolidan reglas comunes de actividad 1 aplicables a actividad 6 por analogia controlada.",
      "Ciclo 67: se evita transferencia de conclusiones o bibliografia exclusiva de un hermano.",
      "Ciclo 67: se refuerza gate de JSON parseable y estructura minima obligatoria.",
      "Ciclo 67: se mantiene ambiguedad del .bib como supuesto abierto hasta verificacion local."
    ]
  }
}