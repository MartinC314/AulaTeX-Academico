# 10:11 - Arquitectura de publicación con una sola fuente de verdad · Investigar

Nota origen: [10:11 - Arquitectura de publicación con una sola fuente de verdad](20260705_101107_arquitectura_de_publicación_con_una_sola_fuente_de_verdad.md)

## Metadata

{
  "action": "research",
  "label": "Investigar",
  "schema_version": "v1",
  "created_at": "2026-07-05T10:18:17.995827",
  "source_note": "20260705_101107_arquitectura_de_publicación_con_una_sola_fuente_de_verdad.md"
}

## Nucleo

La propuesta gira en torno a una arquitectura de publicación con una sola fuente de verdad: el contenido se define una vez, se mantiene en un modelo común y desde ese punto se derivan varias salidas como texto accionable, Markdown y audio. El objetivo principal no es solo eficiencia técnica, sino coherencia entre representaciones y una entrega que siga siendo clara para personas.

El criterio rector combina tres decisiones de diseño:

- La salida principal debe priorizar lectura humana y acción inmediata, por eso conviene publicar primero la pieza más útil para decidir o ejecutar.
- El formato debe conservar literalmente solo aquello que transporta estructura semántica, como saltos de línea en un cuestionario, y no todo rasgo visual sin discriminar.
- La automatización debe ser desigual según el riesgo: los derivados pueden correr solos si existen validaciones de dependencia e idempotencia, mientras que la etapa final de reproducción o publicación conviene activarla solo con estado inequívoco o con una política que justifique ese nivel de automatismo.

La tensión central no es técnica aislada, sino de control: cuánto valor real aporta automatizar el último tramo frente al costo potencial de errores silenciosos, y hasta qué punto preservar el formato literal mejora comprensión o termina haciendo frágil el flujo.

## Desarrollo

Hallazgos relativamente estables

- Una sola fuente de verdad reduce el riesgo estructural de divergencia entre formatos cuando varias representaciones dependen del mismo contenido base y no de ediciones paralelas.
- Varias salidas derivadas tienen sentido cuando el mismo contenido necesita cumplir funciones distintas, como lectura rápida, archivo interoperable y consumo auditivo.
- Priorizar lectura humana cambia el orden óptimo de publicación: la representación más clara para decidir o actuar gana precedencia sobre la más cómoda para el sistema.
- Los saltos de línea no siempre son ornamentales; en cuestionarios, listas guiadas o secuencias de instrucciones pueden contener estructura semántica y afectar comprensión.
- Una estrategia dual de nombres de archivo resuelve dos exigencias legítimas y distintas: legibilidad para personas y estabilidad técnica para sistemas.
- La idempotencia es una propiedad razonable en pipelines automáticos porque evita resultados inconsistentes cuando un proceso se ejecuta más de una vez sobre el mismo estado.
- La validación de dependencias es clave cuando hay derivados encadenados, porque permite saber si un artefacto está actualizado, vencido o generado desde una base incorrecta.
- La automatización del paso final es más delicada que la de derivados internos porque suele tener más visibilidad, más irreversibilidad o más impacto si el estado fue interpretado mal.

Inferencias plausibles

- Para sostener una sola fuente de verdad sin perder flexibilidad, probablemente hace falta separar contenido semántico de presentación, aunque el texto no defina todavía el esquema exacto.
- El modelo fuente más útil no sería una simple copia del texto final, sino una estructura capaz de representar acciones, bloques, saltos semánticos, metadatos y reglas de derivación.
- La pieza “más accionable” parece funcionar como producto principal y las demás salidas como adaptaciones, lo que sugiere una jerarquía deliberada entre artefactos y no una equivalencia total.
- La estrategia dual de nombres sugiere necesidad de trazabilidad entre nombre visible y nombre técnico; sin un mapeo estable pueden aparecer confusión, colisiones o pérdida de contexto.
- La conservación literal del formato probablemente debe gobernarse por reglas explícitas de semántica, porque si se preserva todo sin criterio el pipeline se vuelve frágil ante pequeñas variaciones editoriales.
- La mención de Play como disparo condicionado sugiere que existe una frontera entre procesos seguros de backend y acciones con mayor costo de error, donde conviene exigir confirmación o estados más estrictos.
- El riesgo de errores silenciosos apunta a que no basta con automatizar; hacen falta observabilidad, registros, alertas y criterios de fallo visibles para detectar derivaciones incorrectas.
- La decisión pendiente sobre el automatismo final probablemente no se resuelve con una regla universal, sino con una combinación de contexto de uso, tolerancia al error y capacidad de reversión.

