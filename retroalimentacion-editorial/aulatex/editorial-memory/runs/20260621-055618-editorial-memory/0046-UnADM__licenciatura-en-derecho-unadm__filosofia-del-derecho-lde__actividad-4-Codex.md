{
  "summary": [
    "Se consolida memoria lateral para Actividad 4 con deduplicacion lossless y sin recorte util.",
    "Se preserva identidad UnADM y marco curricular verificado: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se refuerza normalizacion estructurada y validacion JSON estricta antes de cualquier propagacion.",
    "Se transfieren solo patrones reutilizables de estructura, calidad, estilo y argumentacion.",
    "Supuesto: la consigna especifica de Actividad 4 no esta visible; no fijar contenido tematico cerrado."
  ],
  "identity_rules": [
    "Mantener tono formal academico y precision juridica.",
    "Alinear la actividad a Licenciatura en Derecho y Filosofia del Derecho.",
    "Conservar integridad academica con trazabilidad de fuentes.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memorias heredadas no verificadas como provisionales hasta confirmacion local.",
    "Vincular ubicacion curricular a malla-curricular-derecho-unadm.pdf."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Separar hechos, conceptos, argumentos y postura personal.",
    "Alinear el formato final al producto pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Seguir los cinco ejes del programa analitico como columna de desarrollo.",
    "Incluir postura argumentada del estudiante; evitar resumen descriptivo puro.",
    "Sustentar afirmaciones con cita explicita y verificable.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No trasladar conclusiones especificas de Actividad 1 a Actividad 4.",
    "No asumir que bibliografia de Semana 7 aplica automaticamente a Actividad 4."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Exigir estructura minima completa antes de reutilizar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de integrarlas.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y claves del .bib.",
    "Validar correspondencia del producto con la consigna local de Actividad 4."
  ],
  "latex_rules": [
    "Mantener acentos y codificacion correcta en espanol en .tex y .bib.",
    "Citar solo claves existentes en el .bib activo.",
    "No renombrar claves BibTeX ya usadas en documentos activos.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, referencias rotas ni archivos faltantes.",
    "Verificar nombres reales de archivos cuando README tenga tokens sin resolver.",
    "Resolver o sustituir tokens tipo $(@{...}.Slug) antes de automatizar rutas."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables (UnADM, SCJN, UNAM-IIJ).",
    "Registrar fuentes especificas de la actividad en el .bib de la asignatura.",
    "No inventar referencias ni metadatos faltantes.",
    "Conservar metadatos minimos: autor, titulo, ano, editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Usar filosofia-del-derecho-clean.bib solo si coincide con la consigna vigente.",
    "Mantener claves estables para evitar rotura de compilacion."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Reforzar en nodos hermanos reglas institucionales, no contenido tematico puntual.",
    "Aplicar union-dedupe para compresion lossless sin eliminar reglas utiles previas.",
    "Evitar regresiones en gates de calidad ya consolidados.",
    "Si falta consigna local, propagar plantilla base y preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de Actividad 4: producto, extension y criterios.",
    "Confirmar rubrica docente especifica para calibrar profundidad argumentativa.",
    "Confirmar nombre canonico final del .bib cuando el token Slug no esta resuelto.",
    "Confirmar si Actividad 4 reutiliza bibliografia existente o requiere bloque nuevo.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a Semana 7; verificar aplicabilidad en Actividad 4."
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
        "Integridad academica y citas verificables",
        "Entrada canonica en carpeta de asignatura"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Filosofia del Derecho",
        "Semestre 1, bloque 2, obligatoria, 8 creditos"
      ]
    },
    "essence": [
      "Problema juridico o social",
      "Conceptos y marco normativo",
      "Evidencia verificable",
      "Analisis propio",
      "Conclusion juridica transferible"
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros y fundados",
      "Sostener trazabilidad editorial y tecnica en LaTeX",
      "Garantizar coherencia entre identidad institucional y argumentacion juridica"
    ],
    "style_markers": [
      "Objetivo explicito al inicio",
      "Secciones funcionales y ordenadas",
      "Cita explicita en afirmaciones relevantes",
      "Marcado de supuestos cuando falten datos locales"
    ],
    "argumentative_patterns": [
      "Plantear problema",
      "Definir marco conceptual y normativo",
      "Contrastar evidencia con analisis propio",
      "Emitir postura justificada",
      "Concluir con aplicacion juridica"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON estricta",
        "Integridad academica",
        "Relacion problema-evidencia-conclusion",
        "Ejes del programa analitico"
      ],
      "citations": [
        "README.md de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Tono formal academico",
          "kind": "supports",
          "justification": "La pauta editorial exige alineacion institucional explicita."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay reutilizacion segura."
        },
        {
          "source": "Ejes del programa analitico",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Los ejes definen el orden del desarrollo argumentativo."
        },
        {
          "source": "Integridad academica",
          "target": "Conclusion juridica propia",
          "kind": "supports",
          "justification": "La conclusion valida requiere evidencia verificable y postura propia."
        }
      ],
      "evidence": [
        "README fija identidad UnADM, entrada canonica y criterio de conclusion juridica.",
        "Programa analitico define cinco ejes reutilizables.",
        "Historial de salidas no parseables justifica gate de JSON estricto."
      ]
    },
    "reinforcement_log": [
      "Ciclo 46: deduplicacion semantica aplicada sin perdida de reglas utiles.",
      "Ciclo 46: se eliminaron traslados literales de contenido especifico entre hermanos.",
      "Ciclo 46: se fortalecio separacion entre patrones transferibles y datos dependientes de consigna.",
      "Ciclo 46: se mantuvo bandera de supuestos para vacios locales."
    ]
  }
}