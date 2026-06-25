{
  "summary": [
    "Se sincroniza memoria transversal desde actividad de Filosofia del Derecho hacia materia de Etica y Moral juridica sin trasladar literalidad tematica.",
    "Se conserva identidad UnADM, estructura canonica y ejes editoriales reutilizables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se refuerza control de calidad: JSON parseable, normalizacion previa y deduplicacion lossless sin regresion.",
    "Se mantiene enfoque conservador: herencias no verificadas siguen provisionales hasta confirmacion local.",
    "Se prioriza adaptacion etico-moral juridica en contexto mexicano."
  ],
  "identity_rules": [
    "Mantener voz formal academica alineada a UnADM.",
    "Anclar toda entrega a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "No transferir contenido tematico literal de Filosofia del Derecho al nodo etico-moral."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto pedido por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener trazabilidad entre actividad, reporte y presentacion."
  ],
  "activity_rules": [
    "Vincular conceptos eticos y morales con implicaciones juridicas concretas.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Distinguir hechos, valores, normas, doctrina y postura propia.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Verificar correspondencia exacta entre consigna y entregable."
  ],
  "quality_gates": [
    "Bloquear propagacion si salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no se eliminen reglas utiles previas en consolidacion.",
    "Comprobar deduplicacion semantica sin recorte de contenido valido.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en .tex y .bib.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Mantener claves BibTeX estables durante limpieza de duplicados.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Corregir placeholders de slug sin expandir en README y programa analitico.",
    "Corregir nombres de archivo corruptos antes de automatizar validaciones."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas por actividad en etica-y-moral-juridica.bib.",
    "No inventar referencias ni metadatos faltantes.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Depurar duplicados por clave o contenido equivalente con criterio explicito.",
    "Completar entradas truncadas antes de citarlas."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables en saltos transversales.",
    "Priorizar identidad, estructura reusable, gates y grafo conceptual.",
    "Evitar propagar redaccion literal o ejemplos tematicos de otra materia.",
    "Mantener estrategia progresiva y conservadora en ciclos recursivos.",
    "Aplicar normalizacion manual cuando la herencia llegue incompleta.",
    "Marcar como provisional cualquier herencia cruzada no verificada."
  ],
  "open_questions": [
    "Supuesto: falta confirmacion de rubricas especificas de Etica y Moral juridica por actividad.",
    "Confirmar criterio final de deduplicacion bibliografica: clave, DOI o titulo+autor+anio.",
    "Confirmar politica de alias BibTeX historicos tras fusion de duplicados.",
    "Confirmar si existe plantilla LaTeX obligatoria adicional a reporte/presentacion.",
    "Supuesto: el placeholder de slug debe fijarse permanentemente a etica-y-moral-juridica.bib.",
    "Confirmar cierre de la entrada truncada sierraUniversidadNacional1910 en .bib."
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
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Materia: Etica y Moral juridica."
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
      "Convertir planeacion semanal en productos academicos trazables y argumentados.",
      "Asegurar coherencia entre consigna, desarrollo y cierre profesional.",
      "Preservar memoria editorial util sin perdida ni regresion."
    ],
    "style_markers": [
      "Frases claras y accionables.",
      "Supuestos marcados de forma explicita.",
      "Sin afirmaciones sin respaldo.",
      "Cierre con implicacion profesional.",
      "Adaptacion local antes de reutilizacion transversal."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Delimitacion conceptual antes de valorar casos.",
      "Contraste entre marco normativo y postura propia.",
      "Sintesis final con transferencia a practica juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalizacion estructurada",
        "JSON parseable",
        "Deduplicacion lossless",
        "Integridad academica",
        "Citas verificables",
        "Etica y moral juridica",
        "Conclusion transferible"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
        "etica-y-moral-juridica.bib"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay reutilizacion segura."
        },
        {
          "source": "Deduplicacion lossless",
          "target": "Memoria persistente",
          "kind": "supports",
          "justification": "Conserva reglas utiles sin inflar ni recortar."
        },
        {
          "source": "Integridad academica",
          "target": "Citas verificables",
          "kind": "depends_on",
          "justification": "La validez academica exige trazabilidad de fuentes."
        },
        {
          "source": "Etica y moral juridica",
          "target": "Filosofia del Derecho",
          "kind": "contrasts",
          "justification": "Comparten base teorica, pero difieren en foco aplicado."
        },
        {
          "source": "Problema juridico o social",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion surge del analisis delimitado por el problema."
        }
      ],
      "evidence": [
        "README de materia con pauta editorial UnADM.",
        "Programa analitico con ejes de trabajo reutilizables.",
        "Regla persistente: bloquear salida no JSON parseable.",
        "Regla persistente: normalizar respuestas no estructuradas.",
        "Bibliografia local con duplicados y una entrada truncada."
      ]
    },
    "reinforcement_log": [
      "Ciclo 3: se consolida transferencia transversal estable sin recorte.",
      "Ciclo 3: se refuerzan gates de parseo, normalizacion y no regresion.",
      "Ciclo 3: se preserva identidad UnADM y contexto curricular local.",
      "Ciclo 3: se mantiene separacion entre abstracciones transferibles y contenido tematico local.",
      "Ciclo 3: se sostienen vacios locales como preguntas abiertas con supuestos marcados."
    ]
  }
}