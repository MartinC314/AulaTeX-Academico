{
  "summary": [
    "Se consolida memoria lateral para actividad-3 con transferencia reusable desde actividad-1, sin copiar contenido especifico.",
    "Se preserva identidad UnADM y contexto curricular verificado: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se refuerzan ejes editoriales estables: problema, conceptos/fuentes, analisis propio y conclusion juridica transferible.",
    "Se mantiene normalizacion estructurada obligatoria y bloqueo de propagacion sin JSON parseable.",
    "Se aplico deduplicacion lossless y no regresion de reglas utiles.",
    "Se marca como supuesto toda inferencia no confirmada por consigna local de actividad-3."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y criterios de integridad academica.",
    "Vincular actividad-3 a Licenciatura en Derecho, asignatura Filosofia del Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Tratar memorias editoriales externas como antecedente provisional, no como fuente academica.",
    "Marcar como supuesto cualquier dato no visible en la consigna local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear el tipo de producto a la planeacion semanal confirmada.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Heredar solo patrones reutilizables de actividad-1: identidad, estructura, calidad y metodo argumentativo.",
    "No copiar redaccion literal, conclusiones especificas ni bibliografia exclusiva del nodo hermano.",
    "Incluir postura argumentada del estudiante y evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Si falta consigna local, usar estructura base y registrar supuestos explicitos."
  ],
  "quality_gates": [
    "Bloquear guardado y propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizacion recursiva.",
    "Confirmar trazabilidad entre afirmaciones, citas en texto y .bib.",
    "Distinguir evidencia academica de antecedentes editoriales.",
    "Aplicar no regresion: no eliminar reglas utiles previas."
  ],
  "latex_rules": [
    "Mantener codificacion y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves citadas.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y referencias de archivos.",
    "Corregir rutas o nombres solo con verificacion local."
  ],
  "bibliography_rules": [
    "No inventar fuentes ni referencias.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Agregar al .bib solo entradas realmente citadas por la actividad.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de asignatura y bibliografia especifica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib puede no corresponder a actividad-3; validar antes de usar."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validacion de JSON y estructura.",
    "Transferir a nodos hermanos solo reglas generales y patrones argumentativos estables.",
    "No propagar supuestos como hechos confirmados.",
    "Conservar bandera de riesgo cuando existan antecedentes de parseo defectuoso.",
    "Aplicar union-deduplicacion lossless en cada ciclo."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-3.",
    "Confirmar formato requerido de entrega: reporte, presentacion u otro.",
    "Confirmar rubrica especifica de evaluacion para calibrar profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana de actividad-3.",
    "Confirmar si aplica o no la bibliografia depurada de Semana 7.",
    "Confirmar nombre canonico final del .bib operativo para actividad-3."
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
        "Asignatura: Filosofia del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos con fundamento juridico y claridad.",
      "Estandarizar calidad editorial sin perder especificidad de cada actividad.",
      "Garantizar trazabilidad entre afirmaciones, evidencia y cierre argumentativo."
    ],
    "style_markers": [
      "Encuadre inicial breve y enfocado.",
      "Secciones explicitas y orden logico.",
      "Supuestos etiquetados cuando falte evidencia local.",
      "Citas verificables en afirmaciones sustantivas.",
      "Cierre juridico aplicable a practica profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/marco -> analisis propio -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> postura.",
      "Objetivo declarado -> desarrollo coherente -> cierre consistente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad academica",
        "Normalizacion JSON",
        "Problema juridico",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Bibliografia verificable",
        "Supuestos explicitados"
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
          "justification": "La pauta institucional exige evidencia verificable y criterio propio."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Integridad academica",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay memoria confiable ni trazable."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El analisis parte de un problema delimitado."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion depende de argumentacion sustentada."
        },
        {
          "source": "Bibliografia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura requiere respaldo documental verificable."
        }
      ],
      "evidence": [
        "README confirma identidad UnADM, integridad academica y conclusion juridica con criterio propio.",
        "Programa analitico fija ejes de trabajo y proposito de transformacion del producto.",
        "Regla persistente de bloqueo sin JSON parseable se mantiene activa.",
        "Token Slug sin expandir detectado; requiere normalizacion tecnica."
      ]
    },
    "reinforcement_log": [
      "Ciclo 51: deduplicacion completa de reglas repetidas en destino.",
      "Ciclo 51: refuerzo lateral de estructura argumentativa base desde actividad-1.",
      "Ciclo 51: preservacion de no regresion y de validacion JSON obligatoria.",
      "Ciclo 51: mantenimiento de politica de supuestos para datos no confirmados."
    ]
  }
}