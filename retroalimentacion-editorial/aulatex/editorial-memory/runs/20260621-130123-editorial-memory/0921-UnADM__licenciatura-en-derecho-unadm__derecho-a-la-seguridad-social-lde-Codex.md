{
  "summary": [
    "Se mantiene sincronizacion transversal conservadora entre nodos no equivalentes.",
    "Se preserva identidad UnADM y estructura por ejes sin transferir contenido tematico de Filosofia del Derecho.",
    "Se refuerza control de calidad: JSON parseable, normalizacion previa y trazabilidad de supuestos.",
    "Se consolida compresion lossless por union-dedupe sin regresion.",
    "Se actualiza estructura canonica local con plantillas de Actividad 1 declaradas en README."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas utiles previas; aplicar union-dedupe sin recorte."
  ],
  "structure_rules": [
    "Tomar README y programa analitico del destino como canon estructural.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Organizar desarrollo en: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato y alcance al producto solicitado por la planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion, actividad y bibliografia local."
  ],
  "activity_rules": [
    "Delimitar problema y pregunta guia desde el inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Incluir postura argumentada del estudiante; evitar entregas solo descriptivas.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Verificar correspondencia exacta entre consigna y tipo de producto."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de propagacion recursiva.",
    "Confirmar que toda afirmacion tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Verificar no regresion: ninguna regla util previa puede eliminarse."
  ],
  "latex_rules": [
    "Conservar plantilla base y personalizar solo campos variables.",
    "Mantener codificacion correcta de espanol en .tex y .bib.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion tecnica.",
    "Normalizar nombres de archivo y resolver marcadores/tokens corruptos antes de compilar.",
    "Reconocer como canonicos los archivos de Actividad 1 listados en README."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "No inventar referencias; usar solo fuentes consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Agregar solo referencias especificas de actividad con verificacion local.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion."
  ],
  "propagation_hints": [
    "Propagar lateral y arriba solo reglas estables y abstractas.",
    "No transferir redaccion literal ni contenido tematico exclusivo de Filosofia del Derecho.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual comun.",
    "Mantener bandera historica: ciclo 1 requiere normalizacion manual si se reutiliza.",
    "Aplicar estrategia progresiva y conservadora en cada ciclo.",
    "Si falta contexto local en nodos hijos, crear cerebro minimo y abrir vacios."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida en la materia (APA, ISO, institucional o juridica mexicana) [supuesto].",
    "Confirmar si codigo local LDE-S2B1 sigue vigente en documentos evaluables [supuesto].",
    "Confirmar si figura docente debe permanecer como pendiente en plantillas base [supuesto].",
    "Verificar vigencia semestral de URLs legales en .bib antes de entrega final.",
    "Confirmar rubrica oficial por actividad para ajustar profundidad argumentativa."
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
        "Materia destino: Derecho a la Seguridad Social.",
        "Semestre 2, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Fundamento normativo verificable.",
      "Evidencia trazable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar cada consigna en producto juridico verificable y util profesionalmente.",
      "Preservar memoria editorial persistente sin perdida y sin regresion."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiqueta explicita de [supuesto].",
      "Separacion clara entre marco, analisis y cierre.",
      "Trazabilidad de decisiones editoriales."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo y doctrinal pertinente.",
      "Contrastar evidencia.",
      "Fijar postura propia sustentada.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "JSON parseable",
        "Normalizacion estructurada",
        "Compresion union-dedupe",
        "Problema juridico",
        "Marco normativo",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Bibliografia local verificable"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024",
        "cpeum2026",
        "lss2026",
        "lissste2026"
      ],
      "relations": [
        {
          "source": "JSON parseable",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay reutilizacion segura."
        },
        {
          "source": "Compresion union-dedupe",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Conserva reglas utiles sin duplicar ni recortar."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis exige una pregunta delimitada."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida requiere fundamento legal."
        },
        {
          "source": "Bibliografia local verificable",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "Las citas deben existir en .bib local."
        }
      ],
      "evidence": [
        "README destino define estructura canonica y archivos de Actividad 1.",
        "Programa analitico destino fija proposito y ejes juridicos.",
        "derecho-a-la-seguridad-social.bib contiene base institucional y normativa verificable.",
        "Regla historica vigente: normalizar salidas no parseables antes de propagacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 11: se refuerza transferencia transversal por abstracciones estables.",
      "Ciclo 11: se preservan reglas locales del destino y se evita mezcla tematica con origen.",
      "Ciclo 11: se integra canonicidad de plantillas Actividad 1 desde README.",
      "Ciclo 11: se mantiene control estricto de JSON, supuestos y no regresion."
    ]
  }
}