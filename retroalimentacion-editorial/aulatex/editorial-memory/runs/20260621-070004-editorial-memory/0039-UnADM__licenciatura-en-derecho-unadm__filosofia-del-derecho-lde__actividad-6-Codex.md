{
  "summary": [
    "Se consolida memoria lateral de Actividad 1 a Actividad 6 con union-dedupe sin perdida.",
    "Se preserva identidad UnADM y ubicacion curricular verificada: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se refuerzan ejes estables: problema, conceptos o normas, producto, analisis propio y conclusion juridica transferible.",
    "Se mantiene regla critica: no propagar contenido no estructurado; normalizar antes de reutilizar.",
    "Se mantiene separacion entre reglas confirmadas y supuestos marcados."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear toda entrega a Licenciatura en Derecho y asignatura Filosofia del Derecho.",
    "Citar ubicacion curricular cuando aplique: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar regla de no regresion editorial en consolidaciones."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar desarrollo en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Cerrar con conclusion juridica derivada del analisis y transferible a practica.",
    "Alinear el formato final al producto pedido por la planeacion semanal."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Explicitar el problema juridico o social que activa la respuesta.",
    "Relacionar conceptos, normas y doctrina con el problema delimitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir sintesis de fuentes y postura propia.",
    "Evitar entregas solo descriptivas o generalizaciones sin anclaje juridico.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Supuesto: si la consigna de Actividad 6 es interpretacion juridica, priorizar hermeneutica y argumentacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de propagar.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar trazabilidad de afirmaciones a fuente o supuesto marcado.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No eliminar reglas utiles previas durante consolidacion.",
    "Aplicar deduplicacion por union sin perdida semantica.",
    "Verificar que la conclusion derive del desarrollo."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en .tex.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Usar acentos y codificacion correctos en espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir caracteres anomalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: nombre canonico esperado del .bib es filosofia-del-derecho.bib por Slug visible."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Registrar fuentes especificas de actividad en el .bib de la asignatura.",
    "Mantener metadatos minimos: autor, titulo, ano, editorial o nota, URL cuando exista.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No asumir que bibliografia de otra semana aplica automaticamente a Actividad 6.",
    "Marcar como supuesto cualquier dato bibliografico incompleto."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir solo patrones reutilizables, no redaccion literal ni conclusiones especificas.",
    "Mantener advertencias historicas de salidas no parseables en ramas con herencia provisional.",
    "Propagar identidad curricular verificada a nodos hermanos de la asignatura.",
    "Si falta consigna local, propagar estructura base y preguntas abiertas.",
    "Evitar regresiones: conservar reglas utiles previas y agregar solo mejoras verificables."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 6; confirmar producto exacto solicitado.",
    "Confirmar rubrica especifica de evaluacion para ajustar profundidad argumentativa.",
    "Confirmar si Actividad 6 exige reporte, presentacion o ambos.",
    "Confirmar si requiere formato de citacion juridica adicional a BibTeX.",
    "Confirmar nombre canonico final del .bib por coexistencia de archivo base y clean.",
    "Confirmar si las fuentes de interpretacion juridica de Semana 7 aplican formalmente a Actividad 6."
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
        "Asignatura Filosofia del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social delimitado.",
      "Conceptos, normas y doctrina pertinentes.",
      "Producto alineado a planeacion.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos con fundamento juridico, evidencia y criterio propio.",
      "Asegurar calidad estructural y trazabilidad de fuentes en cada entrega."
    ],
    "style_markers": [
      "Inicio con encuadre breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Separacion clara entre fuente y postura propia.",
      "Cierre con utilidad profesional juridica.",
      "Uso constante de marca de supuesto cuando falte dato local."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual y normativo.",
      "Contrastar fuentes relevantes.",
      "Sostener postura propia con evidencia.",
      "Concluir con inferencia juridica derivada del analisis."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco conceptual-normativo",
        "Analisis propio",
        "Conclusion transferible",
        "Hermenautica juridica [supuesto condicionado por consigna]",
        "Argumentacion juridica [supuesto condicionado por consigna]"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "README.md de la asignatura",
        "programa-analitico-filosofia-del-derecho.md"
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
          "justification": "El analisis valido parte de un problema delimitado."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion debe derivar del razonamiento previo."
        },
        {
          "source": "Marco conceptual-normativo",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "Los conceptos y normas fundamentan la postura."
        }
      ],
      "evidence": [
        "README confirma identidad UnADM y ubicacion curricular.",
        "Programa analitico define cinco ejes editoriales.",
        "Memoria origen confirma regla de normalizacion previa a propagacion."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin recortar contenido util.",
      "Se mantuvo regla de bloqueo por JSON no parseable.",
      "Se preservo distincion entre hechos verificados y supuestos.",
      "Se reforzo transferencia lateral por patrones reutilizables."
    ]
  }
}