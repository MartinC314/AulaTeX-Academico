{
  "summary": [
    "Se consolida refuerzo lateral entre actividades hermanas sin copiar contenido especifico.",
    "Se preserva identidad UnADM y ubicacion curricular verificada: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se mantienen ejes editoriales nucleares: problema, conceptos o normas, producto, analisis propio y conclusion transferible.",
    "Se refuerza regla critica: no propagar salidas no estructuradas; normalizar antes de reutilizar.",
    "Se mantiene compresion lossless por union y deduplicacion."
  ],
  "identity_rules": [
    "Mantener tono institucional UnADM en toda entrega.",
    "Alinear cada actividad a Licenciatura en Derecho y asignatura Filosofia del Derecho.",
    "Citar ubicacion curricular cuando contextualice la actividad: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Conservar regla de no regresion: no eliminar reglas utiles previas."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Definir objetivo puntual antes del desarrollo.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado en la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Distinguir sintesis de fuentes frente a postura propia.",
    "Sostener afirmaciones relevantes con fuentes verificables o marcar supuesto.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Relacionar conceptos, normas o doctrina con el problema planteado.",
    "Supuesto: si Actividad 6 trata interpretacion juridica, vincular hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de propagar.",
    "Revisar que no haya respuesta no estructurada reutilizada.",
    "Separar reglas verificadas de supuestos marcados.",
    "Confirmar trazabilidad de afirmaciones relevantes a evidencia o supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib activo.",
    "No eliminar reglas utiles durante consolidacion."
  ],
  "latex_rules": [
    "Mantener compatibilidad .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en .tex.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Usar acentos y codificacion correcta en español en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Marcar como supuesto el nombre canonico del .bib mientras exista ambiguedad por token sin resolver."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar fuentes especificas de la actividad en el .bib de la asignatura.",
    "Mantener metadatos minimos: autor, titulo, año, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No asumir que un .bib depurado de otra semana aplica automaticamente a Actividad 6.",
    "Marcar como supuesto datos bibliograficos incompletos hasta verificacion."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones reutilizables: identidad, estructura, calidad y relaciones conceptuales.",
    "No transferir conclusiones particulares ni bibliografia exclusiva de un hermano.",
    "Conservar advertencias historicas sobre salidas no parseables para prevenir regresiones.",
    "Aplicar union-dedupe lossless en cada ciclo.",
    "Cuando falte dato local, propagar plantilla base y pregunta abierta."
  ],
  "open_questions": [
    "Confirmar consigna exacta de Actividad 6 y producto principal requerido.",
    "Confirmar rubrica especifica de evaluacion para ajustar profundidad argumentativa.",
    "Confirmar nombre canonico final del .bib por token Slug sin resolver en README.",
    "Confirmar si Actividad 6 requiere formato de citacion juridica adicional a BibTeX.",
    "Confirmar si fuentes de interpretacion juridica son obligatorias o solo opcionales en Actividad 6."
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
      "Conceptos y normas pertinentes.",
      "Producto de planeacion semanal.",
      "Analisis propio con postura.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento, evidencia y criterio juridico.",
      "Asegurar consistencia institucional y trazabilidad editorial entre actividades."
    ],
    "style_markers": [
      "Encuadre inicial breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Diferenciacion clara entre fuente y postura.",
      "Cierre con utilidad profesional juridica.",
      "Supuestos marcados de forma explicita."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Construir marco conceptual y normativo.",
      "Analizar evidencia y contrastar fuentes.",
      "Fijar postura propia fundamentada.",
      "Derivar conclusion desde el analisis."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Hermeneutica juridica [supuesto condicionado a consigna]",
        "Argumentacion juridica [supuesto condicionado a consigna]"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
        "README.md de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "filosofia-del-derecho.bib [supuesto de canonicidad pendiente]",
        "filosofia-del-derecho-clean.bib [uso condicionado por consigna]"
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
          "justification": "El analisis requiere delimitacion previa del problema."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida deriva del desarrollo argumentativo."
        },
        {
          "source": "Hermeneutica juridica [supuesto condicionado a consigna]",
          "target": "Argumentacion juridica [supuesto condicionado a consigna]",
          "kind": "supports",
          "justification": "En actividades de interpretacion, la hermeneutica fundamenta la argumentacion."
        }
      ],
      "evidence": [
        "README confirma identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico confirma cinco ejes de trabajo.",
        "Historial confirma necesidad de normalizar salidas no estructuradas antes de propagar."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas de identidad, estructura y calidad.",
      "Se mantuvieron reglas utiles heredadas sin recorte semantico.",
      "Se excluyo transferencia de conclusiones especificas de Actividad 1.",
      "Se conservaron supuestos abiertos donde faltan datos locales verificables.",
      "Se reforzo control de JSON parseable como compuerta obligatoria."
    ]
  }
}