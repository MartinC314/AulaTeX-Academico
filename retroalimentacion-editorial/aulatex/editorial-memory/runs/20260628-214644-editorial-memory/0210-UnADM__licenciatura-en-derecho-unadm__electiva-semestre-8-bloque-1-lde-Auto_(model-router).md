{
  "summary": [
    "Materia destino consolidada: Electiva Semestre 8 Bloque 1.",
    "Sincronización transversal aplicada con estrategia progresiva y conservadora.",
    "Se preserva identidad institucional UnADM.",
    "Se conserva estructura reusable: problema, fuentes, análisis propio y cierre jurídico.",
    "Se refuerza control de calidad por JSON parseable.",
    "Se evita transferir contenido temático específico de Filosofía del Derecho.",
    "Se integran solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Se conserva memoria local sobre placeholders y nombres corruptos en README y programa.",
    "Se mantiene bibliografía local basada en fuentes institucionales verificables.",
    "Supuesto: el destino aún no tiene consigna específica de actividad local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, tono y formato.",
    "Usar tono jurídico formal, claro y verificable.",
    "Conservar contexto curricular local: Licenciatura en Derecho, semestre 8, bloque 1, tipo Electiva.",
    "No propagar metadatos curriculares de Filosofía del Derecho al destino.",
    "Evitar renombrar la asignatura sin confirmación oficial.",
    "Mantener código provisional LDE-S8B1 hasta confirmación oficial distinta.",
    "Conservar autor confirmado en plantilla: Martin Jonathan de la Cruz.",
    "Conservar matrícula confirmada en plantilla: ES2611202040.",
    "Marcar como supuesto todo dato no visible en consigna o documentos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Registrar Codex y GPT-Pro como antecedentes provisionales, no como fuentes académicas.",
    "Usar la carpeta de materia como punto de entrada canónico."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Declarar objetivo puntual antes del desarrollo.",
    "Organizar entregables en secuencia: problema, conceptos o fuentes, producto, análisis propio y conclusión.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear cada entrega al programa analítico de la materia.",
    "Alinear cada actividad al producto solicitado por la planeación semanal.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Conservar README, programa analítico, plantilla de reporte, plantilla de presentación, bibliografía y carpeta de referencias.",
    "Usar el programa analítico como guía de reportes, presentaciones y productos visuales."
  ],
  "activity_rules": [
    "Definir objetivo de la actividad al inicio.",
    "Vincular el producto solicitado con un problema jurídico o social.",
    "Relacionar conceptos, normas, doctrina o datos con el producto solicitado.",
    "Diferenciar síntesis de fuentes y postura propia del estudiante.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir fuentes o instrucciones de semanas distintas sin evidencia.",
    "No trasladar contenido temático de Filosofía del Derecho sin insumo local verificable.",
    "Cerrar con postura académica sustentada."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar respuestas no estructuradas antes de reutilizarlas.",
    "Validar consistencia entre portada, metadatos y nombre de asignatura.",
    "Confirmar trazabilidad de afirmaciones con citas verificables.",
    "Confirmar que toda afirmación tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar que rutas locales citadas existan antes de usarlas como fuente.",
    "Revisar que la malla curricular respalde semestre, bloque y tipo.",
    "Marcar como pendiente todo dato no confirmado, en especial créditos y figura docente.",
    "Corregir literales de generador antes de entrega.",
    "Corregir caracteres corruptos en nombres de archivo antes de entrega.",
    "Compilar sin errores críticos y sin referencias rotas."
  ],
  "latex_rules": [
    "Mantener plantilla LaTeX base de la materia para reportes.",
    "Mantener clase article con spanish, letterpaper y oneside.",
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Completar campos pendientes de portada antes de entrega.",
    "Actualizar figura docente solo con nombre confirmado.",
    "No dejar créditos vacíos si el dato oficial está disponible.",
    "Mantener documenttitle, documentsubtitle, documentsubject, coursename y coursecode consistentes.",
    "Conservar definiciones de universidad y curso sin renombrados inconsistentes.",
    "Conservar universitydepartmentimage como departamentos/UnADM salvo cambio institucional verificado.",
    "Usar electiva-semestre-8-bloque-1.bib como archivo bibliográfico local.",
    "Mantener claves BibTeX estables para evitar compilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Evitar placeholders de automatización como $(@{...}.Slug) en archivos finales.",
    "Resolver tokens sin expandir en README y programa analítico.",
    "Corregir nombres corruptos de reporte y referencias antes de compilar.",
    "Verificar nombres de archivos del README antes de referenciarlos."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM como base contextual.",
    "Conservar entrada institucional unadmSitioWeb sin renombrar.",
    "Conservar entrada unadmMallaDerecho2024 sin renombrar.",
    "Registrar fuentes específicas de cada actividad en electiva-semestre-8-bloque-1.bib.",
    "Agregar referencias doctrinales, normativas o jurisprudenciales solo cuando la actividad las requiera.",
    "No inventar referencias.",
    "Usar solo fuentes consultadas y verificables.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Mantener notas de consulta y ruta de archivo cuando la fuente sea local.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No asumir bibliografía de Filosofía del Derecho como bibliografía local de la electiva."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar arriba y laterales reglas validadas de calidad, estructura y trazabilidad.",
    "Aplicar unión-dedupe lossless en cada ciclo.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Compartir solo abstracciones editoriales estables entre materias no equivalentes.",
    "No propagar metadatos específicos de esta electiva a materias no equivalentes.",
    "No propagar contenido temático específico de Filosofía del Derecho al destino.",
    "Propagar la regla de no inventar fuentes a nodos relacionados.",
    "Propagar la verificación de JSON parseable a nodos superiores.",
    "Registrar ciclo 1 como fase de normalización manual si falta insumo local.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local."
  ],
  "open_questions": [
    "Confirmar créditos oficiales de la electiva.",
    "Confirmar nombre de figura docente para plantilla base.",
    "Confirmar nombre oficial de la electiva si difiere del usado actualmente.",
    "Confirmar código oficial de la asignatura frente al provisional LDE-S8B1.",
    "Confirmar rúbrica de evaluación específica de cada actividad local.",
    "Confirmar consigna textual de actividades locales.",
    "Confirmar fuentes obligatorias de cada semana local.",
    "Confirmar existencia y consistencia de presentacion-electiva-semestre-8-bloque-1.tex.",
    "Corregir en README nombres de archivo con caracteres faltantes.",
    "Corregir en README y programa los placeholders $(@{...}.Slug).",
    "Confirmar si existe carpeta referencias-electiva-semestre-8-bloque-1.",
    "Supuesto: no existe insumo temático local suficiente para reglas específicas de actividad."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Verificable y sobrio.",
        "Conservador en transferencias transversales."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Normalización estructurada obligatoria antes de propagar.",
        "Carpeta de materia como entrada canónica.",
        "Fuentes heredadas tratadas como provisionales hasta confirmación local."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Nodo destino: Electiva Semestre 8 Bloque 1.",
        "Semestre 8, bloque 1, tipo Electiva.",
        "Código provisional: LDE-S8B1.",
        "Transferencia transversal sin mezclar metadatos de materias distintas."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Problema jurídico o social como punto de partida.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeación.",
      "Análisis propio y postura académica.",
      "Conclusión transferible a la práctica jurídica.",
      "Trazabilidad de evidencia.",
      "Bibliografía verificable.",
      "Normalización JSON antes de propagación.",
      "Deduplicación lossless sin regresión.",
      "Vacíos locales abiertos y marcados como supuesto."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Transformar la planeación semanal en reportes, presentaciones y productos visuales.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Garantizar que cada entrega sea verificable, coherente y útil para la práctica jurídica.",
      "Conservar memoria editorial reusable sin importar el formato final del producto.",
      "Evitar contaminación temática entre nodos transversales no equivalentes."
    ],
    "style_markers": [
      "Frases precisas y verificables.",
      "Supuestos explícitos cuando falte evidencia.",
      "Citas explícitas para afirmaciones sustantivas.",
      "Separación visible entre resumen de fuentes y análisis propio.",
      "Conclusiones jurídicas aplicables.",
      "Metadatos locales consistentes.",
      "No renombrar asignaturas sin evidencia oficial.",
      "No inventar fuentes.",
      "No copiar redacción literal entre materias no equivalentes.",
      "No propagar salidas no estructuradas."
    ],
    "argumentative_patterns": [
      "Delimitar el problema jurídico o social.",
      "Definir objetivo puntual.",
      "Presentar conceptos o fuentes pertinentes.",
      "Desarrollar el producto solicitado.",
      "Contrastar fuentes con análisis propio.",
      "Sostener postura académica con evidencia.",
      "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
      "Cerrar con conclusión jurídica transferible.",
      "Marcar límites del análisis cuando falte consigna.",
      "Distinguir abstracción editorial de contenido temático específico."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Electiva Semestre 8 Bloque 1",
        "Problema jurídico o social",
        "Conceptos, normas, doctrina o datos",
        "Producto solicitado por la planeación",
        "Análisis jurídico propio",
        "Postura académica sustentada",
        "Conclusión jurídica transferible",
        "Trazabilidad de evidencia",
        "Fuentes verificables",
        "Bibliografía local",
        "Normalización JSON",
        "Deduplicación lossless",
        "Metadatos curriculares locales",
        "Plantilla LaTeX de reporte",
        "Plantilla LaTeX de presentación",
        "Placeholders de automatización",
        "Nombres de archivo corruptos",
        "Transferencia transversal conservadora"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Trazabilidad de evidencia",
          "kind": "supports",
          "justification": "La integridad académica exige respaldo verificable."
        },
        {
          "source": "Trazabilidad de evidencia",
          "target": "Fuentes verificables",
          "kind": "depends_on",
          "justification": "La evidencia solo es trazable si las fuentes son consultables."
        },
        {
          "source": "Fuentes verificables",
          "target": "Bibliografía local",
          "kind": "develops",
          "justification": "Las fuentes consultadas deben registrarse en el .bib local."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Análisis jurídico propio",
          "kind": "develops",
          "justification": "El análisis parte de una delimitación problemática."
        },
        {
          "source": "Conceptos, normas, doctrina o datos",
          "target": "Análisis jurídico propio",
          "kind": "supports",
          "justification": "El marco conceptual o normativo fundamenta la postura."
        },
        {
          "source": "Análisis jurídico propio",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "La postura argumentada permite una conclusión aplicable."
        },
        {
          "source": "Producto solicitado por la planeación",
          "target": "Plantilla LaTeX de reporte",
          "kind": "depends_on",
          "justification": "El formato final depende de la consigna."
        },
        {
          "source": "Producto solicitado por la planeación",
          "target": "Plantilla LaTeX de presentación",
          "kind": "depends_on",
          "justification": "El formato final puede requerir presentación."
        },
        {
          "source": "Normalización JSON",
          "target": "Transferencia transversal conservadora",
          "kind": "supports",
          "justification": "La estructura parseable permite propagación confiable."
        },
        {
          "source": "Deduplicación lossless",
          "target": "Transferencia transversal conservadora",
          "kind": "supports",
          "justification": "La unión sin duplicados preserva reglas útiles sin recorte."
        },
        {
          "source": "Metadatos curriculares locales",
          "target": "Transferencia transversal conservadora",
          "kind": "contrasts",
          "justification": "Los metadatos locales no deben mezclarse con materias no equivalentes."
        },
        {
          "source": "Placeholders de automatización",
          "target": "Compilación LaTeX confiable",
          "kind": "contrasts",
          "justification": "Los tokens sin expandir rompen la entrega final."
        },
        {
          "source": "Nombres de archivo corruptos",
          "target": "Compilación LaTeX confiable",
          "kind": "contrasts",
          "justification": "Las rutas corruptas impiden referencias estables."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 8, bloque 1, tipo Electiva.",
        "README local: créditos vacíos.",
        "README local: fuente curricular malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: identidad UnADM, integridad académica, citas verificables y conclusión jurídica.",
        "README local: nombres de archivo con caracteres faltantes.",
        "README local: token $(@{...}.Slug) sin expandir.",
        "Programa analítico local: claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: reportes, presentaciones y productos visuales.",
        "Programa analítico local: ejes problema, conceptos, producto, análisis propio y conclusión.",
        "Programa analítico local: fuentes específicas deben agregarse al .bib local.",
        "Bib local: unadmSitioWeb.",
        "Bib local: unadmMallaDerecho2024.",
        "Plantilla reporte local: autor Martin Jonathan de la Cruz.",
        "Plantilla reporte local: matrícula ES2611202040.",
        "Plantilla reporte local: figura docente por definir.",
        "Plantilla reporte local: tipo/créditos incompleto.",
        "Regla heredada: revisar respuesta no estructurada antes de aplicar aguas abajo.",
        "Regla heredada: ciclo 1 necesita normalización manual si se reutiliza."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas de identidad, estructura y calidad.",
      "Se preservaron reglas útiles del destino sin recorte.",
      "Se incorporaron abstracciones estables del origen: problema, fuentes, análisis propio y cierre jurídico.",
      "Se evitó importar bibliografía temática de Filosofía del Derecho.",
      "Se evitó importar ubicación curricular de Filosofía del Derecho.",
      "Se reforzó la regla de marcar supuestos.",
      "Se reforzó la regla de no inventar fuentes.",
      "Se reforzó la validación de citas contra .bib.",
      "Se reforzó la corrección de placeholders y rutas corruptas.",
      "Se consolidó un cerebro editorial mínimo para la materia destino.",
      "Se mantuvo abierta la falta de créditos oficiales.",
      "Se mantuvo abierta la falta de consigna local específica."
    ]
  }
}