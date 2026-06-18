```json
{
  "summary": [
    "Destino: materia Historia del Derecho en Mexico de la Licenciatura en Derecho UnADM.",
    "Materia con plantilla base LaTeX, programa analitico y .bib local disponibles.",
    "Memoria estructural verificada desde README, programa analitico, plantilla y .bib local.",
    "Origen declarado: Filosofia del Derecho, actividad 1; sin contenido adicional verificable en el contexto.",
    "Se conserva alerta: hubo salida no JSON parseable desde Codex en ciclos previos.",
    "Plantilla declara autor Martin Jonathan de la Cruz, matricula ES2611202040, figura docente por definir."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, metadatos y redaccion.",
    "Usar nombre oficial de materia: Historia del Derecho en Mexico.",
    "Conservar datos curriculares: semestre 1, bloque 1, obligatoria, 8 creditos.",
    "Mantener fuente curricular local: UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
    "Fuente provisional vigente: Codex para consolidacion de memoria [supuesto].",
    "Conservar antecedente provisional institucional: Codex desde ingenieria-en-sistemas-computacionales.",
    "Conservar antecedente provisional del destino: Codex desde historia-del-derecho-en-mexico-lde.",
    "Marcar como supuesto cualquier fuente operativa no confirmada."
  ],
  "structure_rules": [
    "Tratar la carpeta de materia como punto de entrada canonico.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib.",
    "Registrar fuentes especificas de actividad en historia-del-derecho-en-mexico.bib.",
    "Alinear cada entrega a cinco ejes: problema, conceptos y fuentes, producto, analisis propio, conclusion transferible.",
    "Transformar planeacion semanal en reportes, presentaciones o productos visuales segun se solicite.",
    "No mezclar contenido tematico de Filosofia del Derecho sin evidencia local verificable.",
    "Conservar subcarpeta referencias-historia-del-derecho-en-mexico para materiales de apoyo."
  ],
  "activity_rules": [
    "Iniciar cada actividad con problema juridico o social concreto.",
    "Usar conceptos, normas, doctrina o datos pertinentes al problema.",
    "Desarrollar analisis propio con postura academica explicita.",
    "Cerrar con conclusion juridica aplicable a practica profesional.",
    "Adaptar formato de salida al producto solicitado: reporte, presentacion o visual.",
    "Conservar integridad academica y citas verificables en cada actividad."
  ],
  "quality_gates": [
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Validar JSON parseable en cada ciclo de memoria.",
    "Verificar consistencia entre datos curriculares y portada del documento.",
    "Comprobar que toda afirmacion sustantiva tenga soporte verificable.",
    "Aplicar union-dedupe sin recortar reglas utiles previas.",
    "Normalizar manualmente ciclo 1 antes de reutilizar aguas abajo.",
    "Revisar render de nombres de archivos en README antes de automatizar."
  ],
  "latex_rules": [
    "Usar reporte-historia-del-derecho-en-mexico.tex como base editable para reportes.",
    "Conservar metadatos clave: documenttitle, documentsubtitle, documentsubject, coursename y coursecode.",
    "Conservar universidad, facultad, departamento, imagen institucional y ubicacion.",
    "Mantener tabla de autor con alumno, matricula, figura docente, semestre/bloque y tipo/creditos.",
    "No eliminar campos institucionales; solo actualizar valores concretos por actividad.",
    "Actualizar documentsubtitle con numero y nombre real de actividad.",
    "Mantener coursecode local LDE-S1B1 salvo confirmacion contraria.",
    "Usar tambien presentacion-historia-del-derecho-en-mexico.tex para productos tipo presentacion."
  ],
  "bibliography_rules": [
    "Usar historia-del-derecho-en-mexico.bib como repositorio bibliografico local.",
    "Conservar entradas institucionales existentes de UnADM y malla curricular.",
    "Agregar solo fuentes realmente consultadas; no inventar referencias.",
    "Incluir trazabilidad minima en notas de referencia: origen y fecha de consulta cuando aplique.",
    "Corregir referencias a placeholders de Slug antes de compilar o citar.",
    "Evitar propagar bibliografia de Filosofia del Derecho sin consulta efectiva."
  ],
  "propagation_hints": [
    "Ciclo 1 necesita normalizacion manual si se reutiliza.",
    "Propagar arriba y laterales solo reglas editoriales transversales verificables.",
    "Propagar validacion JSON y normalizacion temprana a materias hermanas.",
    "Reutilizar estructura de cinco ejes con ajuste tematico por asignatura.",
    "Priorizar deduplicacion por union sin recorte de reglas utiles previas.",
    "Mantener alerta de salidas no JSON parseables en niveles superiores.",
    "No propagar datos curriculares de esta materia a materias laterales."
  ],
  "open_questions": [
    "Confirmar si 'Fuente provisional: Codex' debe reemplazarse por fuente operativa definitiva.",
    "Definir nombre oficial de figura docente para plantillas de actividades.",
    "Verificar y corregir posibles errores de render en listado de archivos del README.",
    "Verificar acentuacion oficial de 'Mexico' en el nombre de la materia.",
    "Confirmar si LDE-S1B1 es codigo oficial o codigo local de plantilla.",
    "Aportar memoria verificable de Filosofia del Derecho actividad 1 si debe fusionarse contenido editorial especifico."
  ],
  "sources": [
    "UnADM/licenciatura-en-derecho-unadm/historia-del-derecho-en-mexico-lde",
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1"
  ],
  "compression": {
    "method": "union-dedupe",
    "lossless": true
  },
  "schema_version": 1
}
```