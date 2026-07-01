{
  "summary": [
    "Materia destino con identidad UnADM y enfoque jurídico aplicado.",
    "Asignatura de Licenciatura en Derecho, semestre 3, bloque 1.",
    "Materia obligatoria seriada de 8 créditos según malla curricular local.",
    "La carpeta local es punto de entrada canónico de la asignatura.",
    "Se consolida sincronización transversal por abstracciones editoriales estables.",
    "Se preservan ejes comunes: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se evita trasladar contenido temático de Filosofía del Derecho sin validación local.",
    "Se conserva alerta por salidas heredadas no JSON parseable.",
    "Se exige normalización manual antes de propagación automática.",
    "README local contiene nombres de archivo corruptos que requieren corrección.",
    "Plantilla local registra alumno Martin Jonathan de la Cruz y matrícula ES2611202040. [supuesto verificar vigencia]"
  ],
  "identity_rules": [
    "Mantener identidad UnADM en portada, redacción y metadatos.",
    "Usar nombre exacto de asignatura: Derechos de la persona y familia.",
    "Alinear productos a Licenciatura en Derecho, semestre 3, bloque 1.",
    "Conservar tipo curricular: obligatoria seriada.",
    "Conservar créditos: 8.",
    "Usar código de curso local LDE-S3B1 cuando aplique.",
    "Usar ubicación institucional Roma Norte, Ciudad de México en metadatos.",
    "Usar carpeta de materia como punto de entrada canónico.",
    "Marcar como [supuesto] todo dato no confirmado por consigna o documento local.",
    "Mantener figura docente como dato no confirmado hasta validación. [supuesto]",
    "No modificar datos de alumno o matrícula sin verificación local.",
    "Tratar memorias Codex y GPT-Pro heredadas como provisionales hasta confirmación local.",
    "Citar malla-curricular-derecho-unadm.pdf como fuente de ubicación curricular."
  ],
  "structure_rules": [
    "Estructurar cada entrega en problema, marco conceptual-normativo, análisis propio y conclusión jurídica.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear la entrega al producto solicitado por planeación, consigna o rúbrica.",
    "Transformar planeación semanal en reporte, presentación o producto visual según consigna.",
    "Conservar coherencia con programa analítico local de la materia.",
    "Incluir trazabilidad entre consigna, desarrollo y cierre.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Verificar consistencia entre nombres de archivo, slug y referencias antes de compilar.",
    "Corregir rutas corruptas del README antes de reutilizar plantilla.",
    "Corregir nombres corruptos de reporte, referencias y carpeta de referencias."
  ],
  "activity_rules": [
    "Identificar consigna, rúbrica y producto solicitado antes de redactar.",
    "Adaptar reglas de actividad origen solo si son compatibles con materia destino. [supuesto]",
    "No trasladar contenido de Filosofía del Derecho sin validación de pertinencia. [supuesto]",
    "Registrar pendientes de consigna faltante en preguntas abiertas.",
    "Vincular cada actividad con planeación o rúbrica vigente cuando exista.",
    "Integrar fundamento jurídico, evidencia y transferencia profesional.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Evitar texto genérico; vincular argumentos al problema jurídico planteado.",
    "Mantener conclusión con criterio jurídico propio en cada actividad.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión."
  ],
  "quality_gates": [
    "Validar JSON parseable en cada intercambio de memoria.",
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar y normalizar cualquier salida no estructurada antes de reutilizarla.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Detener propagación si faltan datos mínimos de actividad.",
    "Verificar que consigna, rúbrica y producto solicitado estén identificados.",
    "Confirmar integridad académica sin afirmaciones sin sustento.",
    "Confirmar que los supuestos estén marcados como [supuesto].",
    "Comprobar que cada afirmación jurídica relevante tenga respaldo verificable.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar nombres corruptos en README local.",
    "Verificar que el .tex use el .bib local y no placeholders antes de compilar.",
    "Corregir placeholders de slug .bib en README y programa analítico antes de reutilizar plantilla.",
    "Compilar sin errores críticos y sin referencias rotas."
  ],
  "latex_rules": [
    "Usar plantilla base de reporte de la materia como punto de partida.",
    "Completar metadatos institucionales y académicos antes de redactar contenido.",
    "Mantener español académico y consistencia terminológica jurídica.",
    "Conservar documentclass article en español, letterpaper y oneside salvo consigna distinta.",
    "Usar título, subtítulo, asignatura y código local coherentes con la actividad.",
    "Actualizar documentsubtitle de Actividad X al número real.",
    "Mantener figura docente como Nombre por definir hasta confirmación.",
    "No modificar datos de alumno o matrícula sin verificación local.",
    "Usar codificación y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico."
  ],
  "bibliography_rules": [
    "Usar derechos-de-la-persona-y-familia.bib como archivo canónico local.",
    "Conservar fuentes institucionales UnADM ya registradas.",
    "Conservar entradas base: unadmSitioWeb y unadmMallaDerecho2024.",
    "Conservar malla curricular de Derecho como fuente curricular local.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar fuentes específicas de cada actividad en el .bib local.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Agregar solo fuentes verificables y pertinentes a cada actividad.",
    "No inventar referencias; marcar ausencias como pendiente.",
    "Usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Reemplazar placeholders dinámicos de nombre .bib por slug canónico fijo.",
    "Corregir placeholder de nombre .bib en programa analítico si se reutiliza."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo tras validación de calidad.",
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "En ciclo 1, aplicar normalización manual previa a reutilización.",
    "Aplicar compresión union-dedupe sin pérdida y sin regresión.",
    "Mantener reglas institucionales estables como base común.",
    "Etiquetar reglas heredadas provisionales hasta confirmación en Derecho.",
    "No propagar reglas dependientes de actividad sin consigna confirmada.",
    "Propagar solo abstracciones generales cuando falte consigna textual.",
    "Priorizar identidad, estructura reusable, calidad y grafo conceptual.",
    "Evitar transferir redacción literal entre materias no equivalentes.",
    "Si reaparece salida no JSON parseable, forzar normalización manual antes de propagar."
  ],
  "open_questions": [
    "Confirmar consigna específica de la actividad destino en Derechos de la persona y familia.",
    "Confirmar si existe plantilla formal de presentación obligatoria para esta materia.",
    "Confirmar datos de figura docente y criterios de evaluación vigentes.",
    "Confirmar si el código LDE-S3B1 es requerido en todos los productos.",
    "Confirmar si los datos de alumno y matrícula de la plantilla local siguen vigentes.",
    "Validar corrección definitiva de rutas y slugs corruptos en README local.",
    "Validar sustitución definitiva del placeholder de .bib en README y programa analítico.",
    "Confirmar si el slug del .bib debe resolverse desde plantilla generadora. [supuesto]",
    "Confirmar fuentes obligatorias de cada semana o unidad.",
    "Confirmar si cada actividad requiere reporte, presentación u otro formato principal."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante datos no verificados.",
        "Aplicado a problemas jurídicos concretos."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Carpeta de materia como entrada canónica.",
        "Metadatos institucionales consistentes.",
        "Normalización estructurada previa a propagación."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Derechos de la persona y familia.",
        "Semestre 3, bloque 1.",
        "Obligatoria seriada de 8 créditos.",
        "Código local LDE-S3B1."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Integridad académica verificable.",
      "Problema jurídico o social delimitado.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por planeación o consigna.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible.",
      "Trazabilidad consigna-producto.",
      "Normalización estructurada.",
      "Bibliografía local verificable."
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Transformar planeación semanal en reportes, presentaciones o productos visuales según consigna.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Conservar coherencia con el programa analítico local.",
      "Proteger la identidad curricular de la materia destino.",
      "Evitar contaminación temática desde materias no equivalentes.",
      "Convertir cada actividad en evidencia evaluable y profesionalmente útil."
    ],
    "style_markers": [
      "Inicio con problema concreto.",
      "Objetivo puntual antes del desarrollo.",
      "Secciones funcionales y verificables.",
      "Lenguaje jurídico preciso.",
      "Citas explícitas y fuentes consultables.",
      "Postura propia diferenciada del resumen.",
      "Cierre con criterio jurídico aplicado.",
      "Supuestos marcados de forma visible.",
      "Metadatos UnADM consistentes.",
      "Nombres de archivo canónicos."
    ],
    "argumentative_patterns": [
      "Problema jurídico -> marco conceptual-normativo -> análisis propio -> conclusión.",
      "Afirmación jurídica -> evidencia verificable -> interpretación propia.",
      "Consigna explícita -> producto solicitado -> cumplimiento comprobable.",
      "Concepto clave -> norma o doctrina -> efecto práctico.",
      "Dato no confirmado -> marca [supuesto] -> pregunta abierta.",
      "Fuente heredada -> verificación local -> uso condicionado.",
      "Bibliografía base -> fuente específica -> cita en texto.",
      "Plantilla local -> metadatos completos -> compilación limpia."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Derechos de la persona y familia",
        "Licenciatura en Derecho",
        "Semestre 3 bloque 1",
        "Obligatoria seriada",
        "Ocho créditos",
        "Código LDE-S3B1",
        "Problema jurídico",
        "Marco conceptual-normativo",
        "Doctrina jurídica",
        "Evidencia verificable",
        "Análisis propio",
        "Postura académica",
        "Conclusión jurídica transferible",
        "Trazabilidad consigna-producto",
        "Integridad académica",
        "Normalización estructurada",
        "Bibliografía local",
        "Malla curricular de Derecho",
        "Plantilla LaTeX local",
        "README local",
        "Programa analítico local",
        "Archivo BibTeX canónico",
        "Placeholders de slug",
        "Rutas corruptas"
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
          "justification": "La pauta local exige identidad UnADM, citas verificables y conclusión jurídica."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Semestre 3 bloque 1",
          "kind": "supports",
          "justification": "El README local declara la ubicación curricular con esa fuente."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Obligatoria seriada",
          "kind": "supports",
          "justification": "El README local registra el tipo curricular."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Ocho créditos",
          "kind": "supports",
          "justification": "El README local registra los créditos."
        },
        {
          "source": "Derechos de la persona y familia",
          "target": "Licenciatura en Derecho",
          "kind": "depends_on",
          "justification": "El README local define la materia dentro de la Licenciatura en Derecho de la UnADM."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere un problema delimitado."
        },
        {
          "source": "Marco conceptual-normativo",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica requiere fundamento conceptual y normativo."
        },
        {
          "source": "Evidencia verificable",
          "target": "Postura académica",
          "kind": "supports",
          "justification": "La postura propia debe sostenerse con fuentes consultables."
        },
        {
          "source": "Trazabilidad consigna-producto",
          "target": "Integridad académica",
          "kind": "develops",
          "justification": "Permite comprobar cumplimiento real de la actividad."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON parseable no hay reutilización segura."
        },
        {
          "source": "Archivo BibTeX canónico",
          "target": "Bibliografía local",
          "kind": "develops",
          "justification": "El archivo derechos-de-la-persona-y-familia.bib concentra las fuentes locales."
        },
        {
          "source": "Placeholders de slug",
          "target": "Compilación limpia",
          "kind": "contrasts",
          "justification": "Los tokens sin expandir pueden romper referencias y rutas."
        },
        {
          "source": "Rutas corruptas",
          "target": "README local",
          "kind": "depends_on",
          "justification": "La corrección debe realizarse en el documento donde aparecen."
        },
        {
          "source": "Plantilla LaTeX local",
          "target": "Metadatos institucionales consistentes",
          "kind": "supports",
          "justification": "La plantilla declara título, asignatura, curso, alumno y ubicación."
        }
      ],
      "evidence": [
        "README local: Materia de la Licenciatura en Derecho de la UnADM.",
        "README local: Semestre 3, bloque 1, obligatoria seriada, 8 créditos.",
        "README local: Fuente curricular UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
        "README local: La carpeta funciona como punto de entrada canónico de la asignatura.",
        "README local: Cada actividad debe conservar identidad UnADM e integridad académica.",
        "Programa analítico local: orientar productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: transformar planeación semanal en reportes, presentaciones y productos visuales.",
        "Programa analítico local: ejes de problema, conceptos, fuentes, análisis propio y conclusión.",
        "Bibliografía local: unadmSitioWeb.",
        "Bibliografía local: unadmMallaDerecho2024.",
        "Plantilla LaTeX local: coursename Derechos de la persona y familia.",
        "Plantilla LaTeX local: coursecode LDE-S3B1.",
        "Plantilla LaTeX local: Figura docente Nombre por definir.",
        "README local: aparecen nombres corruptos de reporte y referencias.",
        "Programa analítico local: aparece placeholder dinámico para el archivo .bib."
      ]
    },
    "reinforcement_log": [
      "Se preservó identidad local de Derechos de la persona y familia.",
      "Se integraron solo abstracciones transversales desde Filosofía del Derecho.",
      "Se descartó transferencia temática no validada por pertinencia local.",
      "Se reforzó patrón problema-marco-análisis-conclusión.",
      "Se consolidó control de JSON parseable como gate institucional.",
      "Se reforzó uso del .bib local como fuente canónica.",
      "Se conservaron alertas sobre placeholders y rutas corruptas.",
      "Se mantuvieron datos de alumno y matrícula como sujetos a verificación.",
      "Se actualizó grafo conceptual con relaciones permitidas.",
      "Se priorizó propagación conservadora, progresiva y sin regresión."
    ]
  }
}