{
  "summary": [
    "Se sincroniza transversalmente un nucleo editorial estable entre actividad y materia.",
    "Se preserva identidad UnADM, estructura problema-analisis-conclusion y control de supuestos.",
    "Se refuerza normalizacion obligatoria de salidas no JSON antes de propagacion recursiva.",
    "Se mantiene estrategia conservadora: sin redaccion literal ni fuentes nuevas inventadas."
  ],
  "identity_rules": [
    "Mantener identidad explicita UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de la materia destino en todos los artefactos.",
    "Conservar programa y ubicacion curricular verificada del destino.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Usar carpeta de asignatura como entrada canonica."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar extrapolar fuentes de otras semanas sin validacion.",
    "Vincular el analisis al campo de propiedad y registro cuando corresponda."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que no existan placeholders sin resolver en artefactos LaTeX."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Verificar nombres de archivos en README antes de referenciarlos.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en rutas y nombres.",
    "Actualizar metadatos de actividad en portada antes de entrega."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de actividad en el .bib local de la materia.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferir redaccion literal o datos hiperlocales del origen.",
    "Aplicar union-dedupe sin regresion en cada ciclo.",
    "Mantener vacios locales abiertos cuando falte evidencia del destino."
  ],
  "open_questions": [
    "Confirmar rubrica docente especifica de la materia destino.",
    "Confirmar estilo de citacion juridica requerido por figura docente.",
    "Confirmar producto exacto por actividad (reporte, presentacion u otro).",
    "Confirmar correccion final de placeholders en plantilla (supuesto: aun hay campos por definir)."
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
        "Entrada canonica en carpeta de asignatura."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia destino: Derecho de la propiedad y registro.",
        "Semestre 7, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Fundamento conceptual y normativo pertinente.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible.",
      "Trazabilidad editorial verificable."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos solidos y verificables.",
      "Sostener continuidad institucional entre nodos sin perder contexto local.",
      "Asegurar calidad formal, argumentativa y bibliografica en LaTeX."
    ],
    "style_markers": [
      "Supuestos explicitos cuando falte evidencia.",
      "Secciones funcionales y reutilizables.",
      "Cierre que responde al problema inicial.",
      "Sin afirmaciones factuales sin fuente."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo.",
      "Construir marco conceptual-normativo.",
      "Contrastar fuentes en analisis propio.",
      "Concluir con criterio juridico aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad academica",
        "Citas verificables",
        "Problema juridico",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion JSON previa",
        "Propiedad y registro"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige rigor y trazabilidad."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere una pregunta juridica delimitada."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion valida aplicabilidad profesional."
        },
        {
          "source": "Normalizacion JSON previa",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita propagar reglas ambiguas o corruptas."
        },
        {
          "source": "Propiedad y registro",
          "target": "Problema juridico",
          "kind": "develops",
          "justification": "El foco disciplinar concreta el planteamiento del caso."
        }
      ],
      "evidence": [
        "README de la materia destino: pauta editorial e identidad institucional.",
        "Programa analitico destino: proposito y ejes de trabajo.",
        "Bib local destino: claves institucionales verificables.",
        "Memoria origen: regla estable de normalizacion y estructura argumentativa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: deduplicacion completa de reglas repetidas.",
      "Ciclo 2: transferidas solo abstracciones estables por salto transversal.",
      "Ciclo 2: preservada regla critica de bloqueo por no-JSON.",
      "Ciclo 2: reforzado patron problema-conceptos-analisis-conclusion en materia destino."
    ]
  }
}