{
  "summary": [
    "Se conserva la normalizacion minima previa por falta de memoria fuente parseable de Actividad 1.",
    "Se consolida memoria de Actividad 2 con deduplicacion lossless y sin recorte.",
    "Se incorporan reglas verificables del README y programa analitico local.",
    "Supuesto: el archivo .bib local contiene duplicados de la misma obra con claves distintas."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en toda entrega.",
    "Conservar enfoque de Licenciatura en Derecho y de la asignatura Etica y Moral juridica.",
    "Alinear la actividad al semestre 1, bloque 2, tipo obligatoria y 8 creditos.",
    "Registrar ruta de origen y destino en cada propagacion.",
    "No reemplazar reglas previas utiles; solo anexar o deduplicar."
  ],
  "structure_rules": [
    "Entregar memoria en JSON valido y parseable.",
    "Usar el esquema requerido completo y sin campos extra.",
    "Redactar reglas en frases cortas, accionables y sin duplicados.",
    "Marcar explicitamente supuestos cuando falte evidencia.",
    "Mantener trazabilidad de cambios por ciclo."
  ],
  "activity_rules": [
    "Estructurar cada actividad en problema, conceptos, fuentes, analisis propio y conclusion juridica.",
    "Incluir postura academica propia sustentada en argumentos verificables.",
    "Ajustar el producto al formato solicitado por la planeacion semanal.",
    "Cerrar con conclusion transferible a la practica juridica y profesional."
  ],
  "quality_gates": [
    "Validar sintaxis JSON antes de guardar memoria.",
    "Bloquear propagacion automatica si la salida no es parseable.",
    "Aplicar compresion por union-dedupe lossless; no recortar contenido valido.",
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
    "Supuesto: conservar temporalmente claves duplicadas existentes hasta definir politica editorial de alias."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas parseables y verificadas.",
    "Mantener historial de ciclos con marca de normalizacion cuando aplique.",
    "Priorizar reglas generales de calidad mientras no exista memoria semantica valida de Actividad 1.",
    "En ciclo 2, conservar continuidad con estado previo y evitar sobreescritura destructiva."
  ],
  "open_questions": [
    "Recuperar memoria estructurada y parseable de Actividad 1 para propagacion semantica completa.",
    "Definir politica editorial para resolver claves bib duplicadas de la misma obra.",
    "Definir umbral de bloqueo tras ciclos consecutivos sin JSON parseable.",
    "Confirmar formato de trazabilidad de fuentes provisionales por modelo en futuras corridas."
  ]
}