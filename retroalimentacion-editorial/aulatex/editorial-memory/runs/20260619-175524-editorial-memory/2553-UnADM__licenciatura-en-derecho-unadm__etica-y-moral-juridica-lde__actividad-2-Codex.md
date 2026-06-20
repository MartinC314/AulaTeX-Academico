{
  "summary": [
    "Se conserva estado previo: no hubo JSON parseable en intentos anteriores de Actividad 2.",
    "Se agrega normalizacion minima para habilitar propagacion sin perder trazabilidad.",
    "Supuesto: no se dispone del contenido valido de Actividad 1 para extraer reglas especificas."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en toda entrega.",
    "Conservar enfoque de Licenciatura en Derecho y de la asignatura Etica y Moral juridica.",
    "Registrar la fuente de cada regla propagada con ruta de origen y destino.",
    "No reemplazar reglas previas utiles; solo anexar o deduplicar."
  ],
  "structure_rules": [
    "Entregar memoria en JSON valido y parseable.",
    "Usar el esquema requerido completo, sin campos extra en esta salida.",
    "Redactar reglas en frases cortas, accionables y sin duplicados.",
    "Marcar explicitamente supuestos cuando falte evidencia."
  ],
  "activity_rules": [
    "Alinear cada actividad a: problema, conceptos, fuentes, analisis propio y conclusion juridica.",
    "Incluir postura academica propia sustentada en argumentos verificables.",
    "Cerrar con una conclusion transferible a la practica juridica."
  ],
  "quality_gates": [
    "Validar sintaxis JSON antes de guardar memoria.",
    "Bloquear propagacion automatica si la salida no es parseable.",
    "Aplicar compresion por union-dedupe lossless; no recortar contenido valido.",
    "Verificar consistencia con README y programa analitico locales."
  ],
  "latex_rules": [
    "Mantener compatibilidad con la suite LaTeX de la asignatura.",
    "Usar UTF-8 y acentos correctos en titulos, autores y secciones.",
    "Separar contenido, citas y bibliografia para compilacion estable."
  ],
  "bibliography_rules": [
    "No inventar fuentes ni metadatos bibliograficos.",
    "Agregar nuevas referencias en etica-y-moral-juridica.bib cuando sean verificables.",
    "Citar fuentes institucionales UnADM cuando apliquen al encuadre curricular.",
    "Supuesto: existen entradas duplicadas en la .bib local; deduplicar claves sin perder registros equivalentes."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas parseables y verificadas.",
    "Mantener historial de ciclos con marca de normalizacion cuando aplique.",
    "Priorizar consolidacion de reglas generales hasta recuperar memoria fuente util."
  ],
  "open_questions": [
    "Falta recuperar memoria estructurada de Actividad 1 para propagacion semantica completa.",
    "Confirmar criterio editorial para deduplicar entradas bib con misma obra y distinta clave.",
    "Definir politica de bloqueo por numero de ciclos consecutivos sin JSON parseable."
  ]
}