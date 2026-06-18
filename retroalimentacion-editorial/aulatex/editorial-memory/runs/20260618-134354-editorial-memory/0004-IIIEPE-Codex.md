{
  "summary": [
    "Inicializar memoria editorial de IIIEPE con base minima verificable.",
    "Aplicar compresion por union y deduplicacion sin recorte.",
    "Marcar supuestos por ausencia de lineamientos institucionales explicitos."
  ],
  "identity_rules": [
    "Usar el nombre institucional objetivo: IIIEPE.",
    "Mantener tono academico, formal y consistente.",
    "No asumir identidad visual ni lema institucional sin fuente. [supuesto]"
  ],
  "structure_rules": [
    "Definir portada, indice, introduccion, desarrollo, conclusiones y referencias como esqueleto por defecto. [supuesto]",
    "Separar secciones con titulos claros y jerarquia consistente.",
    "Conservar trazabilidad entre objetivos, contenido y resultados."
  ],
  "activity_rules": [
    "Registrar nuevas reglas solo si son verificables en contexto o fuente explicita.",
    "No eliminar reglas utiles previas; solo fusionar y deduplicar.",
    "Propagar reglas generales hacia niveles superiores y laterales sin cambiar su sentido.",
    "Anotar conflictos y enviar a preguntas abiertas antes de sobreescribir."
  ],
  "quality_gates": [
    "JSON de salida siempre valido y conforme al esquema requerido.",
    "Sin duplicados semanticos entre listas.",
    "Cada regla debe ser accionable y en frase corta.",
    "Marcar supuestos cuando falten datos institucionales.",
    "No inventar fuentes bibliograficas ni normativas."
  ],
  "latex_rules": [
    "Usar codificacion UTF-8 y soporte para espanol.",
    "Mantener estructura LaTeX modular por secciones/archivos cuando aplique.",
    "Evitar paquetes redundantes o en conflicto.",
    "Compilar sin errores ni warnings criticos antes de liberar."
  ],
  "bibliography_rules": [
    "Incluir solo referencias realmente citadas en el documento.",
    "Usar un estilo bibliografico unico y consistente en todo el proyecto. [supuesto]",
    "Verificar campos minimos: autor, titulo, ano y fuente.",
    "No crear entradas bibliograficas sin respaldo verificable."
  ],
  "propagation_hints": [
    "Propagar estas reglas como baseline institucional inicial de IIIEPE.",
    "En niveles laterales, reutilizar reglas generales y adaptar solo con evidencia local.",
    "Priorizar futuras actualizaciones con lineamientos oficiales de