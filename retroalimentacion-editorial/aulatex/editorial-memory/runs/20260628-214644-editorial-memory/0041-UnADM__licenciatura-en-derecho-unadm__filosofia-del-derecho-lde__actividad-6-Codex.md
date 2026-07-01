{
  "summary": [
    "Se consolida refuerzo lateral de Actividad 1 a Actividad 6 con union-dedupe sin perdida.",
    "Se preserva identidad UnADM y ubicacion curricular verificada.",
    "Se mantienen ejes editoriales estables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se conserva regla critica: no propagar salidas no estructuradas sin normalizacion.",
    "Se refuerza uso de supuestos marcados cuando falte consigna local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear toda entrega a Licenciatura en Derecho, Filosofia del Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar regla de no regresion: no eliminar reglas utiles previas."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Separar desarrollo en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Definir objetivo puntual de Actividad 6 antes del desarrollo.",
    "Explicitar problema juridico o social que activa la respuesta.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir sintesis de fuentes y postura propia.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Supuesto: si Actividad 6 aborda interpretacion juridica, vincular hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar aguas abajo.",
    "Revisar y normalizar toda respuesta no estructurada antes de propagar.",
    "Confirmar trazabilidad de afirmaciones relevantes a fuente o supuesto marcado.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No eliminar reglas vigentes durante consolidacion; solo agregar mejoras verificables."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres/rutas con caracteres anomalos antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y juridicas oficiales/academicas.",
    "Registrar fuentes especificas de la actividad en el .bib de la asignatura.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib puede corresponder a una actividad tematica y no sustituye automaticamente el .bib canonico."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir solo patrones reutilizables; no copiar redaccion ni conclusiones especificas.",
    "Mantener union-dedupe lossless en saltos laterales.",
    "Etiquetar como provisionales reglas de baja confianza hasta verificacion local.",
    "Propagar identidad curricular verificada a nodos hermanos de la misma asignatura.",
    "Cuando falte consigna local, propagar estructura base y abrir preguntas."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 6.",
    "Confirmar rubrica especifica de evaluacion para calibrar profundidad argumentativa.",
    "Confirmar si el producto principal es reporte, presentacion o ambos.",
    "Confirmar nombre canonico final del .bib por token Slug sin resolver en README.",
    "Confirmar si Actividad 6 exige corpus de interpretacion juridica de Semana 7.",
    "Confirmar si existe formato juridico de citacion adicional a BibTeX."
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
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable.",
      "Analisis propio diferenciado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir la planeacion semanal en productos academicos con fundamento juridico y utilidad profesional.",
      "Estandarizar calidad editorial sin perder adaptacion a cada actividad."
    ],
    "style_markers": [
      "Inicio con encuadre del problema.",
      "Secciones explicitas y ordenadas.",
      "Postura propia sustentada.",
      "Cierre aplicado a practica juridica.",
      "Supuestos marcados cuando falten datos."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Definir objetivo puntual.",
      "Exponer marco conceptual-normativo.",
      "Contrastar fuentes y elaborar postura propia.",
      "Derivar conclusion del analisis."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Hermeneutica juridica",
        "Argumentacion juridica",
        "Normalizacion de salida estructurada"
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
          "justification": "La conclusion debe derivar del desarrollo argumentativo."
        },
        {
          "source": "Hermeneutica juridica",
          "target": "Argumentacion juridica",
          "kind": "supports",
          "justification": "En tareas de interpretacion, la hermeneutica fundamenta la argumentacion."
        },
        {
          "source": "Normalizacion de salida estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "No se propaga contenido no parseable."
        }
      ],
      "evidence": [
        "README de asignatura: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo.",
        "Regla historica validada: bloquear propagacion sin JSON parseable.",
        "Archivos .bib locales muestran coexistencia de bibliografia base y bibliografia tematica."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas conservando contenido util.",
      "Se removieron inferencias no verificables como hechos; se marcaron como supuestos.",
      "Se preservo la advertencia de normalizacion obligatoria antes de propagar.",
      "Se reforzo transferencia por patrones reutilizables entre nodos hermanos."
    ]
  }
}