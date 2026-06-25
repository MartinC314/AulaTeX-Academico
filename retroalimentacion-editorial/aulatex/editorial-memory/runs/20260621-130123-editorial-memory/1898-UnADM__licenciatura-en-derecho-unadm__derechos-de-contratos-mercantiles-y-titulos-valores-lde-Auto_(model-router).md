{
  "summary": [
    "Materia destino UnADM Derecho: semestre 6, bloque 2, obligatoria, 8 créditos.",
    "La carpeta de materia es punto de entrada canónico para README, programa, plantillas y bibliografía local.",
    "La pauta local exige identidad UnADM, integridad académica, citas verificables y conclusión jurídica propia.",
    "Existe bibliografía local confirmada en derechos-de-contratos-mercantiles-y-titulos-valores.bib.",
    "Se conserva el eje transversal: problema, conceptos o normas, evidencia, análisis propio y conclusión transferible.",
    "Se mantiene alerta institucional por salidas no JSON parseable hasta confirmación de resolución.",
    "Se aplica transferencia conservadora desde Filosofía del Derecho: solo abstracciones editoriales estables.",
    "No se transfiere contenido temático específico de Filosofía del Derecho a Contratos Mercantiles."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, metadatos y redacción académica.",
    "Alinear entregables a la Licenciatura en Derecho.",
    "Alinear contenidos a Derechos de contratos mercantiles y títulos valores.",
    "Conservar tono jurídico-formal.",
    "Cerrar con postura académica propia y criterio jurídico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Etiquetar como provisionales las fuentes heredadas no confirmadas.",
    "Fuente provisional heredada: Codex desde ingeniería-en-sistemas-computacionales.",
    "Fuente provisional heredada: GPT-Pro desde Actividad 1."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como nodo canónico.",
    "Mantener consistencia entre README, programa analítico, .tex y .bib.",
    "Definir objetivo puntual antes del desarrollo.",
    "Abrir cada actividad con encuadre breve del problema jurídico o social.",
    "Separar desarrollo en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Desarrollar el producto solicitado por la planeación semanal.",
    "Distinguir evidencia citada de interpretación propia.",
    "Incluir transferencia profesional en el cierre.",
    "Corregir en README los nombres truncados de reporte y referencias.",
    "Sustituir placeholders de slug por nombres reales de archivo."
  ],
  "activity_rules": [
    "Contextualizar cada actividad con problema concreto y delimitado.",
    "Vincular argumentos con normas, doctrina o datos verificables.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guía, argumentos y cierre.",
    "Alinear formato final al producto pedido en la planeación semanal.",
    "Cerrar cada entrega con conclusión jurídica aplicable a la práctica profesional."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar que no haya regresión de reglas útiles heredadas.",
    "Comprobar trazabilidad entre afirmaciones y fuentes citadas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Verificar que no se agreguen fuentes inventadas.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar que README y programa apunten al .bib local real.",
    "Validar compilación después de ajustar nombres de archivos y macros."
  ],
  "latex_rules": [
    "Conservar plantilla base de reporte de la materia.",
    "Completar metadatos del curso en cada entrega.",
    "Mantener nomenclatura consistente para reporte y presentación.",
    "Usar español correcto con acentos consistentes en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Corregir macros incompletas o truncadas antes de compilar.",
    "Revisar y completar la macro truncada \\def\\universitydepartmen en la plantilla.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derechos-de-contratos-mercantiles-y-titulos-valores.bib como archivo local confirmado.",
    "Registrar fuentes específicas de actividad en el .bib local de la materia.",
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Conservar entradas existentes unadmSitioWeb y unadmMallaDerecho2024.",
    "No incorporar fuentes no verificadas ni inventadas.",
    "Agregar al .bib solo fuentes realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Agregar fecha de consulta cuando se usen recursos web.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Citar malla-curricular-derecho-unadm.pdf como fuente de ubicación curricular cuando se use el dato curricular."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo reglas normalizadas y sin duplicados.",
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Usar compresión unión-dedupe lossless en cada fusión de memoria.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "No propagar detalles locales de archivo si no aplican a materias laterales.",
    "Propagar lateralmente solo pautas académicas transversales.",
    "Mantener alerta de normalización manual registrada en ciclos 1 a 6 si se reutiliza.",
    "Ciclo 13 refuerza transferencia conservadora entre nodos transversales.",
    "Evitar transferir fuentes o temas específicos de Filosofía del Derecho al destino mercantil."
  ],
  "open_questions": [
    "Confirmar si la incidencia histórica de salida no JSON parseable ya fue resuelta.",
    "Definir plantilla oficial de presentación si difiere del reporte.",
    "Verificar nombre final del archivo .bib generado por slug.",
    "Confirmar si ya se corrigieron en README los nombres truncados de archivos.",
    "Confirmar resolución definitiva de placeholders de slug en README y programa.",
    "Verificar si el README debe listar referencias como carpeta o archivo.",
    "Confirmar si el sitio UnADM debe conservar year 2026 o usar fecha de consulta solamente.",
    "Completar el resto de la plantilla .tex para revisar macros faltantes.",
    "Confirmar fuentes obligatorias por actividad local.",
    "Confirmar rúbrica específica de cada actividad antes de ajustar profundidad argumentativa."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Claro y aplicable a práctica profesional."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Carpeta canónica como punto de entrada.",
        "Normalización estructurada antes de propagar.",
        "Fuentes heredadas tratadas como provisionales hasta confirmación local."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 2, obligatoria, 8 créditos.",
        "Materia: Derechos de contratos mercantiles y títulos valores.",
        "Bibliografía local: derechos-de-contratos-mercantiles-y-titulos-valores.bib.",
        "Fuente curricular local: UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Integridad académica.",
      "Problema jurídico concreto.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible.",
      "Consistencia entre consigna, desarrollo y cierre.",
      "Producto solicitado por la planeación.",
      "Transferencia profesional."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Transformar la planeación semanal en reportes, presentaciones o productos visuales.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Sostener una memoria editorial estable para actividades mercantiles futuras.",
      "Evitar propagación de contenido no verificado o no estructurado."
    ],
    "style_markers": [
      "Apertura breve con problema.",
      "Objetivo explícito antes del desarrollo.",
      "Secciones ordenadas y reconocibles.",
      "Marco normativo o doctrinal visible.",
      "Citas explícitas para afirmaciones sustantivas.",
      "Distinción entre evidencia y postura propia.",
      "Supuestos marcados cuando falte evidencia.",
      "Cierre con implicación profesional.",
      "Tono jurídico-formal sin relleno descriptivo.",
      "Nomenclatura documental consistente."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual y normativo -> evidencia -> análisis propio -> conclusión.",
      "Afirmación jurídica -> fuente verificable -> interpretación propia.",
      "Consigna -> producto esperado -> desarrollo alineado -> cierre evaluable.",
      "Dato no visible -> marca de supuesto -> confirmación pendiente.",
      "Fuente heredada -> etiqueta provisional -> verificación local.",
      "Archivo o macro dudosa -> revisión -> compilación validada."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Derechos de contratos mercantiles y títulos valores",
        "Ubicación curricular",
        "Carpeta canónica de materia",
        "Integridad académica",
        "Citas verificables",
        "Problema jurídico",
        "Marco normativo o doctrinal",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión transferible",
        "Producto solicitado por planeación",
        "Normalización estructurada",
        "JSON parseable",
        "Bibliografía local",
        "Metadatos LaTeX",
        "Nomenclatura de archivos",
        "Placeholders de slug",
        "Macros truncadas"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta local exige identidad UnADM, citas verificables y criterio propio."
        },
        {
          "source": "Licenciatura en Derecho",
          "target": "Derechos de contratos mercantiles y títulos valores",
          "kind": "develops",
          "justification": "La materia pertenece al plan de Derecho según README y programa local."
        },
        {
          "source": "Ubicación curricular",
          "target": "unadmMallaDerecho2024",
          "kind": "depends_on",
          "justification": "El README remite a la malla curricular como fuente del semestre, bloque, tipo y créditos."
        },
        {
          "source": "Carpeta canónica de materia",
          "target": "Bibliografía local",
          "kind": "supports",
          "justification": "La carpeta contiene el .bib local confirmado para la materia."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "Sin problema delimitado no hay argumentación pertinente."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "El cierre profesional requiere fundamento jurídico explícito."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Las afirmaciones deben tener respaldo o marca de supuesto."
        },
        {
          "source": "Producto solicitado por planeación",
          "target": "Nomenclatura de archivos",
          "kind": "depends_on",
          "justification": "El formato final debe corresponder a reporte, presentación u otro producto pedido."
        },
        {
          "source": "Normalización estructurada",
          "target": "JSON parseable",
          "kind": "depends_on",
          "justification": "La propagación recursiva solo es segura con estructura válida."
        },
        {
          "source": "Placeholders de slug",
          "target": "Nomenclatura de archivos",
          "kind": "contrasts",
          "justification": "Los tokens sin resolver contradicen la nomenclatura real esperada."
        },
        {
          "source": "Macros truncadas",
          "target": "Metadatos LaTeX",
          "kind": "contrasts",
          "justification": "Una macro incompleta puede romper compilación y metadatos del documento."
        },
        {
          "source": "Bibliografía local",
          "target": "Citas verificables",
          "kind": "supports",
          "justification": "El .bib local permite trazar fuentes institucionales y específicas."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 6, bloque 2, obligatoria, 8 créditos.",
        "README local: fuente curricular en UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico de la asignatura.",
        "README local: exige identidad UnADM, integridad académica, citas verificables y conclusión jurídica propia.",
        "README local: contiene nombres truncados de reporte y referencias.",
        "README local: contiene placeholder de slug sin resolver para .bib.",
        "Programa local: orienta productos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa local: propósito de transformar planeación en reportes, presentaciones y productos visuales.",
        "Programa local: ejes de trabajo con problema, conceptos, producto, análisis y conclusión.",
        ".bib local: contiene unadmSitioWeb.",
        ".bib local: contiene unadmMallaDerecho2024.",
        "Plantilla local: define curso LDE-S6B2.",
        "Plantilla local: contiene macro truncada \\def\\universitydepartmen.",
        "Memoria institucional heredada: salida sin JSON parseable desde Codex.",
        "Memoria destino previa: salida sin JSON parseable desde GPT-Pro para la materia."
      ]
    },
    "reinforcement_log": [
      "Ciclo 13 consolida memoria transversal en la materia destino.",
      "Se deduplican reglas repetidas sin eliminar contenido útil.",
      "Se preserva identidad UnADM y ubicación curricular local.",
      "Se refuerza la estructura problema, marco, evidencia, análisis y cierre.",
      "Se conserva alerta de JSON parseable antes de propagar.",
      "Se mantiene estrategia progresiva y conservadora.",
      "Se evita transferir citas y conceptos temáticos de Filosofía del Derecho.",
      "Se agregan conexiones verificables entre bibliografía local, citas y calidad.",
      "Se refuerzan incidencias locales de README, slug y macro truncada.",
      "Se dejan abiertos vacíos que requieren confirmación local."
    ]
  }
}