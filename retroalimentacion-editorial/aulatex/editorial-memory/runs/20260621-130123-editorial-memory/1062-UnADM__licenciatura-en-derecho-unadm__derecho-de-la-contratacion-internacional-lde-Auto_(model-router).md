```json
{
  "summary": [
    "Se consolida ADN editorial transversal UnADM desde actividad no equivalente.",
    "Se preservan ejes editoriales estables: problema, marco, analisis, conclusion.",
    "Se refuerza normalizacion estructurada y bloqueo por JSON invalido.",
    "Se sincroniza identidad institucional sin transferir redaccion literal.",
    "Se crea cerebro editorial minimo y reutilizable para la materia destino."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de la asignatura y coursecode local.",
    "Marcar como supuesto todo dato no confirmado por planeacion oficial.",
    "Conservar trazabilidad del origen de reglas heredadas.",
    "Tratar fuentes heredadas no verificadas como provisionales."
  ],
  "structure_rules": [
    "Alinear toda entrega al esquema: problema, marco, analisis, conclusion.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar descripcion de postura propia.",
    "Cerrar con conclusion juridica transferible."
  ],
  "activity_rules": [
    "Identificar problema juridico o social concreto.",
    "Vincular afirmaciones con norma, doctrina o evidencia.",
    "Incluir postura argumentada del estudiante.",
    "Declarar limites del analisis cuando falten datos.",
    "Alinear producto final a la consigna local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar.",
    "Confirmar respaldo de toda afirmacion normativa.",
    "Verificar coherencia entre consigna, desarrollo y conclusion.",
    "Normalizar respuestas no estructuradas antes de propagar."
  ],
  "latex_rules": [
    "Conservar plantilla institucional y macros UnADM.",
    "Evitar cambios de clase o paquetes sin justificacion.",
    "Mantener compilacion sin errores ni referencias rotas.",
    "Usar acentos y codificacion correcta en español.",
    "No sustituir macros institucionales por texto libre."
  ],
  "bibliography_rules": [
    "Usar el .bib local de la materia como repositorio principal.",
    "No inventar fuentes; citar solo obras consultables.",
    "Distinguir bibliografia base y especifica de actividad.",
    "Usar claves BibTeX estables y descriptivas.",
    "Incluir fecha de consulta en fuentes web."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables.",
    "No sobrescribir reglas locales mas especificas.",
    "Aplicar deduplicacion semantica por union.",
    "Mantener aviso de incidente JSON hasta resolucion.",
    "Propagar recursivamente solo tras validacion completa."
  ],
  "open_questions": [
    "Confirmar consignas especificas por actividad.",
    "Definir formato uniforme de citas juridicas.",
    "Confirmar checklist minimo por tipo de producto.",
    "Verificar correccion de placeholders en README.",
    "Confirmar resolucion definitiva del incidente JSON."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico",
        "Claro",
        "Argumentativo"
      ],
      "institutional": [
        "Alineacion explicita con UnADM",
        "Integridad academica",
        "Citas verificables"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Asignatura obligatoria",
        "Transferencia profesional"
      ]
    },
    "essence": [
      "Problema juridico como detonador",
      "Marco normativo o doctrinal",
      "Analisis propio",
      "Conclusion juridica aplicable",
      "Identidad institucional"
    ],
    "reason_for_being": [
      "Estandarizar productos academicos con criterio juridico.",
      "Garantizar trazabilidad y reutilizacion editorial.",
      "Asegurar coherencia institucional entre materias."
    ],
    "style_markers": [
      "Supuestos explicitados",
      "Separacion descripcion-postura",
      "Cierre con criterio juridico",
      "Lenguaje tecnico preciso"
    ],
    "argumentative_patterns": [
      "Problema -> marco -> evidencia -> analisis -> conclusion",
      "Afirmacion -> fuente -> interpretacion propia",
      "Consigna -> producto -> validacion final"
    ],
    "knowledge_graph": {
      "concepts": [
        "Problema juridico",
        "Marco normativo",
        "Analisis propio",
        "Conclusion juridica",
        "Normalizacion estructurada",
        "Identidad UnADM"
      ],
      "citations": [
        "unadmMallaDerecho2024",
        "unadmSitioWeb"
      ],
      "relations": [
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El analisis se activa por una cuestion juridica concreta."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica",
          "kind": "supports",
          "justification": "La conclusion debe sustentarse en norma o doctrina."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay reutilizacion."
        }
      ],
      "evidence": [
        "README y programa analitico de la materia.",
        "Reglas institucionales UnADM consolidadas.",
        "Incidentes historicos de JSON no parseable."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin perdida semantica.",
      "Se reforzaron gates de calidad institucional.",
      "Se alineo identidad transversal entre nodos no equivalentes."
    ]
  }
}
```