```json
{
  "summary": [
    "Supuesto: se conserva memoria institucional heredada por union-dedupe sin recorte.",
    "Materia destino: Filosofía del Derecho en UnADM, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "La actividad debe mantener identidad UnADM, integridad académica, citas verificables y conclusión jurídica propia.",
    "Existe antecedente de salida no parseable desde Codex; aplicar validación JSON estricta.",
    "El contexto local define la carpeta de asignatura como punto de entrada canónico."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato académico.",
    "Alinear contenido con Licenciatura en Derecho y la asignatura Filosofía del Derecho.",
    "Conservar enfoque jurídico con postura propia sustentada.",
    "Tratar la memoria institucional heredada desde Codex como provisional hasta validación local."
  ],
  "structure_rules": [
    "Seguir el flujo editorial: problema, conceptos o fuentes, producto solicitado, análisis propio y conclusión transferible.",
    "Redactar con claridad, fundamento jurídico y evidencia verificable.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Vincular cada entrega con los ejes del programa analítico.",
    "Separar hechos, conceptos, argumentos y postura personal."
  ],
  "activity_rules": [
    "Adaptar la actividad 4 a los ejes de trabajo del programa analítico.",
    "Incluir explícitamente el problema jurídico o social que activa la entrega.",
    "Integrar conceptos, normas, doctrina o datos pertinentes según la consigna.",
    "Desarrollar análisis propio antes de la conclusión.",
    "Cerrar con conclusión jurídica aplicable a la práctica profesional.",
    "Supuesto: confirmar si la actividad 4 corresponde a interpretación jurídica antes de fijar fuentes específicas."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de propagar memoria aguas abajo.",
    "Revisar que no haya respuesta no estructurada heredada de ciclos previos.",
    "Verificar consistencia con la pauta editorial local de la asignatura.",
    "Confirmar instrucciones específicas de la actividad antes de redactar.",
    "Validar que el archivo .bib no tenga entradas truncadas o incompletas.",
    "Comprobar que toda cita tenga referencia bibliográfica verificable.",
    "No propagar reglas dudosas sin marcarlas como supuesto."
  ],
  "latex_rules": [
    "Mantener compatibilidad con archivos .tex de reportes y presentaciones de la materia.",
    "Citar en el .tex solo claves existentes en el .bib.",
    "No renombrar claves bibliográficas ya usadas en documentos activos.",
    "Verificar nombres de archivos listados en README antes de compilar.",
    "Supuesto: README lista nombres con caracteres dañados o plantilla sin resolver; confirmar nombres reales antes de compilar.",
    "Compilar después de actualizar citas y bibliografía.",
    "Evitar cambios estructurales que rompan reportes o presentaciones existentes."
  ],
  "bibliography_rules": [
    "Agregar fuentes específicas de la actividad en el .bib de la asignatura.",
    "Priorizar fuentes institucionales y jurídicas verificables: UnADM, SCJN y UNAM-IIJ.",
    "No inventar fuentes ni metadatos faltantes.",
    "Marcar datos incompletos como pendiente.",
    "Conservar claves originales del .tex para evitar recompilaciones.",
    "Usar filosofia-del-derecho-clean.bib solo si coincide con la actividad y las claves citadas.",
    "No usar entradas bibliográficas truncadas.",
    "Registrar URL verificable cuando la fuente sea digital.",
    "Supuesto: filosofia-del-derecho-clean.bib se asocia a actividad de interpretación jurídica (Semana 7); verificar si aplica a la actividad 4.",
    "Claves verificadas en .bib limpio: hernandezManriquezHermeneutica2019, scjnMemoriaArgumentacion2008, scjnViolenciaFisica2022.",
    "Supuesto: entrada scjnIncapacidadResistencia2019 aparece truncada en la fuente; no citar hasta completarla."
  ],
  "propagation_hints": [
    "Propagar arriba-y-laterales conservando union-dedupe sin regresión.",
    "Mantener bandera de normalización manual en ciclo 1 si existen salidas no estructuradas.",
    "Reutilizar reglas institucionales y ajustar solo elementos propios de actividad.",
    "Preservar reglas útiles previas aunque provengan de memoria provisional.",
    "Propagar mejoras verificables a actividades laterales de la misma asignatura."
  ],
  "open_questions": [
    "Confirmar instrucciones específicas de la actividad 4: producto, extensión y criterios de evaluación.",
    "Definir si se usará el .bib limpio existente o un .bib incremental para esta actividad.",
    "Verificar si hay rúbrica docente adicional no incluida en README o programa analítico.",
    "Confirmar si actividad 4 corresponde a interpretación jurídica o a otra consigna.",
    "Revisar nombres de archivos en README que aparecen con caracteres faltantes o plantilla sin resolver.",
    "Confirmar el nombre real del archivo .bib (README usa plantilla PowerShell sin resolver para el slug)."
  ],
  "sources": [
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-4"
  ],
  "compression": {
    "method": "union-dedupe",
    "lossless": true
  },
  "schema_version": 1
}
```