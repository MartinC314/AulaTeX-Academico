{
  "summary": [
    "Se consolida memoria lateral para Actividad 4 con deduplicacion lossless y sin recorte util.",
    "Se preserva identidad UnADM, marco curricular y ejes editoriales comunes de Filosofia del Derecho.",
    "Se refuerza normalizacion estructurada y validacion JSON estricta por antecedentes no parseables.",
    "Se transfieren solo patrones reutilizables desde Actividad 1, sin copiar conclusiones ni bibliografia exclusiva.",
    "Supuesto: la consigna textual especifica de Actividad 4 no esta visible; se mantiene estructura base verificable."
  ],
  "identity_rules": [
    "Mantener tono formal academico y precision juridica alineados con UnADM.",
    "Anclar la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica documental.",
    "Exigir postura propia sustentada; evitar texto meramente descriptivo.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener trazabilidad entre pregunta guia, desarrollo y conclusion."
  ],
  "activity_rules": [
    "Aplicar los cinco ejes del programa analitico en toda Actividad 4.",
    "Incluir problema, conceptos, evidencia y postura personal de forma explicita.",
    "Sustentar afirmaciones con citas verificables en texto.",
    "Evitar reutilizar contenido literal de actividades hermanas.",
    "No asumir bibliografia de semanas distintas sin validacion de consigna.",
    "Ajustar profundidad argumentativa a la rubrica cuando exista."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema minimo completo antes de reutilizar memoria.",
    "Normalizar respuestas no estructuradas heredadas antes de propagar.",
    "Verificar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Comprobar consistencia entre citas en .tex y entradas en .bib.",
    "Confirmar correspondencia del producto final con consigna de Actividad 4."
  ],
  "latex_rules": [
    "Usar espanol con acentos correctos en .tex y .bib.",
    "Citar solo claves existentes en el .bib activo.",
    "Conservar claves BibTeX estables para evitar roturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) antes de fijar nombres de archivo.",
    "Verificar nombres reales en README por caracteres danados detectados."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables (UnADM, SCJN, UNAM-IIJ).",
    "Agregar al .bib solo fuentes realmente consultables para Actividad 4.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, anio, editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib parece orientado a interpretacion juridica; confirmar aplicabilidad a Actividad 4."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras pasar gates de JSON y estructura.",
    "Mantener union-dedupe sin eliminar reglas utiles previas.",
    "Transferir a nodos hermanos solo patrones generales reutilizables.",
    "Evitar copiar redaccion literal, resultados o bibliografia exclusiva entre actividades.",
    "Registrar mejoras verificables en cada ciclo para evitar regresiones.",
    "Mantener bandera de normalizacion manual para memorias de ciclos con salida no estructurada."
  ],
  "open_questions": [
    "Confirmar consigna textual de Actividad 4: producto, extension y criterios.",
    "Confirmar si el entregable es reporte, presentacion u otro formato.",
    "Confirmar rubrica docente especifica para calibrar nivel argumentativo.",
    "Confirmar nombre canonico final del .bib de asignatura por token Slug no resuelto.",
    "Confirmar si Actividad 4 requiere bibliografia propia o reutiliza base existente."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro.",
        "Juridicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Entrada canonica en carpeta de asignatura.",
        "Normalizacion estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Filosofia del Derecho.",
        "Semestre 1, bloque 2.",
        "Obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y utiles.",
      "Garantizar coherencia entre identidad institucional, evidencia y argumentacion juridica.",
      "Sostener calidad tecnica LaTeX y calidad academica en cada entrega."
    ],
    "style_markers": [
      "Objetivo puntual al inicio.",
      "Secciones funcionales y separadas.",
      "Cita explicita de afirmaciones.",
      "Marcado de supuestos cuando falten datos locales.",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Delimitar conceptos y normas.",
      "Contrastar evidencia y doctrina.",
      "Fijar postura razonada.",
      "Concluir con aplicacion juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales de Filosofia del Derecho",
        "Normalizacion estructurada",
        "Validacion JSON estricta",
        "Integridad academica y verificabilidad",
        "Relacion problema-evidencia-conclusion"
      ],
      "citations": [
        "README.md de la asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Tono y formato academico",
          "kind": "supports",
          "justification": "La pauta editorial exige alineacion explicita institucional."
        },
        {
          "source": "Ejes editoriales de Filosofia del Derecho",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Los ejes ordenan problema, conceptos, evidencia, analisis y cierre."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay reutilizacion segura."
        },
        {
          "source": "Integridad academica y verificabilidad",
          "target": "Conclusion juridica propia",
          "kind": "supports",
          "justification": "La conclusion valida depende de evidencia y citas consistentes."
        }
      ],
      "evidence": [
        "README define identidad UnADM, integridad academica y conclusion juridica propia.",
        "Programa analitico define cinco ejes de trabajo reutilizables.",
        "Antecedentes de salidas no parseables justifican gate JSON estricto.",
        "README y programa muestran token Slug sin resolver; requiere validacion local."
      ]
    },
    "reinforcement_log": [
      "Ciclo 5: deduplicacion completa de reglas repetidas en destino.",
      "Ciclo 5: refuerzo lateral de ejes editoriales comunes sin copiar contenido especifico de Actividad 1.",
      "Ciclo 5: consolidacion de gates de calidad JSON + estructura + citas.",
      "Ciclo 5: mantenimiento de supuestos abiertos donde falta consigna local."
    ]
  }
}