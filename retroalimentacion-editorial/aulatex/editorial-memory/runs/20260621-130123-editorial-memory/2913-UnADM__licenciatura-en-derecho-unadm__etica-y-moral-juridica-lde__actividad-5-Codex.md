{
  "summary": [
    "Se refuerza transferencia lateral desde Filosofía del Derecho hacia Ética y Moral Jurídica con patrones reutilizables.",
    "Se conserva identidad UnADM y ubicación curricular común: semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Se mantiene normalización estricta: solo JSON parseable y deduplicación lossless.",
    "Se consolidan ejes editoriales comunes: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se evita copiar contenido temático o conclusiones específicas del nodo origen.",
    "Se registran incidencias locales verificables: tokens Slug sin expandir y posible truncamiento en .bib [supuesto]."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y trazabilidad.",
    "Vincular cada entrega a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Alinear explícitamente la actividad a Ética y Moral jurídica.",
    "Marcar como [supuesto] todo dato no visible en la consigna local.",
    "Tratar como provisionales las reglas derivadas de salidas no parseables hasta validación manual.",
    "Registrar origen y destino de cada injerto de memoria editorial."
  ],
  "structure_rules": [
    "Responder siempre con JSON válido y parseable según esquema.",
    "Usar frases cortas, accionables y sin duplicados.",
    "Aplicar compresión lossless por unión y deduplicación, sin recorte.",
    "Conservar secciones nucleares: problema, conceptos, marco normativo/doctrinal, análisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear estructura final al producto solicitado por la consigna de Actividad 5."
  ],
  "activity_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "No trasladar conclusiones temáticas de Filosofía del Derecho sin justificación local.",
    "Confirmar consigna textual exacta de Actividad 5 antes de redactar versión final."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de propagar.",
    "Confirmar que no se eliminen reglas útiles previas al fusionar.",
    "Validar ausencia de duplicados semánticos tras la fusión.",
    "Exigir respaldo o marca [supuesto] en afirmaciones no evidentes.",
    "Validar correspondencia entre citas en texto y archivo .bib.",
    "Revisar manualmente incidencias técnicas locales antes de promover a canon."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilación.",
    "Evitar comandos o paquetes no estándar sin justificación editorial.",
    "Compilar sin errores críticos, sin referencias rotas y sin claves huérfanas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir rutas o nombres con caracteres anómalos antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar fuentes específicas de actividad en etica-y-moral-juridica.bib.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor/editor, título, año, editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Marcar duplicados potenciales por autor+título+año para revisión manual.",
    "Verificar cierre sintáctico de cada entrada BibTeX antes de compilar."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones institucionales, estructurales y de calidad reutilizables.",
    "Evitar propagar bibliografía exclusiva o conclusiones específicas entre nodos hermanos.",
    "Usar analogía controlada: reforzar método argumentativo, no contenido temático.",
    "Si falta dato local, conservar plantilla base y abrir pregunta en lugar de inventar."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 5 y tipo de producto final.",
    "Confirmar rúbrica de evaluación específica para calibrar profundidad argumentativa.",
    "Confirmar si el truncamiento de etica-y-moral-juridica.bib existe en archivo real [supuesto].",
    "Confirmar política local para depurar claves BibTeX duplicadas sin perder trazabilidad.",
    "Confirmar si hay fuentes obligatorias de semana para Actividad 5."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Carpeta de asignatura como entrada canónica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos.",
        "Asignatura destino: Ética y Moral jurídica."
      ]
    },
    "essence": [
      "Problema jurídico o social que activa la actividad.",
      "Conceptos y marco normativo o doctrinal pertinentes.",
      "Evidencia verificable y análisis propio.",
      "Conclusión jurídica aplicable a práctica profesional.",
      "Normalización estructural como condición de memoria persistente."
    ],
    "reason_for_being": [
      "Consolidar un cerebro editorial persistente, trazable y reutilizable.",
      "Garantizar calidad argumentativa y técnica en entregas académicas LaTeX.",
      "Permitir transferencia lateral sin contaminación temática entre asignaturas."
    ],
    "style_markers": [
      "Objetivo puntual al inicio.",
      "Secciones explícitas y orden lógico.",
      "Supuestos marcados de forma visible.",
      "Citas en afirmaciones sustantivas.",
      "Cierre con postura jurídica propia."
    ],
    "argumentative_patterns": [
      "Plantear problema y alcance.",
      "Definir conceptos operativos.",
      "Vincular marco normativo o doctrinal.",
      "Desarrollar análisis crítico propio con evidencia.",
      "Concluir con implicación jurídica práctica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad académica",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Normalización JSON",
        "Deduplicación lossless",
        "Analogía controlada lateral"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/programa-analitico-etica-y-moral-juridica.md",
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/etica-y-moral-juridica.bib"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta institucional exige trazabilidad y citas verificables."
        },
        {
          "source": "Evidencia verificable",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "La postura del estudiante requiere sustento documental."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "La conclusión profesional deriva del razonamiento argumentado."
        },
        {
          "source": "Normalización JSON",
          "target": "Deduplicación lossless",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay fusión confiable."
        },
        {
          "source": "Analogía controlada lateral",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "Permite reutilizar método sin copiar contenidos específicos."
        }
      ],
      "evidence": [
        "README local confirma identidad UnADM y ubicación curricular.",
        "Programa analítico local confirma ejes editoriales comunes.",
        "README y programa contienen token Slug sin expandir [incidencia verificable].",
        "Archivo .bib muestra duplicados de obras por claves distintas [incidencia verificable].",
        "Archivo .bib parece truncado al final en contexto capturado [supuesto]."
      ]
    },
    "reinforcement_log": [
      "Ciclo 3: se preservan reglas útiles previas y se deduplican variantes repetidas.",
      "Ciclo 3: se incorporan patrones del origen solo en identidad, estructura, calidad y método argumentativo.",
      "Ciclo 3: se evita transferir bibliografía exclusiva y conclusiones temáticas de Filosofía del Derecho.",
      "Ciclo 3: se refuerza control de supuestos ante datos locales incompletos."
    ]
  }
}