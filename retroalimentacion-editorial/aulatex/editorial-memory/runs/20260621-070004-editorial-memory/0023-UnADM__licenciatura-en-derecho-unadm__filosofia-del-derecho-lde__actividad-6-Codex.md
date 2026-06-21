{
  "summary": [
    "Se consolida memoria lateral de Actividad 1 a Actividad 6 sin perdida y con deduplicacion.",
    "Se preserva identidad UnADM y ubicacion curricular verificada: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se refuerza regla critica: no propagar contenido no estructurado; normalizar antes de reutilizar.",
    "Se mantienen ejes editoriales estables: problema, conceptos o normas, producto, analisis propio y conclusion transferible.",
    "Se conserva distincion entre reglas verificadas y supuestos marcados."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear la actividad a Licenciatura en Derecho, Filosofia del Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar no regresion: no eliminar reglas utiles previas en consolidacion."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de memoria.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Abrir el producto academico con encuadre breve del problema juridico o social.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear el formato final al producto pedido por la planeacion semanal."
  ],
  "activity_rules": [
    "Adaptar la redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir sintesis de fuentes frente a postura propia.",
    "Evitar entregas solo descriptivas o sin criterio juridico.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No trasladar conclusiones especificas de Actividad 1 a Actividad 6.",
    "Supuesto: si Actividad 6 trata interpretacion juridica, vincular hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de propagar.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar trazabilidad de afirmaciones a fuente o supuesto marcado.",
    "Validar consistencia entre citas en texto y archivo .bib activo.",
    "Verificar que la conclusion derive del analisis y no sea decorativa.",
    "Aplicar union-dedupe lossless en cada ciclo."
  ],
  "latex_rules": [
    "Mantener codificacion y acentos correctos en .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en .tex.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico antes de fijar nombres canonicos.",
    "Supuesto: el .bib canonico esperado es filosofia-del-derecho.bib por el Slug visible."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas oficiales o academicas.",
    "Registrar fuentes especificas de cada actividad en el .bib de la asignatura.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No asumir que filosofia-del-derecho-clean.bib aplica a toda actividad; validar por consigna.",
    "Supuesto: filosofia-del-derecho-clean.bib esta orientado a interpretacion juridica (Semana 7)."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones reutilizables: identidad, estructura, calidad, conceptos recurrentes.",
    "No propagar redaccion literal ni bibliografia exclusiva entre hermanos.",
    "Mantener advertencias historicas de herencia no estructurada (Codex/GPT-Pro) como provisionales.",
    "Cuando falten datos locales, propagar plantilla base y preguntas abiertas.",
    "Preservar reglas utiles previas y agregar solo mejoras verificables."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 6.",
    "Confirmar rubrica especifica de evaluacion para calibrar profundidad argumentativa.",
    "Confirmar si el producto principal es reporte, presentacion u otro formato.",
    "Confirmar nombre canonico final del .bib de asignatura tras resolver token Slug.",
    "Confirmar si Actividad 6 requiere fuentes de interpretacion juridica o corpus distinto.",
    "Confirmar si se exige formato de citacion juridica adicional a BibTeX."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico",
        "Claro y juridicamente preciso",
        "Argumentativo con criterio propio"
      ],
      "institutional": [
        "Alineacion explicita con UnADM",
        "Integridad academica con citas verificables",
        "Carpeta de asignatura como entrada canonica"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Filosofia del Derecho",
        "Semestre 1, bloque 2, obligatoria, 8 creditos"
      ]
    },
    "essence": [
      "Problema juridico o social",
      "Conceptos, normas o doctrina pertinentes",
      "Producto alineado a planeacion",
      "Analisis propio con postura academica",
      "Conclusion juridica transferible"
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico y utilidad profesional.",
      "Garantizar consistencia editorial institucional en todas las actividades hermanas."
    ],
    "style_markers": [
      "Encuadre breve del problema al inicio",
      "Secciones explicitas y ordenadas",
      "Fuentes verificables con trazabilidad",
      "Postura personal diferenciada de la sintesis",
      "Cierre con criterio juridico aplicable"
    ],
    "argumentative_patterns": [
      "Delimitar problema",
      "Exponer marco conceptual y normativo",
      "Contrastar fuentes pertinentes",
      "Sostener postura propia fundamentada",
      "Concluir con derivacion logica del analisis"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Analisis propio",
        "Conclusion transferible",
        "Hermeneutica juridica [supuesto condicionado a consigna]",
        "Argumentacion juridica [supuesto condicionado a consigna]"
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
          "justification": "Sin delimitacion del problema no hay argumentacion pertinente."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion debe derivar del desarrollo y servir a la practica juridica."
        },
        {
          "source": "Hermeneutica juridica [supuesto condicionado a consigna]",
          "target": "Argumentacion juridica [supuesto condicionado a consigna]",
          "kind": "supports",
          "justification": "Si la actividad aborda interpretacion, la hermeneutica fundamenta la justificacion argumentativa."
        }
      ],
      "evidence": [
        "README de asignatura: identidad, ubicacion y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo.",
        "Existencia de clean.bib orientado a interpretacion juridica (uso condicionado por consigna).",
        "Regla historica validada: bloquear propagacion de salidas no JSON parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 23: deduplicacion lossless aplicada sin eliminar reglas utiles.",
      "Ciclo 23: se fortalecio separacion entre hechos verificados y supuestos.",
      "Ciclo 23: se mantuvo compatibilidad lateral entre actividades hermanas sin copiar contenido especifico."
    ]
  }
}