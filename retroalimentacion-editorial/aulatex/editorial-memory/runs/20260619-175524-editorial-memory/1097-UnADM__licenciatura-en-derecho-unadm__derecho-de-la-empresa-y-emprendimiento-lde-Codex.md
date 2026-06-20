{
  "summary": [
    "Base de destino consolidada con plantilla LaTeX y programa analitico de la materia.",
    "Materia local en semestre 6, bloque 2, tipo obligatoria y 8 creditos.",
    "Persisten alertas por salidas no estructuradas; exigir normalizacion manual antes de reutilizar.",
    "Compresion aplicada por union-dedupe sin recorte.",
    "Supuesto: el origen actividad-1 no aporta reglas nuevas verificables por falta de JSON parseable.",
    "README y programa analitico presentan token Slug sin expandir.",
    "README local presenta artefactos de salto en nombres de archivo.",
    "Reporte local parece truncado en \\authortable y cierre de tabular."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada y metadatos.",
    "Usar Licenciatura en Derecho como programa academico.",
    "Usar nombre oficial de la materia: Derecho de la empresa y emprendimiento.",
    "Usar codigo local LDE-S6B2 cuando la plantilla lo requiera.",
    "Usar autor visible de plantilla local solo con marca de supuesto hasta confirmacion por actividad.",
    "Marcar como supuesto cualquier dato no confirmado por archivo local.",
    "Fuente provisional: Codex desde ingenieria-en-sistemas-computacionales.",
    "Fuente provisional: Codex desde Actividad 1.",
    "Fuente provisional: GPT-Pro desde Actividad 1.",
    "Fuente provisional: Auto (model-router) desde Actividad 1.",
    "Fuente provisional: Claude Foundry desde Actividad 1."
  ],
  "structure_rules": [
    "Usar README de materia como punto de entrada canonico.",
    "Usar el programa analitico local para orientar productos academicos.",
    "Alinear cada entrega al esquema: problema, conceptos, producto, analisis propio, conclusion.",
    "Conservar correspondencia entre .tex, presentacion y .bib de la materia.",
    "Transformar planeacion semanal en reporte, presentacion y producto visual.",
    "Integrar evidencia, fundamento juridico y transferencia profesional.",
    "Verificar que nombres de archivos no conserven artefactos de generacion automatica.",
    "Resolver tokens de plantilla sin expandir en README y programa analitico."
  ],
  "activity_rules": [
    "Identificar el problema juridico o social que activa la actividad.",
    "Distinguir conceptos, normas, doctrina o datos pertinentes.",
    "Incluir el producto solicitado por la planeacion.",
    "Incluir analisis propio y postura academica.",
    "Cada actividad debe incluir conclusion juridica con criterio propio.",
    "Conectar la conclusion con aplicacion practica.",
    "Cada actividad debe incluir citas verificables y trazables a la bibliografia local.",
    "Agregar fuentes especificas de actividad al archivo .bib de la materia."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de consolidar memoria.",
    "Revisar respuesta no estructurada antes de aplicar propagacion lateral, ascendente o aguas abajo.",
    "Aplicar normalizacion manual antes de reutilizar memoria en este destino.",
    "No eliminar reglas utiles previas durante fusion por union-dedupe.",
    "No propagar datos locales no confirmados como reglas institucionales.",
    "Verificar que los datos curriculares coincidan con la malla local.",
    "Corregir placeholders visibles antes de generar entregables.",
    "Verificar que el README liste archivos reales y rutas existentes.",
    "Verificar integridad sintactica de archivos .tex y cierre de entornos antes de compilar."
  ],
  "latex_rules": [
    "Conservar plantilla base de reporte con metadatos institucionales completos.",
    "Mantener consistencia de campos de curso y licenciatura en macros LaTeX.",
    "Usar spanish, letterpaper y oneside salvo instruccion local distinta.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Reemplazar documenttitle generico por titulo concreto de la actividad.",
    "Mantener universitydepartment como Derecho de la empresa y emprendimiento.",
    "Confirmar universitydepartmentimage como departamentos/UnADM antes de compilar.",
    "Confirmar universitydepartmentimagecfg como height=1.57cm antes de compilar.",
    "Validar que las rutas de imagen institucional existan antes de compilar.",
    "Revisar que el archivo de reporte no quede truncado.",
    "Revisar cierre correcto de tabular y de \\authortable.",
    "Verificar compilacion sin errores tras actualizar portada, secciones y referencias."
  ],
  "bibliography_rules": [
    "No inventar fuentes; registrar solo fuentes verificables.",
    "Priorizar fuentes institucionales UnADM y documentos locales de malla curricular.",
    "Conservar unadmSitioWeb y unadmMallaDerecho2024 como bibliografia base local.",
    "Registrar fuentes especificas en derecho-de-la-empresa-y-emprendimiento.bib.",
    "Mantener claves BibTeX estables y sin duplicados.",
    "No citar fuentes no agregadas al .bib local.",
    "Indicar archivo local cuando la fuente provenga de assets-unadm."
  ],
  "propagation_hints": [
    "Propagar estas reglas a nivel licenciatura en Derecho cuando no exista conflicto local.",
    "Propagar lateralmente a materias hermanas con misma pauta editorial de UnADM.",
    "Propagar alerta de tokens de plantilla sin expandir a materias con README generado.",
    "Propagar alertas de placeholders y rutas generadas a materias con plantillas similares.",
    "Propagar alerta de truncamiento LaTeX solo a plantillas con sintomas equivalentes.",
    "No propagar datos curriculares especificos fuera de esta materia sin confirmacion local.",
    "Exigir normalizacion manual previa por antecedente de salida no estructurada.",
    "Ciclo 11 necesita normalizacion manual si se reutiliza."
  ],
  "open_questions": [
    "Supuesto: la actividad origen no aporta reglas adicionales por falta de JSON estructurado verificable.",
    "Confirmar si existe guia de citacion juridica especifica distinta a la plantilla general.",
    "Confirmar si el nombre de autor en plantilla debe parametrizarse por actividad.",
    "Confirmar valor real del Slug en README y programa analitico tras expansion de tokens.",
    "Confirmar si el README local debe corregir saltos o caracteres perdidos en nombres de archivo.",
    "Confirmar si el archivo de reporte esta incompleto en repositorio o solo en captura local.",
    "Confirmar cierre completo de \\authortable en el reporte local.",
    "Confirmar si year=2026 en unadmSitioWeb se mantiene como anio bibliografico o solo fecha de consulta."
  ]
}