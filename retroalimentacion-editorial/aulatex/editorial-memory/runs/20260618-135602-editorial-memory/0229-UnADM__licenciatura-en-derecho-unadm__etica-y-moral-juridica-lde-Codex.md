{
  "summary": [
    "Materia objetivo: Etica y Moral juridica en Derecho UnADM, semestre 1, bloque 2.",
    "Tipo curricular: obligatoria, 8 creditos.",
    "Mantener identidad UnADM, integridad academica, citas verificables y conclusion juridica propia.",
    "Usar compresion por union-dedupe sin perdida y sin regresion.",
    "La herencia institucional reporta salidas no JSON parseables y requiere normalizacion manual en ciclo 1."
  ],
  "identity_rules": [
    "Conservar voz academica formal alineada a UnADM.",
    "Aterrizar el analisis en contexto juridico mexicano cuando aplique.",
    "Incluir postura propia sustentada en argumentos y evidencia.",
    "Marcar como supuesto cualquier dato no confirmado en fuentes locales.",
    "Tratar herencias de otras carreras como provisionales y no definitivas para Derecho.",
    "Fuente provisional de herencia cruzada: Codex y GPT-Pro."
  ],
  "structure_rules": [
    "Organizar cada entrega con problema, conceptos o fundamento, analisis y cierre.",
    "Integrar ejes locales: problema, conceptos, producto solicitado, analisis propio y conclusion profesional.",
    "Alinear productos a la planeacion semanal y al programa analitico local.",
    "Usar la carpeta de materia como entrada canonica de consistencia editorial.",
    "Mantener trazabilidad entre actividad, reporte y presentacion."
  ],
  "activity_rules": [
    "Definir explicitamente el problema juridico o social de la actividad.",
    "Vincular conceptos eticos y morales con implicaciones juridicas concretas.",
    "Distinguir hechos, valores, normas, doctrina y postura propia.",
    "Verificar que el producto solicitado coincida con la consigna de la actividad.",
    "Cerrar con conclusion transferible a la practica profesional del derecho.",
    "No trasladar reglas de Filosofia del Derecho sin adaptarlas al enfoque etico-moral juridico."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de propagar memoria.",
    "Revisar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que no se eliminen reglas utiles previas durante consolidacion.",
    "Comprobar deduplicacion semantica sin recorte de contenido valido.",
    "Verificar que toda fuente citada exista en la bibliografia local o se agregue con metadatos confirmados.",
    "Validar que los archivos .tex y .bib compilen o parseen antes de cerrar entrega."
  ],
  "latex_rules": [
    "Mantener compatibilidad con reportes y presentaciones .tex de la materia.",
    "Usar secciones claras para problema, desarrollo, analisis y conclusion.",
    "Asegurar consistencia de etiquetas, titulos y nombres de archivo.",
    "Evitar comandos o paquetes no justificados por la plantilla local.",
    "Usar como archivos locales esperados reporte-etica-y-moral-juridica.tex y presentacion-etica-y-moral-juridica.tex.",
    "Usar etica-y-moral-juridica.bib como bibliografia local de la materia.",
    "Corregir placeholders literales o rutas corruptas detectadas antes de compilar.",
    "Resolver el placeholder PowerShell del slug en README y programa analitico hacia etica-y-moral-juridica.bib.",
    "Corregir nombres de archivo con salto o caracter corrupto en README (reporte/referencias) antes de automatizar validaciones."
  ],
  "bibliography_rules": [
    "Registrar fuentes de cada actividad en etica-y-moral-juridica.bib.",
    "No inventar fuentes ni metadatos bibliograficos faltantes.",
    "Priorizar fuentes institucionales UnADM y materiales verificables.",
    "Conservar fuentes base locales verificables sin sustituirlas por referencias no confirmadas.",
    "Depurar entradas duplicadas por clave o contenido equivalente.",
    "Unificar pares de claves duplicadas: huertaEticaConClasicos2000 vs huerta2000etica, ronquilloarmasEticaGeneralProfesional2018 vs ronquillo2018etica, singerCompendioEtica1995 vs singer1995compendio.",
    "Confirmar entradas incompletas o truncadas antes de citarlas.",
    "Completar la entrada truncada sierraUniversidadNacional1910 antes de citarla."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales manteniendo alcance UnADM y contexto Derecho.",
    "Propagar reglas generales de integridad, trazabilidad y bibliografia a materias laterales de Derecho.",
    "No propagar detalles curriculares de esta materia como reglas globales de otras asignaturas.",
    "Aplicar normalizacion manual en ciclo 1 cuando la herencia venga incompleta o no estructurada.",
    "Marcar herencias provisionales de otras carreras como contexto no definitivo."
  ],
  "open_questions": [
    "Supuesto: la memoria de origen de actividad-1 no llego en JSON utilizable para extraer reglas nuevas.",
    "Confirmar si existe plantilla LaTeX obligatoria especifica para esta materia.",
    "Confirmar criterio final de deduplicacion bibliografica: clave, DOI o titulo+autor+anio.",
    "Confirmar si la planeacion semanal local incluye consignas adicionales no reflejadas en esta memoria.",
    "Confirmar si la bibliografia local debe normalizar claves BibTeX conservando alias historicos.",
    "Supuesto: el placeholder PowerShell del slug debe sustituirse de forma permanente por etica-y-moral-juridica.bib en README y programa analitico."
  ]
}