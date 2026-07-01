{
  "summary": [
    "Sincronizacion transversal aplicada de forma conservadora y sin regresion.",
    "Se preserva ADN UnADM y estructura de cinco ejes como abstraccion estable.",
    "Se mantiene regla critica: no propagar salidas no parseables sin normalizacion.",
    "Se refuerza compresion lossless por union-dedupe con deduplicacion semantica.",
    "Destino Economia LDE conserva contexto local verificado: semestre 3, bloque 2, obligatoria, 8 creditos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar contexto curricular local verificado de Economia LDE.",
    "Conservar voz formal, clara y juridicamente precisa.",
    "Marcar como supuesto todo dato no confirmado por consigna o planeacion.",
    "Tratar salidas heredadas de modelos como provisionales hasta verificacion local.",
    "Usar carpeta de materia como punto de entrada canonico."
  ],
  "structure_rules": [
    "Organizar cada entrega en problema, conceptos o datos, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar marco normativo o doctrinal cuando aplique.",
    "Alinear formato final a la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica o impacto social."
  ],
  "activity_rules": [
    "Adaptar cada actividad al tipo solicitado: reporte, presentacion o visual.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con fuente verificable y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir conceptos economicos, datos empiricos y argumento juridico."
  ],
  "quality_gates": [
    "Bloquear propagacion si salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Exigir trazabilidad entre afirmaciones, citas y .bib.",
    "Bloquear si hay campos criticos vacios sin marca de supuesto.",
    "Verificar correspondencia entre producto y consigna."
  ],
  "latex_rules": [
    "Mantener plantilla base local como referencia de formato.",
    "Conservar metadatos academicos completos en portada.",
    "Usar espanol y letterpaper salvo instruccion oficial distinta.",
    "Mantener estilo de citacion consistente con configuracion del documento.",
    "Evitar paquetes o comandos no estandar sin justificacion verificable.",
    "Corregir tokens sin expandir en README o rutas antes de compilar.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar economia.bib como repositorio canonico de la materia.",
    "Priorizar fuentes institucionales y normativas verificables.",
    "No inventar referencias ni usar salidas de modelos como fuente academica.",
    "Agregar solo fuentes realmente usadas en el producto.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/URL.",
    "Registrar fecha de consulta en recursos web cuando aplique."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos no equivalentes.",
    "No transferir redaccion literal ni contenidos tematicos especificos de Filosofia del Derecho.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Mantener estrategia progresiva y conservadora con no regresion.",
    "Si falta contexto local, mantener cerebro minimo y abrir vacios como supuestos."
  ],
  "open_questions": [
    "Confirmar guia formal adicional de formato para Economia LDE.",
    "Confirmar figura docente en metadatos de portada.",
    "Confirmar si hay rubrica especifica por actividad.",
    "Confirmar actualizacion anual de year y consulta en unadmSitioWeb.",
    "Supuesto: economia.bib es el nombre canonico final del .bib local."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico",
        "Claro y preciso",
        "Argumentativo con criterio propio"
      ],
      "institutional": [
        "Alineacion explicita con UnADM",
        "Integridad academica con citas verificables",
        "Entrada canonica por carpeta de materia"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Economia LDE en semestre 3, bloque 2, obligatoria, 8 creditos"
      ]
    },
    "essence": [
      "Problema juridico-social",
      "Conceptos y datos pertinentes",
      "Analisis propio",
      "Conclusion transferible",
      "Trazabilidad de evidencia"
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables y utiles para practica juridica."
    ],
    "style_markers": [
      "Frases breves y accionables",
      "Supuestos explicitados",
      "Separacion clara entre descripcion, analisis y cierre",
      "Sin invencion de fuentes"
    ],
    "argumentative_patterns": [
      "Problema -> concepto -> evidencia -> analisis -> conclusion",
      "Toda afirmacion relevante debe tener respaldo verificable",
      "Cierre con implicacion juridica concreta"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad academica",
        "Trazabilidad de fuentes",
        "Planeacion semanal",
        "Producto alineado",
        "Analisis propio",
        "Conclusion transferible"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad institucional exige evidencia y formato consistente."
        },
        {
          "source": "Planeacion semanal",
          "target": "Producto alineado",
          "kind": "depends_on",
          "justification": "El tipo de entrega se define por la consigna."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion valida deriva del razonamiento sustentado."
        },
        {
          "source": "Trazabilidad de fuentes",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Sin trazabilidad no hay verificabilidad academica."
        }
      ],
      "evidence": [
        "README de Economia LDE",
        "programa-analitico-economia.md",
        "economia.bib",
        "Regla persistente de bloqueo por JSON no parseable"
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas por variante ortografica.",
      "Se conservaron reglas utiles previas sin eliminacion.",
      "Se reforzaron gates de parseo, trazabilidad y supuestos.",
      "Se evito transferir contenido tematico especifico no transversal."
    ]
  }
}