{
  "summary": [
    "Se mantiene memoria transversal UnADM con compresión por unión-deduplicación sin pérdida.",
    "Se preserva normalización estructurada obligatoria antes de propagación recursiva.",
    "Se transfiere solo abstracción estable desde Filosofía del Derecho: ejes editoriales, calidad, citas y cierre jurídico.",
    "Se evita trasladar contenido temático literal entre materias no equivalentes.",
    "Se refuerza saneamiento local de placeholders de slug y campos truncados en README, programa y TeX."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Usar contexto curricular verificado del destino: semestre 2, bloque 2, obligatoria, 8 créditos.",
    "Tomar la carpeta de materia como entrada canónica.",
    "Marcar como [supuesto] cualquier dato no visible en consigna o evidencia local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Conservar autoría real del estudiante y validar matrícula y figura docente antes de entrega."
  ],
  "structure_rules": [
    "Iniciar cada producto con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en bloques: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear el producto al formato exigido por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Sincronizar consistencia entre README, programa analítico, TeX y .bib."
  ],
  "activity_rules": [
    "Mapear cada actividad a un problema penal concreto y verificable.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada propia; evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Agregar fuentes específicas por actividad al .bib local antes de versión final.",
    "No asumir que bibliografía de otra semana o materia aplica automáticamente."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Exigir estructura mínima completa del esquema editorial antes de reutilizar.",
    "Normalizar manualmente cualquier insumo desestructurado antes de aplicar aguas abajo.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de [supuesto].",
    "Validar correspondencia 1:1 entre citas en texto y entradas .bib.",
    "Detectar y corregir placeholders o tokens sin resolver antes de compilar.",
    "Compilar LaTeX sin errores críticos ni referencias rotas antes de entrega."
  ],
  "latex_rules": [
    "Usar español con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas de compilación.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Conservar plantilla base y metadatos completos antes de salida final.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Usar derecho-penal-especial-mexicano.bib como archivo bibliográfico canónico local.",
    "Completar campo truncado Tipo/Créditos en authortable. [supuesto: truncado persiste hasta edición]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y normas/criterios jurídicos verificables.",
    "Usar solo obras realmente consultables; no inventar referencias.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Registrar fecha de consulta en recursos web o variables.",
    "Distinguir bibliografía base de materia y bibliografía específica por actividad.",
    "Mantener entradas institucionales base unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y no contradictorias.",
    "Priorizar identidad, estructura reusable y gates de calidad en saltos transversales.",
    "Aplicar deduplicación semántica sin recorte de reglas útiles previas.",
    "Evitar transferencia de redacción literal y de contenido disciplinar no equivalente.",
    "Mantener bandera de normalización manual activa para ciclo 1.",
    "Propagar correcciones técnicas reutilizables: placeholders, nombres corruptos y campos truncados."
  ],
  "open_questions": [
    "Confirmar nombre definitivo de figura docente en plantillas.",
    "Confirmar si LDE-S2B2 queda fijo como código canónico global de materia.",
    "Verificar que autor y matrícula visibles sean definitivos para entrega.",
    "Confirmar que no queden rutas con caracteres anómalos en README/estructura TeX.",
    "Confirmar consigna de una actividad real del destino para aterrizar reglas de producto específico."
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
        "Normalización estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 2, bloque 2, obligatoria, 8 créditos.",
        "Respaldo curricular en malla institucional."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos, normas y doctrina pertinentes.",
      "Producto alineado a consigna.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos claros, sustentados y útiles para práctica jurídica.",
      "Garantizar consistencia técnica y editorial entre documentos de materia."
    ],
    "style_markers": [
      "Frases directas y verificables.",
      "Marcado explícito de [supuesto] cuando falte evidencia.",
      "Separación entre dato verificado y dato provisional.",
      "Cierre con criterio jurídico propio."
    ],
    "argumentative_patterns": [
      "Problema -> marco normativo/doctrinal -> análisis propio -> conclusión.",
      "Afirmación -> evidencia -> interpretación -> implicación práctica.",
      "Objetivo explícito -> desarrollo coherente -> resultado verificable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización JSON",
        "Ejes editoriales de cinco pasos",
        "Integridad bibliográfica 1:1",
        "Conclusión jurídica transferible",
        "Consistencia README-programa-TeX-bib",
        "Propagación transversal conservadora"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalización JSON",
          "target": "Propagación transversal conservadora",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia confiable."
        },
        {
          "source": "Ejes editoriales de cinco pasos",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "La secuencia guía el cierre jurídico con fundamento."
        },
        {
          "source": "Integridad bibliográfica 1:1",
          "target": "Identidad institucional UnADM",
          "kind": "supports",
          "justification": "La trazabilidad de citas sostiene la integridad académica institucional."
        },
        {
          "source": "Consistencia README-programa-TeX-bib",
          "target": "Normalización JSON",
          "kind": "supports",
          "justification": "La coherencia documental reduce errores de estructura y propagación."
        }
      ],
      "evidence": [
        "README local confirma semestre 2, bloque 2, obligatoria, 8 créditos.",
        "Programa analítico local define propósito y cinco ejes de trabajo.",
        "Bib local contiene base institucional verificable.",
        "Persisten tokens de slug sin expandir en README/programa y campo truncado en TeX. [supuesto: pendiente de corrección final]"
      ]
    },
    "reinforcement_log": [
      "Se consolidan reglas estables compartidas entre materias de Derecho sin traslado temático literal.",
      "Se preservan gates críticos heredados: JSON parseable, estructura mínima, citas 1:1 y compilación limpia.",
      "Se refuerza disciplina de supuestos explícitos para datos no visibles.",
      "Se mantiene estrategia progresiva y conservadora en ciclo 1."
    ]
  }
}