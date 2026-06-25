{
  "summary": [
    "Memoria de materia Electiva S8 B1 consolidada por sincronización transversal conservadora.",
    "Se preserva identidad UnADM, estructura jurídica reusable y trazabilidad bibliográfica.",
    "Se deduplican reglas heredadas sin trasladar contenido temático no verificable de Filosofía del Derecho.",
    "Se refuerza control de JSON parseable, placeholders, rutas corruptas y consistencia LaTeX.",
    "Destino canónico: UnADM/licenciatura-en-derecho-unadm/electiva-semestre-8-bloque-1-lde.",
    "Supuesto: faltan créditos oficiales, figura docente y posible nombre oficial de la electiva."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, tono y formato.",
    "Usar tono jurídico formal, claro, verificable y sobrio.",
    "Conservar contexto curricular local: Licenciatura en Derecho, semestre 8, bloque 1, tipo Electiva.",
    "Mantener la carpeta de materia como punto de entrada canónico.",
    "Evitar renombrar la asignatura sin confirmación oficial.",
    "Mantener código provisional LDE-S8B1 hasta confirmación oficial distinta.",
    "Conservar autor confirmado en plantilla: Martin Jonathan de la Cruz.",
    "Conservar matrícula confirmada en plantilla: ES2611202040.",
    "Marcar como supuesto todo dato no visible o no confirmado en consigna local.",
    "Tratar fuentes heredadas Codex y GPT-Pro como provisionales hasta validación local.",
    "No eliminar reglas útiles previas; extender solo con evidencia local o transversal estable."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Declarar objetivo puntual antes del desarrollo.",
    "Organizar entregables en secuencia: problema, conceptos o fuentes, producto, análisis propio y conclusión.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por la planeación semanal.",
    "Usar el programa analítico como guía para reportes, presentaciones y productos visuales.",
    "Conservar README, programa analítico, plantilla de reporte, plantilla de presentación, bibliografía y referencias.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Adaptar la estructura al tipo de producto solicitado por la consigna."
  ],
  "activity_rules": [
    "Vincular el producto con un problema jurídico o social delimitado.",
    "Relacionar conceptos, normas, doctrina o datos con el producto solicitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Diferenciar resumen de fuentes y postura propia.",
    "Evitar entregas solo descriptivas.",
    "Cerrar con postura académica sustentada.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No extrapolar fuentes o contenidos de otras materias o semanas sin evidencia local.",
    "No trasladar contenido temático de Filosofía del Derecho sin insumo verificable en la electiva.",
    "Confirmar que el producto corresponda a la consigna de la actividad local."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de reutilizar aguas abajo.",
    "Validar consistencia entre portada, metadatos y nombre de asignatura.",
    "Confirmar trazabilidad de afirmaciones con citas o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar respuestas no estructuradas antes de aplicarlas.",
    "Corregir literales de generador antes de entrega.",
    "Corregir caracteres corruptos en nombres de archivo antes de entrega.",
    "Confirmar que rutas locales citadas existan antes de usarlas como fuente.",
    "Verificar que la malla curricular respalde semestre, bloque y tipo.",
    "Marcar como pendiente todo dato no confirmado, especialmente créditos y figura docente.",
    "Compilar LaTeX sin errores críticos ni referencias rotas."
  ],
  "latex_rules": [
    "Mantener plantilla LaTeX base de la materia para reportes.",
    "Mantener clase article con spanish, letterpaper y oneside salvo justificación editorial.",
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener documenttitle, documentsubtitle, documentsubject, coursename y coursecode consistentes.",
    "Conservar definiciones de universidad y curso sin renombrados inconsistentes.",
    "Conservar universitydepartmentimage como departamentos/UnADM salvo cambio institucional verificado.",
    "Completar campos pendientes de portada antes de entrega.",
    "Actualizar figura docente solo con nombre confirmado.",
    "No dejar créditos vacíos si el dato oficial está disponible.",
    "Usar electiva-semestre-8-bloque-1.bib como archivo bibliográfico local.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Eliminar placeholders de automatización como $(@{...}.Slug) en archivos finales.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir rutas con caracteres faltantes antes de compilar."
  ],
  "bibliography_rules": [
    "Registrar fuentes específicas de cada actividad en electiva-semestre-8-bloque-1.bib.",
    "Priorizar fuentes institucionales UnADM como base contextual.",
    "Conservar unadmSitioWeb y unadmMallaDerecho2024 sin renombrar.",
    "No inventar referencias.",
    "Incluir solo fuentes consultadas y verificables.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Mantener notas de consulta y ruta cuando la fuente sea local.",
    "Agregar fuentes doctrinales, normativas o jurisprudenciales solo cuando la actividad las requiera.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No asumir que bibliografía de otra materia corresponde a la electiva."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar a nodos relacionados reglas estables de identidad, estructura, calidad y trazabilidad.",
    "Aplicar unión-dedupe lossless en cada ciclo.",
    "No propagar metadatos específicos de Electiva S8 B1 a materias no equivalentes.",
    "No propagar contenido temático de Filosofía del Derecho a la electiva sin evidencia local.",
    "Propagar la regla de no inventar fuentes a nodos relacionados.",
    "Propagar la verificación de citas contra .bib a nodos LaTeX relacionados.",
    "Registrar ciclo 2 como sincronización transversal conservadora.",
    "Usar normalización manual si aparece salida no estructurada heredada.",
    "Conservar vacíos locales como preguntas abiertas hasta confirmación."
  ],
  "open_questions": [
    "Confirmar créditos oficiales de la electiva para portada y README.",
    "Confirmar nombre de figura docente para plantilla base.",
    "Confirmar nombre oficial de la electiva si difiere del usado actualmente.",
    "Confirmar código oficial de la asignatura frente al provisional LDE-S8B1.",
    "Confirmar si presentación y reporte comparten reglas completas de portada.",
    "Corregir en README nombres de archivo con caracteres faltantes.",
    "Resolver placeholder $(@{...}.Slug) en README y programa analítico.",
    "Confirmar carpeta local de referencias con nombre corregido.",
    "Confirmar fuentes obligatorias de cada actividad local.",
    "Confirmar si cada actividad requiere reporte, presentación u otro producto principal.",
    "Confirmar rúbricas específicas antes de ajustar profundidad argumentativa."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Jurídicamente preciso.",
        "Claro y verificable.",
        "Argumentativo con criterio propio.",
        "Conservador ante datos no confirmados.",
        "Sobrio en inferencias."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Carpeta de materia como entrada canónica.",
        "Portada consistente con plantilla local.",
        "Supuestos etiquetados sin ambigüedad.",
        "Fuentes heredadas tratadas como provisionales."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 8.",
        "Bloque 1.",
        "Tipo Electiva.",
        "Código provisional LDE-S8B1.",
        "Producto académico orientado a transferencia profesional."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Problema jurídico o social delimitado.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeación.",
      "Análisis propio y postura académica.",
      "Conclusión transferible a la práctica jurídica.",
      "Trazabilidad de fuentes.",
      "Normalización estructurada antes de propagar.",
      "Control de placeholders editoriales.",
      "No traslado temático sin evidencia local."
    ],
    "reason_for_being": [
      "Orientar productos académicos de la electiva con claridad, fundamento jurídico y evidencia.",
      "Transformar la planeación semanal en reportes, presentaciones o productos visuales.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Proteger consistencia institucional y compilación LaTeX.",
      "Evitar regresiones por salidas no estructuradas o fuentes no verificadas."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Encuadre jurídico breve.",
      "Secciones estables y reutilizables.",
      "Postura propia sustentada.",
      "Citas verificables.",
      "Supuestos marcados.",
      "Cierre jurídico transferible.",
      "Metadatos curriculares consistentes.",
      "Lenguaje académico sin relleno.",
      "No inventar fuentes ni datos."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> fuentes -> análisis -> conclusión.",
      "Afirmación -> evidencia verificable -> inferencia jurídica.",
      "Descripción breve -> posición crítica -> implicación práctica.",
      "Consigna -> producto -> criterios de cumplimiento.",
      "Dato no confirmado -> marca de supuesto -> pregunta abierta.",
      "Fuente local -> clave BibTeX -> cita en texto.",
      "Plantilla -> metadatos -> compilación estable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM.",
        "Licenciatura en Derecho.",
        "Electiva Semestre 8 Bloque 1.",
        "Código provisional LDE-S8B1.",
        "Problema jurídico o social.",
        "Conceptos clave.",
        "Marco normativo o doctrinal.",
        "Producto solicitado.",
        "Análisis propio.",
        "Conclusión jurídica transferible.",
        "Trazabilidad bibliográfica.",
        "Normalización JSON.",
        "Control de placeholders.",
        "Consistencia de portada.",
        "Compilación LaTeX estable.",
        "Malla curricular de Derecho.",
        "Bibliografía local de la materia."
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Consistencia de portada",
          "kind": "supports",
          "justification": "La portada debe reflejar institución, carrera, asignatura y metadatos locales."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Electiva Semestre 8 Bloque 1",
          "kind": "supports",
          "justification": "El README la registra como fuente para semestre, bloque y tipo."
        },
        {
          "source": "Código provisional LDE-S8B1",
          "target": "Confirmación oficial de código",
          "kind": "depends_on",
          "justification": "El código se conserva solo hasta encontrar dato oficial distinto."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El análisis debe responder a un problema delimitado."
        },
        {
          "source": "Conceptos clave",
          "target": "Marco normativo o doctrinal",
          "kind": "depends_on",
          "justification": "Los conceptos ordenan la selección de fuentes normativas o doctrinales."
        },
        {
          "source": "Trazabilidad bibliográfica",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión gana validez cuando deriva de fuentes verificables."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "La reutilización confiable requiere salida parseable."
        },
        {
          "source": "Control de placeholders",
          "target": "Compilación LaTeX estable",
          "kind": "supports",
          "justification": "Eliminar tokens sin expandir reduce fallas de rutas y bibliografía."
        },
        {
          "source": "Bibliografía local de la materia",
          "target": "Trazabilidad bibliográfica",
          "kind": "supports",
          "justification": "El archivo .bib local concentra fuentes base y específicas."
        },
        {
          "source": "Contenido temático de Filosofía del Derecho",
          "target": "Electiva Semestre 8 Bloque 1",
          "kind": "contrasts",
          "justification": "Los nodos no son equivalentes; solo se transfieren abstracciones editoriales estables."
        }
      ],
      "evidence": [
        "README local: Materia de la Licenciatura en Derecho de la UnADM.",
        "README local: Semestre 8, bloque 1, tipo Electiva.",
        "README local: créditos vacíos.",
        "README local: fuente malla-curricular-derecho-unadm.pdf.",
        "README local: nombres corruptos en reporte y referencias.",
        "README local: placeholder $(@{...}.Slug) en bibliografía.",
        "Programa analítico local: propósito de reportes, presentaciones y productos visuales.",
        "Programa analítico local: ejes problema, conceptos, producto, análisis y conclusión.",
        "Archivo .bib local: claves unadmSitioWeb y unadmMallaDerecho2024.",
        "Plantilla LaTeX local: autor Martin Jonathan de la Cruz.",
        "Plantilla LaTeX local: matrícula ES2611202040.",
        "Plantilla LaTeX local: figura docente por definir.",
        "Plantilla LaTeX local: código LDE-S8B1.",
        "Memoria heredada: salida no JSON parseable desde Codex.",
        "Memoria heredada: normalización manual requerida en ciclo 1."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2 aplica sincronización transversal progresiva y conservadora.",
      "Se preservan reglas locales de Electiva S8 B1.",
      "Se integran abstracciones estables de Filosofía del Derecho.",
      "Se excluyen citas y conceptos temáticos no verificables para la electiva.",
      "Se refuerza bloqueo por JSON no parseable.",
      "Se refuerza validación entre citas y archivo .bib.",
      "Se refuerza control de placeholders y caracteres corruptos.",
      "Se mantienen preguntas abiertas para créditos, docente, código y nombre oficial."
    ]
  }
}