{
  "summary": [
    "Se consolida memoria lateral de Actividad 1 hacia Actividad 6 con union y deduplicacion lossless.",
    "Se preserva identidad UnADM y ubicacion curricular verificada: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se mantiene regla critica: no propagar contenido no estructurado; normalizar antes de reutilizar.",
    "Se refuerzan ejes estables: problema, conceptos o normas, producto, analisis propio y conclusion juridica transferible.",
    "Se conserva trazabilidad de fuentes y se marcan como supuestos los datos no visibles en la consigna local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear cada entrega a Licenciatura en Derecho, asignatura Filosofia del Derecho.",
    "Reconocer y citar ubicacion curricular: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna de Actividad 6.",
    "Tratar como provisionales las fuentes heredadas no verificadas localmente.",
    "Conservar regla de no regresion: no eliminar reglas utiles previas."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar desarrollo en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el producto final a la planeacion semanal de Actividad 6.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base de la asignatura.",
    "Distinguir sintesis de fuentes y postura propia de forma explicita.",
    "Sostener afirmaciones relevantes con fuentes verificables o con supuesto marcado.",
    "Evitar entregas solo descriptivas o sin criterio juridico.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Relacionar conceptos, normas y doctrina con el problema planteado.",
    "Supuesto: si la consigna de Actividad 6 aborda interpretacion juridica, integrar hermeneutica y argumentacion juridica."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib activo.",
    "Verificar que la conclusion derive del analisis y no sea decorativa.",
    "Aplicar deduplicacion por union sin perdida de reglas vigentes."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener compatibilidad entre .tex y .bib sin cambiar claves citadas.",
    "Comprobar que toda clave citada exista en el archivo bibliografico activo.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico antes de fijar nombres canonicos.",
    "Supuesto: el .bib canonico esperado por Slug es filosofia-del-derecho.bib; confirmar localmente."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM, normativas vigentes y repositorios juridicos oficiales o academicos.",
    "Registrar fuentes especificas de Actividad 6 en el .bib de la asignatura.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No asumir que filosofia-del-derecho-clean.bib aplica automaticamente a Actividad 6; validar por consigna."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir a hermanos solo patrones reutilizables, no redaccion literal ni conclusiones especificas.",
    "Conservar advertencias historicas sobre salidas no parseables en nodos con herencia Codex/GPT-Pro.",
    "Aplicar normalizacion manual en ciclos tempranos con baja confiabilidad estructural.",
    "Propagar identidad curricular verificada y reglas de calidad sin reducir especificidad local.",
    "No propagar supuestos como hechos confirmados."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 6; confirmar producto exacto solicitado.",
    "Confirmar rubrica de evaluacion especifica para ajustar profundidad argumentativa.",
    "Confirmar si Actividad 6 exige formato de citacion juridica adicional a BibTeX.",
    "Confirmar nombre canonico final del archivo .bib por coexistencia de filosofia-del-derecho.bib y filosofia-del-derecho-clean.bib.",
    "Confirmar si las fuentes de interpretacion juridica (clean.bib) son obligatorias o solo opcionales en Actividad 6."
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
      "Problema juridico o social que activa la actividad.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeacion semanal.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos con evidencia y criterio juridico.",
      "Garantizar continuidad editorial entre actividades hermanas sin perdida de reglas utiles.",
      "Asegurar trazabilidad, calidad estructural y consistencia institucional."
    ],
    "style_markers": [
      "Inicio con encuadre breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Diferenciacion clara entre fuente y postura propia.",
      "Cierre con utilidad juridica profesional.",
      "Marcado explicito de supuestos."
    ],
    "argumentative_patterns": [
      "Delimitar problema antes de argumentar.",
      "Construir marco conceptual y normativo pertinente.",
      "Contrastar fuentes verificables.",
      "Sostener postura propia fundamentada.",
      "Derivar conclusion del desarrollo."
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
        "Argumentacion juridica"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
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
          "justification": "La pauta editorial exige citas verificables y formato institucional."
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
          "justification": "La conclusion valida debe derivar de la argumentacion."
        },
        {
          "source": "Hermeneutica juridica",
          "target": "Argumentacion juridica",
          "kind": "supports",
          "justification": "En tareas de interpretacion, la hermeneutica fundamenta la justificacion argumentativa."
        }
      ],
      "evidence": [
        "README confirma identidad UnADM, ubicacion curricular y pauta editorial.",
        "Programa analitico confirma cinco ejes de trabajo recurrentes.",
        "Memoria origen confirma regla de normalizacion estructurada previa a propagacion.",
        "Contexto local evidencia token Slug sin resolver en nombres de .bib."
      ]
    },
    "reinforcement_log": [
      "Ciclo 83: se mantiene union-dedupe lossless sin recorte.",
      "Ciclo 83: se refuerza no propagacion de contenido no estructurado.",
      "Ciclo 83: se transfiere solo patron reusable de actividad hermana, sin copiar conclusiones ni bibliografia exclusiva.",
      "Ciclo 83: se preservan reglas de identidad, estructura, calidad, LaTeX y bibliografia con supuestos marcados."
    ]
  }
}