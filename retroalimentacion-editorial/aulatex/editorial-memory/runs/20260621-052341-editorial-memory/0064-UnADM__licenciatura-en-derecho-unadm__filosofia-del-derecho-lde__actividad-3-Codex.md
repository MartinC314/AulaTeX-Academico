{
  "summary": [
    "Se consolida refuerzo lateral de actividad-1 a actividad-3 con deduplicacion lossless.",
    "Se preserva identidad UnADM y contexto curricular verificado en README y programa analitico.",
    "Se mantienen ejes editoriales estables: problema, conceptos/fuentes, analisis propio y conclusion juridica.",
    "Se conserva regla critica: no propagar sin JSON parseable ni estructura minima valida.",
    "Se mantiene politica de supuestos para datos no visibles en la consigna local.",
    "Se evita transferencia de redaccion literal, conclusiones especificas y bibliografia exclusiva del hermano."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no confirmado en la consigna local.",
    "Tratar memorias editoriales Codex/GPT-Pro como antecedente provisional, no como fuente academica.",
    "Usar malla-curricular-derecho-unadm.pdf solo para ubicacion curricular."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato pedido en la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Si falta consigna local, usar estructura base y marcar supuestos."
  ],
  "activity_rules": [
    "Heredar solo patrones reutilizables de actividad-1.",
    "No copiar redaccion literal ni conclusiones especificas entre hermanos.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir semana, consigna o formato de actividad-3 sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado y propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar aguas abajo.",
    "Confirmar trazabilidad entre afirmaciones y fuentes citadas.",
    "Exigir marca de supuesto en toda afirmacion no verificada localmente.",
    "Aplicar no regresion: no eliminar reglas utiles previas.",
    "Distinguir evidencia academica de antecedentes editoriales."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre citas en .tex y claves BibTeX.",
    "No renombrar claves bibliograficas ya usadas.",
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico antes de automatizar rutas.",
    "Supuesto: archivo .bib canonico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Agregar al .bib solo entradas realmente citadas en la actividad.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Mantener URLs verificables cuando existan.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No usar memoria editorial como bibliografia academica.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a interpretacion juridica (Semana 7) y su uso en actividad-3 debe confirmarse."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validacion de JSON y estructura.",
    "Propagar a hermanos solo reglas generales y estables.",
    "No propagar supuestos como hechos confirmados.",
    "Aplicar union-dedupe lossless en cada ciclo.",
    "Conservar bandera de riesgo cuando existan incidencias previas de parseo.",
    "Si falta consigna local, propagar plantilla estructural y preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-3.",
    "Confirmar formato de entrega requerido en actividad-3.",
    "Confirmar rubrica de evaluacion especifica de actividad-3.",
    "Confirmar bibliografia obligatoria de la semana de actividad-3.",
    "Confirmar si actividad-3 trata interpretacion juridica o otro tema.",
    "Confirmar archivo .tex principal canonico para actividad-3."
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
      "Problema juridico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto alineado a planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos con fundamento juridico y evidencia.",
      "Asegurar consistencia editorial institucional entre actividades de la misma asignatura.",
      "Garantizar trazabilidad entre argumento, evidencia y cierre juridico."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones explicitas con orden logico.",
      "Citas verificables en afirmaciones clave.",
      "Supuestos marcados de forma transparente.",
      "Cierre juridico aplicable a practica profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/marco -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> postura.",
      "Objetivo declarado -> desarrollo coherente -> cierre consistente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalizacion JSON",
        "Integridad academica",
        "Problema juridico",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Bibliografia verificable",
        "Politica de supuestos"
      ],
      "citations": [
        "README.md de la asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib [supuesto condicionado]"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige rigor de citas y coherencia formal."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay transferencia confiable."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El analisis se construye desde un problema delimitado."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion depende de argumentacion sustentada."
        },
        {
          "source": "Politica de supuestos",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita presentar inferencias como hechos."
        }
      ],
      "evidence": [
        "README: identidad UnADM, citas verificables y conclusion juridica propia.",
        "Programa analitico: ejes problema-conceptos-producto-analisis-conclusion.",
        "Regla persistente: bloqueo por salida no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 64: deduplicacion integral sin perdida semantica.",
      "Ciclo 64: refuerzo lateral de patrones reutilizables desde hermano actividad-1.",
      "Ciclo 64: se mantiene no regresion y politica de supuestos.",
      "Ciclo 64: se conserva separacion entre memoria editorial y evidencia academica."
    ]
  }
}