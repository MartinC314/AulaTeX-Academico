```json
{
  "summary": [
    "Se consolida memoria editorial transversal para materia mercantil UnADM.",
    "Se transfieren abstracciones estables: identidad, estructura, calidad y grafo conceptual.",
    "Se preserva estrategia conservadora: sin contenido tematico filosofico.",
    "Se refuerza normalizacion previa y control JSON parseable.",
    "Se mantiene compresion lossless por union y deduplicacion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en todo entregable.",
    "Alinear productos a Licenciatura en Derecho y materia mercantil.",
    "Conservar tono juridico-formal y cierre con criterio propio.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales."
  ],
  "structure_rules": [
    "Usar carpeta de materia como nodo canonico.",
    "Estructurar actividades: problema, conceptos/normas, desarrollo del producto, analisis propio y conclusion.",
    "Mantener consistencia entre README, programa, .tex y .bib.",
    "Incluir transferencia profesional en el cierre."
  ],
  "activity_rules": [
    "Contextualizar con problema juridico concreto y delimitado.",
    "Sustentar afirmaciones con normas, doctrina o datos verificables.",
    "Distinguir evidencia citada de interpretacion propia.",
    "Evitar entregas meramente descriptivas.",
    "Cerrar con conclusion juridica aplicable."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar.",
    "Verificar trazabilidad entre afirmaciones y fuentes.",
    "Confirmar uso del .bib local real.",
    "Evitar regresion de reglas utiles heredadas."
  ],
  "latex_rules": [
    "Usar plantilla base de la materia y completar metadatos.",
    "Mantener nomenclatura consistente de archivos.",
    "Corregir macros truncadas antes de compilar.",
    "Usar español correcto con acentos.",
    "Mantener claves BibTeX estables."
  ],
  "bibliography_rules": [
    "Usar el .bib local confirmado de la materia.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "No inventar referencias.",
    "Conservar metadatos minimos completos.",
    "Distinguir bibliografia base de bibliografia por actividad."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables.",
    "Evitar transferir redaccion literal o contenido tematico ajeno.",
    "Marcar alertas heredadas hasta confirmacion.",
    "Aplicar union-dedupe lossless en cada ciclo."
  ],
  "open_questions": [
    "Confirmar resolucion definitiva de salidas no JSON parseable.",
    "Confirmar plantilla oficial de presentacion.",
    "Verificar resolucion de placeholders de slug.",
    "Confirmar consignas especificas por actividad."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico",
        "Juridicamente preciso",
        "Argumentativo con criterio propio"
      ],
      "institutional": [
        "Alineacion explicita con UnADM",
        "Integridad academica con citas verificables",
        "Normalizacion estructurada antes de propagar"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Semestre 6, bloque 2, obligatoria, 8 creditos",
        "Materia mercantil con enfoque practico"
      ]
    },
    "essence": [
      "Problema juridico como eje",
      "Marco normativo verificable",
      "Analisis propio argumentado",
      "Conclusion transferible a la practica"
    ],
    "reason_for_being": [
      "Servir como cerebro editorial persistente reutilizable",
      "Asegurar calidad academica transversal",
      "Facilitar transferencia profesional del conocimiento"
    ],
    "style_markers": [
      "Apertura breve con problema",
      "Secciones claras y ordenadas",
      "Supuestos explicitados",
      "Cierre con implicacion profesional"
    ],
    "argumentative_patterns": [
      "Problema -> normas y conceptos -> analisis -> conclusion",
      "Afirmaciones siempre respaldadas",
      "Contraste entre evidencia y postura propia"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema juridico",
        "Marco normativo",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion estructurada",
        "JSON parseable"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad institucional exige trazabilidad y citas verificables."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin problema delimitado no hay analisis pertinente."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion profesional requiere base normativa."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "JSON parseable",
          "kind": "depends_on",
          "justification": "La propagacion segura exige estructura valida."
        }
      ],
      "evidence": [
        "README de materia",
        "Programa analitico",
        ".bib local confirmado"
      ]
    },
    "reinforcement_log": [
      "Se refuerza identidad UnADM como eje transversal.",
      "Se consolidan gates de calidad y normalizacion.",
      "Se preserva estrategia conservadora sin regresiones."
    ]
  }
}
```