{
  "summary": [
    "Memoria de materia consolidada para Electiva Semestre 8 Bloque 1.",
    "Sincronización transversal aplicada desde Filosofía del Derecho con enfoque conservador.",
    "Se preservan abstracciones editoriales estables sin trasladar contenido temático no verificable.",
    "Se mantiene identidad institucional UnADM y trazabilidad académica.",
    "Se refuerzan estructura argumentativa, gates de calidad y control LaTeX.",
    "Se conserva antecedente de salidas no estructuradas como riesgo editorial.",
    "Supuesto: faltan consignas locales de actividades específicas.",
    "Supuesto: créditos, figura docente y nombre oficial de la electiva siguen pendientes."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, tono y formato.",
    "Usar tono jurídico formal, claro y verificable.",
    "Conservar contexto curricular local: Licenciatura en Derecho, semestre 8, bloque 1, tipo Electiva.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Evitar renombrar la asignatura sin confirmación oficial.",
    "Mantener código provisional LDE-S8B1 hasta confirmación oficial distinta.",
    "Conservar autor y matrícula definidos en plantilla base.",
    "Marcar como supuesto todo dato no visible o no confirmado localmente.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "Reconocer antecedente provisional: Codex desde ingeniería-en-sistemas-computacionales.",
    "Reconocer antecedente provisional: GPT-Pro desde Actividad 1.",
    "No eliminar reglas útiles previas; extender solo con evidencia local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Declarar objetivo puntual antes del desarrollo.",
    "Organizar entregables en secuencia: problema, conceptos o fuentes, producto, análisis propio y conclusión.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por la planeación semanal.",
    "Alinear cada actividad al programa analítico de la materia.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna.",
    "Diferenciar desarrollo del producto y comentario crítico.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Conservar README, programa analítico, plantillas, bibliografía y referencias locales."
  ],
  "activity_rules": [
    "Definir objetivo de la actividad al inicio.",
    "Vincular el producto con un problema jurídico o social delimitado.",
    "Relacionar conceptos, normas, doctrina o datos con el producto solicitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Diferenciar resumen de fuentes y postura propia.",
    "Incluir postura académica argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Confirmar que el producto corresponda a la consigna local.",
    "No extrapolar fuentes o contenidos de otras semanas sin evidencia local.",
    "No trasladar contenido temático de Filosofía del Derecho sin insumo verificable."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de reutilizar aguas abajo.",
    "Revisar respuestas no estructuradas antes de aplicarlas.",
    "Validar consistencia entre portada, metadatos y nombre de asignatura.",
    "Confirmar trazabilidad de afirmaciones con respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar que rutas locales citadas existan antes de usarlas como fuente.",
    "Revisar que la malla curricular respalde semestre, bloque y tipo.",
    "Marcar como pendiente todo dato no confirmado.",
    "Corregir literales de generador antes de entrega.",
    "Corregir caracteres corruptos en nombres de archivo antes de compilar.",
    "Compilar sin errores críticos y sin referencias rotas."
  ],
  "latex_rules": [
    "Mantener plantilla LaTeX base de la materia para reportes.",
    "Mantener clase article con spanish, letterpaper y oneside.",
    "Mantener documenttitle, documentsubtitle, documentsubject, coursename y coursecode consistentes.",
    "Completar campos pendientes de portada antes de entrega.",
    "Actualizar figura docente solo con nombre confirmado.",
    "No dejar créditos vacíos si el dato oficial está disponible.",
    "Conservar universitydepartmentimage como departamentos/UnADM salvo cambio verificado.",
    "Usar codificación y acentos correctos en español.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Usar electiva-semestre-8-bloque-1.bib como archivo bibliográfico local.",
    "Mantener claves BibTeX estables.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug).",
    "Corregir rutas con caracteres faltantes antes de compilar."
  ],
  "bibliography_rules": [
    "Registrar fuentes específicas de cada actividad en electiva-semestre-8-bloque-1.bib.",
    "Priorizar fuentes institucionales UnADM como base contextual.",
    "Conservar entrada unadmSitioWeb sin renombrar.",
    "Conservar entrada unadmMallaDerecho2024 sin renombrar.",
    "Citar la malla curricular de Derecho para ubicación curricular.",
    "Agregar fuentes doctrinales, normativas o jurisprudenciales solo cuando la actividad las requiera.",
    "No inventar referencias.",
    "Usar solo obras realmente consultadas y verificables.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Mantener notas de consulta y ruta de archivo cuando la fuente sea local.",
    "Distinguir bibliografía base y bibliografía específica de actividad.",
    "Validar correspondencia entre citas usadas y entradas del .bib."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Compartir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Propagar reglas de calidad, estructura y trazabilidad ya validadas.",
    "Propagar la regla de no inventar fuentes a nodos relacionados.",
    "Propagar control de placeholders a materias con plantillas automatizadas.",
    "No propagar metadatos específicos de esta electiva a materias no equivalentes.",
    "No propagar contenido temático de Filosofía del Derecho sin validación local.",
    "Aplicar unión-dedupe lossless en cada ciclo.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Registrar ciclo 1 como normalización manual reutilizable cuando falte insumo temático."
  ],
  "open_questions": [
    "Confirmar créditos oficiales de la electiva.",
    "Confirmar nombre de figura docente.",
    "Confirmar nombre oficial de la electiva si difiere del usado actualmente.",
    "Confirmar código oficial de la asignatura frente a LDE-S8B1.",
    "Confirmar consignas locales de actividades específicas.",
    "Confirmar rúbricas de evaluación locales.",
    "Confirmar fuentes obligatorias por semana.",
    "Confirmar existencia y consistencia de presentacion-electiva-semestre-8-bloque-1.tex.",
    "Corregir en README nombres de archivo con caracteres faltantes.",
    "Corregir en README y programa analítico tokens $(@{...}.Slug).",
    "Confirmar si debe existir carpeta referencias-electiva-semestre-8-bloque-1.",
    "Confirmar si se requiere bibliografía adicional para la electiva."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Verificable y sobrio.",
        "Argumentativo con criterio propio.",
        "Conservador ante datos no confirmados."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Carpeta de materia como entrada canónica.",
        "Portada consistente con plantilla local.",
        "Supuestos marcados sin ambigüedad."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 8.",
        "Bloque 1.",
        "Tipo Electiva.",
        "Código provisional LDE-S8B1."
      ]
    },
    "essence": [
      "Producto académico jurídico con identidad UnADM.",
      "Problema jurídico o social delimitado.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Fuentes verificables y trazables.",
      "Análisis propio del estudiante.",
      "Conclusión transferible a la práctica jurídica.",
      "Plantilla LaTeX estable y limpia.",
      "Bibliografía local controlada.",
      "Normalización antes de propagación."
    ],
    "reason_for_being": [
      "Orientar reportes, presentaciones y productos visuales de la electiva.",
      "Convertir la planeación semanal en entregables jurídicos verificables.",
      "Asegurar claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Preservar identidad institucional sin inventar datos.",
      "Servir como cerebro editorial mínimo mientras faltan consignas locales."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Encuadre jurídico o social breve.",
      "Secciones estables y reutilizables.",
      "Postura propia sustentada.",
      "Citas explícitas y verificables.",
      "Supuestos etiquetados.",
      "Cierre jurídico transferible.",
      "Metadatos de portada consistentes.",
      "Sin placeholders en entregables finales.",
      "Sin fuentes inventadas."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos y fuentes -> análisis -> conclusión.",
      "Afirmación -> evidencia verificable -> inferencia jurídica.",
      "Descripción breve -> posición crítica -> implicación práctica.",
      "Consigna -> producto requerido -> criterios de cumplimiento.",
      "Dato no confirmado -> marca de supuesto -> pregunta abierta.",
      "Fuente institucional -> ubicación curricular -> metadato de portada.",
      "Cita en texto -> entrada .bib -> verificación de compilación."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Electiva Semestre 8 Bloque 1",
        "Código provisional LDE-S8B1",
        "Problema jurídico o social",
        "Conceptos jurídicos pertinentes",
        "Marco normativo o doctrinal",
        "Producto solicitado por planeación",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Trazabilidad de fuentes",
        "Bibliografía local",
        "Normalización JSON",
        "Control de placeholders editoriales",
        "Compilación LaTeX estable",
        "Metadatos de portada",
        "Malla curricular de Derecho",
        "Supuestos editoriales"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Metadatos de portada",
          "kind": "supports",
          "justification": "La portada debe conservar universidad, carrera, materia y datos académicos consistentes."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Electiva Semestre 8 Bloque 1",
          "kind": "supports",
          "justification": "El README local la usa como fuente para semestre, bloque y tipo."
        },
        {
          "source": "Código provisional LDE-S8B1",
          "target": "Metadatos de portada",
          "kind": "supports",
          "justification": "La plantilla local define coursecode como LDE-S8B1 mientras no exista confirmación distinta."
        },
        {
          "source": "Producto solicitado por planeación",
          "target": "Estructura argumentativa jurídica",
          "kind": "develops",
          "justification": "La consigna determina si el entregable será reporte, presentación o producto visual."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El análisis debe responder a un problema delimitado, no solo resumir fuentes."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "Las fuentes jurídicas verificables sostienen la postura académica."
        },
        {
          "source": "Trazabilidad de fuentes",
          "target": "Bibliografía local",
          "kind": "depends_on",
          "justification": "Cada cita usada debe existir en el archivo .bib local."
        },
        {
          "source": "Conclusión jurídica transferible",
          "target": "Transferencia profesional",
          "kind": "supports",
          "justification": "El cierre debe conectar el aprendizaje con la práctica jurídica."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay reutilización confiable aguas abajo."
        },
        {
          "source": "Control de placeholders editoriales",
          "target": "Compilación LaTeX estable",
          "kind": "supports",
          "justification": "Eliminar tokens sin expandir y rutas corruptas reduce errores de compilación."
        },
        {
          "source": "Supuestos editoriales",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Marcar datos no confirmados evita afirmar información no verificada."
        },
        {
          "source": "Contenido temático de Filosofía del Derecho",
          "target": "Electiva Semestre 8 Bloque 1",
          "kind": "contrasts",
          "justification": "La relación es transversal; solo se transfieren abstracciones editoriales estables."
        }
      ],
      "evidence": [
        "README local identifica la materia como Licenciatura en Derecho de la UnADM.",
        "README local indica semestre 8, bloque 1 y tipo Electiva.",
        "README local deja créditos vacíos.",
        "README local cita UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
        "README local contiene nombres corruptos: eporte y eferencias.",
        "README local contiene token sin expandir $(@{...}.Slug).",
        "Programa analítico local define propósito con problema, conceptos, fuentes, análisis y cierre.",
        "Programa analítico local indica agregar fuentes específicas al .bib local.",
        "Archivo .bib local contiene unadmSitioWeb.",
        "Archivo .bib local contiene unadmMallaDerecho2024.",
        "Plantilla LaTeX local define autor Martin Jonathan de la Cruz.",
        "Plantilla LaTeX local define matrícula ES2611202040.",
        "Plantilla LaTeX local define Figura docente como Nombre por definir.",
        "Plantilla LaTeX local define coursecode LDE-S8B1.",
        "Memoria heredada registra salida no JSON parseable desde Codex.",
        "Memoria actual registra salida no JSON parseable desde GPT-Pro.",
        "Transferencia indicada como transversal entre nodos no equivalentes."
      ]
    },
    "reinforcement_log": [
      "Ciclo 1: se aplica sincronización transversal progresiva y conservadora.",
      "Se preserva identidad UnADM del destino.",
      "Se deduplican reglas equivalentes sin recortar contenido útil.",
      "Se incorporan solo abstracciones estables desde Filosofía del Derecho.",
      "Se evita trasladar bibliografía temática de Filosofía del Derecho.",
      "Se refuerza estructura problema-fuentes-análisis-conclusión.",
      "Se refuerza la obligación de postura propia sustentada.",
      "Se refuerza control de JSON parseable antes de propagación.",
      "Se refuerza control de placeholders y nombres corruptos detectados localmente.",
      "Se mantienen vacíos locales como preguntas abiertas."
    ]
  }
}