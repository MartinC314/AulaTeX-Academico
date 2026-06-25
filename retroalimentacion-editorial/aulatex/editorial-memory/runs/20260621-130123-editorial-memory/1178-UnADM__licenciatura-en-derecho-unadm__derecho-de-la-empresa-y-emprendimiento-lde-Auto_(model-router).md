```json
{
  "summary": [
    "Se consolida cerebro editorial minimo y estable para la materia Derecho de la empresa y emprendimiento.",
    "Se refuerzan abstracciones transversales heredadas: identidad UnADM, estructura reusable y gates de calidad.",
    "No se transfiere contenido doctrinal especifico de Filosofia del Derecho por no equivalencia disciplinar.",
    "Se mantiene estrategia conservadora con normalizacion previa obligatoria."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial de la materia en todos los artefactos.",
    "Usar Licenciatura en Derecho como programa academico.",
    "Respetar contexto curricular local: semestre 6, bloque 2, obligatoria, 8 creditos.",
    "Marcar como supuesto cualquier dato no confirmado por archivos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales."
  ],
  "structure_rules": [
    "Usar README de materia como punto de entrada canonico.",
    "Alinear entregables al eje reusable: problema, conceptos, evidencia, analisis propio, conclusion.",
    "Conservar correspondencia entre .tex, presentacion y .bib locales.",
    "Usar programa analitico local para orientar profundidad y producto.",
    "Resolver tokens de plantilla sin expandir antes de producir entregables."
  ],
  "activity_rules": [
    "Identificar problema juridico o social relevante para la empresa o emprendimiento.",
    "Distinguir conceptos, normas y doctrina aplicables.",
    "Incluir analisis propio con criterio juridico.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Usar solo fuentes verificables registradas en el .bib local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Exigir estructura minima completa antes de reutilizar memoria.",
    "Confirmar consistencia entre citas en texto y archivo .bib.",
    "Marcar y separar supuestos de hechos confirmados.",
    "Corregir placeholders y artefactos de plantilla antes de compilar.",
    "No eliminar reglas utiles previas durante fusion por union-dedupe."
  ],
  "latex_rules": [
    "Mantener plantilla base con macros institucionales coherentes.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Usar spanish, letterpaper y oneside salvo instruccion local.",
    "Verificar compilacion sin errores y sin referencias rotas.",
    "Confirmar rutas de imagen institucional antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar fuentes; registrar solo obras consultables.",
    "Priorizar fuentes institucionales UnADM y marco juridico vigente.",
    "Mantener claves BibTeX estables y sin duplicados.",
    "Registrar fuentes especificas de cada actividad en el .bib local.",
    "No citar fuentes no presentes en el archivo .bib."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables a nodos hermanos.",
    "Evitar propagar datos curriculares locales sin confirmacion.",
    "Exigir normalizacion manual en ciclos iniciales por antecedente de salidas no estructuradas.",
    "Propagar alertas de tokens Slug y artefactos de plantilla a materias con sintomas equivalentes."
  ],
  "open_questions": [
    "Confirmar guia de citacion juridica especifica de la materia.",
    "Confirmar parametrizacion del autor por actividad.",
    "Confirmar expansion correcta del Slug en README y programa analitico.",
    "Confirmar si year=2026 en fuentes institucionales es anio bibliografico o fecha de consulta."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico",
        "Claro y juridicamente preciso",
        "Argumentativo con criterio propio"
      ],
      "institutional": [
        "Alineacion explicita con UnADM",
        "Integridad academica",
        "Trazabilidad bibliografica"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Semestre avanzado",
        "Enfoque en transferencia profesional"
      ]
    },
    "essence": [
      "Identidad institucional UnADM",
      "Normalizacion estructurada",
      "Problema juridico",
      "Evidencia verificable",
      "Analisis propio",
      "Conclusion juridica transferible",
      "Control de supuestos"
    ],
    "reason_for_being": [
      "Orientar productos academicos con fundamento juridico y aplicacion profesional.",
      "Garantizar consistencia editorial transversal en la licenciatura.",
      "Servir como cerebro persistente reusable entre actividades."
    ],
    "style_markers": [
      "Frases cortas y directas",
      "Supuestos marcados explicitamente",
      "Sin afirmaciones sin fuente",
      "Cierre aplicado a la practica profesional"
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis propio -> conclusion",
      "Marco normativo como soporte del criterio personal",
      "Coherencia entre pregunta guia y cierre"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Problema juridico empresarial",
        "Evidencia verificable",
        "Analisis juridico aplicado",
        "Conclusion profesional"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura valida no se transfiere memoria."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La aplicacion profesional requiere respaldo documental."
        },
        {
          "source": "Control de supuestos",
          "target": "Integridad argumentativa",
          "kind": "supports",
          "justification": "Distingue hechos confirmados de inferencias."
        }
      ],
      "evidence": [
        "README local y programa analitico de la materia.",
        "Bibliografia institucional UnADM incluida en .bib local."
      ]
    },
    "reinforcement_log": [
      "Se refuerza marco reusable problema-conclusion sin importar la materia.",
      "Se evita contaminacion doctrinal entre nodos no equivalentes.",
      "Se preservan reglas institucionales y gates de calidad previos."
    ]
  }
}
```