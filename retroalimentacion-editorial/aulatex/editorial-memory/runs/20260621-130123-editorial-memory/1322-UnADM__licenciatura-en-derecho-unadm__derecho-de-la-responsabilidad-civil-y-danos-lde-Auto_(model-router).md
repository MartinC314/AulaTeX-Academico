```json
{
  "summary": [
    "Se consolida cerebro editorial de materia con identidad UnADM.",
    "Se sincronizan abstracciones estables desde actividad transversal.",
    "Se refuerzan ejes editoriales reutilizables sin traslado temático.",
    "Se preservan alertas técnicas y control de normalización JSON.",
    "Compresión aplicada por unión y deduplicación, sin regresión."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar contexto confirmado: Licenciatura en Derecho, semestre 6, bloque 1, obligatoria, 8 créditos.",
    "Usar la carpeta de la materia como entrada canónica.",
    "Marcar como supuesto cualquier dato no confirmado por guía oficial.",
    "Tratar memorias heredadas no verificadas como provisionales.",
    "No declarar códigos o convenciones como oficiales sin fuente documental."
  ],
  "structure_rules": [
    "Iniciar cada entrega con encuadre breve del problema jurídico.",
    "Separar secciones: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear cada producto a la planeación semanal y consigna vigente.",
    "Mantener separación editorial entre reporte, presentación, programa analítico y .bib.",
    "Definir objetivo puntual antes del desarrollo."
  ],
  "activity_rules": [
    "Formular problema jurídico activador de responsabilidad civil y daño.",
    "Integrar conceptos, normas y doctrina pertinentes a la actividad.",
    "Incluir análisis propio con postura argumentada del estudiante.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Evitar arrastre de contenido temático no compatible."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de reutilizar.",
    "Verificar que toda afirmación tenga fuente o marca de análisis propio.",
    "Validar metadatos curriculares contra la malla local.",
    "Detectar rutas truncadas, placeholders y caracteres rotos.",
    "Aplicar control de no regresión sobre reglas útiles heredadas."
  ],
  "latex_rules": [
    "Usar español con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Completar plantillas antes de compilar.",
    "Verificar nombres de archivos y rutas canónicas.",
    "Compilar sin errores críticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "No inventar referencias; registrar vacíos como preguntas abiertas.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Registrar fuentes específicas en el .bib local de la materia."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables.",
    "Evitar transferir redacción literal entre nodos no equivalentes.",
    "Propagar recursivamente tras validación de JSON y estructura.",
    "Mantener alerta de normalización manual en ciclo 1.",
    "Conservar reglas institucionales sin reducir especificidad local."
  ],
  "open_questions": [
    "Confirmar guía oficial de formato para actividades de la materia.",
    "Confirmar convención definitiva de nombres con danos/daños.",
    "Confirmar código de curso oficial con documento institucional.",
    "Validar y completar plantilla .tex truncada.",
    "Confirmar fuentes obligatorias por semana."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico",
        "Claro y jurídicamente preciso",
        "Argumentativo con criterio propio"
      ],
      "institutional": [
        "Alineación explícita con UnADM",
        "Integridad académica con citas verificables",
        "Entrada canónica por carpeta de materia"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Semestre 6, bloque 1, obligatoria, 8 créditos",
        "Asignatura: Derecho de la responsabilidad civil y daños"
      ]
    },
    "essence": [
      "Problema jurídico como eje activador",
      "Marco normativo y doctrinal verificable",
      "Análisis propio del estudiante",
      "Conclusión jurídica aplicada",
      "Transferencia a la práctica profesional"
    ],
    "reason_for_being": [
      "Orientar productos académicos claros, fundamentados y transferibles.",
      "Estandarizar estructura y calidad editorial.",
      "Garantizar reutilización segura del conocimiento."
    ],
    "style_markers": [
      "Declarar supuestos explícitamente",
      "Estructura seccional constante",
      "Cierre con utilidad profesional",
      "Separación estricta de tipos de artefacto"
    ],
    "argumentative_patterns": [
      "Problema → marco → análisis → conclusión",
      "Contraste de fuentes y postura propia",
      "Aplicación práctica del criterio jurídico"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización estructurada JSON",
        "Problema jurídico",
        "Marco normativo/doctrinal",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Responsabilidad civil",
        "Daño"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere una pregunta jurídica definida."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión se sustenta en normas y doctrina."
        },
        {
          "source": "Responsabilidad civil",
          "target": "Daño",
          "kind": "depends_on",
          "justification": "La responsabilidad se articula a partir del daño."
        },
        {
          "source": "Normalización estructurada JSON",
          "target": "Propagación segura",
          "kind": "supports",
          "justification": "Evita reutilizar salidas ambiguas o no parseables."
        }
      ],
      "evidence": [
        "README y programa analítico locales",
        "Archivo .bib institucional",
        "Plantilla .tex local con alertas técnicas",
        "Reglas editoriales heredadas sin regresión"
      ]
    },
    "reinforcement_log": [
      "Se sincronizan ejes editoriales transversales.",
      "Se refuerza identidad UnADM en nodo de materia.",
      "Se preservan alertas técnicas verificables.",
      "Se mantiene compresión lossless por deduplicación."
    ]
  }
}
```