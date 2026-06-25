{
  "summary": [
    "Se consolida refuerzo lateral desde Actividad 1 hacia Actividad 6 con union-dedupe sin perdida.",
    "Se preserva identidad UnADM y ubicacion curricular verificada: Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se mantienen ejes editoriales estables: problema, conceptos o normas, producto, analisis propio y conclusion juridica transferible.",
    "Se mantiene regla critica: no propagar contenido no estructurado; normalizar antes de reutilizar.",
    "Se conserva estado provisional de fuentes heredadas no verificadas localmente.",
    "Se refuerza uso de carpeta de asignatura como entrada canonica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear toda entrega a Filosofia del Derecho de la Licenciatura en Derecho.",
    "Citar ubicacion curricular al contextualizar: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar regla de no regresion: no eliminar reglas utiles previas."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido y sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Cerrar con conclusion juridica aplicable a practica profesional.",
    "Alinear formato final al producto pedido por la planeacion semanal."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Distinguir sintesis de fuentes y postura propia.",
    "Sustentar afirmaciones relevantes con fuentes verificables.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Relacionar conceptos y normas con el problema planteado.",
    "Supuesto: si la consigna aborda interpretacion juridica, vincular hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Separar reglas confirmadas de supuestos marcados.",
    "Verificar trazabilidad minima de afirmaciones a fuente o supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib activo.",
    "Revisar que la conclusion derive del analisis y no sea decorativa.",
    "Aplicar compresion lossless por deduplicacion, no por recorte."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en .tex.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Usar acentos y codificacion correcta en espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico antes de fijar nombres canonicos."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y juridicas oficiales o academicas.",
    "Registrar fuentes especificas de actividad en el .bib de la asignatura.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No asumir que filosofia-del-derecho-clean.bib aplica a toda actividad; confirmar por consigna."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir a hermanos solo patrones reutilizables: identidad, estructura, calidad, conceptos y relaciones recurrentes.",
    "No transferir redaccion literal ni conclusiones especificas entre actividades hermanas.",
    "Preservar advertencias historicas de salidas no estructuradas en nodos con herencia Codex/GPT-Pro.",
    "Mantener union-dedupe lossless en cada ciclo.",
    "Cuando falten datos locales, propagar plantilla base y preguntas abiertas."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 6; confirmar producto exacto solicitado.",
    "Confirmar rubrica especifica de evaluacion de Actividad 6.",
    "Confirmar si Actividad 6 exige reporte, presentacion u otro formato principal.",
    "Confirmar nombre canonico final del .bib por token Slug sin resolver y coexistencia de archivos .bib.",
    "Confirmar si se requiere formato de citacion juridica adicional a BibTeX.",
    "Confirmar si fuentes de interpretacion juridica (clean.bib) son obligatorias o solo opcionales en Actividad 6."
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
      "Problema juridico o social como detonante.",
      "Marco conceptual y normativo verificable.",
      "Producto alineado a planeacion semanal.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible a la practica."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, fundados y aplicables.",
      "Sostener coherencia entre identidad institucional, evidencia y argumentacion juridica."
    ],
    "style_markers": [
      "Inicio con encuadre breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Diferenciacion visible entre fuente y postura propia.",
      "Cierre con utilidad profesional juridica.",
      "Marcado explicito de supuestos."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer conceptos y normas pertinentes.",
      "Contrastar fuentes verificables.",
      "Tomar postura fundamentada.",
      "Derivar conclusion del analisis."
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
          "justification": "La pauta institucional exige evidencia verificable y formato consistente."
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
          "justification": "La conclusion valida debe derivar del desarrollo argumentativo."
        },
        {
          "source": "Hermeneutica juridica",
          "target": "Argumentacion juridica",
          "kind": "supports",
          "justification": "La interpretacion de normas fortalece la justificacion argumentativa."
        }
      ],
      "evidence": [
        "README de asignatura: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo.",
        "Regla historica: bloquear propagacion de salidas no estructuradas.",
        "Supuesto: aplicacion de corpus de interpretacion juridica depende de consigna local."
      ]
    },
    "reinforcement_log": [
      "Ciclo 18: refuerzo lateral aplicado sin eliminar reglas utiles previas.",
      "Ciclo 18: deduplicacion semantica de reglas repetidas en identidad, estructura y calidad.",
      "Ciclo 18: se conserva advertencia de fuentes provisionales heredadas.",
      "Ciclo 18: se refuerza control de tokens Slug sin resolver como riesgo editorial-tecnico."
    ]
  }
}