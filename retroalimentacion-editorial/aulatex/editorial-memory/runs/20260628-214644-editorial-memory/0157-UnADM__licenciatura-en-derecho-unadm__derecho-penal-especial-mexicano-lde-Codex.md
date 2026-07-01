{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad de origen y materia destino.",
    "Se preservan reglas estables: identidad UnADM, normalizacion estructurada, compresion union-dedupe sin perdida.",
    "Se transfieren solo abstracciones reutilizables; no se transfiere contenido tematico literal de Filosofia del Derecho.",
    "Se refuerzan ejes editoriales de cinco pasos para toda actividad del destino.",
    "Se mantiene control estricto: JSON parseable, citas verificables y coherencia README-programa-TeX-bib."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar contexto curricular verificado del destino: semestre 2, bloque 2, obligatoria, 8 creditos.",
    "Tomar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Conservar autoria real del estudiante y validar matricula y figura docente antes de entrega."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en bloques: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear el producto final a la consigna semanal real.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Sincronizar consistencia entre README, programa analitico, TeX y .bib."
  ],
  "activity_rules": [
    "Mapear cada actividad a un problema penal concreto.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada propia; evitar resumen descriptivo puro.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Agregar bibliografia especifica por actividad al .bib local antes de version final.",
    "No asumir fuentes de semanas posteriores sin evidencia de consigna."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Exigir esquema editorial minimo completo antes de reutilizar.",
    "Normalizar manualmente cualquier insumo desestructurado.",
    "Exigir correspondencia 1:1 entre citas en texto y entradas .bib.",
    "Bloquear entrega si hay placeholders, tokens sin resolver o campos truncados.",
    "Compilar LaTeX sin errores criticos ni referencias rotas."
  ],
  "latex_rules": [
    "Mantener plantilla base en espanol y letterpaper.",
    "Completar metadatos del documento antes de salida final.",
    "Corregir el campo truncado Tipo/Creditos en authortable. [supuesto: queda 'Obligatoria / 8']",
    "Sustituir tokens tipo $(@{...}.Slug) por nombres reales de archivo.",
    "Usar derecho-penal-especial-mexicano.bib como archivo bibliografico canonico local.",
    "Evitar comandos no estandar sin justificacion editorial."
  ],
  "bibliography_rules": [
    "Usar solo fuentes consultables y verificables; no inventar referencias.",
    "Mantener metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Registrar fecha de consulta en recursos web variables.",
    "Conservar entradas institucionales base: unadmSitioWeb y unadmMallaDerecho2024.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Tratar referencias heredadas de origen como no transferibles salvo validacion disciplinar local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y no contradictorias.",
    "Priorizar identidad, gates de calidad y estructura reusable en nodos transversales.",
    "Aplicar deduplicacion semantica sin recortar informacion util.",
    "Propagar correcciones tecnicas de placeholders y nombres corruptos a nodos hermanos.",
    "Mantener bandera activa de normalizacion manual para insumos heredados no estructurados.",
    "Evitar regresion de reglas utiles ya consolidadas."
  ],
  "open_questions": [
    "Confirmar figura docente real en plantillas del destino.",
    "Confirmar si LDE-S2B2 queda como codigo oficial fijo de materia. [supuesto: provisional]",
    "Validar si todas las actividades usan reporte y presentacion o solo un tipo por consigna.",
    "Confirmar rubrica de evaluacion local para ajustar profundidad argumentativa.",
    "Verificar cierre definitivo de campos truncados detectados en TeX y README."
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
        "Normalizacion estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia destino en semestre 2, bloque 2, obligatoria, 8 creditos.",
        "Respaldo curricular en malla institucional."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y norma aplicable.",
      "Analisis propio con evidencia.",
      "Cierre juridico transferible.",
      "Consistencia tecnica y academica de todo el expediente."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables juridicos solidos y verificables.",
      "Asegurar calidad editorial transversal sin contaminar disciplina entre materias no equivalentes."
    ],
    "style_markers": [
      "Frases directas y accionables.",
      "Supuestos marcados de forma explicita.",
      "Separacion entre dato verificado y dato provisional.",
      "Cierre con implicacion practica profesional."
    ],
    "argumentative_patterns": [
      "Problema -> marco normativo/doctrinal -> analisis propio -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> impacto practico.",
      "Objetivo declarado -> desarrollo coherente -> resultado verificable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalizacion JSON",
        "Ejes editoriales de cinco pasos",
        "Integridad bibliografica 1:1",
        "Compilacion LaTeX estable",
        "No transferencia tematica literal entre nodos transversales"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia confiable."
        },
        {
          "source": "Ejes editoriales de cinco pasos",
          "target": "Calidad argumentativa",
          "kind": "supports",
          "justification": "Ordenan el desarrollo y evitan entregas descriptivas."
        },
        {
          "source": "Integridad bibliografica 1:1",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Toda afirmacion queda trazable a evidencia."
        },
        {
          "source": "Correccion de placeholders",
          "target": "Compilacion LaTeX estable",
          "kind": "supports",
          "justification": "Previene fallos tecnicos y rutas invalidas."
        },
        {
          "source": "No transferencia tematica literal entre nodos transversales",
          "target": "Coherencia disciplinar del destino",
          "kind": "supports",
          "justification": "Evita mezclar contenido no equivalente sin evidencia local."
        }
      ],
      "evidence": [
        "README local con ubicacion curricular del destino.",
        "Programa analitico local con ejes de trabajo.",
        "Plantilla TeX local con campo truncado y figura docente pendiente.",
        "Archivo .bib local con base institucional verificable.",
        "Historial de salidas no parseables que exige normalizacion manual."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: se mantiene compresion lossless por union-dedupe.",
      "Ciclo 2: se preservan reglas previas utiles sin eliminacion.",
      "Ciclo 2: se refuerza gate de JSON parseable como bloqueo duro.",
      "Ciclo 2: se consolida transferencia de abstracciones estables, no redaccion literal.",
      "Ciclo 2: se mantienen abiertos vacios locales de consigna y rubrica."
    ]
  }
}