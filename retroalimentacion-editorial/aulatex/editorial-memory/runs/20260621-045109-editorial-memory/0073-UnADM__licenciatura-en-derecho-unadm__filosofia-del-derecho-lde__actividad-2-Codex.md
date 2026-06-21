{
  "summary": [
    "Se consolida memoria de actividad-2 con transferencia lateral controlada desde actividad-1.",
    "Se preservan reglas validas previas con union-dedupe lossless y sin regresion.",
    "Se refuerza normalizacion obligatoria antes de propagacion recursiva.",
    "Se mantienen ejes troncales: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se evita copiar contenido exclusivo de actividad-1; solo se transfieren patrones reutilizables.",
    "Se mantiene estado provisional de fuentes heredadas no verificadas localmente."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular actividad-2 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Redactar con enfoque academico-juridico y transferencia a practica profesional.",
    "Incluir conclusion juridica con criterio propio.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto pedido en la planeacion semanal.",
    "Diferenciar postura propia, cita textual y parafrasis.",
    "Cerrar con conclusion transferible a la practica juridica."
  ],
  "activity_rules": [
    "Ajustar actividad-2 a la consigna docente disponible.",
    "No asumir tema, semana ni formato sin evidencia local.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Usar fuentes de hermeneutica o argumentacion solo si la consigna lo requiere."
  ],
  "quality_gates": [
    "Bloquear propagacion si salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "No eliminar reglas utiles previas; solo unir y deduplicar.",
    "Exigir respaldo o marca de supuesto en cada afirmacion sustantiva.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar correspondencia del producto con consigna local de actividad-2."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Verificar rutas y nombres de archivo antes de referenciar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: .bib canonico esperado es filosofia-del-derecho.bib por Slug local."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y malla curricular como contexto base.",
    "Registrar fuentes especificas de actividad-2 en el .bib canonico de la asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base vs bibliografia especifica de actividad.",
    "Tratar filosofia-del-derecho-clean.bib como complemento tematico, no reemplazo automatico.",
    "Supuesto: filosofia-del-derecho-clean.bib esta orientado a Semana 7 y aplica solo si consigna coincide."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir entre hermanos solo identidad, estructura, calidad y patrones argumentativos reutilizables.",
    "No propagar conclusiones ni bibliografia exclusiva de un hermano a otro.",
    "Aplicar union-dedupe lossless en cada ciclo.",
    "Mantener historial de herencia provisional sin volverlo regla definitiva.",
    "Si faltan datos locales, propagar plantilla base y preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-2: tema, semana y producto.",
    "Confirmar plantilla obligatoria de secciones definida por docente.",
    "Confirmar si hay estilo de citacion institucional obligatorio. [supuesto: no confirmado]",
    "Confirmar nombre canonico final del .bib de asignatura.",
    "Confirmar si actividad-2 reutiliza bibliografia existente o requiere .bib propio."
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
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Filosofia del Derecho."
      ]
    },
    "essence": [
      "Problema juridico o social activa el trabajo.",
      "Conceptos y fuentes sustentan el analisis.",
      "Postura propia evita resumen pasivo.",
      "Cierre juridico transfiere a practica profesional.",
      "Normalizacion estructurada habilita propagacion segura."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables.",
      "Sostener continuidad editorial entre actividades sin copiar contenido especifico.",
      "Proteger calidad institucional en ciclos recursivos."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales y trazables.",
      "Marcado explicito de supuestos.",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> analisis -> conclusion.",
      "Afirmacion juridica -> evidencia verificable -> interpretacion propia.",
      "Consigna local -> adaptacion de formato -> verificacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales troncales",
        "Normalizacion de salidas",
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
          "justification": "Define tono, formato y finalidad comun."
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
          "justification": "Permite verificar respaldo real de afirmaciones."
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
        "Programa analitico fija proposito y ejes de trabajo.",
        "Regla historica valida: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 73: se refuerza transferencia por analogia controlada entre hermanos.",
      "Ciclo 73: se mantiene deduplicacion lossless sin recorte de reglas utiles.",
      "Ciclo 73: se consolida frontera entre patrones transferibles y contenido no transferible.",
      "Ciclo 73: se preserva caracter provisional de fuentes heredadas no verificadas."
    ]
  }
}