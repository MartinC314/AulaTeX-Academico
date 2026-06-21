{
  "summary": [
    "Se consolida memoria lateral A1->A6 con union-dedupe lossless.",
    "Se preserva identidad UnADM y contexto curricular verificado.",
    "Se mantienen ejes estables: problema, conceptos/normas, producto, analisis propio y conclusion juridica.",
    "Se refuerza regla critica: no propagar salidas no estructuradas sin normalizacion.",
    "Se conserva trazabilidad de fuentes provisionales y supuestos marcados."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear contenido a Licenciatura en Derecho, asignatura Filosofia del Derecho.",
    "Reconocer ubicacion curricular al contextualizar: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Conservar regla de no regresion en consolidaciones."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar en bloques: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el producto al formato pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Explicitar problema juridico o social desde el inicio.",
    "Relacionar conceptos, normas o doctrina con el problema planteado.",
    "Sustentar afirmaciones relevantes con fuentes verificables.",
    "Distinguir sintesis de fuente y postura propia.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Supuesto: si la consigna de A6 es interpretacion juridica, vincular hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar aguas abajo.",
    "Revisar y normalizar cualquier respuesta no estructurada heredada.",
    "Confirmar que cada afirmacion relevante tenga fuente o marca de supuesto.",
    "Validar consistencia entre citas en texto y .bib activo.",
    "No eliminar reglas utiles previas durante consolidacion.",
    "Separar reglas confirmadas de supuestos editoriales."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener compatibilidad .tex/.bib sin cambiar claves ya citadas.",
    "Comprobar que toda clave citada exista en el archivo bibliografico activo.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir caracteres anomalos en rutas y nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: nombre canonico esperado del .bib es filosofia-del-derecho.bib hasta confirmacion local."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo fuentes realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas oficiales/academicas.",
    "Registrar fuentes especificas de la actividad en el .bib de la asignatura.",
    "Mantener metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No asumir que bibliografia de otra semana aplica automaticamente a A6.",
    "Supuesto: filosofia-del-derecho-clean.bib esta orientado a una actividad de interpretacion juridica (Semana 7)."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir solo patrones reutilizables, no redaccion literal ni conclusiones de hermano.",
    "Reutilizar reglas institucionales de calidad sin perder especificidad local.",
    "Propagar identidad curricular verificada a nodos hermanos de la misma asignatura.",
    "Mantener advertencias historicas de salidas no parseables en nodos con herencia similar.",
    "Cuando falte consigna local, propagar estructura base y abrir preguntas."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 6.",
    "Confirmar rubrica de evaluacion especifica de Actividad 6.",
    "Confirmar formato principal exigido: reporte, presentacion u otro.",
    "Confirmar nombre canonico final del .bib por token Slug sin resolver en documentos base.",
    "Confirmar si A6 requiere fuentes obligatorias distintas a las disponibles en bibliografia local.",
    "Confirmar si se exige estilo juridico de citacion adicional al flujo BibTeX institucional."
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
        "Filosofia del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social bien delimitado.",
      "Marco conceptual y normativo pertinente.",
      "Producto alineado a la planeacion.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico.",
      "Garantizar trazabilidad entre fuentes, analisis y cierre argumentativo.",
      "Preservar consistencia editorial entre actividades hermanas sin perder contexto local."
    ],
    "style_markers": [
      "Inicio con encuadre breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Postura personal diferenciada de la sintesis.",
      "Citas verificables y consistentes con .bib.",
      "Cierre aplicable a practica juridica."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Definir objetivo.",
      "Exponer conceptos y marco normativo.",
      "Contrastar fuentes y desarrollar postura.",
      "Concluir desde el analisis, no de forma decorativa."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco conceptual-normativo",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion estructurada",
        "Hermeneutica juridica [supuesto condicionado]"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
        "README.md de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib [uso condicionado]"
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
          "justification": "El analisis requiere un problema delimitado."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida debe derivar del desarrollo argumentativo."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "supports",
          "justification": "Se evita contaminar nodos con salidas no parseables."
        }
      ],
      "evidence": [
        "README: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo.",
        "Historial: incidentes de salida no JSON parseable y regla de bloqueo.",
        "Coexistencia de archivos .bib y token Slug sin resolver en documentos base."
      ]
    },
    "reinforcement_log": [
      "Ciclo 68: deduplicacion integral de reglas repetidas en destino.",
      "Ciclo 68: preservada regla de bloqueo por JSON no parseable.",
      "Ciclo 68: reforzada separacion entre hechos confirmados y supuestos.",
      "Ciclo 68: transferidos patrones reutilizables de A1 sin copiar conclusiones ni bibliografia exclusiva.",
      "Ciclo 68: mantenida alerta sobre token Slug sin resolver y canonicidad del .bib."
    ]
  }
}