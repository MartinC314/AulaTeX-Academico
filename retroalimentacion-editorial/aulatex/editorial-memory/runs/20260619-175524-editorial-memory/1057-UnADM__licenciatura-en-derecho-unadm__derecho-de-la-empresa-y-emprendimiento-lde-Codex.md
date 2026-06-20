{
  "summary": [
    "Base de destino consolidada con plantilla LaTeX y programa analitico de la materia.",
    "Materia local ubicada en semestre 6, bloque 2, tipo obligatoria y 8 creditos.",
    "Compresion aplicada por union-dedupe sin recorte.",
    "Persisten alertas por salidas no estructuradas en ciclo 1; exigir normalizacion manual.",
    "README local presenta artefactos de salto en nombres de archivo.",
    "README y programa analitico presentan token Slug sin expandir.",
    "Reporte local parece truncado en la definicion de authortable y cierre tabular."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada y metadatos.",
    "Usar nombre oficial de la materia: Derecho de la empresa y emprendimiento.",
    "Usar Licenciatura en Derecho como programa academico.",
    "Usar codigo local LDE-S6B2 cuando la plantilla lo requiera.",
    "Marcar como supuesto cualquier dato no confirmado por archivo local.",
    "Usar autor de plantilla local solo si la actividad lo confirma.",
    "Autor visible en plantilla local: Martin Jonathan de la Cruz; supuesto: confirmar por actividad.",
    "Fuente provisional: Codex desde ingenieria-en-sistemas-computacionales."
  ],
  "structure_rules": [
    "Usar README de materia como punto de entrada canonico.",
    "Alinear cada entrega al esquema: problema, conceptos, producto, analisis propio, conclusion.",
    "Conservar correspondencia entre .tex, presentacion y .bib de la materia.",
    "Usar el programa analitico local para orientar productos academicos.",
    "Integrar evidencia, fundamento juridico y transferencia profesional.",
    "Transformar planeacion semanal en reporte, presentacion y producto visual.",
    "Verificar que nombres de archivos no conserven artefactos de generacion automatica.",
    "Resolver tokens de plantilla sin expandir en README y programa analitico."
  ],
  "activity_rules": [
    "Identificar el problema juridico o social que activa la actividad.",
    "Distinguir conceptos, normas, doctrina o datos pertinentes.",
    "Incluir el producto solicitado por la planeacion.",
    "Incluir analisis propio y postura academica.",
    "Cerrar con conclusion juridica con criterio propio.",
    "Conectar la conclusion con aplicacion practica.",
    "Incluir citas verificables y trazables a la bibliografia local.",
    "Agregar fuentes especificas de actividad al archivo .bib de la materia."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de consolidar memoria.",
    "Revisar respuesta no estructurada antes de aplicar propagacion lateral, ascendente o aguas abajo.",
    "No eliminar reglas utiles previas durante fusion por union-dedupe.",
    "Aplicar normalizacion manual en ciclo 1 antes de reutilizar memoria.",
    "Verificar que los datos curriculares coincidan con la malla local.",
    "Corregir placeholders visibles antes de generar entregables.",
    "Verificar que el README liste archivos reales y rutas existentes.",
    "Verificar integridad sintactica de archivos .tex y cierre de entornos antes de compilar.",
    "No propagar datos locales no confirmados como reglas institucionales."
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
    "Mantener claves BibTeX estables y sin duplicados.",
    "Conservar unadmSitioWeb y unadmMallaDerecho2024 como bibliografia base local.",
    "Registrar fuentes especificas en derecho-de-la-empresa-y-emprendimiento.bib.",
    "No citar fuentes no agregadas al .bib local.",
    "Indicar archivo local cuando la fuente provenga de assets-unadm."
  ],
  "propagation_hints": [
    "Propagar estas reglas a nivel licenciatura en Derecho cuando no exista conflicto local.",
    "Propagar lateralmente a materias hermanas con misma pauta editorial de UnADM.",
    "En ciclo 1, exigir normalizacion manual previa por antecedente de salida no estructurada.",
    "Propagar alerta de tokens de plantilla sin expandir a materias con README generado.",
    "Propagar alertas de placeholders y rutas generadas a materias con plantillas similares.",
    "Propagar alerta de truncamiento LaTeX solo a plantillas con sintomas equivalentes.",
    "No propagar datos curriculares especificos fuera de esta materia sin confirmacion local."
  ],
  "open_questions": [
    "Supuesto: la actividad origen no aporta reglas adicionales por falta de JSON estructurado verificable.",
    "Confirmar si existe guia de citacion juridica especifica distinta a la plantilla general.",
    "Confirmar si el nombre de autor en plantilla debe parametrizarse por actividad.",
    "Confirmar si el README local debe corregir saltos o caracteres perdidos en nombres de archivo.",
    "Confirmar valor real del Slug en README y programa analitico tras expansion de tokens.",
    "Confirmar si el archivo de reporte esta incompleto en repositorio o solo en captura local.",
    "Confirmar cierre completo de \\authortable en el reporte local.",
    "Confirmar si year=2026 en unadmSitioWeb se mantiene como anio bibliografico o solo fecha de consulta."
  ]
}