{
  "summary": [
    "Materia electiva de Derecho UnADM en semestre 7 bloque 2.",
    "La carpeta de materia es punto de entrada canonico.",
    "Se sincroniza memoria transversal con abstracciones estables desde Filosofia del Derecho.",
    "Se conservan ejes editoriales reutilizables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se preserva identidad UnADM sin trasladar contenido tematico de otra asignatura.",
    "Se mantiene compresion lossless por union y deduplicacion.",
    "Historial: ciclos previos reportaron salidas no JSON parseables desde Codex, GPT-Pro y Auto.",
    "Contexto local confirma README, programa analitico, plantilla LaTeX y bibliografia base.",
    "La memoria estructurada del origen permite refuerzo transversal conservador."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en todo entregable.",
    "Usar encuadre local: Licenciatura en Derecho, semestre 7, bloque 2, tipo electiva.",
    "Conservar autoria, matricula y datos academicos en portada cuando aplique.",
    "Conservar autor Martin Jonathan de la Cruz y matricula ES2611202040 en portada local.",
    "Usar la carpeta de materia como entrada canonica para plantillas y referencias.",
    "Marcar como supuesto todo dato no visible en consigna o documentos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No mezclar identidad de Ingenieria con productos de Derecho.",
    "No transferir identidad curricular de Filosofia del Derecho al destino.",
    "Usar malla-curricular-derecho-unadm.pdf solo para ubicacion curricular verificable."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear contenido con planeacion semanal y producto solicitado.",
    "Transformar la planeacion en reporte, presentacion o producto visual segun consigna.",
    "Conservar claridad, fundamento juridico, evidencia y transferencia profesional.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener el programa analitico como guia editorial local.",
    "Evitar redaccion literal importada desde otra materia.",
    "Adaptar la estructura al formato real de cada actividad."
  ],
  "activity_rules": [
    "Vincular cada actividad con el problema juridico o social que la activa.",
    "Incluir postura academica propia sustentada en fuentes verificables.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con cita explicita.",
    "Verificar coherencia entre pregunta guia, objetivo, desarrollo y conclusion.",
    "Registrar supuestos operativos cuando falten instrucciones.",
    "Agregar fuentes especificas de actividad al .bib local.",
    "Verificar que el producto corresponda a la consigna local.",
    "No importar reglas tematicas de Filosofia del Derecho sin validacion documental.",
    "No asumir que fuentes de otra semana o asignatura aplican al encargo local."
  ],
  "quality_gates": [
    "Validar que toda memoria entrante sea JSON parseable antes de propagar.",
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Marcar y aislar insumos no estructurados para normalizacion manual.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar coherencia entre objetivo, analisis, evidencia y conclusion.",
    "Comprobar que rutas citadas existan en el repositorio local.",
    "Corregir placeholders y nombres rotos en README y programa analitico.",
    "Verificar creditos vacios antes de cerrar portada o README.",
    "Validar nombre oficial de la electiva con malla curricular antes de publicarlo.",
    "Normalizar manualmente ciclos heredados no estructurados antes de reutilizarlos."
  ],
  "latex_rules": [
    "Usar la plantilla .tex local como base de nuevos reportes.",
    "Mantener metadatos del curso: LDE-S7B2, semestre 7, bloque 2.",
    "Conservar portada con tabla de identificacion academica completa.",
    "Usar documentclass article con spanish, letterpaper y oneside salvo instruccion distinta.",
    "Mantener macros editoriales de titulo, subtitulo, autor, curso, universidad y portada.",
    "Sustituir Actividad X por el nombre real del producto.",
    "Conservar Figura docente como Nombre por definir hasta confirmacion.",
    "Mantener Tipo/Creditos como Electiva solo hasta confirmar creditos oficiales.",
    "No compilar con placeholders tipo Slug sin normalizarlos.",
    "Resolver tokens generados en README y programa analitico antes de referenciarlos.",
    "Corregir caracteres anomalos en rutas o nombres antes de compilar.",
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Mantener universitydepartmentimage en departamentos/UnADM con height 1.57cm."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo fuentes consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos pertinentes al encargo local.",
    "Centralizar referencias en electiva-semestre-7-bloque-2.bib.",
    "Conservar entradas locales unadmSitioWeb y unadmMallaDerecho2024 como base.",
    "Registrar fuentes especificas de cada actividad como entradas BibTeX completas.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Verificar fecha de consulta y disponibilidad antes de citar fuentes web.",
    "Usar archivo local de malla curricular solo si permanece disponible en assets-unadm.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No trasladar bibliografia de Filosofia del Derecho sin verificacion tematica y documental.",
    "Validar consistencia entre claves citadas y entradas .bib."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y no duplicadas.",
    "Compartir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Separar reglas institucionales de reglas tematicas de asignatura.",
    "Reusar estas reglas en actividades hijas con union-dedupe.",
    "No propagar contenido tematico lateral sin evidencia local.",
    "Mantener bandera de normalizacion manual para insumos no estructurados.",
    "Propagar como alerta institucional la revision de salidas no JSON.",
    "Conservar compresion lossless por deduplicacion, no por recorte.",
    "Evitar regresiones respecto de reglas utiles previas.",
    "Ciclos heredados no parseables requieren normalizacion manual si se reutilizan.",
    "En saltos transversales, priorizar identidad, estructura, gates y grafo conceptual."
  ],
  "open_questions": [
    "Confirmar nombre oficial de la electiva en malla curricular.",
    "Confirmar creditos oficiales para portada y README.",
    "Definir nombre de figura docente en plantilla base.",
    "Corregir en README el nombre roto de reporte.",
    "Corregir en README el nombre roto de carpeta de referencias.",
    "Corregir en README y programa analitico el placeholder del archivo .bib.",
    "Confirmar si unadmSitioWeb debe conservar year 2026 o usar solo fecha de consulta.",
    "Confirmar consigna textual de cada actividad local.",
    "Confirmar rubrica especifica para ajustar profundidad argumentativa.",
    "Confirmar fuentes obligatorias de cada semana.",
    "Confirmar si la electiva requiere productos adicionales a reporte y presentacion."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Sobrio y verificable.",
        "Conservador en transferencias transversales."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de materia como entrada canonica.",
        "Metadatos locales preservados en portada.",
        "Fuentes heredadas tratadas como provisionales hasta verificacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 7, bloque 2, tipo electiva.",
        "Curso local LDE-S7B2.",
        "Producto alineado a planeacion semanal.",
        "Creditos oficiales pendientes de confirmacion."
      ]
    },
    "essence": [
      "Problema juridico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeacion.",
      "Evidencia verificable.",
      "Analisis propio y postura academica.",
      "Conclusion transferible a la practica juridica.",
      "Identidad institucional UnADM.",
      "Integridad academica.",
      "Normalizacion estructurada antes de propagar.",
      "Separacion entre abstraccion editorial y contenido tematico."
    ],
    "reason_for_being": [
      "Orientar productos academicos con claridad, fundamento juridico, evidencia y transferencia profesional.",
      "Transformar la planeacion semanal en reportes, presentaciones y productos visuales.",
      "Integrar problema, conceptos, fuentes, analisis propio y cierre argumentativo.",
      "Crear continuidad editorial entre materia y actividades hijas.",
      "Evitar regresiones mediante memoria persistente deduplicada.",
      "Proteger la identidad local frente a transferencias transversales."
    ],
    "style_markers": [
      "Frases directas y verificables.",
      "Supuestos etiquetados cuando falta evidencia.",
      "Separacion clara entre descripcion, analisis y cierre.",
      "Citas explicitas para afirmaciones sustantivas.",
      "Conclusion con utilidad profesional.",
      "Sin redaccion literal importada de otra asignatura.",
      "Sin placeholders visibles en productos finales.",
      "Metadatos curriculares locales consistentes.",
      "Lenguaje juridico claro, no ornamental.",
      "Compresion por union-dedupe."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo.",
      "Definir conceptos clave.",
      "Ubicar marco normativo o doctrinal pertinente.",
      "Relacionar evidencia con la pregunta guia.",
      "Contrastar fuentes con postura propia.",
      "Distinguir hechos, normas y valoracion juridica.",
      "Evitar resumen sin criterio.",
      "Cerrar con implicacion juridica practica.",
      "Verificar coherencia entre objetivo, desarrollo y conclusion.",
      "Ajustar profundidad a rubrica y consigna."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Semestre 7 bloque 2",
        "Electiva",
        "Carpeta de materia canonica",
        "Planeacion semanal",
        "Producto solicitado",
        "Problema juridico o social",
        "Conceptos juridicos",
        "Marco normativo",
        "Marco doctrinal",
        "Evidencia verificable",
        "Analisis propio",
        "Postura academica",
        "Conclusion juridica transferible",
        "Integridad academica",
        "Bibliografia local",
        "JSON parseable",
        "Normalizacion manual",
        "Propagacion transversal conservadora",
        "Union-dedupe",
        "Placeholders de plantilla",
        "Malla curricular de Derecho",
        "Sitio institucional UnADM"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta local exige identidad UnADM, citas verificables y conclusion con criterio propio."
        },
        {
          "source": "Carpeta de materia canonica",
          "target": "Plantillas y referencias locales",
          "kind": "supports",
          "justification": "El README define la carpeta como punto de entrada canonico."
        },
        {
          "source": "Planeacion semanal",
          "target": "Producto solicitado",
          "kind": "depends_on",
          "justification": "El programa analitico indica transformar la planeacion en productos concretos."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "El analisis debe partir de una tension juridica o social identificable."
        },
        {
          "source": "Conceptos juridicos",
          "target": "Marco normativo",
          "kind": "develops",
          "justification": "Los conceptos ordenan la lectura de normas, doctrina o datos pertinentes."
        },
        {
          "source": "Evidencia verificable",
          "target": "Postura academica",
          "kind": "supports",
          "justification": "La postura propia debe sostenerse con fuentes consultables."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion deriva del razonamiento aplicado al problema."
        },
        {
          "source": "JSON parseable",
          "target": "Propagacion transversal conservadora",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay reutilizacion segura."
        },
        {
          "source": "Normalizacion manual",
          "target": "Insumos no estructurados",
          "kind": "depends_on",
          "justification": "Las salidas no JSON deben aislarse y revisarse antes de usarse."
        },
        {
          "source": "Union-dedupe",
          "target": "Memoria persistente",
          "kind": "supports",
          "justification": "La compresion conserva reglas utiles sin duplicarlas."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Ubicacion curricular local",
          "kind": "supports",
          "justification": "El README cita el PDF de malla curricular como fuente de ubicacion."
        },
        {
          "source": "Placeholders de plantilla",
          "target": "Calidad LaTeX",
          "kind": "contrasts",
          "justification": "Los placeholders visibles contradicen una compilacion y publicacion limpias."
        },
        {
          "source": "Bibliografia local",
          "target": "Citas verificables",
          "kind": "supports",
          "justification": "El archivo .bib local centraliza fuentes base y especificas."
        },
        {
          "source": "Contenido tematico de otra asignatura",
          "target": "Identidad curricular local",
          "kind": "contrasts",
          "justification": "La transferencia transversal solo permite abstracciones estables, no temas ajenos."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 7, bloque 2, tipo electiva.",
        "README local: fuente curricular malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canonico.",
        "README local: integridad academica, citas verificables y conclusion juridica con criterio propio.",
        "Programa analitico local: productos con claridad, fundamento juridico, evidencia y transferencia profesional.",
        "Programa analitico local: transformar planeacion semanal en reportes, presentaciones y productos visuales.",
        "Programa analitico local: ejes de problema, conceptos, producto, analisis propio y conclusion.",
        "Bib local: unadmSitioWeb como fuente institucional.",
        "Bib local: unadmMallaDerecho2024 como fuente de malla curricular.",
        "Plantilla LaTeX local: article, spanish, letterpaper y oneside.",
        "Plantilla LaTeX local: curso LDE-S7B2 y portada academica.",
        "Origen estructurado: regla de no propagar salidas no JSON sin normalizacion.",
        "Origen estructurado: ejes editoriales problema, conceptos, evidencia, analisis propio y conclusion juridica.",
        "Transferencia transversal: solo abstracciones editoriales estables entre nodos no equivalentes."
      ]
    },
    "reinforcement_log": [
      "Ciclo 1 aplica sincronizacion transversal progresiva y conservadora.",
      "Se deduplicaron reglas repetidas de identidad, estructura, actividad y calidad.",
      "Se conservaron reglas locales de semestre 7 bloque 2 y tipo electiva.",
      "Se incorporaron solo abstracciones estables desde Filosofia del Derecho.",
      "Se excluyo bibliografia tematica de Filosofia del Derecho por falta de pertinencia local verificada.",
      "Se reforzo gate critico de JSON parseable antes de propagacion recursiva.",
      "Se mantuvo alerta historica sobre salidas no estructuradas de modelos previos.",
      "Se corrigio el grafo para usar relaciones permitidas: supports, contrasts, depends_on y develops.",
      "Se reforzo la separacion entre identidad institucional, estructura reusable y contenido tematico.",
      "Se preservo compresion lossless por union-dedupe sin recorte de reglas utiles."
    ]
  }
}