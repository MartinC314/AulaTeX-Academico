{
  "summary": [
    "Se consolida refuerzo lateral desde Actividad 1 hacia Actividad 6 con deduplicacion sin perdida.",
    "Se preserva identidad UnADM y contexto curricular verificado: Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se mantiene regla critica: no propagar contenido no estructurado; normalizar antes de reutilizar.",
    "Se refuerzan ejes estables: problema, conceptos o normas, producto, analisis propio y conclusion juridica transferible.",
    "Se conserva tratamiento provisional de fuentes heredadas no verificadas y de salidas no JSON parseables."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear contenido a Filosofia del Derecho de la Licenciatura en Derecho.",
    "Reconocer ubicacion curricular al contextualizar: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar regla de no regresion en consolidaciones editoriales."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el producto al formato solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Explicitar el problema juridico o social que activa la respuesta.",
    "Relacionar conceptos, normas, doctrina o datos con el problema planteado.",
    "Sostener afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir sintesis de fuente y postura propia.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Supuesto: si la consigna trata interpretacion juridica, integrar hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna local de Actividad 6.",
    "No eliminar reglas utiles previas durante consolidacion.",
    "Aplicar union y deduplicacion lossless."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener compatibilidad entre .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en .tex.",
    "Comprobar que toda clave citada exista en el archivo bibliografico activo.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Marcar como supuesto el nombre canonico del .bib mientras persista ambiguedad por token sin resolver."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar fuentes especificas de actividad en el .bib de la asignatura.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Marcar como supuesto todo dato bibliografico incompleto hasta verificarlo.",
    "No asumir que clean.bib aplica a toda actividad; usarlo solo si coincide con la consigna."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir a hermanos solo patrones reutilizables: identidad, estructura, calidad, conceptos y relaciones recurrentes.",
    "No transferir redaccion literal, conclusiones especificas ni bibliografia exclusiva de otra actividad.",
    "Mantener advertencias historicas de ciclos con salida no estructurada.",
    "Separar reglas verificadas de supuestos antes de propagar.",
    "Si faltan datos locales, propagar plantilla base y preguntas abiertas."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 6; confirmar producto exacto solicitado.",
    "Confirmar rubrica especifica de evaluacion para ajustar profundidad argumentativa.",
    "Confirmar si Actividad 6 requiere reporte, presentacion u otro formato principal.",
    "Confirmar nombre canonico final del archivo .bib de la asignatura.",
    "Confirmar si corresponde usar corpus de interpretacion juridica del clean.bib en Actividad 6.",
    "Confirmar si existe formato de citacion juridica adicional a BibTeX institucional."
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
      "Problema juridico o social como detonador.",
      "Marco conceptual y normativo pertinente.",
      "Producto alineado a planeacion.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico y utilidad profesional.",
      "Sostener trazabilidad editorial, tecnica y bibliografica en cada actividad."
    ],
    "style_markers": [
      "Encuadre inicial breve y preciso.",
      "Secciones explicitas y ordenadas.",
      "Postura propia diferenciada de la fuente.",
      "Cierre derivado del analisis, no decorativo."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer conceptos y normas relevantes.",
      "Contrastar fuentes verificables.",
      "Tomar postura razonada.",
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
        "Normalizacion de salida estructurada"
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
          "justification": "La pauta institucional exige citas verificables y consistencia formal."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin problema delimitado no hay argumentacion pertinente."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion debe derivar del desarrollo argumentativo."
        },
        {
          "source": "Hermeneutica juridica",
          "target": "Argumentacion juridica",
          "kind": "supports",
          "justification": "En actividades de interpretacion, la hermeneutica fundamenta la argumentacion."
        },
        {
          "source": "Normalizacion de salida estructurada",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita propagacion de errores y conserva trazabilidad editorial."
        }
      ],
      "evidence": [
        "README de asignatura: identidad, pauta editorial y ubicacion curricular.",
        "Programa analitico: cinco ejes de trabajo.",
        "Regla persistente: bloquear propagacion ante salida no JSON parseable.",
        "Contexto local: coexistencia de filosofia-del-derecho.bib y filosofia-del-derecho-clean.bib con token Slug sin resolver."
      ]
    },
    "reinforcement_log": [
      "Ciclo 20: refuerzo lateral aplicado con union-dedupe lossless.",
      "Se preservaron reglas utiles previas sin recorte.",
      "Se agregaron mejoras verificables de control de supuestos y consistencia JSON.",
      "Se evitó transferencia de conclusiones o bibliografia exclusiva entre hermanos."
    ]
  }
}