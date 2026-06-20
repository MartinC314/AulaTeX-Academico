{
  "summary": [
    "Materia ADM-CAL con plantilla maestra de reporte y actividad.",
    "Compilacion estandar con latexmk-build.ps1 desde raiz del proyecto.",
    "Bibliografia canonica de la materia en administracion-de-calidad.bib.",
    "Se hereda alerta institucional: salida previa no estructurada en ciclo 1.",
    "Plantilla indica fuente tipo Helvetica/Arial equivalente e interlineado 1.5.",
    "Watermark de portada configurable y opcional segun plantilla.",
    "Actividad 1 presenta criterios truncados en el archivo fuente."
  ],
  "identity_rules": [
    "Usar identidad de materia: Administracion de calidad (ADM-CAL).",
    "Conservar ruta canonica: UCNL/licenciatura-en-administracion/administracion-de-calidad-lad.",
    "Mantener nombre base de bibliografia: administracion-de-calidad.bib.",
    "Usar codigo ADM-CAL en metadatos del reporte."
  ],
  "structure_rules": [
    "Mantener formato de reporte de la materia para nuevas actividades.",
    "Incluir caratula, resumen breve, desarrollo, producto solicitado, conclusion y bibliografia.",
    "No pegar instrucciones completas de planeacion dentro del producto final.",
    "Aplicar tipografia Helvetica o equivalente visual a Arial.",
    "Usar interlineado 1.5 en todo el documento."
  ],
  "activity_rules": [
    "Responder exactamente a lo solicitado por la actividad de planeacion.",
    "Construir el producto academico solicitado dentro del documento cuando aplique.",
    "Redactar con comprension propia a partir de la bibliografia revisada.",
    "Usar la planeacion como checklist de cumplimiento, sin copiarla en el producto.",
    "Documentar supuestos cuando la planeacion sea ambigua. Supuesto: explicitar en una nota breve.",
    "Para Actividad 1, detectar y corregir truncamientos en el archivo antes de redactar."
  ],
  "quality_gates": [
    "Verificar que toda clave citada exista en administracion-de-calidad.bib.",
    "Validar compilacion correcta del .tex objetivo con script institucional.",
    "Revisar consistencia academica: claridad, coherencia, formalidad y ortografia.",
    "Revisar respuesta no estructurada heredada antes de propagar aguas abajo.",
    "Verificar tipografia Helvetica/Arial equivalente e interlineado 1.5.",
    "Confirmar que \\input{template} resuelve a base/Plantilla-Informe/template.tex.",
    "Confirmar PDF final junto al .tex y auxiliares en .build/latex y .build/latex/aux.",
    "No incluir instrucciones de planeacion en el PDF final.",
    "Detectar y corregir caracteres anomalos en rutas o textos (ej.: ase en COMPILACION.md)."
  ],
  "latex_rules": [
    "Ejecutar compilacion siempre desde la raiz del proyecto.",
    "Usar .\\scripts\\latexmk-build.ps1 con la ruta del .tex como unico argumento obligatorio.",
    "No pasar \\input{template} como argumento; se resuelve por TEXINPUTS en .latexmkrc.",
    "En reportes, \\input{template} debe resolver a base/Plantilla-Informe/template.tex.",
    "No pasar .bib al script; declarar \\bibliography{administracion-de-calidad} en reportes.",
    "Permitir resolucion de atnumurl.bst mediante BSTINPUTS.",
    "Esperar PDF final junto al .tex y auxiliares en .build/latex y .build/latex/aux.",
    "Confiar en .latexmkrc para TEXINPUTS, BIBINPUTS y BSTINPUTS.",
    "Configurar interlineado 1.5 y fuente Helvetica en el preambulo conforme a la plantilla.",
    "Variables coverwatermark* controlan la marca de agua en portada; desactivarla si no procede.",
    "No modificar el script latexmk-build.ps1 ni pasar parametros extra.",
    "Usar rutas relativas canonicas desde la raiz al invocar el script."
  ],
  "bibliography_rules": [
    "Usar administracion-de-calidad.bib como archivo bibliografico canonico de la materia.",
    "Agregar en ese .bib las fuentes usadas por reportes y actividades de la carpeta.",
    "No inventar fuentes ni claves bibliograficas.",
    "Aplicar citas autor-anio con natbib: \\citep{clave} y \\citet{clave}.",
    "Supuesto: se busca estilo APA 7 en cuerpo y referencias segun comentarios de plantilla.",
    "Registrar en administracion-de-calidad.bib toda fuente efectivamente citada por actividades.",
    "Clave disponible actual: unadm100TecnicasDidacticas2023 (uso metodologico)."
  ],
  "propagation_hints": [
    "Propagar estas reglas a actividades hermanas de la misma materia.",
    "Priorizar reglas de compilacion y bibliografia por su impacto transversal.",
    "Mantener compresion union-dedupe sin regresion ni recorte semantico.",
    "Ciclo 1: normalizacion manual recomendada si se detecta texto no estructurado heredado.",
    "Elevar a plantilla comun las reglas de tipografia, interlineado y watermark.",
    "Corregir caracteres anomalos heredados en documentos hermanos."
  ],
  "open_questions": [
    "Confirmar si el estilo bibliografico final exigido en entrega es exactamente APA 7.",
    "Confirmar si la marca de agua institucional en portada es obligatoria u opcional.",
    "Completar criterios truncados en el archivo de actividad 1 (texto fuente incompleto)."
  ]
}