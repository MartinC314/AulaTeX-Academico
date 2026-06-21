{
  "summary": [
    "Se consolida transferencia lateral desde Actividad 1 a Actividad 6 con union-dedupe sin perdida.",
    "Se preserva identidad UnADM y ubicacion curricular verificada: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se refuerzan ejes editoriales comunes: problema, conceptos o normas, producto, analisis propio y conclusion juridica transferible.",
    "Se mantiene regla critica: bloquear propagacion si no hay JSON parseable y normalizar antes de reutilizar.",
    "Se conserva tratamiento provisional de fuentes heredadas no verificadas y de datos no visibles en consigna."
  ],
  "identity_rules": [
    "Mantener tono institucional UnADM en toda entrega.",
    "Alinear contenido a Licenciatura en Derecho y asignatura Filosofia del Derecho.",
    "Citar ubicacion curricular al contextualizar: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar regla de no regresion: no eliminar reglas utiles previas."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido y sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual de la actividad antes del desarrollo.",
    "Alinear formato de salida al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Adaptar la redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Distinguir sintesis de fuentes y postura propia del estudiante.",
    "Sustentar afirmaciones relevantes con fuentes verificables.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Relacionar conceptos, normas y doctrina con el problema planteado.",
    "Supuesto: si la consigna de Actividad 6 aborda interpretacion juridica, articular hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Separar reglas confirmadas de supuestos marcados.",
    "Verificar trazabilidad minima de afirmaciones relevantes a fuente o supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib activo.",
    "Revisar que la conclusion derive del desarrollo.",
    "Aplicar compresion lossless por union y deduplicacion."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en .tex.",
    "Comprobar que toda clave citada exista en el .bib usado.",
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico antes de fijar nombres canonicos.",
    "Marcar como supuesto cualquier nombre de archivo ambiguo hasta confirmacion."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas oficiales o academicas.",
    "Registrar fuentes especificas de la actividad en el .bib de la asignatura.",
    "Conservar metadatos minimos: autor, titulo, ano, editorial o nota, URL cuando exista.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No asumir que filosofia-del-derecho-clean.bib aplica automaticamente a Actividad 6."
  ],
  "propagation_hints": [
    "Propagar a nodos hermanos solo reglas reutilizables de identidad, estructura y calidad.",
    "No transferir redaccion literal ni conclusiones especificas entre actividades hermanas.",
    "Cuando falte consigna local, propagar estructura base y abrir preguntas.",
    "Mantener advertencias historicas sobre salidas no estructuradas en ciclos previos.",
    "Aplicar validacion JSON previa a toda propagacion recursiva.",
    "Conservar union-dedupe lossless en cada ciclo."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 6; confirmar producto exacto requerido.",
    "Confirmar rubrica de evaluacion especifica para calibrar profundidad argumentativa.",
    "Confirmar si Actividad 6 exige reporte, presentacion o ambos.",
    "Confirmar nombre canonico final del .bib por token Slug no resuelto en README.",
    "Confirmar si se reutiliza bibliografia depurada de interpretacion juridica o se requiere corpus propio.",
    "Confirmar si hay formato de citacion juridica adicional a BibTeX institucional."
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
      "Problema juridico delimitado.",
      "Conceptos y normas pertinentes.",
      "Producto alineado a planeacion semanal.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos solidos y verificables.",
      "Asegurar coherencia entre identidad institucional, rigor juridico y utilidad profesional."
    ],
    "style_markers": [
      "Encuadre inicial breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Citas verificables con trazabilidad.",
      "Diferenciacion clara entre fuente y postura propia.",
      "Cierre con criterio juridico aplicable."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual y normativo.",
      "Contrastar fuentes relevantes.",
      "Tomar postura fundamentada.",
      "Concluir desde el analisis y no por formula decorativa."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion estructurada",
        "Validacion JSON"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/programa-analitico-filosofia-del-derecho.md"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y rigor editorial."
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
          "justification": "La conclusion debe derivar del desarrollo argumentativo."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Validacion JSON",
          "kind": "supports",
          "justification": "La propagacion recursiva exige salida estructurada y parseable."
        }
      ],
      "evidence": [
        "README: define identidad UnADM, entrada canonica y pauta editorial.",
        "Programa analitico: fija cinco ejes de trabajo recurrentes.",
        "Historial de ciclos: registra incidentes de salida no JSON y necesidad de normalizacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 10: se deduplican reglas repetidas sin recorte de contenido util.",
      "Ciclo 10: se preservan reglas nucleares de identidad, estructura, calidad y bibliografia.",
      "Ciclo 10: se evita transferir conclusiones especificas de Actividad 1 hacia Actividad 6.",
      "Ciclo 10: se mantienen supuestos explicitos donde falta consigna local verificable."
    ]
  }
}