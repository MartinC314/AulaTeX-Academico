```json
{
  "summary": [
    "Consolidar memoria base de la materia Filosofia del Derecho con identidad UnADM.",
    "Aplicar union-dedupe lossless y conservar reglas heredadas sin regresion.",
    "Usar la carpeta de materia como entrada canonica para actividades y entregables.",
    "Mantener integridad academica, citas verificables y conclusion juridica con criterio propio.",
    "Normalizar insumos heredados no JSON parseable antes de reutilizarlos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en redaccion y formato.",
    "Alinear entregables con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "No eliminar reglas heredadas de control de calidad y normalizacion.",
    "Usar la malla curricular de Derecho UnADM como fuente curricular verificada.",
    "Conservar fuente provisional heredada: Codex desde ingenieria-en-sistemas-computacionales. [supuesto]"
  ],
  "structure_rules": [
    "Usar la materia como nodo canonico para reportes, presentaciones y bibliografia.",
    "Estructurar cada producto con problema, conceptos o fuentes, analisis propio y cierre argumentativo.",
    "Reflejar los cinco ejes editoriales del programa analitico en cada actividad.",
    "Mantener trazabilidad entre actividad, archivo .tex y .bib de materia.",
    "Separar productos en reporte, presentacion, programa analitico y referencias locales.",
    "Tratar nombres anomalos del README como pendientes de correccion, no como canon definitivo. [supuesto]"
  ],
  "activity_rules": [
    "Iniciar cada actividad con problema juridico o social delimitado.",
    "Integrar normas, doctrina o datos pertinentes al problema.",
    "Cumplir el tipo de producto solicitado por la planeacion semanal.",
    "Incluir postura academica propia y conclusion transferible a la practica juridica.",
    "Agregar fuentes especificas de actividad solo cuando sean verificables.",
    "Conservar el vinculo editorial con actividad-1 al propagar reglas a la materia."
  ],
  "quality_gates": [
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Validar coherencia curricular con datos del README de materia.",
    "Exigir citas verificables para toda afirmacion sustantiva.",
    "Confirmar que no se eliminen reglas utiles previas en cada ciclo.",
    "Verificar que cada cita en .tex tenga entrada BibTeX correspondiente.",
    "Compilar o revisar referencias antes de cerrar entregables."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre claves BibTeX y citas usadas en .tex.",
    "No renombrar claves bibliograficas citadas sin migracion completa.",
    "Separar entregables por tipo: reporte y presentacion en archivos .tex dedicados.",
    "Preservar rutas y nombres canonicos de la materia para evitar roturas de compilacion.",
    "Usar filosofia-del-derecho-clean.bib como archivo depurado disponible mientras se confirma el .bib canonico. [supuesto]",
    "Mantener claves originales de filosofia-del-derecho-clean.bib si ya estan citadas en .tex."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y malla curricular como base contextual.",
    "Agregar fuentes especificas de actividad en el .bib de la materia.",
    "Usar solo fuentes verificables; no inventar referencias.",
    "Conservar entradas depuradas ya existentes y deduplicar sin perdida.",
    "Preservar entradas academicas verificables de UNAM, IIJ y SCJN ya incluidas.",
    "Registrar URL, ano, autor institucional y datos de tesis cuando existan.",
    "Conservar claves verificables: hernandezManriquezHermeneutica2019, scjnMemoriaArgumentacion2008, scjnViolenciaFisica2022, scjnIncapacidadResistencia2019."
  ],
  "propagation_hints": [
    "Propagar estas reglas arriba al nivel licenciatura y lateralmente a materias afines de Derecho.",
    "Marcar ciclo 1 con normalizacion manual cuando haya insumos no estructurados.",
    "Reusar puertas de calidad heredadas como filtro previo en nuevas actividades.",
    "Mantener etiqueta de compresion union-dedupe lossless en toda propagacion.",
    "Propagar reglas bibliograficas y de trazabilidad a materias con reportes y presentaciones LaTeX.",
    "Evitar propagar nombres de archivo anomalos hasta resolverlos localmente."
  ],
  "open_questions": [
    "Definir fuente definitiva para reemplazar la fuente provisional heredada.",
    "Confirmar nombre final del archivo .bib canonico de la materia. [supuesto]",
    "Corregir posibles nombres de archivo con caracteres anomalos en README. [supuesto]",
    "Precisar plantilla minima obligatoria para reporte vs presentacion.",
    "Determinar si filosofia-del-derecho-clean.bib reemplaza al placeholder del README. [supuesto]",
    "Confirmar si las fuentes depuradas de Semana 7 aplican tambien a actividad-1. [supuesto]",
    "Resolver el placeholder PowerShell del nombre .bib en README y programa analitico. [supuesto]"
  ],
  "sources": [
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde",
    "UnADM"
  ],
  "compression": {
    "method": "union-dedupe",
    "lossless": true
  },
  "schema_version": 1
}
```