```json
{
  "summary": [
    "Materia destino UnADM Derecho: semestre 6, bloque 2, obligatoria, 8 creditos.",
    "La carpeta de materia es punto de entrada canonico para plantilla, programa analitico y bibliografia local.",
    "La pauta exige identidad UnADM, integridad academica, citas verificables y conclusion juridica propia.",
    "Existe bibliografia local en derechos-de-contratos-mercantiles-y-titulos-valores.bib con entradas institucionales.",
    "Ejes editoriales estables: problema, conceptos o normas, evidencia, analisis propio y conclusion juridica.",
    "Aplicar compresion lossless por union y deduplicacion sin recortar reglas utiles.",
    "Supuesto heredado: persiste alerta institucional por salida no JSON parseable hasta nueva evidencia.",
    "Transferencia transversal desde Filosofia del Derecho: solo abstracciones editoriales estables, no redaccion literal."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, metadatos y redaccion academica.",
    "Alinear entregables a Licenciatura en Derecho y a la asignatura Derechos de contratos mercantiles y titulos valores.",
    "Conservar tono juridico-formal y postura academica propia en el cierre.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Citar malla-curricular-derecho-unadm.pdf como fuente de ubicacion curricular.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Fuente provisional heredada: GPT-Pro desde Actividad 1.",
    "Fuente provisional heredada: Codex desde ingenieria-en-sistemas-computacionales."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como nodo canonico para plantillas, programa analitico y bibliografia local.",
    "Estructurar cada actividad con problema, conceptos o normas, desarrollo del producto, analisis propio y conclusion transferible.",
    "Mantener consistencia entre README, programa analitico, .tex y .bib de la materia.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear la entrega al producto solicitado por la planeacion semanal.",
    "Corregir en README nombres truncados de reporte y referencias.",
    "Sustituir placeholders de slug por nombres reales de archivo."
  ],
  "activity_rules": [
    "Contextualizar cada actividad con un problema juridico o social concreto.",
    "Vincular argumentos con normas, doctrina o datos pertinentes y verificables.",
    "Cerrar cada entrega con conclusion juridica aplicable a la practica profesional.",
    "Desarrollar el producto solicitado por la planeacion.",
    "Distinguir evidencia citada de analisis propio.",
    "Definir objetivo puntual antes del desarrollo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo resumen descriptivo.",
    "Evitar entregas meramente descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion."
  ],
  "quality_gates": [
    "Validar que la salida sea JSON parseable antes de propagar memoria aguas abajo.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar que no haya regresion de reglas utiles heredadas.",
    "Comprobar trazabilidad entre afirmaciones, citas en texto y archivo .bib.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Verificar que no se agreguen fuentes inventadas.",
    "Confirmar que README y programa apunten al .bib local real.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar compilacion despues de ajustar nombres de archivos y macros."
  ],
  "latex_rules": [
    "Conservar plantilla base de reporte de la materia y completar metadatos del curso.",
    "Mantener nomenclatura consistente de archivos de reporte y presentacion por asignatura.",
    "Corregir y validar macros incompletas o truncadas antes de compilar.",
    "Revisar y completar la macro truncada \\def\\universitydepartmen en la plantilla.",
    "Mantener codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas de actividad en el .bib local de la materia.",
    "Priorizar fuentes institucionales UnADM y documentos curriculares locales cuando apliquen.",
    "No incorporar fuentes no verificadas ni inventadas.",
    "Usar derechos-de-contratos-mercantiles-y-titulos-valores.bib como archivo local confirmado.",
    "Conservar entradas existentes unadmSitioWeb y unadmMallaDerecho2024.",
    "Agregar fecha de consulta cuando se usen recursos web.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo reglas normalizadas y sin duplicados.",
    "Compartir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Evitar transferir redaccion literal entre Filosofia del Derecho y materia destino.",
    "Usar compresion union-dedupe lossless en cada fusion de memoria.",
    "Mantener alerta institucional sobre salida no JSON parseable hasta confirmacion.",
    "No propagar detalles locales de archivo si no aplican a materias laterales.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Ciclo 1 necesita normalizacion manual si se reutiliza."
  ],
  "open_questions": [
    "Confirmar rubricas y consignas reales de actividades de la materia destino.",
    "Definir plantilla oficial de presentacion si difiere del reporte.",
    "Verificar nombre final del archivo .bib generado por slug para evitar placeholders sin resolver.",
    "Confirmar correccion final de nombres truncados en README.",
    "Completar el resto de la plantilla .tex para revisar macros faltantes.",
    "Confirmar si la incidencia historica de salida no JSON parseable ya fue resuelta en flujos actuales.",
    "Confirmar si el sitio UnADM debe conservar year 2026 o usar fecha de consulta solamente.",
    "Definir conceptos juridicos propios de contratos mercantiles y titulos valores (vacio de contexto local)."
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
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Derechos de contratos mercantiles y titulos valores."
      ]
    },
    "essence": [
      "Problema juridico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion transferible a la practica juridica.",
      "Identidad institucional UnADM y trazabilidad de fuentes.",
      "Conclusion juridica transferible como cierre estable."
    ],
    "reason_for_being": [
      "Transformar la planeacion semanal en reportes, presentaciones y productos visuales que integren problema, conceptos, fuentes, analisis propio y cierre argumentativo.",
      "Usar la carpeta de materia como nodo canonico para plantillas, programa analitico y bibliografia local.",
      "Estructurar cada actividad con problema, conceptos o normas, producto, analisis propio y conclusion transferible.",
      "Mantener consistencia entre README, programa analitico, .tex y .bib de la materia."
    ],
    "style_markers": [
      "Afirmaciones con respaldo verificable.",
      "Supuestos marcados de forma explicita.",
      "Secciones claras y orden argumentativo estable.",
      "Cierre con criterio juridico propio.",
      "Mantener identidad institucional UnADM en tono, metadatos y presentacion.",
      "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Definir conceptos y marco normativo.",
      "Contrastar evidencia.",
      "Emitir analisis propio.",
      "Concluir con aplicabilidad profesional.",
      "Definir objetivo puntual antes del desarrollo.",
      "Sustentar afirmaciones con fuentes verificables y cita explicita."
    ],
    "knowledge_graph": {
      "concepts": [
        "identidad institucional UnADM",
        "integridad academica",
        "trazabilidad de fuentes",
        "problema juridico",
        "analisis propio",
        "conclusion juridica transferible",
        "marco normativo o doctrinal",
        "evidencia citada"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "identidad institucional UnADM",
          "target": "integridad academica",
          "kind": "supports",
          "justification": "La pauta local exige citas verificables y formato institucional."
        },
        {
          "source": "problema juridico",
          "target": "analisis propio",
          "kind": "develops",
          "justification": "La estructura editorial parte del problema y culmina en postura razonada."
        },
        {
          "source": "trazabilidad de fuentes",
          "target": "conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion gana validez cuando deriva de evidencia verificable."
        },
        {
          "source": "marco normativo o doctrinal",
          "target": "analisis propio",
          "kind": "depends_on",
          "justification": "El analisis propio se apoya en conceptos y normas previamente definidos."
        },
        {
          "source": "evidencia citada",
          "target": "analisis propio",
          "kind": "contrasts",
          "justification": "El analisis propio se distingue de la evidencia citada para evitar resumen descriptivo."
        }
      ],
      "evidence": [
        "README de materia: pauta editorial y ubicacion curricular.",
        "Programa analitico: ejes de trabajo y proposito de realizacion.",
        ".bib local: entradas institucionales confirmadas (unadmSitioWeb, unadmMallaDerecho2024).",
        "Plantilla .tex: metadatos del curso y macro truncada \\def\\universitydepartmen detectada."
      ]
    },
    "reinforcement_log": [
      "Ciclo 1 transversal: ingreso de abstracciones editoriales estables desde Filosofia del Derecho.",
      "Reforzada estructura argumentativa: problema, conceptos/normas, evidencia, analisis propio, conclusion.",
      "Reforzada identidad UnADM y trazabilidad de fuentes como ADN editorial.",
      "Anadido contraste evidencia citada vs analisis propio para evitar entregas descriptivas.",
      "Preservadas alertas heredadas: salida no JSON parseable y fuentes provisionales no verificadas.",
      "No se transfirio bibliografia ni conceptos juridicos especificos de Filosofia del Derecho (no equivalentes)."
    ]
  }
}
```