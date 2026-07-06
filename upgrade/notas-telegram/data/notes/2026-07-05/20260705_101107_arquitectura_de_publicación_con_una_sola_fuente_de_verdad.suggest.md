# 10:11 - Arquitectura de publicación con una sola fuente de verdad · Sugerencias

Nota origen: [10:11 - Arquitectura de publicación con una sola fuente de verdad](20260705_101107_arquitectura_de_publicación_con_una_sola_fuente_de_verdad.md)

## Metadata

{
  "action": "suggest",
  "label": "Sugerencias",
  "schema_version": "v1",
  "created_at": "2026-07-05T10:16:04.963295",
  "source_note": "20260705_101107_arquitectura_de_publicación_con_una_sola_fuente_de_verdad.md"
}

## Nucleo

El objetivo práctico es montar un flujo de publicación donde el contenido se define una sola vez, desde un modelo canónico, y desde ahí se generan de forma consistente el texto más accionable para personas, el Markdown y el audio, sin editar cada salida por separado. La prioridad operativa debe ser doble: que la entrega siga siendo clara para lectura humana y que la automatización solo avance hasta el punto donde los errores puedan detectarse y corregirse con fiabilidad.

## Desarrollo

La decisión más importante no es técnica sino de control: si cada formato se toca por separado, la divergencia deja de ser una excepción y pasa a ser el estado normal. Por eso conviene fijar primero una fuente canónica única y retrasar cualquier automatismo adicional hasta que esa base sea estable.

La fuente canónica debería modelar significado, no apariencia. Eso implica guardar estructura explícita como bloques, preguntas, opciones, pasos y marcas de salto relevante, en vez de confiar en que un formato visual arrastre el sentido por sí solo. Cuando un salto de línea cambia la forma en que se responde o interpreta un cuestionario, ese salto debe considerarse parte del contenido. Cuando solo responde a maquetación o comodidad visual, conviene normalizarlo para evitar fragilidad.

La prioridad de lectura humana obliga a decidir qué salida manda en la experiencia. Si la pieza más útil para actuar es el texto con acciones, esa salida debería ser la primera derivación y también la referencia visible de control. El Markdown puede ser una proyección fiel de esa estructura. El audio, en cambio, rara vez es una copia literal perfecta: suele necesitar ajustes de oralidad, pausas, pronunciación o eliminación de elementos visuales. Eso sugiere tratar el audio como derivado controlado, no como espejo ciego.

La estrategia dual de nombres de archivo resuelve una tensión real. Las personas necesitan un nombre visible completo y reconocible. Los sistemas necesitan un nombre técnico estable, normalizado y predecible. Si ambos nombres nacen del mismo registro canónico, se evita que el archivo “humano” y el archivo “técnico” se desalineen con el tiempo. Si se resuelven manualmente en momentos distintos, tarde o temprano aparecerán colisiones, ambigüedad o búsquedas fallidas.

La automatización de derivados solo compensa cuando se puede repetir sin efectos extraños y cuando cada paso conoce sus dependencias. Idempotencia y validación previa son el mínimo para automatizar sin sorpresas. El disparo final de Play merece más cautela porque introduce un riesgo distinto: un error silencioso en una etapa intermedia suele dejar rastros; un error silencioso al publicar o reproducir puede parecer éxito mientras entrega algo incorrecto. Por eso conviene exigir un estado inequívoco, trazabilidad y una política de uso clara antes de automatizar ese último tramo.

## Accionables

1. Definir un modelo canónico mínimo antes de automatizar salidas.
   - Crea un esquema con ID estable, título visible, nombre técnico, tipo de pieza, bloques ordenados, marcas de salto significativo, estado editorial y hash del contenido.
   - Usa tipos de bloque explícitos como párrafo, pregunta, opción, paso, cita o nota de audio para que cada renderizador sepa qué preservar y qué adaptar.
   - Aplica cuando hoy existe edición duplicada entre texto, Markdown y audio o cuando aparecen inconsistencias entre representaciones.
   - Riesgo principal: sobrediseñar el esquema y volver lenta la adopción. La contención útil es empezar por el menor número de campos que ya evita divergencias reales y versionar el esquema cuando aparezcan nuevos casos.

2. Establecer un orden de derivación donde la salida más accionable sea la referencia humana.
   - Genera primero la pieza de texto orientada a la acción y úsala como revisión primaria; genera Markdown desde la misma estructura y genera el guion de audio desde reglas específicas de oralización.
   - Separa “contenido base” de “ajustes de salida” para que el audio pueda introducir pausas, pronunciaciones o simplificaciones sin romper la fuente única.
   - Aplica cuando la claridad para personas es más importante que la simetría perfecta entre formatos o cuando el audio necesita sonar natural y no solo exacto.
   - Riesgo principal: intentar que el audio sea una copia literal del texto y terminar con una experiencia torpe o ambigua. La señal de alerta es que la salida oral empiece a reproducir marcas visuales sin valor para quien escucha.

