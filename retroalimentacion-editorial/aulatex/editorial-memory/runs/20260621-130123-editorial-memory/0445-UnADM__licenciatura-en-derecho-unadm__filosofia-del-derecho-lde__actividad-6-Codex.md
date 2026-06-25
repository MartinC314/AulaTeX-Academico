{
  "summary": [
    "Consolidacion lateral ciclo 2 aplicada con union-dedupe lossless entre actividades hermanas.",
    "Se preserva identidad UnADM y ubicacion curricular verificada: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se mantiene regla critica: no propagar contenido no estructurado sin normalizacion previa.",
    "Se refuerzan ejes estables de la asignatura: problema, conceptos o normas, producto, analisis propio y conclusion juridica transferible.",
    "Se evita transferencia de conclusiones o bibliografia exclusiva de Actividad 1 hacia Actividad 6."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y trazabilidad.",
    "Alinear toda entrega a Licenciatura en Derecho, asignatura Filosofia del Derecho.",
    "Citar contexto curricular solo con datos verificados: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar regla de no regresion: no eliminar reglas utiles previas."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion de memoria.",
    "Usar exactamente el esquema requerido y sin claves extra.",
    "Estructurar productos con: problema, marco conceptual o normativo, desarrollo, analisis propio y cierre.",
    "Definir objetivo puntual de la actividad antes del desarrollo.",
    "Cerrar con conclusion juridica derivada del analisis y transferible a practica.",
    "Alinear formato final al producto pedido por la planeacion semanal."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes troncales.",
    "Distinguir siempre sintesis de fuente y postura propia.",
    "Sustentar afirmaciones relevantes con fuentes verificables o marcar supuesto.",
    "Evitar entregas solo descriptivas sin argumentacion.",
    "Relacionar conceptos, normas o doctrina con el problema planteado.",
    "No asumir que bibliografia de otra semana aplica automaticamente a Actividad 6."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de propagar recursivamente.",
    "Separar reglas confirmadas de supuestos marcados.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Validar consistencia entre claves citadas en texto y archivo .bib activo.",
    "No eliminar reglas utiles previas durante consolidacion."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre .tex y .bib.",
    "No cambiar claves BibTeX ya citadas sin migracion controlada.",
    "Comprobar que toda clave citada exista en el .bib usado.",
    "Usar codificacion y acentos correctos en espanol.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: el .bib canonico esperado es filosofia-del-derecho.bib por Slug visible."
  ],
  "bibliography_rules": [
    "No inventar fuentes ni metadatos.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar fuentes especificas de la actividad en el .bib de la asignatura.",
    "Mantener metadatos minimos: autor, titulo, ano, editorial o nota, URL cuando exista.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No forzar uso de filosofia-del-derecho-clean.bib fuera de su alcance si la consigna no lo exige."
  ],
  "propagation_hints": [
    "Propagar a hermanos solo patrones reutilizables: identidad, estructura, calidad y relaciones recurrentes.",
    "No propagar redaccion literal ni conclusiones especificas entre actividades.",
    "Mantener advertencia historica sobre salidas no estructuradas en ciclos previos.",
    "Aplicar normalizacion manual cuando aparezca memoria no parseable.",
    "Propagar supuestos como supuestos, nunca como hechos confirmados."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual completa de Actividad 6; confirmar producto exacto.",
    "Confirmar rubrica de evaluacion especifica de Actividad 6.",
    "Confirmar si Actividad 6 exige reporte, presentacion o ambos.",
    "Confirmar nombre canonico final del .bib por coexistencia de archivo base y clean.",
    "Confirmar si se requiere formato de citacion juridica adicional al flujo BibTeX."
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
      "Problema juridico o social bien delimitado.",
      "Uso de conceptos y normas pertinentes.",
      "Analisis propio sustentado en evidencia.",
      "Cierre juridico transferible a practica profesional."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico y claridad argumentativa.",
      "Garantizar consistencia editorial y tecnica entre actividades hermanas."
    ],
    "style_markers": [
      "Inicio con encuadre breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Postura personal diferenciada de la fuente.",
      "Conclusion no decorativa, derivada del desarrollo."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual o normativo.",
      "Contrastar evidencia relevante.",
      "Fijar postura argumentada.",
      "Concluir con criterio juridico aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion estructurada previa a propagacion"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "README.md de asignatura",
        "programa-analitico-filosofia-del-derecho.md"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y formato consistente."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitacion del problema no hay argumentacion pertinente."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida deriva del razonamiento y evidencia previos."
        },
        {
          "source": "Normalizacion estructurada previa a propagacion",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita arrastre de errores y reglas ambiguas entre nodos."
        }
      ],
      "evidence": [
        "README: identidad UnADM, entrada canonica y pauta editorial.",
        "Programa analitico: cinco ejes editoriales estables.",
        "Historial: incidentes de salida no JSON parseable en ciclos previos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: deduplicacion de reglas repetidas sin perdida semantica.",
      "Ciclo 2: refuerzo de puertas de calidad JSON + estructura minima.",
      "Ciclo 2: mantenimiento de supuestos marcados ante datos locales incompletos.",
      "Ciclo 2: transferencia lateral limitada a patrones reutilizables, sin copiar contenido especifico de Actividad 1."
    ]
  }
}