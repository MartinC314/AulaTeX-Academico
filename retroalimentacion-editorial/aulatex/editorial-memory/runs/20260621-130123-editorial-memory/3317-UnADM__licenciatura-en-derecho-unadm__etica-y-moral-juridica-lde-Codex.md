{
  "summary": [
    "Sincronizacion transversal consolidada entre Filosofia del Derecho y Etica y Moral juridica con estrategia conservadora.",
    "Se preservan reglas estables: identidad UnADM, estructura por ejes, evidencia verificable, analisis propio y conclusion juridica transferible.",
    "Se mantiene compresion lossless por union-dedupe sin regresion y sin recorte de reglas utiles.",
    "Se refuerza gate critico: no propagar si salida no es JSON parseable y normalizar herencias no estructuradas.",
    "Se mantiene separacion tematica: transferir abstracciones editoriales, no literalidad disciplinar."
  ],
  "identity_rules": [
    "Conservar tono formal academico alineado a UnADM.",
    "Anclar contexto curricular en Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica editorial.",
    "Marcar como supuesto todo dato no visible en consigna o fuente local.",
    "Mantener integridad academica con citas verificables y trazables.",
    "Tratar herencias Codex o GPT-Pro como provisionales hasta verificacion local.",
    "Aterrizar analisis en contexto juridico mexicano cuando aplique."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en bloques: conceptos clave, fundamento normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener trazabilidad entre actividad, reporte y presentacion."
  ],
  "activity_rules": [
    "Distinguir hechos, valores, normas, doctrina y postura propia.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Evitar entregas solo descriptivas; exigir postura argumentada.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Verificar correspondencia exacta entre consigna y producto entregable.",
    "Vincular conceptos eticos y morales con implicaciones juridicas concretas."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizacion.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no se eliminen reglas utiles previas en consolidacion.",
    "Comprobar deduplicacion semantica sin perdida de contenido valido.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar que cada afirmacion tenga respaldo o marca de supuesto."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en espanol en .tex y .bib.",
    "Mantener compatibilidad con reporte-etica-y-moral-juridica.tex y presentacion-etica-y-moral-juridica.tex.",
    "Usar secciones claras para problema, desarrollo, analisis y conclusion.",
    "Evitar comandos o paquetes no justificados por plantilla local.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Corregir placeholders de slug sin expandir en README y programa analitico.",
    "Corregir nombres de archivo corruptos antes de automatizar validaciones."
  ],
  "bibliography_rules": [
    "Usar etica-y-moral-juridica.bib como repositorio local de referencias de materia.",
    "No inventar fuentes ni metadatos faltantes.",
    "Registrar metadatos minimos: autor o editor, titulo, anio, fuente editorial o URL.",
    "Depurar duplicados por clave o por equivalencia autor-titulo-anio.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Completar entradas truncadas antes de citarlas [supuesto: sierraUniversidadNacional1910 incompleta]."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas abstractas y estables entre nodos no equivalentes.",
    "No trasladar contenido tematico literal de Filosofia del Derecho al nodo etico-moral.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Mantener estrategia progresiva: integrar mejoras verificables por ciclo.",
    "Mantener estrategia conservadora: evitar regresiones y cambios no validados localmente.",
    "Marcar toda herencia externa como provisional hasta confirmacion documental local."
  ],
  "open_questions": [
    "Confirmar plantilla LaTeX obligatoria especifica de la materia.",
    "Confirmar criterio final de deduplicacion bibliografica: clave, DOI o autor+titulo+anio.",
    "Confirmar si se conservaran alias historicos al unificar claves BibTeX duplicadas.",
    "Confirmar correccion permanente de placeholders de slug a etica-y-moral-juridica.bib en README y programa.",
    "Confirmar integridad de entradas .bib truncadas antes de siguiente ciclo."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Etico sin moralismo declarativo."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Normalizacion estructurada obligatoria antes de propagacion.",
        "Integridad academica con trazabilidad de fuentes.",
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2.",
        "Obligatoria, 8 creditos.",
        "Sincronizacion transversal sin fusion tematica."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y fundamento normativo-doctrinal.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y verificables.",
      "Sostener criterio juridico propio con base etica y documental."
    ],
    "style_markers": [
      "Frases claras y accionables.",
      "Supuestos marcados de forma explicita.",
      "Sin afirmaciones sin respaldo.",
      "Cierre con implicacion profesional concreta."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Delimitacion conceptual antes de valorar casos.",
      "Contraste entre marco normativo y postura propia.",
      "Sintesis final con transferencia a practica juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Integridad academica",
        "Normalizacion estructurada",
        "JSON parseable",
        "Deduplicacion lossless",
        "Problema juridico o social",
        "Fundamento normativo y doctrinal",
        "Etica y moral juridica",
        "Postura argumentada",
        "Conclusion transferible"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/programa-analitico-etica-y-moral-juridica.md",
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/etica-y-moral-juridica.bib"
      ],
      "relations": [
        {
          "source": "Integridad academica",
          "target": "Evidencia verificable",
          "kind": "depends_on",
          "justification": "La validez editorial requiere respaldo trazable."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay reutilizacion segura."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "Delimita alcance y pertinencia argumentativa."
        },
        {
          "source": "Fundamento normativo y doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La transferencia profesional exige base juridica explicita."
        },
        {
          "source": "Etica y moral juridica",
          "target": "Filosofia del Derecho",
          "kind": "contrasts",
          "justification": "Comparten base teorica pero difieren en foco aplicado."
        },
        {
          "source": "Deduplicacion lossless",
          "target": "Memoria persistente",
          "kind": "develops",
          "justification": "Conserva reglas utiles sin inflacion ni perdida."
        }
      ],
      "evidence": [
        "README local fija identidad UnADM y conclusion juridica propia.",
        "Programa analitico local fija ejes de trabajo reutilizables.",
        "Memoria origen confirma gates de parseo JSON y normalizacion previa.",
        "Bibliografia local evidencia duplicados y una entrada truncada [supuesto confirmado por texto visible]."
      ]
    },
    "reinforcement_log": [
      "Ciclo 16: se refuerzan reglas estables transversales sin fusion tematica.",
      "Ciclo 16: se conserva gate de JSON parseable como bloqueo duro de propagacion.",
      "Ciclo 16: se integra eje problema-conceptos-evidencia-analisis-conclusion como patron comun.",
      "Ciclo 16: se mantienen fuentes heredadas no verificadas en estado provisional."
    ]
  }
}