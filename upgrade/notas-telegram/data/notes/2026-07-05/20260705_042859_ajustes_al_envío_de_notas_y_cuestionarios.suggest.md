# 04:28 - Ajustes al envío de notas y cuestionarios · Sugerencias

Nota origen: [04:28 - Ajustes al envío de notas y cuestionarios](20260705_042859_ajustes_al_envío_de_notas_y_cuestionarios.md)

## Metadata

{
  "action": "suggest",
  "label": "Sugerencias",
  "schema_version": "v1",
  "created_at": "2026-07-05T04:33:35.116227",
  "source_note": "20260705_042859_ajustes_al_envío_de_notas_y_cuestionarios.md"
}

## Nucleo

El objetivo práctico es convertir el envío en un flujo determinista y verificable: primero debe salir el texto principal con sus botones de acción, después la versión en Markdown y el audio, luego deben ejecutarse los procesos derivados y, sólo cuando esos procesos queden resueltos, debe dispararse Play. En paralelo, el sistema debe conservar los saltos de línea en cuestionarios y dejar de recortar nombres de archivo, porque ambas cosas afectan claridad, trazabilidad y operación.

## Desarrollo

La prioridad principal es el orden de entrega, porque cada elemento cumple una función distinta y su secuencia cambia la experiencia. El texto con botones sirve como punto de entrada operativo; el Markdown y el audio amplían el contenido; los derivados procesan lo ya enviado; Play depende de que lo anterior exista o esté estable. Si esa cadena no se respeta, aparecen estados ambiguos, acciones fuera de contexto o ejecuciones incompletas.

Conviene separar contenido, presentación y orquestación. El problema de los saltos de línea no es de “limpieza” sino de semántica: en cuestionarios, una ruptura de línea puede separar opciones, instrucciones o bloques de respuesta. Filtrarla mejora uniformidad visual sólo a costa de perder claridad funcional. La regla correcta es conservar estructura textual cuando esa estructura tiene valor para la comprensión.

El nombre del archivo no es un detalle cosmético. Si se corta, se pierde trazabilidad entre lo que el usuario recibe, lo que el sistema guarda y lo que los procesos posteriores consumen. Un nombre útil debe mantener legibilidad, unicidad y compatibilidad con los límites del canal o del almacenamiento, sin perder la extensión ni los identificadores clave.

También hace falta decidir qué pasos son bloqueantes y cuáles pueden degradarse. Si falta el texto con botones, el envío queda roto y debe frenarse. Si falla un elemento complementario como un audio, puede convenir continuar con aviso interno y reintento posterior, siempre que eso no rompa los derivados. Ese criterio evita que un fallo secundario detenga todo, pero también impide que se dispare Play sobre un estado inconsistente.

La validación debe centrarse en resultados observables: que el receptor vea el orden correcto, que los botones acompañen al texto principal, que el Markdown y el audio lleguen asociados al mismo envío lógico, que los derivados se ejecuten una sola vez, que Play ocurra después y que los cuestionarios mantengan exactamente los saltos de línea esperados.

## Accionables

1. Implementar una orquestación por etapas con estados explícitos para el envío completo.
   - Aplicar cuando el flujo combine varios artefactos y acciones asíncronas en una misma experiencia.
   - Definir estados mínimos como: texto_con_botones_enviado, markdown_enviado, audio_enviado, derivados_ejecutados y play_ejecutado.
   - Hacer que cada paso se habilite sólo tras confirmación del paso anterior o tras una política de timeout bien definida.
   - Riesgo a cuidar: un encadenamiento demasiado rígido puede bloquear todo el flujo por fallos no críticos; conviene marcar qué elementos son obligatorios y cuáles admiten reintento diferido.

2. Encadenar Play a un evento de finalización real de los derivados, no a una llamada secuencial ciega.
   - Aplicar cuando los derivados tengan latencia variable, dependan de colas o puedan ejecutarse en paralelo.
   - Emitir un evento de “derivados completados” con un identificador único del envío y usar una clave de idempotencia para que Play se ejecute una sola vez.
   - Definir una salida controlada si los derivados quedan colgados: espera máxima, reintento o modo degradado explícito.
   - Riesgo a cuidar: si no hay idempotencia, los reintentos pueden disparar Play varias veces; si no hay timeout, Play puede no ocurrir nunca.

