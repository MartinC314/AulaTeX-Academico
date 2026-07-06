# 04:28 - Ajustes al envío de notas y cuestionarios · Investigar

Nota origen: [04:28 - Ajustes al envío de notas y cuestionarios](20260705_042859_ajustes_al_envío_de_notas_y_cuestionarios.md)

## Metadata

{
  "action": "research",
  "label": "Investigar",
  "schema_version": "v1",
  "created_at": "2026-07-05T04:35:38.302091",
  "source_note": "20260705_042859_ajustes_al_envío_de_notas_y_cuestionarios.md"
}

## Nucleo

El tema central es la corrección de un flujo de envío de notas y cuestionarios para que respete mejor el orden de entrega, la completitud del paquete enviado y la legibilidad del contenido.

La intención operativa que aparece con más claridad es esta: primero enviar el texto visible con botones de acción, después la nota limpia en Markdown, luego el audio, más tarde ejecutar los procesos derivados y finalmente ejecutar Play. Hoy ese flujo está incompleto o desordenado en al menos tres puntos: el sistema ya está enviando la nota limpia como Markdown, los derivados ya se ejecutan, pero Play todavía no se lanza; además, los nombres de archivo se están cortando.

La decisión más estable del contenido es preservar los saltos de línea en cuestionarios. El criterio no es técnico sino de comprensión: eliminar esos saltos reduce claridad y puede deteriorar la interpretación de preguntas o respuestas.

La tesis funcional es que el problema no se limita al formato, sino a la secuencia completa de entrega: presentación al usuario, integridad de archivos, conservación del significado textual y encadenamiento correcto de automatizaciones.

## Desarrollo

### Hallazgos

- Hecho relativamente estable: la nota limpia ya se está enviando como Markdown.
- Hecho relativamente estable: el envío deseado no debería limitarse al Markdown; antes debería salir un texto acompañado por botones de acción.
- Hecho relativamente estable: después del texto con botones, debería enviarse el Markdown que hoy ya se envía.
- Hecho relativamente estable: el audio forma parte del orden esperado de entrega y debería enviarse después del Markdown.
- Hecho relativamente estable: los procesos derivados ya se ejecutan después del envío.
- Hecho relativamente estable: Play debería ejecutarse después de los derivados, pero todavía no ocurre.
- Hecho relativamente estable: los nombres de archivo enviados están siendo recortados.
- Hecho relativamente estable: en cuestionarios no debe filtrarse ni eliminarse el salto de línea.
- Hecho relativamente estable: la razón para conservar saltos de línea es mantener claridad en el contenido.

### Inferencias plausibles

- Inferencia plausible: el flujo actual privilegia el formato estructurado de la nota, pero no está priorizando la experiencia de lectura inmediata ni la interacción rápida mediante botones.
- Inferencia plausible: el orden de envío importa porque cada elemento cumple una función distinta: el texto con botones orienta la acción, el Markdown conserva estructura, el audio aporta contexto o fidelidad, los derivados generan productos secundarios y Play parece cerrar o activar una fase posterior del proceso.
- Inferencia plausible: el recorte de nombres de archivo puede afectar trazabilidad, asociación entre activos y facilidad para identificar una nota frente a otras.
- Inferencia plausible: la preservación de saltos de línea en cuestionarios no es un detalle cosmético; probablemente evita ambigüedad semántica, especialmente cuando hay opciones, bloques de instrucciones o preguntas compuestas.
- Inferencia plausible: la ausencia de Play sugiere un problema de secuenciación, disparo de eventos o condición no satisfecha al final del pipeline.
- Inferencia plausible: la coexistencia de texto con botones, Markdown y audio indica que el sistema trabaja con múltiples representaciones del mismo contenido y necesita reglas claras sobre prioridad, sincronización y confirmación de envío.
- Inferencia plausible: el problema de nombres truncados puede originarse en normalización automática, límites del canal de envío o una función de generación de nombres que no conserva el identificador completo.

## Accionables

- Verificar con una prueba controlada el orden real de salida: texto con botones, Markdown, audio, derivados y Play.
- Definir un criterio de éxito observable para cada etapa, de modo que el sistema no marque el flujo como completo si Play no se ejecutó.
- Revisar el disparador de Play y confirmar si depende del éxito del envío, de la generación de derivados o de ambos.
- Inspeccionar la función que construye nombres de archivo y registrar exactamente dónde ocurre el recorte: antes del envío, durante la serialización o por una restricción del canal receptor.
- Comparar el nombre original del archivo con el nombre final recibido para distinguir entre truncamiento local y truncamiento externo.
- Confirmar si el texto con botones y el Markdown deben enviarse como dos mensajes separados o como un mismo mensaje con componentes distintos.
- Aclarar si el audio es obligatorio en todos los envíos o solo cuando existe una fuente de audio asociada.
- Probar cuestionarios con saltos de línea conservados frente a versiones filtradas para medir claridad, legibilidad y posibles errores de interpretación.
- Verificar si los derivados consumen el Markdown, el texto plano, el audio o una combinación de ellos, porque esa dependencia condiciona el orden correcto del pipeline.
- Establecer casos de prueba con nombres largos, caracteres especiales y múltiples líneas en cuestionarios para detectar fallos reproducibles.
- Consultar si existen límites impuestos por la plataforma de destino sobre longitud de nombres, tamaño de mensajes, adjuntos o componentes interactivos.
- Registrar eventos con marcas de tiempo por etapa para detectar si el problema de Play es ausencia de ejecución, ejecución fallida o ejecución fuera de orden.

## Evidencias y supuestos

### Evidencias directas disponibles

- El sistema empezó a enviar la nota limpia como Markdown.
- Se desea enviar primero texto con botones de acción.
- Después del texto con botones se desea enviar el Markdown actual.
- Después del Markdown se desea enviar el audio.
- Los derivados ya se ejecutan después del envío.
- Play todavía no se ejecuta y debería correr después de los derivados.
- Los nombres de archivo están saliendo cortados.
- En cuestionarios no deben filtrarse los saltos de línea.
- La conservación de saltos de línea se justifica por claridad.

### Supuestos razonables, pero no confirmados por fuente explícita

- Los botones de acción son elementos interactivos visibles para el usuario final.
- El audio pertenece al mismo paquete lógico que la nota y no a un flujo separado.
- El recorte de nombres es un defecto no deseado y no una política deliberada de abreviación.
- Play representa una acción automatizada posterior y no una función manual.
- La claridad de los cuestionarios impacta directamente en calidad de respuesta, comprensión o conversión operativa.

### Vacíos que requieren verificación externa o técnica

- La plataforma exacta de envío y sus restricciones sobre adjuntos, componentes interactivos y longitud de nombres.
- La definición funcional precisa de Play y la razón técnica por la que no se ejecuta.
- La condición exacta que dispara los derivados y si existe dependencia entre derivados y Play.
- El formato exacto en que se envía el texto con botones y cómo convive con el Markdown.
- El alcance del problema de truncamiento: todos los archivos, ciertos tipos de archivo o casos con nombres largos.
- El comportamiento de renderizado de saltos de línea en cada cliente o canal donde se consumen los cuestionarios.

## Sintesis breve

La línea de trabajo más sólida es tratar el problema como una corrección de pipeline: entregar primero la capa de interacción, después las representaciones de contenido, conservar la estructura textual que aporta claridad y cerrar con automatizaciones en orden verificable. La prioridad práctica es asegurar secuencia, integridad de nombres y preservación de formato antes de expandir funciones nuevas.
