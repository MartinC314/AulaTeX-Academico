{
  "summary": [
    "Sincronizacion transversal ciclo 2 aplicada con estrategia progresiva y conservadora.",
    "Se preserva identidad UnADM y contexto curricular local de Etica y Moral Juridica.",
    "Se refuerza patron reusable: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se conserva compresion lossless por union y deduplicacion semantica sin recorte.",
    "Se integran alertas tecnicas verificables: placeholders de slug y nombres de archivo corruptos en README.",
    "Se mantienen fuentes heredadas no verificadas como provisionales con marca explicita."
  ],
  "identity_rules": [
    "Mantener voz academica formal alineada a UnADM.",
    "Anclar cada entrega a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica editorial.",
    "Aterrizar analisis en contexto juridico mexicano cuando aplique.",
    "Marcar como supuesto todo dato no visible en consigna o fuente local.",
    "Tratar herencias de Codex y GPT-Pro como provisionales hasta verificacion local.",
    "No transferir literalidad entre materias; transferir abstracciones estables."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto pedido en planeacion semanal.",
    "Mantener trazabilidad entre consigna, desarrollo, evidencia y conclusion.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Explicitar problema, pregunta guia y alcance en cada actividad.",
    "Distinguir hechos, valores, normas, doctrina y postura propia.",
    "Vincular conceptos eticos y morales con implicaciones juridicas concretas.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Verificar correspondencia exacta entre producto entregado y consigna local."
  ],
  "quality_gates": [
    "Bloquear propagacion si salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de consolidar.",
    "Confirmar que no se eliminen reglas utiles previas en cada ciclo.",
    "Comprobar deduplicacion semantica sin perdida de contenido valido.",
    "Exigir respaldo o marca de supuesto en cada afirmacion sensible.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar compilacion o parseo de .tex y .bib sin errores criticos."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener consistencia de titulos, etiquetas y nombres de archivo.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver placeholders de slug sin expandir en README y programa analitico.",
    "Corregir rutas o nombres corruptos antes de automatizar validaciones.",
    "Mantener claves BibTeX estables para evitar roturas en citas.",
    "Compilar sin referencias rotas ni warnings criticos."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de actividad en etica-y-moral-juridica.bib.",
    "No inventar referencias ni metadatos faltantes.",
    "Conservar metadatos minimos: autor o editor, titulo, anio, fuente editorial o URL.",
    "Depurar duplicados por clave o equivalencia autor-titulo-anio.",
    "Unificar duplicados detectados: Huerta 2000, Ronquillo 2018, Singer 1995.",
    "Completar entradas truncadas antes de citarlas."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Compartir entre nodos no equivalentes solo reglas editoriales estables.",
    "Priorizar identidad, estructura reusable, gates y grafo conceptual.",
    "Evitar transferir redaccion literal o contenidos tematicos hiperlocales.",
    "Mantener alerta: ciclos previos con salida no estructurada requieren normalizacion manual.",
    "Evitar regresiones frente a reglas utiles ya consolidadas."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de actividades locales futuras; confirmar formato exigido por semana.",
    "Confirmar criterio final de deduplicacion bibliografica operativo.",
    "Confirmar politica de alias BibTeX al unificar claves historicas.",
    "Supuesto: placeholder de slug debe sustituirse de forma permanente por etica-y-moral-juridica.bib.",
    "Confirmar correccion definitiva de nombres corruptos en README.",
    "Confirmar completado de la entrada truncada sierraUniversidadNacional1910."
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
        "Normalizacion estructurada obligatoria antes de propagacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Materia: Etica y Moral Juridica."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco aplicable.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y utiles para practica juridica.",
      "Asegurar coherencia entre consigna, argumentacion, evidencia y cierre.",
      "Sostener identidad institucional sin perder adaptacion local de materia."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Objetivo explicito antes del desarrollo.",
      "Secciones funcionales y trazables.",
      "Supuestos marcados de forma visible.",
      "Cierre con postura juridica propia."
    ],
    "argumentative_patterns": [
      "Plantear problema y pregunta guia.",
      "Definir conceptos y marco normativo o doctrinal.",
      "Contrastar evidencia y fuentes.",
      "Desarrollar postura propia razonada.",
      "Concluir con implicacion practica juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad academica",
        "Normalizacion JSON",
        "Problema juridico-social",
        "Analisis propio",
        "Conclusion juridica",
        "Etica juridica",
        "Moral juridica",
        "Trazabilidad editorial",
        "Deduplicacion lossless"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
        "etica-y-moral-juridica.bib"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige formato consistente y citas verificables."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Trazabilidad editorial",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay propagacion confiable."
        },
        {
          "source": "Problema juridico-social",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El analisis nace de un problema delimitado."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica",
          "kind": "supports",
          "justification": "La conclusion valida depende de razonamiento y evidencia."
        },
        {
          "source": "Etica juridica",
          "target": "Moral juridica",
          "kind": "contrasts",
          "justification": "Distinguir planos evita ambiguedad conceptual."
        }
      ],
      "evidence": [
        "README local confirma identidad UnADM y ubicacion curricular.",
        "Programa analitico local confirma ejes de trabajo y proposito editorial.",
        "Bibliografia local muestra duplicados y una entrada truncada verificable.",
        "Historial heredado confirma necesidad de normalizacion por salidas no parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: se consolida patron transversal estable sin trasladar literalidad de Filosofia del Derecho.",
      "Ciclo 2: se refuerzan gates de parseo JSON, estructura minima y no regresion.",
      "Ciclo 2: se mantienen alertas tecnicas de slug placeholder y nombres corruptos en README.",
      "Ciclo 2: se preservan reglas bibliograficas de no invencion y deduplicacion verificable."
    ]
  }
}