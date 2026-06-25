{
  "summary": [
    "Se refuerza actividad-2 con patrones reutilizables de actividad-1 sin copiar contenido exclusivo.",
    "Se mantiene compresion lossless por union y deduplicacion, sin recorte ni regresion.",
    "Se conserva normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se consolidan ejes troncales: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se preserva caracter provisional de fuentes heredadas no verificadas y se marca como supuesto cuando falten datos locales."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y cierre.",
    "Vincular actividad-2 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Mantener integridad academica con citas verificables."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual de la actividad antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el desarrollo al producto solicitado por la planeacion semanal.",
    "Diferenciar postura propia, cita textual y parafrasis.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Ajustar actividad-2 a la instruccion docente disponible.",
    "Evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir tema, semana o formato de actividad-2 sin evidencia local.",
    "No reutilizar automaticamente bibliografia de semana 7 si la consigna no lo requiere."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de reutilizarlas.",
    "Confirmar que cada afirmacion sustantiva tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No eliminar reglas utiles previas; solo unir y deduplicar."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables y no renombrar claves ya citadas.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Verificar rutas y nombres canonicos de archivos antes de referenciarlos.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: archivo .bib canonico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y malla curricular de Derecho como contexto base.",
    "Agregar fuentes especificas de actividad-2 en el .bib canonico de la asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, año y fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib es complementario tematico y no reemplazo automatico del .bib canonico."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones reutilizables entre hermanos.",
    "Evitar copiar redaccion literal, conclusiones especificas o bibliografia exclusiva.",
    "Mantener reglas institucionales UnADM sin perder especificidad local.",
    "Aplicar normalizacion manual cuando reaparezcan entradas no estructuradas.",
    "Registrar como provisionales los antecedentes Codex y GPT-Pro hasta verificacion local."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-2: tema, semana y producto final.",
    "Confirmar si existe plantilla obligatoria de secciones para actividad-2.",
    "Confirmar estilo de citacion obligatorio institucional. [supuesto: no confirmado]",
    "Confirmar si actividad-2 requiere reporte, presentacion u otro formato.",
    "Confirmar nombre canonico final del .bib de la asignatura.",
    "Confirmar si la bibliografia de interpretacion juridica aplica a actividad-2 o solo a semana 7."
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
        "Integridad academica y citas verificables.",
        "Carpeta de asignatura como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Filosofia del Derecho."
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
      "Transformar planeacion semanal en productos academicos trazables y argumentados.",
      "Asegurar transferencia lateral controlada entre actividades hermanas.",
      "Preservar continuidad editorial sin copiar contenidos exclusivos."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales y trazables.",
      "Postura propia explicitada.",
      "Supuestos marcados de forma visible.",
      "Cierre juridico transferible."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos y fuentes -> analisis -> conclusion.",
      "Afirmacion juridica -> evidencia verificable -> interpretacion propia.",
      "Consigna local -> adecuacion de formato -> verificacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion de salidas",
        "Ejes editoriales troncales",
        "Integridad academica",
        "Trazabilidad cita-bibliografia",
        "Transferencia lateral controlada"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/programa-analitico-filosofia-del-derecho.md"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Ejes editoriales troncales",
          "kind": "supports",
          "justification": "Define tono, finalidad y coherencia del producto."
        },
        {
          "source": "Normalizacion de salidas",
          "target": "Transferencia lateral controlada",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay propagacion segura."
        },
        {
          "source": "Trazabilidad cita-bibliografia",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Permite verificar respaldo de afirmaciones."
        },
        {
          "source": "Ejes editoriales troncales",
          "target": "Actividad-2",
          "kind": "develops",
          "justification": "Son patrones reutilizables entre nodos hermanos."
        }
      ],
      "evidence": [
        "README fija identidad UnADM, integridad academica y conclusion juridica.",
        "Programa analitico fija proposito y ejes transferibles.",
        "Regla persistente: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 19: se refuerza transferencia por analogia controlada entre hermanos.",
      "Ciclo 19: se deduplican reglas repetidas manteniendo cobertura total.",
      "Ciclo 19: se preserva herencia valida y se evita mover contenido exclusivo de actividad-1.",
      "Ciclo 19: se mantienen abiertas preguntas locales cuando faltan datos verificables."
    ]
  }
}