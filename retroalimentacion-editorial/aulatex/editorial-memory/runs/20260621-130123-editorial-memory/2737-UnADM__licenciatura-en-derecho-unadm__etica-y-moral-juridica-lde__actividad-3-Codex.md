{
  "summary": [
    "Se refuerza memoria lateral entre asignaturas sin copiar contenido especifico.",
    "Se preservan reglas validas previas y se deduplican sin perdida.",
    "Se mantiene normalizacion JSON obligatoria antes de cualquier propagacion.",
    "Se consolida el marco comun UnADM: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se confirma enfoque de transferencia por patrones reutilizables: identidad, estructura, calidad y metodo argumentativo.",
    "Se agregan alertas verificables del destino: token Slug sin expandir en README/programa y entrada BibTeX truncada."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y trazabilidad.",
    "Alinear toda actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como [Supuesto] todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No transferir conclusiones ni redaccion literal entre asignaturas laterales."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Si falta consigna local, usar estructura base y declarar [Supuesto]."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo resumen descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Integrar los cinco ejes del programa analitico en la actividad.",
    "Transferir solo patrones editoriales reutilizables, no bibliografia exclusiva del nodo hermano.",
    "Evitar asumir que fuentes de otra semana o asignatura aplican automaticamente."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [Supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Escalar a revision humana si persiste falla de parseo por ciclo."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Evitar comandos o paquetes no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Corregir rutas o nombres con caracteres anómalos antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Verificar nombres canonicos locales de salida y bibliografia antes de referenciar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos o eticos verificables.",
    "Registrar fuentes especificas de Actividad 3 en etica-y-moral-juridica.bib.",
    "No inventar referencias ni metadatos bibliograficos.",
    "Conservar metadatos minimos: autor o editor, titulo, año, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Depurar duplicados solo cuando la equivalencia de obra sea verificable.",
    "Corregir entradas truncadas antes de citarlas."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura completa.",
    "Mantener compresion lossless por union y deduplicacion semantica.",
    "Preservar reglas utiles previas; solo agregar mejoras verificables.",
    "Aplicar analogia controlada: transferir arquitectura editorial, no contenido tematico cerrado.",
    "Registrar por ciclo incidentes de parseo y acciones de normalizacion.",
    "En saltos laterales, reforzar identidad comun y adaptar solo lo localmente verificable."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 3 en Etica y Moral juridica.",
    "Confirmar tipo de producto requerido por la actividad (reporte, presentacion u otro).",
    "Confirmar rubrica de evaluacion para ajustar profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana para Actividad 3.",
    "Confirmar politica local para fusionar claves duplicadas (por ejemplo, huertaEticaConClasicos2000 y huerta2000etica).",
    "Corregir y completar entrada truncada sierraUniversidadNacional1910 en .bib.",
    "Confirmar nombre canonico final del .bib tras resolver token Slug en documentos de control."
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
        "Normalizacion JSON previa a propagacion.",
        "Trazabilidad editorial por ciclo."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura destino: Etica y Moral juridica."
      ]
    },
    "essence": [
      "Problema juridico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion transferible a la practica juridica."
    ],
    "reason_for_being": [
      "Transformar la planeacion semanal en entregables con fundamento juridico y evidencia.",
      "Mantener consistencia institucional entre actividades y asignaturas del mismo plan.",
      "Permitir transferencia lateral segura por patrones editoriales reutilizables."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones con funcion argumentativa definida.",
      "Citas verificables y postura propia visible.",
      "Cierre con utilidad juridica practica.",
      "Supuestos declarados cuando falte informacion local."
    ],
    "argumentative_patterns": [
      "Plantear problema y alcance.",
      "Delimitar conceptos y marco normativo o doctrinal.",
      "Contrastar fuentes con analisis propio.",
      "Sostener tesis breve con evidencia.",
      "Concluir con implicaciones profesionales transferibles."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Estructura canonica de actividad",
        "Integridad academica y cita verificable",
        "Analisis propio con postura argumentada",
        "Normalizacion JSON previa a propagacion",
        "Compresion lossless por deduplicacion",
        "Etica y moral juridica"
      ],
      "citations": [
        "README.md de etica-y-moral-juridica-lde",
        "programa-analitico-etica-y-moral-juridica.md",
        "etica-y-moral-juridica.bib",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura canonica de actividad",
          "kind": "supports",
          "justification": "La pauta institucional define formato y criterios minimos del entregable."
        },
        {
          "source": "Estructura canonica de actividad",
          "target": "Analisis propio con postura argumentada",
          "kind": "develops",
          "justification": "La secuencia de secciones obliga pasar de descripcion a argumentacion."
        },
        {
          "source": "Integridad academica y cita verificable",
          "target": "Analisis propio con postura argumentada",
          "kind": "supports",
          "justification": "La postura se valida con evidencia trazable."
        },
        {
          "source": "Normalizacion JSON previa a propagacion",
          "target": "Compresion lossless por deduplicacion",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay fusion segura sin perdida."
        },
        {
          "source": "Etica y moral juridica",
          "target": "Estructura canonica de actividad",
          "kind": "depends_on",
          "justification": "Cambia el contenido tematico, se conserva la arquitectura editorial."
        }
      ],
      "evidence": [
        "README local establece identidad UnADM e integridad academica.",
        "Programa analitico local define proposito y cinco ejes de trabajo.",
        "Historial del destino registra fallas repetidas de parseo JSON.",
        "README/programa muestran token Slug sin expandir que requiere normalizacion.",
        "Bib local contiene claves duplicadas y una entrada truncada verificable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 3: se transfiere ADN editorial comun desde Filosofia del Derecho hacia Etica y Moral juridica por analogia controlada.",
      "Ciclo 3: se preservan reglas previas y se eliminan duplicados semanticos sin recorte de contenido util.",
      "Ciclo 3: se refuerza gate de JSON parseable como condicion dura de propagacion recursiva.",
      "Ciclo 3: se mantiene separacion entre patrones reutilizables y contenido especifico no transferible."
    ]
  }
}