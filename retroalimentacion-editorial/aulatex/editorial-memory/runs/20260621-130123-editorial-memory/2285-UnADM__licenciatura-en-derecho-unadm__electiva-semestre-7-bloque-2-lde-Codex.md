{
  "summary": [
    "Se sincroniza memoria transversal con transferencia de abstracciones editoriales estables.",
    "Se conserva identidad UnADM y encuadre local de Derecho semestre 7 bloque 2 electiva.",
    "Se refuerza normalizacion estructurada obligatoria antes de toda propagacion recursiva.",
    "Se consolidan ejes reutilizables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene estrategia progresiva y conservadora sin importar redaccion literal del origen.",
    "Supuesto: el destino no aporta aun consigna tematica especifica de actividades."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Usar encuadre local: Licenciatura en Derecho, semestre 7, bloque 2, electiva.",
    "Usar carpeta de materia como entrada canonica.",
    "No mezclar identidades de otras carreras en productos de Derecho.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "Marcar como supuesto todo dato no visible en consigna, rubrica o malla."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Registrar fuentes especificas de actividad en el .bib local.",
    "No asumir bibliografia de otra asignatura o semana sin verificacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Marcar y aislar insumos no estructurados para normalizacion manual.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Corregir placeholders y nombres rotos en README y programa antes de reutilizar."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base.",
    "Mantener metadatos de curso LDE-S7B2 y portada academica completa.",
    "Usar article con spanish, letterpaper y oneside salvo instruccion distinta.",
    "No compilar con tokens sin expandir tipo $(@{...}).",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo fuentes verificables y consultables.",
    "Priorizar fuentes institucionales UnADM y normativas pertinentes al encargo.",
    "Centralizar referencias en electiva-semestre-7-bloque-2.bib.",
    "Conservar metadatos minimos: autor, titulo, año, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas, generales y no duplicadas.",
    "Transferir identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferencia de contenido tematico literal entre nodos no equivalentes.",
    "Mantener compresion lossless por union-dedupe sin recorte.",
    "Conservar alertas de ciclos con normalizacion manual pendiente."
  ],
  "open_questions": [
    "Confirmar nombre oficial de la electiva en malla curricular.",
    "Confirmar creditos oficiales en README y portada.",
    "Confirmar figura docente en plantilla base.",
    "Resolver nombre canonico final del .bib en README y programa con placeholders activos.",
    "Supuesto: falta consigna local de actividades para ajustar granularidad de reglas."
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
        "Normalizacion estructurada previa a propagacion.",
        "Trazabilidad entre README, programa, plantillas y .bib."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 7, bloque 2, electiva.",
        "Produccion orientada a planeacion semanal y transferencia profesional."
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
      "Convertir planeacion semanal en entregables juridicos claros, sustentados y utiles.",
      "Preservar coherencia institucional y calidad editorial en toda actividad."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones explicitas y trazables.",
      "Supuestos etiquetados cuando falte informacion.",
      "Cierre con implicacion juridica practica."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma/doctrina -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion propia.",
      "Consigna -> objetivo -> verificacion final de coherencia."
    ],
    "knowledge_graph": {
      "concepts": [
        "identidad institucional",
        "normalizacion estructurada",
        "evidencia verificable",
        "postura argumentada",
        "alineacion con consigna",
        "conclusion transferible"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "identidad institucional",
          "target": "alineacion con consigna",
          "kind": "supports",
          "justification": "Define limites formales y curriculares del entregable."
        },
        {
          "source": "normalizacion estructurada",
          "target": "evidencia verificable",
          "kind": "supports",
          "justification": "Permite validar trazabilidad y evitar ruido heredado."
        },
        {
          "source": "evidencia verificable",
          "target": "postura argumentada",
          "kind": "supports",
          "justification": "La postura propia requiere respaldo documental."
        },
        {
          "source": "postura argumentada",
          "target": "conclusion transferible",
          "kind": "develops",
          "justification": "El analisis propio habilita cierre juridico util."
        },
        {
          "source": "alineacion con consigna",
          "target": "conclusion transferible",
          "kind": "depends_on",
          "justification": "Sin correspondencia con consigna, el cierre pierde pertinencia."
        }
      ],
      "evidence": [
        "README local confirma identidad UnADM y entrada canonica de carpeta.",
        "Programa analitico local define ejes de problema, conceptos, producto, analisis y cierre.",
        "Bibliografia local contiene base institucional verificable.",
        "Origen aporta reglas estables de calidad y estructura transferibles transversalmente."
      ]
    },
    "reinforcement_log": [
      "Ciclo 22: se integran reglas estables del origen sin traslado tematico literal.",
      "Ciclo 22: se refuerza gate de JSON parseable como condicion de propagacion.",
      "Ciclo 22: se mantiene separacion entre abstraccion editorial y contenido disciplinar especifico.",
      "Ciclo 22: se preserva memoria previa del destino sin eliminar reglas utiles."
    ]
  }
}