3. Convertir la preservación del formato en una regla semántica y no en una herencia ciega.
   - Conserva saltos de línea solo cuando cambien la interpretación, el orden de respuesta o la legibilidad operativa, como en cuestionarios, listas de opciones o pasos secuenciales.
   - Normaliza espacios, envolturas visuales y otros detalles cuando no aporten significado, para reducir fragilidad en renderizados y diferencias artificiales.
   - Añade una marca explícita para “salto significativo” o usa tipos de bloque que ya lo hagan inequívoco, en lugar de confiar en texto plano ambiguo.
   - Aplica cuando parte del contenido funciona como formulario, checklist o secuencia donde la disposición altera el uso.
   - Riesgo principal: preservar demasiado y volver quebradizo el flujo ante cambios menores, o preservar demasiado poco y dañar el sentido de uso. La validación práctica es revisar algunos casos reales donde un salto de línea sí cambie la respuesta o la comprensión.

4. Resolver nombres de archivo con una estrategia dual generada desde el mismo origen.
   - Mantén un nombre visible completo para personas y un nombre técnico normalizado para sistemas, ambos emitidos desde el registro canónico y nunca escritos a mano por separado.
   - Usa un ID estable para evitar colisiones y permite que el nombre visible cambie sin romper referencias internas, siempre que el identificador técnico permanezca consistente.
   - Normaliza el nombre técnico con reglas fijas de minúsculas, separación uniforme, eliminación de caracteres conflictivos y longitud segura para los sistemas destino.
   - Aplica cuando los archivos circulan entre personas y automatizaciones, o cuando deben convivir en almacenamiento, URLs, buscadores o procesos batch.
   - Riesgo principal: que el nombre visible y el técnico se desacoplen o que el nombre técnico falle en alguna plataforma concreta. La prevención es probar compatibilidad real con los sistemas donde se guardará, sincronizar ambos desde el mismo origen y registrar la relación entre ID, nombre visible y nombre técnico.

5. Automatizar solo los derivados seguros y poner el último disparo bajo estado inequívoco, validación e idempotencia.
   - Ejecuta automáticamente solo los pasos que puedan validar dependencias, repetir sin efectos inconsistentes y dejar trazabilidad clara de entradas y salidas.
   - Haz que cada derivación verifique prerequisitos, compare el hash del contenido fuente y no reescriba salidas si no hubo cambios efectivos.
   - Reserva Play para dos casos: estado aprobado sin ambigüedad y señales técnicas limpias, o una política explícita que acepte ese nivel de automatismo por costo-beneficio.
   - Añade modo de prueba, registro de ejecución, prueba de reversibilidad y alarmas cuando falle una dependencia o cambie una salida sin cambio de fuente.
   - Aplica cuando el flujo ya tiene una fuente canónica razonablemente estable y el costo de publicar algo incorrecto supera el ahorro de un clic manual.
   - Riesgo principal: errores silenciosos que parecen éxitos, especialmente en la etapa final. La mitigación es fallar por defecto ante incertidumbre, exigir estados explícitos y conservar intervención manual hasta que las ejecuciones reales demuestren estabilidad suficiente.

## Evidencias y supuestos

El valor real de automatizar el último tramo depende de validación externa con datos de operación: frecuencia de errores silenciosos, tiempo realmente ahorrado, facilidad de reversión y costo de una publicación incorrecta. Sin esa evidencia, la automatización final debe tratarse como hipótesis útil, no como decisión cerrada.

La conveniencia de preservar saltos de línea de forma literal depende de validación externa con ejemplos reales de uso. Hay que comprobar en piezas concretas si esos saltos mejoran comprensión, completitud o tasa de acierto, especialmente en cuestionarios y secuencias de acción.

La idea de usar una sola fuente para texto y audio depende de validación externa sobre naturalidad de la voz, reglas de oralización, pronunciaciones especiales y restricciones del motor o política de uso. Es posible que el audio necesite una capa intermedia de adaptación aunque siga derivando del mismo origen.

La estrategia dual de nombres de archivo depende de validación externa en los sistemas concretos donde vivirán los archivos: sistema operativo, almacenamiento en nube, URLs, indexadores, reproductores y herramientas de automatización. Lo que es estable en un entorno puede romperse en otro.

La idempotencia y la validación de dependencias dependen de validación externa en ejecución real, especialmente si hay concurrencia, cachés, procesos interrumpidos o cambios en metadatos que también afectan la salida. Conviene asumir que la primera versión del pipeline revelará dependencias ocultas.

## Sintesis breve

La recomendación ejecutiva es implantar primero una fuente canónica mínima con estructura semántica explícita, generar desde ahí el texto accionable, el Markdown y un guion de audio, y no automatizar el último disparo hasta que exista un estado inequívoco y trazabilidad suficiente. Preserva el formato solo cuando cambie el significado o el uso, resuelve nombres visibles y técnicos desde el mismo origen y exige idempotencia más validación de dependencias en todo derivado automático. Si hay duda entre automatismo final y riesgo silencioso, conviene mantener Play condicionado o manual hasta que la operación real demuestre que el ahorro supera el costo potencial del error.
