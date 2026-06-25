{
  "summary": [
    "Memoria editorial consolidada para la materia Electiva Semestre 8 Bloque 2.",
    "Se preserva identidad UnADM para Licenciatura en Derecho.",
    "Se refuerza enfoque academico-juridico con postura propia sustentada.",
    "Se transfieren solo abstracciones transversales desde Filosofia del Derecho.",
    "No se transfiere contenido tematico especifico de otra materia sin validacion local.",
    "Se conserva normalizacion estructurada antes de propagacion recursiva.",
    "Se mantiene compresion lossless por union y deduplicacion.",
    "Se preserva control de placeholders, nombres truncados y tokens sin expandir.",
    "Se fija autor confirmado: Martin Jonathan de la Cruz.",
    "Se fija matricula confirmada: ES2611202040.",
    "Se mantienen como provisionales herencias Codex y GPT-Pro no verificadas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, metadatos y redaccion.",
    "Alinear entregables con Licenciatura en Derecho.",
    "Ubicar la materia en semestre 8, bloque 2, tipo Electiva.",
    "Usar codigo de curso LDE-S8B2 en metadatos locales.",
    "Fijar autor Martin Jonathan de la Cruz en front matter.",
    "Fijar matricula ES2611202040 en front matter.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Conservar tono academico-juridico con postura propia sustentada.",
    "Marcar como [supuesto] todo dato no confirmado en consigna o documentos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Citar malla-curricular-derecho-unadm.pdf solo para ubicacion curricular verificable."
  ],
  "structure_rules": [
    "Organizar cada actividad en problema, conceptos y fuentes, producto, analisis propio y conclusion.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar marco conceptual, marco normativo o doctrinal y analisis propio.",
    "Transformar la planeacion semanal en entregable concreto.",
    "Alinear formato final con la consigna vigente.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener consistencia entre README, programa analitico, reporte, presentacion y .bib local.",
    "Corregir placeholders de plantillas en nombres de archivo y referencias.",
    "Restaurar nombres truncados en listados de estructura."
  ],
  "activity_rules": [
    "Traducir la consigna semanal al producto solicitado.",
    "Vincular conceptos, normas, doctrina o datos con el problema juridico tratado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir analisis juridico propio, no solo resumen de fuentes.",
    "Evitar entregas puramente descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir bibliografia base de fuentes especificas de actividad.",
    "No asumir fuentes de otra actividad o materia sin confirmacion.",
    "No trasladar contenido especifico de Filosofia del Derecho sin fuente verificable local.",
    "Cerrar cada actividad con aplicacion a la practica juridica."
  ],
  "quality_gates": [
    "Validar que toda salida de memoria sea JSON parseable.",
    "Bloquear propagacion si la salida no es estructurada.",
    "Revisar manualmente artefactos heredados de ciclo 1 antes de reutilizar.",
    "Confirmar estructura minima completa antes de aplicar aguas abajo.",
    "Verificar trazabilidad entre afirmaciones, citas en texto y .bib.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Comprobar que los datos de portada coincidan con la materia destino.",
    "Confirmar ausencia de placeholders visibles en README, programa, .tex y .bib.",
    "Verificar que no queden plantillas PowerShell sin evaluar.",
    "Confirmar nombres de archivo coherentes entre README, programa y carpeta real.",
    "Validar que el producto corresponda a la consigna vigente.",
    "Compilar sin errores criticos y sin referencias rotas."
  ],
  "latex_rules": [
    "Conservar plantilla LaTeX base de la materia.",
    "Usar reporte-electiva-semestre-8-bloque-2.tex como base del reporte.",
    "Actualizar titulo, subtitulo y numero real de actividad antes de compilar.",
    "Completar campos pendientes del front matter solo con datos confirmados.",
    "Mantener metadatos institucionales consistentes con README y programa.",
    "Completar figura docente solo con dato confirmado.",
    "Completar creditos solo con dato confirmado.",
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener compatibilidad de nombres de archivos entre .tex y recursos.",
    "Resolver tokens tipo $(@{...}.Slug) antes de entrega.",
    "Corregir nombres mal renderizados como eporte o eferencias.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas de cada actividad en electiva-semestre-8-bloque-2.bib.",
    "Priorizar fuentes institucionales UnADM cuando correspondan.",
    "Conservar la malla curricular de Derecho como fuente institucional local.",
    "Reutilizar claves unadmSitioWeb y unadmMallaDerecho2024 como base institucional.",
    "No inventar referencias.",
    "Agregar entradas BibTeX solo con metadatos comprobables.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente editorial o URL.",
    "Marcar como [supuesto] cualquier dato bibliografico no confirmado.",
    "Mantener trazabilidad entre citas del texto y claves BibTeX.",
    "Verificar fecha de consulta del sitio UnADM antes de entrega.",
    "Distinguir bibliografia base de bibliografia especifica de actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Compartir solo reglas transversales entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferencia de redaccion literal entre materias.",
    "Propagar reglas de integridad academica a materias UnADM compatibles.",
    "No propagar datos incompletos de creditos o figura docente.",
    "Mantener etiqueta provisional para herencias Codex o GPT-Pro no verificadas.",
    "Usar ciclo 1 como etapa de normalizacion, no como evidencia definitiva.",
    "Propagar leccion transversal de corregir placeholders y nombres truncados.",
    "Evitar regresiones respecto de reglas utiles previas.",
    "Aplicar union-dedupe sin eliminar reglas vigentes."
  ],
  "open_questions": [
    "[supuesto] Confirmar creditos oficiales de Electiva Semestre 8 Bloque 2.",
    "[supuesto] Confirmar nombre oficial de figura docente para front matter.",
    "[supuesto] Confirmar si existe nombre oficial alterno de la electiva.",
    "[supuesto] Confirmar consignas concretas de actividades de la materia destino.",
    "[supuesto] Confirmar rubricas especificas de evaluacion.",
    "[supuesto] Confirmar fuentes obligatorias por semana.",
    "[supuesto] Verificar si el sitio institucional UnADM debe citarse con fecha de consulta actualizada.",
    "[supuesto] Confirmar si el ano 2026 del sitio UnADM en .bib es correcto o placeholder.",
    "[supuesto] Confirmar politica institucional para year y fecha de consulta en @misc.",
    "[supuesto] Confirmar correccion definitiva de README con nombres de archivo literales."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Institucional sin rigidez excesiva.",
        "Conservador ante datos no confirmados."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de materia como entrada canonica.",
        "Metadatos institucionales consistentes.",
        "Control explicito de supuestos.",
        "Trazabilidad entre documentos locales."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Electiva Semestre 8 Bloque 2.",
        "Semestre 8.",
        "Bloque 2.",
        "Tipo Electiva.",
        "Codigo de curso LDE-S8B2.",
        "[supuesto] Creditos pendientes de confirmacion."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Integridad academica.",
      "Problema juridico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Postura academica sustentada.",
      "Conclusion juridica transferible.",
      "Trazabilidad cita-texto-bib.",
      "Control de supuestos.",
      "Normalizacion estructurada."
    ],
    "reason_for_being": [
      "Orientar productos academicos con claridad, fundamento juridico y evidencia.",
      "Transformar planeacion semanal en reportes, presentaciones o productos visuales.",
      "Integrar problema, conceptos, fuentes, analisis propio y cierre argumentativo.",
      "Asegurar transferencia profesional de la conclusion juridica.",
      "Prevenir errores editoriales por placeholders, datos incompletos o fuentes no verificadas."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Objetivo puntual visible.",
      "Secciones explicitas y ordenadas.",
      "Marco conceptual o normativo delimitado.",
      "Postura propia respaldada.",
      "Citas verificables.",
      "Cierre con transferencia profesional.",
      "Marcado explicito de [supuesto].",
      "Metadatos UnADM consistentes.",
      "Nombres de archivo literales y corregidos."
    ],
    "argumentative_patterns": [
      "Plantear problema -> delimitar objetivo -> desarrollar marco conceptual o normativo -> argumentar postura -> concluir aplicacion.",
      "Vincular cada concepto con el problema juridico tratado.",
      "Usar evidencia verificable para sostener afirmaciones clave.",
      "Contrastar descripcion de fuentes con juicio juridico propio.",
      "Derivar la conclusion desde el analisis, no desde una opinion aislada.",
      "Conectar cierre academico con practica profesional.",
      "Revisar coherencia entre consigna, desarrollo, citas y producto final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Electiva Semestre 8 Bloque 2",
        "Integridad academica",
        "Normalizacion estructurada",
        "Propagacion recursiva segura",
        "Problema juridico",
        "Marco conceptual",
        "Marco normativo o doctrinal",
        "Evidencia verificable",
        "Analisis juridico propio",
        "Conclusion juridica transferible",
        "Trazabilidad cita-texto-bib",
        "Control de supuestos",
        "Compresion union-dedupe",
        "Placeholders de plantilla",
        "Nombres de archivo truncados"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Metadatos institucionales consistentes",
          "kind": "supports",
          "justification": "La identidad se expresa en portada, front matter, README y programa."
        },
        {
          "source": "Licenciatura en Derecho",
          "target": "Electiva Semestre 8 Bloque 2",
          "kind": "develops",
          "justification": "La materia destino pertenece al trayecto curricular local confirmado."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva segura",
          "kind": "supports",
          "justification": "Evita heredar salidas no parseables o reglas ambiguas."
        },
        {
          "source": "Integridad academica",
          "target": "Trazabilidad cita-texto-bib",
          "kind": "depends_on",
          "justification": "La verificabilidad requiere correspondencia entre afirmaciones, citas y .bib."
        },
        {
          "source": "Control de supuestos",
          "target": "Rigor editorial",
          "kind": "supports",
          "justification": "Distingue datos confirmados de datos pendientes."
        },
        {
          "source": "Problema juridico",
          "target": "Marco conceptual",
          "kind": "develops",
          "justification": "El marco conceptual delimita las categorias usadas para resolver el problema."
        },
        {
          "source": "Problema juridico",
          "target": "Marco normativo o doctrinal",
          "kind": "develops",
          "justification": "El problema exige normas, doctrina o datos pertinentes."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis juridico propio",
          "kind": "supports",
          "justification": "La postura del estudiante debe sustentarse en fuentes consultables."
        },
        {
          "source": "Analisis juridico propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion profesional surge del razonamiento argumentado."
        },
        {
          "source": "Placeholders de plantilla",
          "target": "Calidad LaTeX",
          "kind": "contrasts",
          "justification": "Los tokens sin expandir contradicen una entrega final compilable."
        },
        {
          "source": "Nombres de archivo truncados",
          "target": "Trazabilidad documental",
          "kind": "contrasts",
          "justification": "Los nombres incompletos rompen consistencia entre README, programa y archivos reales."
        },
        {
          "source": "Compresion union-dedupe",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Conserva reglas utiles sin duplicados ni recortes."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 8, bloque 2, tipo Electiva.",
        "README local: creditos vacios y pendientes de confirmacion.",
        "README local: fuente curricular malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canonico.",
        "README local: pauta de integridad academica, citas verificables y conclusion juridica propia.",
        "README local: nombres truncados eporte y eferencias.",
        "README local: token $(@{...}.Slug) visible.",
        "Programa analitico local: productos con claridad, fundamento juridico, evidencia y transferencia profesional.",
        "Programa analitico local: ejes problema, conceptos, producto, analisis propio y conclusion.",
        "Archivo .bib local: claves unadmSitioWeb y unadmMallaDerecho2024.",
        "Reporte local: autor Martin Jonathan de la Cruz.",
        "Reporte local: matricula ES2611202040.",
        "Reporte local: figura docente por definir.",
        "Reporte local: creditos vacios.",
        "Origen transversal: normalizacion estructurada antes de propagar.",
        "Origen transversal: no inventar referencias.",
        "Origen transversal: sostener afirmaciones con citas verificables.",
        "Origen transversal: evitar entregas solo descriptivas."
      ]
    },
    "reinforcement_log": [
      "Ciclo 10 consolida memoria de materia con estrategia progresiva y conservadora.",
      "Se deduplican reglas repetidas sin eliminar reglas utiles.",
      "Se preservan reglas locales sobre autor, matricula, codigo y plantilla base.",
      "Se incorporan abstracciones estables del origen: problema, conceptos, evidencia, analisis y conclusion.",
      "Se excluye contenido tematico especifico de Filosofia del Derecho por relacion transversal no equivalente.",
      "Se refuerza gate de JSON parseable antes de propagacion recursiva.",
      "Se refuerza trazabilidad entre texto, citas y .bib.",
      "Se refuerza marcado [supuesto] para creditos, figura docente y datos no confirmados.",
      "Se refuerza correccion de placeholders y nombres truncados como riesgo operativo transversal.",
      "Se mantiene herencia Codex/GPT-Pro como provisional hasta validacion manual."
    ]
  }
}