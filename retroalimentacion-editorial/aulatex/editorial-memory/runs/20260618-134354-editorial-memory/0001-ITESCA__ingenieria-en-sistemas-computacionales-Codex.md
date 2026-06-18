{
  "summary": [
    "Carrera objetivo: ITESCA Ingenieria en Sistemas Computacionales.",
    "La estructura se basa en reticulas oficiales 2024 con tronco comun y dos especialidades.",
    "Cada materia debe incluir reporte, presentacion, bibliografia local y guia de compilacion.",
    "Existe una materia semilla no curricular: primer-ingreso-isc.",
    "Hay archivos base de carrera: README, bibliografia-itesca-isc.bib y reporte-itesca-isc.tex."
  ],
  "identity_rules": [
    "Mantener nombre institucional completo: Instituto Tecnologico Superior de Cajeme.",
    "Usar identificador de carrera ISC en metadatos y nombres cortos.",
    "Conservar enfoque de trayectoria academica por carrera en documentos marco.",
    "Marcar como supuesto todo dato pendiente en metadatos (por definir)."
  ],
  "structure_rules": [
    "Conservar separacion por bloques: Tronco comun, Especialidad Software y Especialidad Produccion Multimedia.",
    "Mantener slugs de materias en minusculas con guiones y sufijo -isc.",
    "Preservar carpeta primer-ingreso-isc como semilla no curricular.",
    "Asegurar que cada carpeta de materia tenga reporte, presentacion, bibliografia local y guia de compilacion."
  ],
  "activity_rules": [
    "Generar contenidos por materia alineados al slug oficial de la reticula.",
    "Reutilizar plantilla de reporte de carrera como base para materias.",
    "Registrar cambios de estructura en README de carrera cuando se agreguen materias o especialidades.",
    "Validar que la bibliografia local de cada materia exista antes de cerrar una entrega."
  ],
  "quality_gates": [
    "No eliminar reglas previas utiles; solo ampliar por union y deduplicacion.",
    "No inventar fuentes; citar solo recursos existentes y verificables.",
    "Verificar consistencia entre README y carpetas reales de materias.",
    "Confirmar codificacion UTF-8 y compilacion limpia de .tex principales.",
    "Marcar campos truncados o incompletos como pendiente de revision."
  ],
  "latex_rules": [
    "Usar \\providecommand para metadatos institucionales reutilizables.",
    "Centralizar variables de portada y contexto en reporte-itesca-isc.tex.",
    "Evitar sobrescribir comandos ya definidos en capas inferiores sin justificacion.",
    "Mantener