3. Desactivar el filtrado de saltos de línea en cuestionarios y mover la normalización a reglas por tipo de contenido.
   - Aplicar cuando el texto incluya opciones, instrucciones por bloques, respuestas abiertas o cualquier estructura donde la separación visual cambie el sentido.
   - Conservar el texto fuente tal como se genera y escapar sólo los caracteres que el canal necesite para no romper el render, sin colapsar líneas.
   - Probar la visualización en los destinos reales, porque algunos canales interpretan distinto una ruptura simple y un párrafo.
   - Riesgo a cuidar: ciertos renderizadores pueden introducir espacios extra o dobles separaciones; la solución no es volver a filtrar todo, sino ajustar el renderer por canal.

4. Corregir la estrategia de nombres de archivo para preservar legibilidad, unicidad y extensión completa.
   - Aplicar cuando el sistema exporte, adjunte o procese archivos que luego deban rastrearse entre envío, almacenamiento y tareas derivadas.
   - Usar un esquema como nombre_base_normalizado + identificador_unico + tipo + extensión, manteniendo la extensión al final aunque exista truncamiento.
   - Si hay límites de longitud, recortar sólo la parte menos crítica del nombre y conservar identificador y extensión; si hace falta, separar nombre visible y clave interna.
   - Riesgo a cuidar: un truncamiento ingenuo puede generar colisiones, romper asociaciones con derivados o producir archivos inválidos para ciertas APIs.

5. Añadir validaciones automáticas y observabilidad del flujo antes de considerar resuelto el ajuste.
   - Aplicar cuando se modifique la secuencia de envío, los conectores externos o la forma de renderizar contenido.
   - Registrar un identificador de correlación por envío y validar automáticamente: orden de salida, presencia de botones, entrega de Markdown y audio, nombre final de archivo, ejecución única de derivados, disparo posterior de Play y preservación de saltos de línea.
   - Incorporar pruebas de integración con el canal real o con un entorno que reproduzca su comportamiento, no sólo pruebas unitarias del código interno.
   - Riesgo a cuidar: si la observabilidad no distingue entre fallo real y latencia normal, generará ruido operativo y diagnósticos falsos.

## Evidencias y supuestos

La solución depende de validación externa en varios puntos. Hace falta confirmar que el canal de envío respeta o al menos permite reconstruir el orden de mensajes y adjuntos, porque algunos conectores reordenan entregas asíncronas. También hay que verificar que los botones de acción puedan viajar junto al texto principal en el formato esperado y que el receptor los renderice de forma consistente.

La preservación de saltos de línea depende del motor de render del destino. Hay plataformas que convierten una línea nueva en espacio, otras la convierten en salto visual y otras requieren doble salto para separar bloques. La regla de conservar líneas es correcta desde el punto de vista semántico, pero necesita pruebas reales por canal para no introducir un resultado visual inesperado.

La política de nombres de archivo depende de límites externos de longitud, caracteres permitidos, codificación Unicode y tratamiento de extensiones en cada API o sistema de almacenamiento. La corrección no debe darse por válida hasta probar nombres largos, acentos, símbolos y casos con colisión potencial.

El encadenamiento de derivados y Play depende de cómo se exponen sus estados. Si los derivados no informan éxito, error o finalización parcial, Play no puede dispararse de forma confiable. También debe validarse que los reintentos no generen duplicados y que la idempotencia funcione de extremo a extremo.

## Sintesis breve

La mejora más rentable es convertir el envío en una cadena con estados verificables: texto con botones, luego Markdown y audio, después derivados y finalmente Play. En paralelo, conviene dejar intactos los saltos de línea en cuestionarios y corregir el esquema de nombres de archivo para no perder trazabilidad. Si ese flujo se implementa con validaciones, eventos de finalización e idempotencia, se reduce el desorden operativo y se vuelve mucho más fácil detectar y corregir fallos reales.
