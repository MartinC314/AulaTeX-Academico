{
  "summary": [
    "Consolidacion lateral aplicada con union y deduplicacion sin perdida entre actividades hermanas.",
    "Se preserva identidad UnADM y ubicacion curricular verificada: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se refuerza pauta transversal: problema, conceptos o normas, producto, analisis propio y conclusion juridica transferible.",
    "Se mantiene regla critica de normalizar salidas no estructuradas antes de propagar.",
    "Supuesto: la consigna especifica de actividad 6 no esta visible; se conserva estructura base reusable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear contenido a Licenciatura en Derecho, asignatura Filosofia del Derecho.",
    "Reconocer ubicacion curricular al contextualizar: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar no regresion: no eliminar reglas utiles previas."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato exigido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Definir objetivo puntual de la actividad antes del desarrollo.",
    "Explicitar el problema que activa la respuesta.",
    "Relacionar conceptos, normas, doctrina o datos con el problema planteado.",
    "Distinguir sintesis de fuentes y postura propia.",
    "Evitar entregas solo descriptivas.",
    "Sustentar afirmaciones relevantes con fuentes verificables.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Supuesto: si actividad 6 aborda interpretacion juridica, vincular hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar aguas abajo.",
    "Revisar que no existan respuestas no estructuradas sin normalizacion.",
    "Separar reglas confirmadas de supuestos marcados.",
    "Confirmar que afirmaciones relevantes tengan fuente o etiqueta de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib activo.",
    "Verificar que la conclusion derive del analisis y no sea decorativa."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en espanol en .tex y .bib.",
    "Mantener compatibilidad entre .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en .tex sin migracion controlada.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Marcar como supuesto el nombre canonico del .bib mientras exista ambiguedad."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo fuentes realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y juridicas confiables.",
    "Registrar fuentes especificas de actividad en el .bib de la asignatura.",
    "Conservar metadatos minimos: autor, titulo, ano, editorial o nota, URL cuando exista.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No asumir que un .bib depurado de otra semana aplica automaticamente a actividad 6."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones reutilizables, no redaccion literal ni conclusiones especificas.",
    "Mantener union-dedupe lossless en consolidaciones futuras.",
    "Conservar advertencias historicas de nodos con salida no estructurada.",
    "Aplicar normalizacion manual a ciclos heredados de baja confianza antes de reutilizar.",
    "No propagar supuestos como hechos confirmados."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de actividad 6; confirmar producto exacto solicitado.",
    "Confirmar rubrica especifica de evaluacion para actividad 6.",
    "Confirmar si se exige formato de citacion juridica adicional a BibTeX.",
    "Confirmar nombre canonico final del .bib por token Slug sin resolver en README.",
    "Confirmar si actividad 6 reutiliza fuentes de interpretacion juridica o requiere corpus distinto."
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
      "Conceptos, normas o doctrina pertinentes.",
      "Producto de planeacion semanal.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico y criterio propio.",
      "Garantizar trazabilidad de afirmaciones mediante fuentes verificables.",
      "Asegurar utilidad profesional del cierre argumentativo."
    ],
    "style_markers": [
      "Inicio con encuadre del problema.",
      "Secciones explicitas y ordenadas.",
      "Postura personal diferenciada de la sintesis.",
      "Cierre con aplicacion juridica."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Construir marco conceptual-normativo.",
      "Contrastar fuentes pertinentes.",
      "Tomar postura fundamentada.",
      "Derivar conclusion del analisis."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco conceptual-normativo",
        "Analisis propio",
        "Conclusion transferible",
        "Hermeneutica juridica [supuesto condicionado]",
        "Argumentacion juridica [supuesto condicionado]"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
        "hernandezManriquezHermeneutica2019",
        "scjnMemoriaArgumentacion2008"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta editorial exige citas verificables y formato institucional."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere delimitacion previa del problema."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida debe derivar del desarrollo argumentativo."
        },
        {
          "source": "Hermeneutica juridica [supuesto condicionado]",
          "target": "Argumentacion juridica [supuesto condicionado]",
          "kind": "supports",
          "justification": "Si la actividad trata interpretacion, la hermeneutica fundamenta la argumentacion."
        }
      ],
      "evidence": [
        "README: identidad institucional, ubicacion curricular y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo.",
        "Regla persistente: no propagar salidas no estructuradas sin normalizacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 19: se deduplican reglas repetidas y se conserva cobertura funcional completa.",
      "Ciclo 19: se mantiene compatibilidad lateral entre actividades hermanas sin copiar contenido especifico.",
      "Ciclo 19: se refuerza control de supuestos por falta de consigna local visible.",
      "Ciclo 19: se preserva gate de JSON parseable como condicion de propagacion."
    ]
  }
}