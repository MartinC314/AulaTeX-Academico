{
  "summary": [
    "Memoria de materia Electiva S8 B1 consolidada con sincronización transversal conservadora.",
    "Se preserva identidad institucional UnADM y contexto curricular local.",
    "Se reutilizan solo abstracciones editoriales estables desde Filosofía del Derecho.",
    "No se trasladan contenidos temáticos ni fuentes específicas de nodos no equivalentes.",
    "Se refuerzan ejes editoriales: problema, conceptos, fuentes, análisis propio y conclusión jurídica.",
    "Se mantiene control obligatorio de JSON parseable antes de propagar.",
    "Se conserva antecedente de salidas no estructuradas desde Codex y GPT-Pro como fuente provisional.",
    "Se integran mejoras verificables del destino: placeholders, nombres corruptos y metadatos incompletos.",
    "Se consolida cerebro editorial mínimo de materia con vacíos locales marcados como supuestos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, tono y formato.",
    "Usar tono jurídico formal, claro, sobrio y verificable.",
    "Conservar contexto curricular local: Licenciatura en Derecho, semestre 8, bloque 1, tipo Electiva.",
    "Mantener código provisional LDE-S8B1 hasta confirmación oficial distinta.",
    "Evitar renombrar la asignatura sin confirmación oficial.",
    "Conservar autor y matrícula de plantilla base salvo instrucción institucional contraria.",
    "Conservar autor confirmado: Martin Jonathan de la Cruz.",
    "Conservar matrícula confirmada: ES2611202040.",
    "Marcar como supuesto todo dato no visible o no confirmado en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validación local.",
    "Reconocer fuente provisional heredada: Codex desde ingeniería-en-sistemas-computacionales.",
    "Reconocer fuente provisional heredada: GPT-Pro desde Actividad 1.",
    "No eliminar reglas útiles previas; extender solo con evidencia local."
  ],
  "structure_rules": [
    "Usar carpeta de materia como punto de entrada canónico.",
    "Alinear cada actividad al programa analítico de la materia.",
    "Abrir con encuadre breve del problema jurídico o social.",
    "Declarar objetivo puntual antes del desarrollo.",
    "Organizar entregables en secuencia: problema, conceptos o fuentes, producto, análisis propio y conclusión.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna.",
    "Alinear la entrega al producto solicitado por la planeación semanal.",
    "Incluir conclusión jurídica transferible a la práctica profesional.",
    "Conservar README, programa analítico, plantilla de reporte, plantilla de presentación, bibliografía y carpeta de referencias.",
    "Usar el programa analítico como guía de reportes, presentaciones y productos visuales."
  ],
  "activity_rules": [
    "Declarar objetivo de la actividad al inicio del reporte.",
    "Vincular el producto con al menos un problema jurídico o social delimitado.",
    "Relacionar conceptos, normas, doctrina o datos con el producto solicitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Diferenciar resumen de fuentes y análisis propio del estudiante.",
    "Incluir postura académica sustentada.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Cerrar con postura jurídica transferible a la práctica.",
    "No extrapolar fuentes o contenidos de otras semanas sin evidencia local.",
    "No trasladar contenido temático de Filosofía del Derecho sin insumo verificable en el destino.",
    "Verificar que el producto corresponda a la consigna específica de cada actividad."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar respuestas no estructuradas antes de reutilizarlas.",
    "Validar consistencia entre portada, metadatos y nombre de asignatura.",
    "Confirmar trazabilidad de afirmaciones con citas verificables.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar que rutas locales citadas existan antes de usarlas como fuente.",
    "Revisar que la malla curricular respalde semestre, bloque y tipo.",
    "Marcar como pendiente todo dato no confirmado, especialmente créditos y figura docente.",
    "Corregir literales de generador antes de entrega.",
    "Corregir caracteres corruptos en nombres de archivo antes de entrega.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Evitar regresiones respecto de reglas útiles previas."
  ],
  "latex_rules": [
    "Mantener plantilla LaTeX base de la materia para reportes.",
    "Mantener clase article con spanish, letterpaper y oneside en reporte base.",
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener documenttitle, documentsubtitle, documentsubject, coursename y coursecode consistentes.",
    "Conservar definiciones de curso y universidad sin renombrados inconsistentes.",
    "Conservar universitydepartmentimage como departamentos/UnADM salvo cambio institucional verificado.",
    "Completar campos pendientes de portada antes de entrega.",
    "Actualizar figura docente solo con nombre confirmado.",
    "No dejar créditos vacíos si el dato oficial está disponible.",
    "Usar electiva-semestre-8-bloque-1.bib como archivo bibliográfico local.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Evitar placeholders de automatización como $(@{...}.Slug) en archivos finales.",
    "Resolver tokens sin expandir en README y programa analítico.",
    "Corregir nombres corruptos en README: reporte y referencias.",
    "Compilar sin errores críticos y sin referencias rotas."
  ],
  "bibliography_rules": [
    "Usar electiva-semestre-8-bloque-1.bib como archivo bibliográfico local.",
    "Registrar fuentes específicas de cada actividad en el .bib local.",
    "Priorizar fuentes institucionales UnADM como base contextual.",
    "Conservar entrada institucional unadmSitioWeb si fue consultada.",
    "Conservar entrada unadmMallaDerecho2024 sin renombrar.",
    "Conservar la malla curricular de Derecho como fuente local de ubicación curricular.",
    "Agregar referencias doctrinales, normativas o jurisprudenciales solo cuando la actividad las requiera.",
    "No inventar referencias.",
    "Usar solo obras realmente consultadas y verificables.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Mantener notas de consulta y ruta de archivo cuando la fuente sea local.",
    "Usar claves BibTeX estables y descriptivas.",
    "Distinguir bibliografía base de bibliografía específica de actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar arriba y laterales reglas validadas de calidad, estructura y trazabilidad.",
    "Aplicar unión-dedupe lossless en cada ciclo.",
    "Compartir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "No propagar metadatos específicos de esta electiva a materias no equivalentes.",
    "No propagar fuentes temáticas de Filosofía del Derecho a esta electiva sin evidencia local.",
    "Propagar la regla de no inventar fuentes a nodos relacionados.",
    "Propagar la verificación de JSON parseable a nodos superiores.",
    "Aplicar normalización manual si se detecta salida no estructurada en nodos vecinos.",
    "Registrar ciclos con salida no estructurada como antecedentes provisionales.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Mantener vacíos locales como preguntas abiertas hasta confirmación documental."
  ],
  "open_questions": [
    "Confirmar créditos oficiales de la electiva para portada y README.",
    "Confirmar nombre de figura docente para plantilla base.",
    "Confirmar nombre oficial de la electiva si difiere de Electiva Semestre 8 Bloque 1.",
    "Confirmar código oficial de la asignatura frente al provisional LDE-S8B1.",
    "Confirmar si presentacion-electiva-semestre-8-bloque-1.tex comparte reglas de portada.",
    "Corregir en README los nombres de archivo con caracteres faltantes o placeholders.",
    "Confirmar existencia de carpeta referencias-electiva-semestre-8-bloque-1.",
    "Confirmar consigna textual de cada actividad antes de generar reglas específicas.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar si la actividad requiere reporte, presentación u otro formato principal.",
    "Confirmar rúbrica de evaluación específica.",
    "Supuesto: la materia destino carece de contenido temático local suficiente para reglas doctrinales específicas."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Jurídicamente preciso.",
        "Claro y verificable.",
        "Argumentativo con criterio propio.",
        "Sobrio ante datos no confirmados.",
        "Conservador en inferencias."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Portada consistente con plantilla local.",
        "Carpeta de materia como entrada canónica.",
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
      "Estructura argumentativa jurídica.",
      "Problema jurídico o social delimitado.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeación.",
      "Análisis propio y postura académica.",
      "Conclusión transferible a la práctica jurídica.",
      "Trazabilidad de fuentes.",
      "Normalización JSON.",
      "Control de placeholders editoriales.",
      "Conservadurismo ante datos curriculares incompletos."
    ],
    "reason_for_being": [
      "Orientar productos académicos de la electiva con claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Transformar la planeación semanal en reportes, presentaciones y productos visuales.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Evitar entregas descriptivas sin postura ni evidencia.",
      "Proteger la consistencia institucional de la carpeta de materia.",
      "Permitir propagación recursiva confiable sin pérdida de reglas útiles."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Encuadre breve del problema.",
      "Secciones estables y reutilizables.",
      "Fuentes verificables y citas explícitas.",
      "Postura propia sustentada.",
      "Supuestos etiquetados.",
      "Cierre jurídico transferible.",
      "Metadatos de portada consistentes.",
      "Sin placeholders en entregables finales.",
      "Sin extrapolación temática no verificada."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> análisis -> conclusión.",
      "Afirmación -> evidencia verificable -> inferencia jurídica.",
      "Descripción breve -> posición crítica -> implicación práctica.",
      "Consigna -> producto solicitado -> formato de entrega.",
      "Dato no confirmado -> marca de supuesto -> pregunta abierta.",
      "Fuente local -> cita BibTeX estable -> trazabilidad documental.",
      "Regla heredada -> validación local -> propagación conservadora."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Electiva Semestre 8 Bloque 1",
        "Código provisional LDE-S8B1",
        "Malla curricular de Derecho",
        "Problema jurídico o social",
        "Conceptos jurídicos pertinentes",
        "Marco normativo o doctrinal",
        "Producto solicitado por planeación",
        "Análisis propio del estudiante",
        "Postura académica sustentada",
        "Conclusión jurídica transferible",
        "Trazabilidad de fuentes",
        "Bibliografía local",
        "Normalización JSON",
        "Control de placeholders editoriales",
        "Compilación LaTeX estable",
        "Supuestos marcados",
        "Propagación transversal conservadora",
        "Unión-dedupe lossless"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Portada consistente",
          "kind": "supports",
          "justification": "La plantilla local define universidad, carrera, alumno y metadatos."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Semestre 8 bloque 1 tipo Electiva",
          "kind": "supports",
          "justification": "El README local la declara como fuente de ubicación curricular."
        },
        {
          "source": "Código provisional LDE-S8B1",
          "target": "Nombre oficial de la electiva",
          "kind": "depends_on",
          "justification": "Debe conservarse solo hasta confirmación oficial distinta."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Análisis propio del estudiante",
          "kind": "develops",
          "justification": "El encuadre del problema activa la argumentación del producto."
        },
        {
          "source": "Conceptos jurídicos pertinentes",
          "target": "Marco normativo o doctrinal",
          "kind": "supports",
          "justification": "Los conceptos ordenan la selección de normas, doctrina o datos."
        },
        {
          "source": "Trazabilidad de fuentes",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Evita afirmaciones sin respaldo y referencias inventadas."
        },
        {
          "source": "Bibliografía local",
          "target": "Citas verificables",
          "kind": "supports",
          "justification": "El archivo .bib local concentra fuentes institucionales y específicas."
        },
        {
          "source": "Control de placeholders editoriales",
          "target": "Compilación LaTeX estable",
          "kind": "supports",
          "justification": "Reduce errores por tokens sin expandir y rutas corruptas."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación transversal conservadora",
          "kind": "depends_on",
          "justification": "Sin formato parseable no hay reutilización confiable."
        },
        {
          "source": "Unión-dedupe lossless",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Conserva reglas útiles y elimina duplicados semánticos sin recorte."
        },
        {
          "source": "Supuestos marcados",
          "target": "Conservadurismo editorial",
          "kind": "supports",
          "justification": "Permite avanzar sin inventar datos curriculares o bibliográficos."
        },
        {
          "source": "Conclusión jurídica transferible",
          "target": "Transferencia profesional",
          "kind": "develops",
          "justification": "El cierre conecta el análisis académico con la práctica jurídica."
        }
      ],
      "evidence": [
        "README local: Materia de la Licenciatura en Derecho de la UnADM.",
        "README local: Semestre 8, bloque 1, tipo Electiva.",
        "README local: créditos vacíos.",
        "README local: fuente curricular UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
        "README local: placeholders Slug sin expandir.",
        "README local: nombres corruptos en reporte y referencias.",
        "Programa analítico local: claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: transformar planeación semanal en reportes, presentaciones y productos visuales.",
        "Programa analítico local: ejes problema, conceptos, producto, análisis propio y conclusión.",
        "Bib local: unadmSitioWeb.",
        "Bib local: unadmMallaDerecho2024.",
        "Plantilla LaTeX local: documentauthor Martin Jonathan de la Cruz.",
        "Plantilla LaTeX local: matrícula ES2611202040.",
        "Plantilla LaTeX local: coursecode LDE-S8B1.",
        "Plantilla LaTeX local: figura docente por definir.",
        "Plantilla LaTeX local: tipo Electiva con créditos vacíos.",
        "Memoria heredada institucional: revisar salida no estructurada antes de aplicar aguas abajo.",
        "Memoria origen: bloquear propagación si la salida no es JSON parseable.",
        "Memoria origen: sustentar afirmaciones con fuentes verificables y cita explícita.",
        "Memoria origen: no inventar referencias."
      ]
    },
    "reinforcement_log": [
      "Ciclo 16 aplica sincronización transversal progresiva y conservadora.",
      "Se preservan reglas institucionales UnADM del destino.",
      "Se absorben solo patrones estructurales reutilizables del origen.",
      "Se excluyen fuentes temáticas específicas de Filosofía del Derecho por nodo no equivalente.",
      "Se refuerza estructura problema-conceptos-evidencia-análisis-conclusión.",
      "Se refuerza regla de no inventar fuentes.",
      "Se refuerza validación de JSON parseable antes de propagación.",
      "Se refuerza control de placeholders y nombres corruptos detectados localmente.",
      "Se mantienen preguntas abiertas sobre créditos, figura docente, código oficial y nombre oficial.",
      "Se corrigen relaciones conceptuales a tipos permitidos: supports, contrasts, depends_on y develops."
    ]
  }
}