```json
{
  "summary": [
    "Se sincroniza ADN editorial transversal desde actividad origen hacia materia destino.",
    "Se preservan ejes editoriales estables: problema, conceptos o normas, evidencia, análisis propio y conclusión jurídica.",
    "Se refuerza identidad institucional UnADM y normalización estructural obligatoria.",
    "Se consolida memoria mínima de materia con enfoque progresivo y conservador."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en todo entregable.",
    "Alinear contenidos a Licenciatura en Derecho y a la materia destino.",
    "Conservar tono jurídico-formal con postura académica propia.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Etiquetar fuentes heredadas no verificadas como provisionales."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como nodo canónico.",
    "Estructurar actividades en: problema, conceptos o normas, desarrollo del producto, análisis propio y conclusión.",
    "Mantener consistencia entre README, programa analítico, .tex y .bib.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Vincular argumentos con normas, doctrina o datos verificables.",
    "Distinguir evidencia citada de análisis propio.",
    "Evitar entregas meramente descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar trazabilidad entre afirmaciones y fuentes.",
    "Verificar correspondencia con la consigna específica.",
    "Evitar regresión de reglas útiles heredadas."
  ],
  "latex_rules": [
    "Mantener codificación correcta para español en .tex y .bib.",
    "Usar nomenclatura consistente de archivos por asignatura.",
    "Corregir macros truncadas antes de compilar.",
    "Compilar sin errores críticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar el .bib local confirmado de la materia destino.",
    "Registrar fuentes específicas por actividad.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos verificables.",
    "Agregar fecha de consulta en recursos web."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables.",
    "Aplicar compresión union-dedupe sin pérdida.",
    "Evitar transferir redacción literal entre nodos no equivalentes.",
    "Mantener alerta institucional de normalización manual en ciclo 1."
  ],
  "open_questions": [
    "Confirmar consignas y rúbricas reales de actividades de la materia destino.",
    "Verificar resolución histórica de salidas no JSON parseables.",
    "Confirmar plantilla oficial de presentación si difiere del reporte.",
    "Validar nombres finales de archivos y slugs."
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
        "Integridad académica",
        "Carpeta de materia como entrada canónica"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Semestre 6, bloque 2, obligatoria, 8 créditos",
        "Derechos de contratos mercantiles y títulos valores"
      ]
    },
    "essence": [
      "Problema jurídico como punto de partida",
      "Marco normativo y conceptual verificable",
      "Análisis propio del estudiante",
      "Conclusión jurídica aplicable"
    ],
    "reason_for_being": [
      "Estandarizar productos académicos con identidad UnADM",
      "Garantizar trazabilidad entre fuentes, análisis y conclusión",
      "Facilitar transferencia profesional del aprendizaje"
    ],
    "style_markers": [
      "Secciones claras y orden argumentativo estable",
      "Supuestos explícitos",
      "Cierre con criterio jurídico propio"
    ],
    "argumentative_patterns": [
      "Delimitar problema",
      "Definir conceptos y normas",
      "Contrastar evidencia",
      "Emitir análisis propio",
      "Concluir con aplicabilidad profesional"
    ],
    "knowledge_graph": {
      "concepts": [
        "identidad institucional UnADM",
        "integridad académica",
        "problema jurídico",
        "análisis propio",
        "conclusión jurídica transferible"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "problema jurídico",
          "target": "análisis propio",
          "kind": "develops",
          "justification": "El análisis se construye a partir del problema delimitado."
        },
        {
          "source": "integridad académica",
          "target": "conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión depende de fuentes y análisis verificables."
        }
      ],
      "evidence": [
        "README y programa analítico de la materia destino",
        ".bib local con fuentes institucionales UnADM"
      ]
    },
    "reinforcement_log": [
      "Se refuerzan ejes editoriales transversales sin eliminar reglas previas.",
      "Se preserva la alerta institucional sobre normalización JSON.",
      "Se consolida cerebro editorial mínimo para materia destino."
    ]
  }
}
```