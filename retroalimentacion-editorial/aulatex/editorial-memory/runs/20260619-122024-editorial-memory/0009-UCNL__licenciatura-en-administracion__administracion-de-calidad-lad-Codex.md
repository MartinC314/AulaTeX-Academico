{
  "summary": [
    "Materia ADM-CAL con plantilla maestra de reporte y actividad.",
    "Compilacion estandar con latexmk-build.ps1 desde raiz del proyecto.",
    "Bibliografia canonica de la materia en administracion-de-calidad.bib.",
    "Se hereda alerta institucional: salida previa no estructurada en ciclo 1."
  ],
  "identity_rules": [
    "Usar identidad de materia: Administracion de calidad (ADM-CAL).",
    "Conservar ruta canonica: UCNL/licenciatura-en-administracion/administracion-de-calidad-lad.",
    "Mantener nombre base de bibliografia: administracion-de-calidad.bib."
  ],
  "structure_rules": [
    "Mantener formato de reporte de la materia para nuevas actividades.",
    "Incluir caratula, resumen breve, desarrollo, producto solicitado, conclusion y bibliografia.",
    "No pegar instrucciones completas de planeacion dentro del producto final."
  ],
  "activity_rules": [
    "Responder exactamente a lo solicitado por la actividad de planeacion.",
    "Construir el producto academico solicitado dentro del documento cuando aplique.",
    "Redactar con comprension propia a partir de la bibliografia revisada."
  ],
  "quality_gates": [
    "Verificar que toda clave citada exista en administracion-de-calidad.bib.",
    "Validar compilacion correcta del .tex objetivo con script institucional.",
    "Revisar consistencia academica: claridad, coherencia, formalidad y ortografia.",
    "Revisar respuesta no estructurada heredada antes de propagar aguas abajo."
  ],
  "latex_rules": [
    "Ejecutar compilacion siempre desde la raiz del proyecto.",
    "Usar .\\\\scripts\\\\latexmk-build.ps1 con la ruta del .tex como unico argumento obligatorio.",
    "No pasar \\\\input{template} como argumento; se resuelve por TEXINPUTS en .latexmkrc.",
    "En reportes, \\\\input{template} debe resolver a base/Plantilla-Informe/template.tex.",
    "No pasar .bib al script; declarar \\\\bibliography{administracion-de-calidad} en reportes.",
    "Permitir resolucion de atnumurl.bst mediante BSTINPUTS.",
    "Esperar PDF final junto al .tex y auxiliares en .build/latex y .build/latex/aux."
  ],
  "bibliography_rules": [
    "Usar administracion-de-calidad.bib como archivo bibliografico canonico de la materia.",
    "Agregar en ese .bib las fuentes usadas por reportes y actividades de la carpeta.",
    "No inventar fuentes ni claves bibliograficas.",
    "Aplicar citas autor-anio con natbib: \\\\citep{clave} y \\\\citet{clave}.",
    "Supuesto: se busca estilo APA 7 en cuerpo y referencias segun comentarios de plantilla."
  ],
  "propagation_hints": [
    "Propagar estas reglas a actividades hermanas de la misma materia.",
    "Priorizar reglas de compilacion y bibliografia por su impacto transversal.",
    "Mantener compresion union-dedupe sin regresion ni recorte semantico.",
    "Ciclo 1: normalizacion manual recomendada si se detecta texto no estructurado heredado."
  ],
  "open_questions": [
    "Confirmar si el estilo bibliografico final exigido en entrega es exactamente APA 7.",
    "Confirmar si la marca de agua institucional en portada es obligatoria u opcional.",
    "Completar criterios truncados en el archivo de actividad 1 (texto fuente incompleto)."
  ]
}