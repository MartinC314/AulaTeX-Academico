{
  "summary": [
    "Se consolida memoria lateral de Actividad 5 con transferencia reusable desde Actividad 1.",
    "Se preservan reglas troncales UnADM: identidad institucional, estructura argumentativa y control de calidad.",
    "Se aplica deduplicacion lossless y se eliminan repeticiones semanticas sin recortar contenido util.",
    "Se mantiene restriccion: no copiar conclusiones especificas ni bibliografia exclusiva del nodo hermano.",
    "Se refuerza control de normalizacion JSON parseable antes de propagacion recursiva.",
    "Supuesto: falta consigna y rubrica locales de Actividad 5; se conserva estructura base y preguntas abiertas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y encuadre.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Conservar enfoque juridico-academico con claridad, fundamento y transferencia profesional.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas de modelos como provisionales hasta verificacion local.",
    "No usar memorias de modelo como fuentes academicas citables."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Distinguir explicitamente afirmacion, evidencia e inferencia juridica.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Adaptar el producto al enunciado real de Actividad 5 sin romper reglas de asignatura.",
    "Incluir postura argumentada del estudiante y evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No arrastrar bibliografia de otra semana sin confirmar pertinencia.",
    "Registrar supuesto operativo si hay duda de alcance y continuar con consistencia."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en afirmaciones relevantes.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Rechazar respuestas no estructuradas antes de reutilizar.",
    "Aplicar revision manual extra a memorias con historial de parseo defectuoso."
  ],
  "latex_rules": [
    "Usar acentos y codificacion en espanol de forma consistente en .tex y .bib.",
    "Mantener claves BibTeX estables ya usadas en .tex.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Validar nombres reales de archivos cuando README muestre tokens sin expandir.",
    "Resolver tokens tipo $(@{...}.Slug) en README y programa analitico antes de automatizar rutas.",
    "Supuesto: el .bib canonico esperado es filosofia-del-derecho.bib por Slug."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar en .bib solo fuentes realmente citadas en el texto.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Tratar filosofia-del-derecho-clean.bib como potencialmente tematico de otra semana hasta confirmar pertinencia.",
    "Conservar claves originales cuando ya existan citas activas en el .tex."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones reutilizables: identidad, estructura, calidad, conceptos y relaciones recurrentes.",
    "Evitar regresiones: no eliminar reglas utiles previas.",
    "Agregar solo mejoras verificables por evidencia local.",
    "Si falta consigna local, propagar plantilla base y preguntas abiertas.",
    "No propagar bibliografia exclusiva de un hermano como obligatoria en otro."
  ],
  "open_questions": [
    "Confirmar enunciado especifico de Actividad 5.",
    "Confirmar rubrica de evaluacion de Actividad 5.",
    "Confirmar tipo de producto requerido: reporte, presentacion o recurso visual.",
    "Confirmar si Actividad 5 reutiliza bibliografia existente o requiere .bib propio.",
    "Confirmar nombre canonico final del archivo .bib en README tras resolver token Slug."
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
        "Carpeta de asignatura como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Filosofia del Derecho."
      ]
    },
    "essence": [
      "Problema juridico o social como punto de partida.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto alineado a planeacion semanal.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible a la practica."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables academicos consistentes.",
      "Asegurar trazabilidad entre consigna, evidencia, analisis y cierre.",
      "Garantizar continuidad editorial entre actividades sin contaminar contenido especifico."
    ],
    "style_markers": [
      "Encuadre breve y preciso al inicio.",
      "Secciones funcionales y no ornamentales.",
      "Postura propia sustentada.",
      "Uso explicito de supuestos cuando falte informacion.",
      "Cierre con transferencia profesional."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual o normativo -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> inferencia juridica.",
      "Contraste doctrinal breve -> toma de postura.",
      "Regla general -> aplicacion al caso -> implicacion practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Problema juridico",
        "Marco normativo/doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion JSON",
        "Consistencia cita-.bib",
        "Bibliografia base vs bibliografia especifica"
      ],
      "citations": [
        "README.md",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Estructura de actividad",
          "kind": "supports",
          "justification": "La pauta institucional define tono, forma y criterio de cierre."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin problema delimitado no hay argumentacion dirigida."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica exige respaldo trazable."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia confiable."
        },
        {
          "source": "Bibliografia especifica de actividad",
          "target": "Bibliografia base",
          "kind": "contrasts",
          "justification": "La base orienta; la especifica responde a la consigna concreta."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad academica, citas verificables y conclusion juridica propia.",
        "Programa analitico: ejes problema-conceptos-fuentes-analisis-cierre.",
        "Historial de parseo: necesidad de gate estricto JSON."
      ]
    },
    "reinforcement_log": [
      "Ciclo 25: se deduplican reglas repetidas y se conserva totalidad util.",
      "Ciclo 25: se refuerza transferencia lateral por patrones, no por contenido especifico.",
      "Ciclo 25: se mantiene bandera de riesgo por salidas no parseables historicas.",
      "Ciclo 25: se preserva separacion entre bibliografia base y bibliografia por actividad.",
      "Ciclo 25: se agregan supuestos explicitos donde falta consigna local verificable."
    ]
  }
}