{
  "summary": [
    "Se refuerza memoria lateral entre actividades de materias distintas con patron reutilizable y sin copia literal.",
    "Se preservan reglas validas previas y se aplica fusion lossless por union y deduplicacion.",
    "Se mantiene normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se consolidan ejes comunes: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se agrega mejora verificable local: resolver tokens Slug sin expandir en README y programa analitico.",
    "Se agrega mejora verificable local: marcar .bib truncado como bloqueo de calidad hasta correccion.",
    "Supuesto: no se cuenta con consigna textual de Actividad 8 en este ciclo."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y cierre juridico.",
    "Vincular toda actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Mantener referencia explicita a la asignatura destino: Etica y Moral juridica.",
    "Registrar ruta origen-destino y ciclo en cada fusion editorial.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Responder siempre en JSON valido y parseable.",
    "Usar el esquema canonico completo sin omitir secciones.",
    "Aplicar compresion lossless por union y deduplicacion semantica.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el artefacto al formato solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Marcar supuestos de forma explicita cuando falte evidencia."
  ],
  "activity_rules": [
    "Alinear desarrollo con pregunta guia y producto solicitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Evitar entregas exclusivamente descriptivas.",
    "Verificar coherencia entre problema, desarrollo y conclusion.",
    "No asumir fuentes de otras semanas sin validacion en consigna local.",
    "Aplicar lista de control de cinco ejes del programa analitico local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Bloquear guardado si falta alguna seccion del esquema requerido.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar correspondencia entre citas en texto y claves en .bib.",
    "Validar deduplicacion semantica antes de persistir memoria.",
    "No eliminar reglas utiles previas durante la fusion.",
    "Aceptar solo mejoras verificables contra archivos locales o memoria previa.",
    "Bloquear compilacion si el .bib contiene entradas truncadas."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar compilaciones rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Verificar nombres de archivos contra README antes de referenciar.",
    "Corregir caracteres anommalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Mantener consistencia de nombres .tex y .bib segun slug canonico de materia."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor o editor, titulo, anio, fuente/editorial o URL.",
    "Registrar fuentes especificas de actividad en etica-y-moral-juridica.bib.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Evitar claves duplicadas para una misma obra; si existen, normalizar con alias trazable.",
    "Marcar entradas truncadas como incidencia abierta antes de editar o compilar.",
    "Supuesto: entrada sierraUniversidadNacional1910 esta truncada y requiere correccion local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura completa.",
    "Transferir solo patrones reutilizables, no redaccion literal ni conclusiones especificas.",
    "Reforzar conexiones laterales por analogia controlada entre asignaturas del mismo bloque.",
    "Mantener bandera de normalizacion manual mientras existan salidas no estructuradas historicas.",
    "Si falta consigna local, propagar estructura base y abrir preguntas en lugar de inventar contenido."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 8 y producto requerido.",
    "Confirmar rubrica especifica para calibrar profundidad argumentativa.",
    "Confirmar criterio local de normalizacion de claves BibTeX duplicadas.",
    "Confirmar correccion completa de la entrada truncada sierraUniversidadNacional1910.",
    "Supuesto: curso conserva esquema de cinco ejes sin cambios en semana actual."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Etico con rigor juridico."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de asignatura como entrada canonica.",
        "Normalizacion estructurada obligatoria antes de propagar.",
        "Trazabilidad por ruta y ciclo."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura destino: Etica y Moral juridica.",
        "Fuente curricular: malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo pertinente.",
      "Evidencia verificable.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos solidos y verificables.",
      "Sostener coherencia institucional entre actividades y materias del mismo bloque.",
      "Permitir propagacion segura mediante memoria estructurada y trazable."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Supuestos etiquetados explicitamente.",
      "Sin invencion de fuentes.",
      "Sin copia literal entre nodos laterales.",
      "Fusion por deduplicacion, no por recorte."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo al inicio.",
      "Exponer conceptos y marco normativo antes del analisis.",
      "Contrastar postura propia con evidencia citada.",
      "Cerrar con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion JSON",
        "Ejes editoriales de actividad",
        "Integridad academica",
        "Trazabilidad bibliografica",
        "Etica y moral juridica",
        "Tokens Slug sin expandir",
        "Entrada .bib truncada"
      ],
      "citations": [
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/programa-analitico-etica-y-moral-juridica.md",
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/etica-y-moral-juridica.bib",
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Ejes editoriales de actividad",
          "kind": "supports",
          "justification": "La pauta institucional define criterios minimos de entrega."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia segura."
        },
        {
          "source": "Trazabilidad bibliografica",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Claves estables y metadatos completos permiten verificacion."
        },
        {
          "source": "Tokens Slug sin expandir",
          "target": "Consistencia de archivos",
          "kind": "depends_on",
          "justification": "Si no se resuelven, se rompen referencias nominales."
        },
        {
          "source": "Entrada .bib truncada",
          "target": "Compilacion LaTeX",
          "kind": "depends_on",
          "justification": "Una entrada incompleta puede causar error de bibliografia."
        }
      ],
      "evidence": [
        "README local confirma identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico local confirma cinco ejes de trabajo.",
        ".bib local muestra duplicados y una entrada truncada visible.",
        "Memoria origen aporta patron transversal de estructura y calidad reutilizable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 15: se refuerza transferencia lateral de patrones sin copiar contenido especifico.",
      "Ciclo 15: se preservan reglas previas utiles y se deduplican variantes redundantes.",
      "Ciclo 15: se agrega control verificable sobre tokens Slug no expandidos.",
      "Ciclo 15: se agrega gate de bloqueo por entrada .bib truncada.",
      "Ciclo 15: se mantiene supuesto abierto por falta de consigna textual local."
    ]
  }
}