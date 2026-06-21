{
  "summary": [
    "Sincronizacion transversal consolidada en destino con union-dedupe lossless y sin regresion.",
    "Se preservan reglas institucionales UnADM, estructura canonica, validacion JSON y trazabilidad de fuentes.",
    "Se transfieren solo abstracciones estables del origen: objetivo puntual, evidencia verificable, postura propia y coherencia cierre-consigna.",
    "Se excluye transferencia de contenido tematico especifico de Filosofia del Derecho por no equivalencia disciplinar."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "No trasladar metadatos curriculares de otra asignatura al destino."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco teorico-normativo, analisis propio y cierre.",
    "Alinear el producto al entregable solicitado por la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias de estructura reusable."
  ],
  "activity_rules": [
    "Sustentar afirmaciones relevantes con fuente verificable y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar resumen descriptivo puro.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Cerrar con conclusion transferible a la practica juridica.",
    "Marcar supuestos cuando falte contexto local de la actividad."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema minimo completo antes de reutilizar memoria.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No promover reglas provisionales a definitivas sin validacion local."
  ],
  "latex_rules": [
    "Usar configuracion en espanol coherente con la plantilla local.",
    "Mantener clase y formato base salvo justificacion academica.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Mantener coursename y coursecode locales salvo instruccion institucional.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver placeholders y tokens dinamicos en README, programa, rutas y nombres de archivo.",
    "Corregir caracteres truncados o anomalias de ruta antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Registrar fuentes especificas de actividad en el .bib local de la materia.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No citar claves inexistentes en el .bib."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y estables.",
    "Compartir entre nodos no equivalentes solo abstracciones editoriales, no redaccion literal.",
    "Preservar reglas utiles previas; evitar regresiones en cada ciclo.",
    "Etiquetar incidencias de parseo como alertas reutilizables inter-materias.",
    "Si falta contexto local, mantener cerebro minimo y abrir vacios como preguntas."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de actividades del destino; confirmar tipos de producto por semana.",
    "Confirmar estandar de citacion oficial de la licenciatura (APA u otro).",
    "Confirmar si LDE-S4B2 es clave oficial o convencion local.",
    "Confirmar politica institucional sobre conclusion juridica en actividades de enfoque antropologico.",
    "Confirmar que el nombre canonico del .bib queda fijo como antropologia-de-la-cultura-en-mexico.bib."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con trazabilidad de fuentes.",
        "Entrada canonica por carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos.",
        "Asignatura destino: Antropologia de la cultura en Mexico."
      ]
    },
    "essence": [
      "Problema, conceptos, evidencia, analisis propio y conclusion transferible.",
      "Normalizacion estructurada antes de toda propagacion.",
      "Compresion lossless por deduplicacion, no por recorte.",
      "Transferencia transversal conservadora basada en abstracciones estables."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con rigor, evidencia y utilidad profesional.",
      "Asegurar continuidad editorial entre nodos sin contaminar contexto disciplinar local.",
      "Resguardar memoria institucional verificable y reutilizable."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Cierre argumentativo aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> respaldo verificable -> interpretacion propia.",
      "Consigna -> desarrollo alineado -> cierre coherente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Validacion JSON parseable",
        "Normalizacion estructurada",
        "Transferencia transversal conservadora"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Validacion JSON parseable",
          "target": "Normalizacion estructurada",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay propagacion confiable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura se legitima con respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "El cierre util deriva del razonamiento y no del resumen."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige trazabilidad y verificabilidad."
        }
      ],
      "evidence": [
        "README local confirma identidad UnADM y pauta editorial.",
        "Programa analitico local confirma ejes problema-conceptos-producto-analisis-cierre.",
        "Bib local contiene unadmSitioWeb y unadmMallaDerecho2024.",
        "Memoria origen aporta gates de JSON, supuestos y coherencia argumentativa como abstracciones estables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 85: deduplicadas reglas repetidas y conservadas reglas utiles previas.",
      "Ciclo 85: reforzada barrera de parseo JSON y normalizacion previa a propagacion.",
      "Ciclo 85: incorporadas abstracciones estables del origen sin transferir contenido tematico de Filosofia del Derecho.",
      "Ciclo 85: mantenida alerta sobre fuentes heredadas no verificadas como provisionales."
    ]
  }
}