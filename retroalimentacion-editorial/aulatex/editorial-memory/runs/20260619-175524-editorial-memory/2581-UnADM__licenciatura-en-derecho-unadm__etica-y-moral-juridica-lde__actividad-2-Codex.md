{
  "summary": [
    "Se consolida memoria de Actividad 2 con union-dedupe lossless.",
    "Se preserva trazabilidad historica de salidas no parseables en ciclos previos.",
    "Se mantiene normalizacion minima para permitir propagacion recursiva.",
    "Se integran reglas verificables de README, programa analitico y .bib local.",
    "Supuesto: la memoria semantica de Actividad 1 no esta disponible en JSON parseable."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en toda entrega.",
    "Conservar enfoque de Licenciatura en Derecho y asignatura Etica y Moral juridica.",
    "Alinear la actividad a semestre 1, bloque 2, tipo obligatoria y 8 creditos.",
    "Registrar ruta de origen y destino en cada propagacion.",
    "Registrar fuente provisional por modelo cuando no exista fuente semantica valida.",
    "No reemplazar reglas utiles previas; solo anexar o deduplicar."
  ],
  "structure_rules": [
    "Entregar memoria en JSON valido y parseable.",
    "Usar el esquema requerido completo y sin campos extra.",
    "Redactar reglas en frases cortas, accionables y sin duplicados.",
    "Marcar supuestos de forma explicita cuando falte evidencia.",
    "Mantener trazabilidad de cambios por ciclo."
  ],
  "activity_rules": [
    "Estructurar cada actividad en problema, conceptos, fuentes, analisis propio y conclusion juridica.",
    "Ajustar el producto al formato solicitado por la planeacion semanal.",
    "Incluir postura academica propia sustentada en argumentos verificables.",
    "Orientar el desarrollo a claridad, fundamento juridico, evidencia y transferencia profesional.",
    "Cerrar con conclusion transferible a la practica juridica y profesional."
  ],
  "quality_gates": [
    "Validar sintaxis JSON antes de guardar memoria.",
    "Bloquear propagacion automatica si la salida no es parseable.",
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Aplicar compresion por union-dedupe lossless sin recortar contenido valido.",
    "Verificar consistencia con README y programa analitico locales.",
    "Revisar integridad academica y citas verificables antes de publicar."
  ],
  "latex_rules": [
    "Mantener compatibilidad con la suite LaTeX de la asignatura.",
    "Usar UTF-8 y acentos correctos en titulos, autores y secciones.",
    "Separar contenido, citas y bibliografia para compilacion estable.",
    "Conservar como entradas canonicas reporte-etica-y-moral-juridica.tex y presentacion-etica-y-moral-juridica.tex."
  ],
  "bibliography_rules": [
    "No inventar fuentes ni metadatos bibliograficos.",
    "Agregar referencias verificables en etica-y-moral-juridica.bib.",
    "Priorizar fuentes institucionales UnADM y malla curricular cuando apliquen al encuadre.",
    "Deduplicar obras equivalentes con distinta clave sin perder trazabilidad de claves previas.",
    "Supuesto: existen entradas duplicadas de la misma obra en la .bib local.",
    "Supuesto: conservar temporalmente claves duplicadas existentes hasta definir politica editorial de alias."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas parseables y verificadas.",
    "Mantener historial de ciclos con marca de normalizacion cuando aplique.",
    "Conservar continuidad entre ciclos y evitar sobreescritura destructiva.",
    "Priorizar reglas generales de calidad mientras no exista memoria semantica valida de Actividad 1.",
    "Ciclo 8 necesita normalizacion manual si se reutiliza."
  ],
  "open_questions": [
    "Recuperar memoria estructurada y parseable de Actividad 1 para propagacion semantica completa.",
    "Definir politica editorial para resolver claves .bib duplicadas de la misma obra.",
    "Definir umbral de bloqueo tras ciclos consecutivos sin JSON parseable.",
    "Confirmar formato de trazabilidad de fuentes provisionales por modelo en futuras corridas."
  ]
}