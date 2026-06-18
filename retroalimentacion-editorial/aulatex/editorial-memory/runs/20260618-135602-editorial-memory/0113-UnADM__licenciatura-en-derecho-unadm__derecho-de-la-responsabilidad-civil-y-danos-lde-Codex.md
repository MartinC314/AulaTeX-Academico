{
  "summary": [
    "Base institucional UnADM heredada y activa.",
    "Destino sin memoria previa; se inicializa con reglas minimas verificables.",
    "Se conserva alerta de salida no estructurada en ciclo 1."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en toda entrega.",
    "Usar contexto de Licenciatura en Derecho y materia de responsabilidad civil y danos.",
    "Marcar como supuesto cualquier dato no confirmado por guia oficial."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Alinear cada producto a: problema, conceptos/fuentes, analisis propio y conclusion juridica.",
    "Mantener separacion entre reporte, presentacion, programa analitico y bibliografia .bib."
  ],
  "activity_rules": [
    "Adaptar actividades heredadas de filosofia del derecho al enfoque de responsabilidad civil y danos.",
    "Incluir transferencia a practica juridica en el cierre.",
    "No arrastrar contenido tematico de origen si no aplica al dano o la responsabilidad civil."
  ],
  "quality_gates": [
    "Validar que la salida sea JSON parseable antes de propagar.",
    "Revisar consistencia con pauta editorial de la materia.",
    "Verificar que toda afirmacion juridica tenga fuente o se marque como analisis propio.",
    "Aplicar control de no regresion sobre reglas utiles heredadas."
  ],
  "latex_rules": [
    "Conservar plantilla LaTeX de la materia como base de reportes.",
    "Completar metadatos del documento por actividad sin cambiar identidad institucional.",
    "Evitar caracteres rotos en rutas, nombres de archivo y comandos."
  ],
  "bibliography_rules": [
    "Agregar fuentes especificas de cada actividad en el .bib local de la materia.",
    "Conservar fuentes institucionales UnADM ya registradas.",
    "No inventar fuentes; si falta referencia, registrar pregunta abierta."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo reglas estables y no tematicas de una actividad puntual.",
    "En ciclo 1, aplicar normalizacion manual por antecedente de salida no estructurada.",
    "Usar compresion por union-dedupe sin recorte semantico."
  ],
  "open_questions": [
    "Confirmar si existe guia oficial de formato para actividades de esta materia.",
    "Confirmar convencion final de nombres de archivos con 'danos' versus 'daños' en todo el arbol.",
    "Validar plantilla .tex por posible truncamiento local antes de reutilizar."
  ]
}