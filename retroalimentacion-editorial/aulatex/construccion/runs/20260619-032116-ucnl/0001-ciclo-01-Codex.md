{
  "memoria_fundacional": {
    "summary": [
      "Nodo institucional UCNL reforzado como raiz reutilizable para reportes, actividades y presentaciones con compilacion canonica via scripts.",
      "Se conserva compatibilidad con estructura interinstitucional: archivo .bib institucional, entradas .tex maestras y carpetas por asignatura/carrera.",
      "Se integra el Modelo Educativo UC como restriccion contextual de enfoque formativo, sin extraer ni inventar contenido no verificado."
    ],
    "identity_rules": [
      "Mantener prefijo institucional en archivos troncales: reporte-ucnl.tex, presentacion-ucnl.tex, bibliografia-ucnl.bib.",
      "Alinear entregables al enfoque academico formal de UCNL: claridad, argumentacion propia y evidencia de fuentes.",
      "Usar UCNL como nodo base para derivar materias sin romper convenciones del repositorio."
    ],
    "structure_rules": [
      "Conservar raiz UCNL con: bibliografia institucional, referencias institucionales, assets y subcarpetas academicas.",
      "Cada materia/carrera debe incluir COMPILACION.md con comando exacto, contrato de compilacion y bib esperado.",
      "Separar plantilla maestra (institucional) de entregables por actividad (nivel materia/semana)."
    ],
    "style_rules": [
      "Redaccion academica formal, precisa y sin copiar instrucciones de la actividad.",
      "Priorizar sintesis, analisis y postura fundamentada sobre transcripcion.",
      "Mantener consistencia terminologica entre portada, cuerpo, figuras y referencias."
    ],
    "quality_gates": [
      "Cumple exactamente el producto solicitado (ensayo, cuadro, mapa, reporte, presentacion, etc.).",
      "Incluye citas en texto y referencias bibliograficas trazables en .bib institucional o de materia.",
      "Compila sin errores bloqueantes y genera PDF en carpeta objetivo.",
      "No hay plagio textual de consignas, fuentes o plantillas."
    ],
    "latex_rules": [
      "Compilar mediante scripts institucionales pasando solo el .tex de entrada.",
      "Resolver plantillas por TEXINPUTS y bibliografia por BIBINPUTS definidos en .latexmkrc.",
      "Usar natbib para citacion autor-anio (\\citet, \\citep) y mantener compatibilidad APA 7 en salida.",
      "Preservar plantilla maestra UCNL como fuente base; derivar copias por actividad."
    ],
    "bibliography_rules": [
      "Centralizar fuentes institucionales en bibliografia-ucnl.bib y complementar en bib de materia cuando aplique.",
      "No inventar referencias; registrar solo fuentes verificables usadas en el texto.",
      "Toda cita en cuerpo debe corresponder a una entrada valida en .bib."
    ],
    "research_markers": [
      "Validar lineamientos formales del Modelo Educativo UC antes de redactar actividades.",
      "Identificar criterios de evaluacion explicitos por materia y mapearlos a secciones del reporte.",
      "Confirmar formato de entrega solicitado en aula (nomenclatura, extension, producto visual)."
    ]
  },
  "plan_editorial": {
    "objetivo_editorial": [
      "Reforzar UCNL como nodo institucional estable, reusable y compatible con el flujo interinstitucional AulaTeX."
    ],
    "alcance": [
      "Nivel institucion: normas de identidad, estructura, estilo, calidad y compilacion.",
      "No incluye redaccion completa de actividades ni investigacion de fondo en este ciclo."
    ],
    "estructura_base": [
      "UCNL/reporte-ucnl.tex (plantilla maestra institucional).",
      "UCNL/presentacion-ucnl.tex (entrada canonica para diapositivas).",
      "UCNL/bibliografia-ucnl.bib (fuente bibliografica institucional).",
      "UCNL/referencias-ucnl/ (insumos documentales).",
      "UCNL/assets/ (imagenes, tablas exportadas, logos permitidos).",
      "UCNL/<carrera-o-materia>/ con entregables y COMPILACION.md."
    ],
    "criterios_evaluacion": [
      "Coherencia con lineamientos UCNL e interinstitucionales.",
      "Trazabilidad editorial: consigna -> estructura -> evidencia -> referencia.",
      "Calidad tecnica LaTeX: compilacion limpia y formato consistente.",
      "Cumplimiento de citacion y bibliografia verificable."
    ],
    "bibliografia_requerida": [
      "Modelo Educativo UC (documento institucional, uso contextual).",
      "Planeacion oficial de la asignatura correspondiente.",
      "Fuentes academicas primarias/fiables definidas por docente o programa."
    ],
    "riesgos": [
      "Deriva de estilo por copiar consignas literalmente en el cuerpo.",
      "Inconsistencias entre cita en texto y registro en .bib.",
      "Uso de plantillas fuera del contrato de compilacion institucional."
    ],
    "siguiente_fase_agente": [
      "Auditar estructura real de carpetas UCNL y normalizar faltantes (assets, COMPILACION.md por materia).",
      "Crear maqueta derivada por materia con metadatos completos y secciones vacias guiadas.",
      "Mapear criterios de rubrica a checklist de validacion precompilacion."
    ]
  },
  "maqueta_inicial": {
    "titulo": "UCNL | Maqueta institucional base de actividad academica",
    "objetivo": [
      "Proveer un esqueleto reusable para construir entregables UCNL sin romper reglas editoriales ni tecnicas."
    ],
    "competencias": [
      "Redaccion academica argumentada.",
      "Sintesis y analisis de fuentes.",
      "Gestion de referencias con BibTeX/natbib.",
      "Produccion documental en LaTeX."
    ],
    "resultados_esperados": [
      "Documento compilable en PDF con estructura academica completa.",
      "Citas y referencias coherentes con fuentes usadas.",
      "Cumplimiento de producto solicitado por consigna."
    ],
    "estructura_sugerida": [
      "Portada institucional.",
      "Resumen breve.",
      "Introduccion y contexto.",
      "Desarrollo por criterios/rubrica.",
      "Producto solicitado (tabla, esquema, analisis, etc.).",
      "Conclusion.",
      "Referencias bibliograficas."
    ],
    "criterios_evaluacion": [
      "Pertinencia y profundidad del contenido.",
      "Organizacion y coherencia argumentativa.",
      "Correccion formal de citacion y referencias.",
      "Calidad de formato y compilacion final."
    ],
    "bibliografia_requerida": [
      "bibliografia-ucnl.bib como base.",
      "Fuentes de planeacion y documentos institucionales aplicables."
    ],
    "marcadores_investigacion": [
      "Pendiente: extraer lineamientos verificables del Modelo Educativo UC.",
      "Pendiente: identificar rubrica especifica de materia/actividad.",
      "Pendiente: definir corpus minimo de fuentes por entrega."
    ]
  },
  "tex_editorial": {
    "plantilla": [
      "Archivo base institucional derivable desde UCNL/reporte-ucnl.tex.",
      "Bloques obligatorios: metadatos, resumen, desarrollo, conclusion, bibliografia.",
      "Variables de portada y marca de agua configurables sin tocar estructura troncal."
    ],
    "actividad": [
      "Plantilla hija por materia/semana con secciones guiadas y placeholders de evidencia.",
      "Checklist embebido en comentarios para cumplimiento de consigna y rubrica.",
      "Sin texto final redactado; solo andamiaje editorial."
    ],
    "reporte": [
      "Entrada canonica por producto academico con natbib activo y bibliografia enlazada.",
      "Secciones orientadas a analisis y producto solicitado.",
      "Compatible con compilacion por scripts institucionales."
    ],
    "presentacion": [
      "Entrada canonica UCNL/presentacion-ucnl.tex para sintesis visual del reporte.",
      "Estructura minima: objetivo, hallazgos, evidencia, cierre, referencias.",
      "Consistencia terminologica con el reporte escrito."
    ]
  }
}