{
  "summary": [
    "Se consolida refuerzo lateral entre actividades hermanas con union-dedupe sin perdida.",
    "Se preserva identidad UnADM y ubicacion curricular verificada: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se mantiene regla critica: no propagar contenido no estructurado; normalizar antes de reutilizar.",
    "Se refuerzan ejes estables de la asignatura: problema, conceptos o normas, producto, analisis propio y conclusion transferible.",
    "Se conserva tratamiento provisional de fuentes heredadas no verificadas.",
    "Se agrega control de analogia: transferir solo patrones reutilizables, no conclusiones ni bibliografia exclusiva."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear toda actividad a Licenciatura en Derecho, asignatura Filosofia del Derecho.",
    "Citar ubicacion curricular al contextualizar: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar regla de no regresion editorial en cada consolidacion."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable cuando la tarea sea de memoria editorial.",
    "Usar exactamente el esquema requerido y sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el producto al tipo solicitado en la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo de Actividad 6 sin romper ejes base de la asignatura.",
    "Distinguir con claridad sintesis de fuente y postura propia.",
    "Sostener afirmaciones relevantes con fuentes verificables disponibles.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Relacionar conceptos, normas y doctrina con el problema planteado.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Supuesto: si la consigna trata interpretacion juridica, vincular hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar que no haya respuesta no estructurada reutilizada.",
    "Separar reglas confirmadas de supuestos marcados.",
    "Validar trazabilidad de afirmaciones a fuente o supuesto.",
    "Comprobar consistencia entre citas en texto y archivo .bib activo.",
    "No eliminar reglas utiles previas durante consolidacion."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en .tex.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Usar codificacion correcta para espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico antes de automatizar rutas.",
    "Marcar como supuesto el nombre canonico del .bib hasta confirmacion local."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y juridicas oficiales o academicas.",
    "Registrar fuentes especificas de cada actividad en el .bib de la asignatura.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No transferir bibliografia exclusiva de una actividad hermana sin evidencia de uso local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Aplicar union-dedupe lossless en nodos hermanos.",
    "Transferir solo patrones reutilizables: identidad, estructura, calidad, conceptos y relaciones recurrentes.",
    "No propagar conclusiones especificas ni redaccion literal entre hermanos.",
    "Mantener advertencia historica de ciclos con salida no estructurada.",
    "Etiquetar como provisional toda regla derivada de fuente heredada no verificada."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 6; confirmar producto exacto solicitado.",
    "Confirmar rubrica especifica de evaluacion para ajustar profundidad argumentativa.",
    "Confirmar si Actividad 6 exige formato juridico de citacion adicional a BibTeX.",
    "Confirmar nombre canonico final del .bib por token Slug sin resolver en README.",
    "Confirmar si se usa filosofia-del-derecho.bib, filosofia-del-derecho-clean.bib o ambos segun consigna.",
    "Confirmar si las fuentes de interpretacion juridica (Semana 7) aplican formalmente a Actividad 6."
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
      "Conceptos, normas y doctrina pertinentes.",
      "Producto alineado a planeacion.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico, evidencia y criterio propio.",
      "Asegurar consistencia editorial entre actividades de la misma asignatura."
    ],
    "style_markers": [
      "Inicio con encuadre breve.",
      "Secciones explicitas y ordenadas.",
      "Postura propia diferenciada de la fuente.",
      "Cierre aplicable a practica juridica.",
      "Supuestos marcados de forma explicita."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual y normativo.",
      "Contrastar fuentes verificables.",
      "Sostener postura propia fundamentada.",
      "Concluir con criterio juridico derivado del desarrollo."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Analisis propio",
        "Conclusion transferible",
        "Hermeneutica juridica",
        "Argumentacion juridica"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "hernandezManriquezHermeneutica2019",
        "scjnMemoriaArgumentacion2008",
        "scjnViolenciaFisica2022",
        "scjnIncapacidadResistencia2019"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y formato consistente."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitacion del problema no hay argumentacion focalizada."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida debe derivar del razonamiento previo."
        },
        {
          "source": "Hermeneutica juridica",
          "target": "Argumentacion juridica",
          "kind": "supports",
          "justification": "La interpretacion de normas fortalece la justificacion argumentativa."
        }
      ],
      "evidence": [
        "README de asignatura: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: ejes de trabajo y proposito de realizacion.",
        "Existencia de fuentes juridicas en archivos .bib locales.",
        "Regla historica consolidada: normalizar salidas no estructuradas antes de propagar."
      ]
    },
    "reinforcement_log": [
      "Ciclo 10: se mantuvo compresion lossless por deduplicacion.",
      "Ciclo 10: se reforzo transferencia controlada por analogia entre hermanos.",
      "Ciclo 10: se excluyo transferencia de conclusiones especificas de Actividad 1.",
      "Ciclo 10: se preservaron reglas de calidad, estructura e identidad sin recorte util."
    ]
  }
}