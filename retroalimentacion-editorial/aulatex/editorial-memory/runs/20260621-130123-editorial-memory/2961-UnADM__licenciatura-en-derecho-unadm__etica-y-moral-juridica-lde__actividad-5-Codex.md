{
  "summary": [
    "Se refuerza memoria lateral con patrones reutilizables verificados entre asignaturas UnADM.",
    "Se preservan reglas útiles previas y se elimina duplicidad semántica sin recorte de contenido válido.",
    "Se mantiene normalización obligatoria: salida JSON parseable antes de toda propagación recursiva.",
    "Se consolida eje editorial común: problema, conceptos, evidencia, análisis propio y conclusión jurídica transferible.",
    "Se integra control de supuestos para todo dato no visible en la consigna local.",
    "Se incorpora incidencia local verificable: tokens Slug sin expandir en README y programa analítico.",
    "Se incorpora incidencia local verificable: entradas BibTeX duplicadas por misma obra con claves distintas.",
    "Se mantiene trazabilidad de injertos entre origen y destino con estado provisional cuando aplique."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y trazabilidad.",
    "Vincular cada entrega a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura destino como entrada canónica.",
    "Alinear explícitamente la actividad a Ética y Moral jurídica, Actividad 5.",
    "Marcar como [supuesto] todo dato no visible en consigna, rúbrica o planeación local.",
    "Tratar como provisionales reglas provenientes de salidas no parseables hasta validación manual.",
    "Registrar origen-destino de cada transferencia lateral para auditoría editorial."
  ],
  "structure_rules": [
    "Responder siempre con JSON válido y parseable según esquema requerido.",
    "Usar frases cortas, accionables y sin duplicados.",
    "Conservar reglas previas útiles y agregar solo mejoras verificables.",
    "Aplicar compresión lossless por unión y deduplicación, no por recorte.",
    "Definir objetivo puntual antes del desarrollo del contenido académico.",
    "Mantener macrosecciones: problema, conceptos, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear estructura final al producto solicitado por la consigna de Actividad 5."
  ],
  "activity_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir conceptos operativos pertinentes al dilema ético-jurídico tratado.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "No trasladar conclusiones específicas de Filosofía del Derecho sin justificación local."
  ],
  "quality_gates": [
    "Bloquear propagación recursiva si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de fusionar memoria.",
    "Confirmar que no se eliminen reglas útiles previas en cada ciclo.",
    "Validar ausencia de duplicados semánticos tras la fusión.",
    "Exigir respaldo o marca [supuesto] en toda afirmación no verificable localmente.",
    "Validar correspondencia entre citas en texto y claves del .bib.",
    "Registrar incidencias técnicas por ciclo con plantilla única deduplicada."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilación.",
    "Evitar comandos o paquetes no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Corregir rutas o nombres con caracteres anómalos antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "No copiar bloques LaTeX completos entre nodos; transferir solo patrón estructural."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar fuentes específicas de Actividad 5 en etica-y-moral-juridica.bib.",
    "No inventar referencias ni metadatos bibliográficos.",
    "Conservar metadatos mínimos: autor o editor, título, año, editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Marcar para revisión manual entradas potencialmente duplicadas por autor+título+año.",
    "Depurar duplicados solo tras validación manual para no perder trazabilidad de claves usadas."
  ],
  "propagation_hints": [
    "Propagar lateralmente solo patrones generales reutilizables, no redacción literal.",
    "Mantener analogía controlada: transferir método, no contenido temático específico.",
    "Priorizar reglas de identidad, estructura y calidad cuando falte consigna textual.",
    "Si hay conflicto entre reglas, conservar la más restrictiva y verificable.",
    "Mantener bitácora de ciclos con estado parseable/no-parseable para decisiones futuras.",
    "Escalar a revisión manual tras fallos consecutivos de parseo [supuesto: umbral por definir]."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 5.",
    "Confirmar rúbrica de evaluación específica para calibrar profundidad argumentativa.",
    "Confirmar si el producto final requerido es reporte, presentación u otro formato.",
    "Definir umbral operativo de bloqueo automático tras fallos consecutivos de parseo [supuesto].",
    "Confirmar política local de consolidación de claves BibTeX duplicadas sin romper citas previas.",
    "Confirmar si todos los tokens Slug del README/programa deben resolverse en preproceso."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Reflexivo ante dilemas ético-jurídicos."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Carpeta de asignatura como entrada canónica.",
        "Trazabilidad de memoria editorial y fuentes."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos.",
        "Asignatura destino: Ética y Moral jurídica.",
        "Actividad destino: Actividad 5."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos y marco normativo/doctrinal pertinente.",
      "Evidencia verificable.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos claros, fundados y útiles para práctica jurídica.",
      "Sostener consistencia editorial entre nodos sin perder especificidad local.",
      "Asegurar calidad técnica y trazabilidad documental en todo ciclo de propagación."
    ],
    "style_markers": [
      "Objetivo puntual al inicio.",
      "Secciones explícitas y ordenadas.",
      "Supuestos marcados cuando falte evidencia local.",
      "Citas verificables en afirmaciones sustantivas.",
      "Cierre con criterio jurídico propio."
    ],
    "argumentative_patterns": [
      "Plantear problema y alcance.",
      "Definir conceptos operativos.",
      "Vincular norma o doctrina aplicable.",
      "Contrastar posturas y justificar posición propia.",
      "Concluir con implicación jurídica práctica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad académica",
        "Normalización JSON",
        "Deduplicación lossless",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Consigna local de Actividad 5",
        "Trazabilidad bibliográfica"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/programa-analitico-etica-y-moral-juridica.md",
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/etica-y-moral-juridica.bib"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y trazabilidad."
        },
        {
          "source": "Normalización JSON",
          "target": "Deduplicación lossless",
          "kind": "depends_on",
          "justification": "La fusión confiable requiere estructura parseable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "La postura argumentativa se sostiene en fuentes consultables."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "La conclusión profesional deriva del razonamiento crítico."
        },
        {
          "source": "Consigna local de Actividad 5",
          "target": "Conclusión jurídica transferible",
          "kind": "depends_on",
          "justification": "El alcance final debe ajustarse al producto y rúbrica locales."
        }
      ],
      "evidence": [
        "README confirma identidad UnADM, ubicación curricular y pauta editorial.",
        "Programa analítico confirma ejes de trabajo y propósito de realización.",
        "README y programa muestran token Slug sin expandir, incidencia técnica verificable.",
        "Archivo .bib muestra entradas duplicadas por misma obra con claves distintas."
      ]
    },
    "reinforcement_log": [
      "Ciclo 15: se refuerza transferencia lateral por analogía controlada entre asignaturas.",
      "Ciclo 15: se deduplican reglas repetidas manteniendo cobertura total de criterios útiles.",
      "Ciclo 15: se preserva bloqueo por no-JSON parseable como compuerta crítica.",
      "Ciclo 15: se agregan incidencias técnicas locales verificables sin inventar fuentes.",
      "Ciclo 15: se mantiene estado provisional para reglas no verificadas localmente."
    ]
  }
}