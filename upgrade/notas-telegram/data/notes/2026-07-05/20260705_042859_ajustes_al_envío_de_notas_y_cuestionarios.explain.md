# 04:28 - Ajustes al envío de notas y cuestionarios · Explicar

Nota origen: [04:28 - Ajustes al envío de notas y cuestionarios](20260705_042859_ajustes_al_envío_de_notas_y_cuestionarios.md)

## Metadata

{
  "action": "explain",
  "label": "Explicar",
  "schema_version": "v1",
  "created_at": "2026-07-05T04:31:43.848998",
  "source_note": "20260705_042859_ajustes_al_envío_de_notas_y_cuestionarios.md"
}

## Nucleo

La idea central es corregir el flujo de envío para que respete mejor la experiencia de uso, la secuencia lógica del sistema y la claridad del contenido. El orden propuesto es: primero entregar el texto principal con botones de acción, después la versión en Markdown que ya se envía, luego el audio, después ejecutar los procesos derivados y, al final, disparar Play, que todavía no se está ejecutando.

El alcance no es solo visual. Abarca tres capas del sistema al mismo tiempo: la presentación al usuario, la orquestación técnica de eventos y la conservación de la estructura informativa. Por eso también aparecen dos ajustes complementarios: corregir el recorte de nombres de archivo y dejar de filtrar los saltos de línea en cuestionarios, porque esos saltos aportan claridad y no son ruido.

## Desarrollo

La propuesta parte de un supuesto fuerte: el primer contacto del usuario debe ser el contenido más útil para actuar de inmediato. Por eso el texto con botones de acción va primero. No se trata solo de “mostrar algo antes”, sino de priorizar una salida que permita decidir, responder o continuar el flujo sin depender de formatos secundarios.

La versión en Markdown cumple otra función. Aporta estructura, portabilidad y consistencia de formato. Si ya existe y se envía correctamente, no hay que reemplazarla, sino ubicarla en un lugar coherente dentro de la secuencia. Su valor no es la inmediatez interactiva, sino la fidelidad estructural del contenido.

El audio aparece después porque su función suele ser complementaria. Sirve como modalidad adicional de consumo, pero no reemplaza la capacidad de inspección rápida y acción que da el texto visible con controles. Esto sugiere una jerarquía de utilidad: primero lo accionable, después lo estructurado, después lo multimodal.

La mención a los derivados introduce una distinción importante entre entrega y postproceso. El sistema ya ejecuta tareas posteriores al envío, lo cual implica que existe una canalización por etapas. La decisión propuesta es mantener esos derivados después de las entregas principales, evitando que compitan con la salida inicial o alteren la percepción de completitud del envío.

La incorporación de Play al final indica que falta cerrar el ciclo de automatización. Si Play no se ejecuta todavía, el flujo queda técnicamente incompleto aunque parte del contenido ya llegue. Esto sugiere una dependencia operacional: Play debe dispararse cuando lo anterior ya ocurrió en el orden esperado. Si no se define esa dependencia, pueden aparecer estados inconsistentes, como reproducción antes de que todo esté listo o ausencia de reproducción aun cuando el resto terminó bien.

El problema de los nombres de archivo apunta a trazabilidad y confiabilidad. Un nombre cortado no es solo un defecto cosmético. Puede romper asociaciones entre contenido y recurso, dificultar búsquedas, generar ambigüedad entre versiones y entorpecer auditorías o depuración. Si el sistema distribuye varios artefactos por envío, el nombre completo pasa a ser un identificador operativo, no solo una etiqueta.

La decisión de no filtrar saltos de línea en cuestionarios revela otra idea de fondo: no toda normalización mejora el resultado. En formularios, preguntas o bloques con opciones, los saltos de línea suelen codificar estructura semántica. Separan enunciados, opciones, aclaraciones o instrucciones. Eliminar esos cortes puede compactar el texto, pero reduce comprensión, aumenta carga cognitiva y vuelve más fácil interpretar mal una pregunta.

Los conceptos involucrados se ordenan así:
- Markdown funciona como formato estructurado y portable del contenido.
- Los botones de acción funcionan como interfaz para decidir o continuar el flujo sin fricción.
- Los derivados funcionan como tareas posteriores que enriquecen o completan el procesamiento.
- Play funciona como acción final automatizada que hoy está ausente o mal encadenada.
- Los saltos de línea funcionan como marcadores de claridad y estructura, especialmente en cuestionarios.

La implicación técnica más importante es que el sistema necesita una secuencia explícita de eventos, no solo una lista de salidas. Cuando hay varios formatos, procesos posteriores y una acción final, el orden deja de ser un detalle de implementación y pasa a ser parte del comportamiento esperado del producto.

## Accionables

- Documentar el orden objetivo del flujo como contrato operativo: texto con botones, Markdown, audio, derivados y Play.
- Registrar marcas de tiempo por etapa para verificar si el sistema respeta la secuencia prevista en condiciones reales.
- Separar claramente las salidas visibles para el usuario de los procesos internos posteriores para evitar bloqueos o confusiones de estado.
- Definir la condición exacta que dispara Play: éxito de todos los derivados, finalización del audio, o simple cierre de la cola principal.
- Revisar la lógica de nombres de archivo en todos los puntos donde puedan truncarse: generación, serialización, transporte, interfaz y almacenamiento temporal.
- Establecer pruebas con nombres largos, caracteres especiales y múltiples extensiones para detectar recortes o normalizaciones no deseadas.
- Eliminar el filtrado de saltos de línea en cuestionarios y verificar que el renderizado final conserve la estructura original.
- Probar cuestionarios con listas, opciones multilínea e instrucciones intercaladas para confirmar que la legibilidad mejora al preservar los cortes.
- Añadir validaciones de integridad para confirmar que cada envío incluye los artefactos esperados y que Play no se omite silenciosamente.
- Definir un comportamiento de contingencia cuando falle una etapa intermedia, para que el usuario reciba una señal clara y no un flujo aparentemente completo pero incompleto.

## Evidencias y supuestos

Hay señales explícitas de que el sistema ya entrega una versión en Markdown y ya ejecuta derivados. También hay una indicación clara de que Play todavía no ocurre y de que los nombres de archivo se están cortando. La conservación de saltos de línea en cuestionarios aparece como una necesidad funcional, no como una preferencia estética.

Quedan algunas incertidumbres que conviene validar:
- No está completamente especificado si el texto con botones y la versión en Markdown son dos artefactos distintos o dos vistas del mismo contenido.
- No está confirmado si Play debe esperar el éxito total de los derivados o simplemente ejecutarse después de iniciarlos.
- No está localizado el origen del recorte de nombres: puede estar en backend, transporte, cliente o capa de presentación.
- No está detallado si preservar saltos de línea afecta otros consumidores del contenido, como indexadores, exportadores o parsers automáticos.
- No está indicado si el audio depende del mismo contenido estructurado que el Markdown o si sigue una ruta separada de generación.

El supuesto dominante es que la claridad para el usuario y la integridad del flujo valen más que cualquier simplificación basada en compactar formato o adelantar procesos internos.

## Sintesis breve

La decisión correcta no es reducir formatos ni “limpiar” estructura, sino ordenar el sistema para que entregue primero lo más accionable, conserve después lo más estructurado, ejecute al final lo automático y no destruya señales de claridad como los nombres completos y los saltos de línea. Un flujo bien secuenciado mejora comprensión, trazabilidad y confiabilidad al mismo tiempo.
