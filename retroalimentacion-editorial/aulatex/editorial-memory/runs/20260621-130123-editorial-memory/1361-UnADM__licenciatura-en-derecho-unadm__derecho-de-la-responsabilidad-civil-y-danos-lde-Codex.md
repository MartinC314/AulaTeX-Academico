{
  "summary": [
    "Sincronización transversal aplicada con estrategia conservadora y sin regresión.",
    "Se preservan reglas estables de identidad UnADM, estructura argumentativa y control JSON.",
    "Se deduplican reglas repetidas y se mantienen alertas técnicas locales verificadas.",
    "Se evita transferir contenido temático literal de Filosofía del Derecho al destino no equivalente.",
    "Se refuerza base editorial de materia con foco en responsabilidad civil y daño."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar contexto curricular local confirmado: Licenciatura en Derecho, semestre 6, bloque 1, obligatoria, 8 créditos.",
    "Usar la carpeta de materia como entrada canónica.",
    "Marcar como [supuesto] todo dato no visible en consigna o guía oficial.",
    "Tratar memorias heredadas no verificadas como provisionales hasta confirmación local.",
    "No declarar oficial el código LDE-S6B1 sin fuente documental explícita.",
    "No cambiar convención local danos/daños sin confirmación documental."
  ],
  "structure_rules": [
    "Iniciar cada entrega con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear el producto a la planeación semanal y consigna vigente.",
    "Mantener separación editorial entre reporte, presentación, programa analítico y .bib.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Formular problema jurídico activador de responsabilidad civil.",
    "Integrar conceptos, normas, doctrina o datos pertinentes a la actividad.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar contenido temático de origen si no aplica a daño o responsabilidad civil."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que toda afirmación jurídica tenga fuente o marca de análisis propio.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar control de no regresión sobre reglas útiles heredadas.",
    "Detectar y corregir rutas truncadas y placeholders sin resolver."
  ],
  "latex_rules": [
    "Usar español con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilación.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Completar plantilla .tex truncada antes de compilar [supuesto técnico local].",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Verificar nombres de archivos canónicos antes de referenciarlos."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "Registrar fuentes específicas por actividad en el .bib local de la materia.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Si falta referencia, abrir pregunta editorial en lugar de completar con inferencia."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo abstracciones estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar trasladar redacción literal o contenido temático puntual de actividades origen.",
    "Mantener alerta histórica: ciclos con salida no estructurada requieren normalización manual.",
    "Aplicar compresión lossless por unión y deduplicación, nunca por recorte semántico."
  ],
  "open_questions": [
    "Confirmar guía oficial de formato para actividades de la materia.",
    "Confirmar estatus oficial del código LDE-S6B1.",
    "Confirmar convención final de nombres: danos vs daños en todo el árbol.",
    "Validar y corregir truncamientos en README (rutas de reporte/referencias).",
    "Resolver placeholder del nombre .bib en README y programa analítico.",
    "Completar sección authortable truncada en plantilla .tex."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante datos no verificados."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Normalización estructurada previa a propagación.",
        "Carpeta de materia como entrada canónica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 1, obligatoria, 8 créditos.",
        "Asignatura: Derecho de la responsabilidad civil y daños [nombre con tilde sujeto a convención local].",
        "Fuente curricular: UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Problema jurídico bien delimitado.",
      "Marco conceptual y normativo verificable.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible.",
      "Rigurosidad técnica de salida estructurada."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos verificables.",
      "Garantizar coherencia jurídica entre consigna, desarrollo y cierre.",
      "Asegurar trazabilidad de fuentes y calidad editorial reutilizable."
    ],
    "style_markers": [
      "Declarar [supuesto] cuando falte evidencia documental.",
      "Usar secciones funcionales y auditables.",
      "Cerrar con criterio jurídico aplicable a práctica profesional.",
      "Evitar afirmaciones absolutas sin respaldo."
    ],
    "argumentative_patterns": [
      "Plantear problema inicial breve.",
      "Desarrollar marco normativo/doctrinal con fuentes.",
      "Contrastar ideas en análisis propio.",
      "Concluir con regla o criterio jurídico aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización JSON",
        "Problema jurídico",
        "Marco normativo/doctrinal",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Responsabilidad civil",
        "Daño",
        "Integridad académica"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "El marco institucional exige citas verificables y consistencia formal."
        },
        {
          "source": "Normalización JSON",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Evita propagación de contenido ambiguo o no auditable."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere una pregunta jurídica delimitada."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión válida depende de fundamento verificable."
        },
        {
          "source": "Daño",
          "target": "Responsabilidad civil",
          "kind": "depends_on",
          "justification": "La imputación de responsabilidad se articula desde la noción de daño."
        }
      ],
      "evidence": [
        "README local de la materia.",
        "Programa analítico local.",
        "Archivo .bib local con claves institucionales.",
        "Plantilla .tex local con truncamiento detectado [supuesto técnico]."
      ]
    },
    "reinforcement_log": [
      "Ciclo 11: deduplicación integral sin eliminar reglas útiles previas.",
      "Ciclo 11: reforzados gates de parseo JSON y normalización estructurada.",
      "Ciclo 11: consolidada transferencia transversal por abstracciones estables.",
      "Ciclo 11: preservadas alertas técnicas locales (truncamientos y placeholders)."
    ]
  }
}