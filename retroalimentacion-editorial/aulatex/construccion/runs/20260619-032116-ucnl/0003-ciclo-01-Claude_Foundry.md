```json
{
  "memoria_fundacional": {
    "summary": [
      "UCNL es nodo institucional estable y reutilizable, alineado al flujo interinstitucional AulaTeX, raiz para reportes, actividades y presentaciones con compilacion canonica via scripts.",
      "Conserva compatibilidad estructural interinstitucional: .bib institucional, entradas .tex maestras (reporte/presentacion) y subcarpetas por carrera/materia.",
      "Integra el Modelo Educativo UC como marco contextual obligatorio, usado solo como referencia de enfoque formativo sin extraer ni inventar contenido no verificado (PDF binario no extraible).",
      "Mantiene contrato central: al script solo se le pasa el .tex; plantilla via TEXINPUTS y bibliografia via BIBINPUTS definidos en .latexmkrc.",
      "Refuerzo de ciclo 1: se consolidan reglas previas y se incorpora carpeta assets y COMPILACION.md por materia como estandar homogeneo con instituciones hermanas."
    ],
    "identity_rules": [
      "Mantener prefijos institucionales en troncales: reporte-ucnl.tex, presentacion-ucnl.tex, bibliografia-ucnl.bib.",
      "Alinear entregables al enfoque academico formal UCNL: claridad, argumentacion propia y evidencia de fuentes.",
      "Usar UCNL como nodo base para derivar materias sin romper convenciones del repositorio interinstitucional.",
      "Permitir marca de agua institucional discreta mediante variables coverwatermark sin alterar el tronco."
    ],
    "structure_rules": [
      "Conservar raiz UCNL con: bibliografia institucional, plantillas maestras, referencias-ucnl/, assets/ y subcarpetas academicas.",
      "Cada materia/carrera debe incluir COMPILACION.md con comando exacto, contrato de compilacion y .bib esperado.",
      "Separar plantilla maestra institucional de entregables por actividad a nivel materia/semana.",
      "Centralizar insumos documentales en referencias-ucnl/ y recursos graficos en assets/."
    ],
    "style_rules": [
      "Redaccion academica formal, precisa, cohesionada y sin copiar instrucciones de la actividad.",
      "Priorizar sintesis, analisis y postura fundamentada sobre transcripcion de fuentes.",
      "Mantener consistencia terminologica entre portada, cuerpo, figuras, producto y referencias.",
      "Aplicar interlineado 1.5 y fuente equivalente a Arial segun formato institucional recomendado."
    ],
    "quality_gates": [
      "Cumple exactamente el producto solicitado (ensayo, cuadro, mapa, reporte, presentacion, etc.).",
      "Incluye citas en texto y referencias trazables en .bib institucional o de materia, formato APA 7.",
      "Compila sin errores bloqueantes y genera PDF en la carpeta objetivo.",
      "No hay plagio textual de consignas, fuentes ni plantillas."
    ],
    "latex_rules": [
      "Compilar solo via scripts institucionales pasando unicamente el .tex de entrada.",
      "Resolver plantillas por TEXINPUTS y bibliografia por BIBINPUTS definidos en .latexmkrc.",
      "Usar natbib con citacion autor-anio (\\citet, \\citep) y salida compatible APA 7.",
      "Preservar plantilla maestra UCNL como fuente base inmodificable; derivar copias por actividad."
    ],
    "bibliography_rules": [
      "Centralizar fuentes comunes en bibliografia-ucnl.bib y complementar con .bib de materia cuando aplique.",
      "No inventar referencias; registrar solo fuentes verificables efectivamente usadas en el texto.",
      "Toda cita en cuerpo debe corresponder a una entrada valida en el .bib."
    ],
    "research_markers": [
      "Validar lineamientos formales del Modelo Educativo UC antes de redactar (uso contextual, sin extraer texto no verificado).",
      "Identificar rubricas y criterios de evaluacion explicitos por materia y mapearlos a secciones del reporte.",
      "Confirmar formato de entrega en aula: nomenclatura, extension y tipo de producto visual."
    ]
  },
  "plan_editorial": {
    "objetivo_editorial": [
      "Reforzar UCNL como nodo institucional estable, reusable y compatible con el flujo interinstitucional AulaTeX.",
      "Homogeneizar UCNL con instituciones hermanas en estructura, contrato de compilacion y criterios editoriales."
    ],
    "alcance": [
      "Nivel institucion: normas de identidad, estructura, estilo, calidad y compilacion.",
      "No incluye redaccion completa de actividades ni investigacion de fondo en este ciclo.",
      "Define andamiaje reutilizable para que el Agente investigue y redacte en fases posteriores."