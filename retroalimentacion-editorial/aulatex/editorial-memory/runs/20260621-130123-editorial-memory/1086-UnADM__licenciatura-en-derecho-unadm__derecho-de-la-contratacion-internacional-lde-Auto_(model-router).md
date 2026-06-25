```json
{
  "summary": [
    "Se consolida ADN editorial transversal UnADM aplicable a materia.",
    "Se preservan ejes editoriales estables: problema, marco, analisis, conclusion.",
    "Se refuerza normalizacion JSON y deduplicacion lossless.",
    "Se integra trazabilidad desde actividad no equivalente.",
    "Se crea cerebro editorial minimo con vacios locales abiertos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de asignatura y curso local.",
    "Vincular toda entrega a Licenciatura en Derecho.",
    "Marcar como supuesto cualquier dato no confirmado localmente.",
    "Conservar trazabilidad del nodo origen en herencias transversales."
  ],
  "structure_rules": [
    "Usar esquema estable: problema, conceptos/normas, evidencia, analisis propio, conclusion.",
    "Alinear estructura al producto solicitado por planeacion semanal.",
    "Usar carpeta de materia como punto de entrada canonico.",
    "Separar descripcion de postura argumentada."
  ],
  "activity_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Identificar problema juridico concreto.",
    "Sustentar afirmaciones con norma, doctrina o evidencia verificable.",
    "Incluir postura propia y cierre transferible a la practica profesional.",
    "Declarar limites del analisis cuando falte informacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Confirmar respaldo de toda afirmacion normativa.",
    "Verificar coherencia entre consigna, desarrollo y conclusion.",
    "Revisar y normalizar salidas no estructuradas."
  ],
  "latex_rules": [
    "Mantener plantilla institucional y macros oficiales.",
    "Evitar paquetes o clases no estandar sin justificacion.",
    "Usar acentos correctos en .tex y .bib.",
    "Compilar sin errores criticos ni referencias rotas.",
    "No sustituir macros institucionales por texto libre."
  ],
  "bibliography_rules": [
    "Usar BibTeX local de la asignatura como repositorio principal.",
    "No inventar fuentes; citar solo materiales consultables.",
    "Conservar metadatos minimos completos.",
    "Distinguir bibliografia base de fuentes especificas de actividad.",
    "No reutilizar citas heredadas si no fueron consultadas."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable y gates de calidad.",
    "Aplicar union-dedupe lossless sin eliminar reglas utiles.",
    "Etiquetar herencias como provisionales hasta verificacion local.",
    "Evitar propagar rutas o archivos corruptos sin normalizacion."
  ],
  "open_questions": [
    "Confirmar planeacion oficial y consignas especificas de actividades.",
    "Definir formato uniforme de citas juridicas para la materia.",
    "Confirmar checklist minimo por tipo de producto.",
    "Verificar resolucion definitiva del incidente JSON historico."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico",
        "Claro",
        "Juridicamente preciso",
        "Argumentativo con criterio propio"
      ],
      "institutional": [
        "Alineacion explicita con UnADM",
        "Integridad academica",
        "Citas verificables",
        "Entrada canonica por carpeta de materia"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Semestre 6, bloque 2",
        "Asignatura obligatoria",
        "Transferencia profesional"
      ]
    },
    "essence": [
      "Resolver problemas juridicos con fundamento normativo.",
      "Articular analisis propio sustentado en fuentes.",
      "Cerrar con criterio juridico aplicable."
    ],
    "reason_for_being": [
      "Guiar produccion academica consistente y verificable.",
      "Permitir reutilizacion transversal sin perdida de identidad.",
      "Asegurar calidad editorial institucional."
    ],
    "style_markers": [
      "Supuestos explicitados",
      "Separacion clara entre descripcion y analisis",
      "Conclusiones juridicas accionables",
      "Trazabilidad de fuentes y reglas"
    ],
    "argumentative_patterns": [
      "Problema -> marco normativo/doctrinal -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente -> interpretacion propia.",
      "Consigna -> producto alineado -> validacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema juridico",
        "Marco normativo",
        "Analisis propio",
        "Conclusion juridica",
        "Normalizacion estructurada",
        "Compresion lossless",
        "Trazabilidad editorial"
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
          "justification": "El analisis se activa por una pregunta juridica concreta."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica",
          "kind": "supports",
          "justification": "La conclusion requiere sustento normativo."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay reutilizacion segura."
        },
        {
          "source": "Compresion lossless",
          "target": "Trazabilidad editorial",
          "kind": "supports",
          "justification": "La deduplicacion conserva memoria sin regresion."
        }
      ],
      "evidence": [
        "README y programa analitico de la materia.",
        "Reglas institucionales UnADM heredadas.",
        "Registro de incidentes JSON y gates de bloqueo."
      ]
    },
    "reinforcement_log": [
      "Se preservaron reglas utiles previas sin eliminacion.",
      "Se reforzaron gates de calidad y normalizacion.",
      "Se mejoro claridad del grafo conceptual transversal."
    ]
  }
}
```