## Accionables

- Definir cuál será la unidad real de la fuente única: documento completo, bloque estructurado, objeto con metadatos o esquema intermedio independiente del formato final.
- Delimitar qué elementos del formato tienen valor semántico y deben preservarse literalmente, con ejemplos concretos de cuestionarios, listas, guiones y párrafos normales.
- Redactar una matriz de salidas que especifique para cada derivado qué transforma, qué conserva y qué pierde respecto del modelo fuente.
- Diseñar una tabla de estados que indique cuándo un derivado puede ejecutarse automáticamente y cuándo el paso final debe quedar bloqueado hasta revisión humana.
- Especificar la condición de idempotencia por artefacto, incluyendo qué se considera “mismo input”, cómo se detecta cambio real y qué ocurre si se repite la ejecución.
- Probar la estrategia dual de nombres con casos conflictivos: títulos largos, caracteres especiales, acentos, colisiones semánticas y versiones casi idénticas.
- Verificar que el nombre visible y el nombre técnico queden unidos por un identificador estable para evitar desalineación entre interfaz humana y almacenamiento.
- Ejecutar pruebas de regresión donde el mismo contenido genere texto, Markdown y audio, y revisar si alguna salida introduce divergencias de significado.
- Simular errores de estado para medir el costo de automatizar Play sin confirmación, especialmente en escenarios donde el sistema interpreta como listo algo que aún no lo está.
- Formular criterios de aceptación centrados en personas: qué debe entender un lector en la primera salida, qué no puede perderse al derivar y qué errores son tolerables o no.
- Consultar explícitamente si el objetivo prioritario es rapidez operativa, seguridad contra errores o fidelidad de representación, porque esa jerarquía cambia la arquitectura.
- Verificar si el audio requiere reglas propias de puntuación, pausas o pronunciación que obliguen a enriquecer el modelo fuente más allá del texto y el Markdown.

## Evidencias y supuestos

- Falta evidencia comparativa que demuestre cuánto reduce la divergencia esta arquitectura frente al flujo actual o frente a edición manual de múltiples formatos.
- Falta evidencia de uso que confirme que la pieza más accionable debe ser siempre la primera salida para todas las audiencias involucradas.
- Falta definición verificable de “estado inequívoco” para permitir el disparo automático de Play sin elevar el riesgo operativo.
- Falta criterio medible para decidir cuándo un salto de línea expresa estructura semántica y cuándo es solo una preferencia de estilo.
- Falta especificación técnica del modelo fuente, por lo que todavía no puede validarse si soporta sin pérdida los requisitos de texto, Markdown y audio.
- Falta una política explícita de tolerancia al error, reversión y observabilidad; sin ella no puede evaluarse bien el costo del automatismo final.
- Se asume que texto, Markdown y audio pueden derivarse desde un mismo modelo sin introducir compromisos excesivos entre claridad humana y normalización técnica.
- Se asume que la estrategia dual de nombres mejora simultáneamente experiencia humana y robustez del sistema, pero ese beneficio depende de una relación estable entre ambos nombres.
- Se asume que los derivados pueden ser idempotentes en el entorno real, aunque todavía no se definieron dependencias, cachés, side effects ni artefactos externos.
- Se asume que preservar formato literal ayuda a la comprensión solo cuando coincide con semántica; esa frontera es razonable, pero necesita pruebas con ejemplos reales.

## Sintesis breve

Conviene tratar la publicación como un pipeline con un modelo fuente único, salidas derivadas y reglas explícitas sobre qué se conserva, qué se transforma y qué se automatiza. La decisión crítica para seguir investigando es fijar la frontera entre automatización segura y revisión humana, usando evidencia sobre errores silenciosos, estados válidos y valor real de preservar el formato literal.
