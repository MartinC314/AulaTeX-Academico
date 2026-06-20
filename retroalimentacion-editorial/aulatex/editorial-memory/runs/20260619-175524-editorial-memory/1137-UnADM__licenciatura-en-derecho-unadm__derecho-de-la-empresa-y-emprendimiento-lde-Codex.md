{
  "summary": [
    "Base de destino consolidada con plantilla LaTeX y programa analitico de la materia.",
    "Materia local confirmada: semestre 6, bloque 2, obligatoria y 8 creditos.",
    "Persisten antecedentes de salidas no JSON parseables; mantener normalizacion manual previa.",
    "Compresion aplicada por union-dedupe sin recorte.",
    "Se detectan tokens Slug sin expandir en README y programa analitico.",
    "README presenta artefactos en nombres de archivo (saltos en reporte y referencias).",
    "Reporte LaTeX local truncado en \\authortable y cierre de tabular.",
    "Supuesto: el origen actividad-1 no aporta reglas nuevas verificables por falta de JSON parseable en este ciclo."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada y metadatos.",
    "Usar nombre oficial de materia: Derecho de la empresa y emprendimiento.",
    "Usar programa academico: Licenciatura en Derecho.",
    "Usar codigo de curso LDE-S6B2 cuando la plantilla lo requiera.",
    "Marcar como supuesto todo dato no confirmado por archivo local.",
    "Usar autor visible de plantilla solo con marca de supuesto hasta confirmacion por actividad.",
    "Conservar traza de fuente provisional heredada sin elevarla a hecho institucional.",
    "Fuente provisional: Codex desde ingenieria-en-sistemas-computacionales."
  ],
  "structure_rules": [
    "Usar README de materia como punto de entrada canonico.",
    "Alinear entregables al flujo: problema, conceptos, producto, analisis propio y conclusion.",
    "Conservar correspondencia entre .tex, presentacion y .bib.",
    "Usar programa analitico local para orientar productos.",
    "Transformar planeacion semanal en reporte, presentacion y producto visual.",
    "Integrar evidencia, fundamento juridico y transferencia profesional.",
    "Corregir artefactos de nombres de archivo en README.",
    "Resolver tokens de plantilla sin expandir en README y programa analitico."
  ],
  "activity_rules": [
    "Identificar problema juridico o social de la actividad.",
    "Incluir conceptos, normas, doctrina o datos pertinentes.",
    "Incluir producto solicitado por la planeacion.",
    "Incluir analisis propio y postura academica.",
    "Cerrar con conclusion juridica con criterio propio.",
    "Conectar conclusion con aplicacion practica.",
    "Incluir citas verificables trazables al .bib local.",
    "Agregar al .bib solo fuentes especificas realmente usadas."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de consolidar memoria.",
    "Revisar y normalizar salida no estructurada antes de propagar.",
    "No eliminar reglas utiles previas durante fusion por union-dedupe.",
    "Aplicar normalizacion manual antes de reutilizar memoria en este destino.",
    "Verificar consistencia con malla curricular local.",
    "Verificar que README liste archivos reales y rutas existentes.",
    "Corregir placeholders visibles antes de generar entregables.",
    "Verificar integridad sintactica de .tex y cierre de entornos antes de compilar.",
    "No propagar datos locales no confirmados como reglas institucionales."
  ],
  "latex_rules": [
    "Conservar plantilla base con metadatos institucionales completos.",
    "Mantener consistencia de curso y licenciatura en macros.",
    "Usar spanish, letterpaper y oneside salvo instruccion local distinta.",
    "Reemplazar documenttitle generico por titulo concreto de actividad.",
    "Actualizar documentsubtitle por numero y nombre de actividad.",
    "Mantener universitydepartment como nombre oficial de la materia.",
    "Confirmar universitydepartmentimage=departamentos/UnADM.",
    "Confirmar universitydepartmentimagecfg=height=1.57cm.",
    "Confirmar existencia de ruta de imagen institucional antes de compilar.",
    "Reparar truncamiento en \\authortable.",
    "Cerrar correctamente \\end{tabular} y entornos pendientes.",
    "Compilar y validar sin errores tras cambios."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Registrar solo fuentes verificables.",
    "Priorizar fuentes institucionales UnADM y documentos locales.",
    "Conservar unadmSitioWeb y unadmMallaDerecho2024 como base local.",
    "Registrar fuentes de actividad en derecho-de-la-empresa-y-emprendimiento.bib.",
    "No citar fuentes ausentes en el .bib local.",
    "Indicar archivo local cuando la fuente provenga de assets-unadm.",
    "Conservar claves BibTeX estables y sin duplicados."
  ],
  "propagation_hints": [
    "Propagar reglas generales a nivel licenciatura si no hay conflicto local.",
    "Propagar lateralmente a materias hermanas con la misma pauta UnADM.",
    "Exigir normalizacion manual previa por antecedente de salida no estructurada.",
    "Ciclo 21 necesita normalizacion manual si se reutiliza.",
    "Propagar alerta de tokens Slug sin expandir a plantillas similares.",
    "Propagar alerta de truncamiento LaTeX solo donde existan sintomas equivalentes.",
    "No propagar datos curriculares especificos sin confirmacion local."
  ],
  "open_questions": [
    "Supuesto: la actividad origen no aporta reglas adicionales por falta de JSON estructurado verificable.",
    "Confirmar autoria final por actividad para retirar marca de supuesto.",
    "Confirmar correccion definitiva de tokens Slug en README y programa analitico.",
    "Confirmar si el README debe corregir saltos o caracteres perdidos en nombres de archivo.",
    "Confirmar cierre completo de \\authortable en el reporte local.",
    "Confirmar si el truncamiento del reporte proviene del archivo fuente completo o de captura parcial.",
    "Confirmar guia de citacion juridica especifica de la materia si existe.",
    "Confirmar si year=2026 en unadmSitioWeb queda como anio bibliografico o solo fecha de consulta."
  ]
}