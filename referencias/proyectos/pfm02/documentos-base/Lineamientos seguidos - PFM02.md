# Lineamientos seguidos para reportes y presentaciones PFM02

## Proposito del archivo

Este documento registra los criterios usados para actualizar las actividades de PFM02 en formato de reporte y presentacion. La finalidad es mantener continuidad entre sesiones, evitar que los productos sean solo respuestas mecanicas y asegurar que cada actividad muestre procedimiento, justificacion, evaluacion y retroalimentacion.

Aunque el nombre del archivo conserva la referencia inicial a las sesiones 01 y 02, los lineamientos ya integran los ajustes realizados hasta la sesion 03. Por tanto, debe leerse como una guia acumulativa para conversion de fracciones y decimales, suma y resta con fracciones, y multiplicacion y division con fracciones.

## Fuentes institucionales consideradas

- `Sesion 01_ conversion de fracci - PFM02.pdf` y su version `.md`: contenido, ejercicios, situaciones y criterios de conversion entre fracciones y decimales.
- `Sesion 02_ suma y resta con fra - PFM02.pdf`: contenido, PDA, aprendizaje de la secuencia, ejercicios y situaciones en contexto.
- `Sesion 02_ suma y resta con fra - PFM02.md`: insumo editable de la actividad.
- `Sesion 03_ multiplicacion y div - PFM02.pdf` y su version `.md`: contenido, ejercicios y situaciones para multiplicacion y division con fracciones.
- `solucion_sesion_03_multiplicacion_division_fracciones.tex`: fuente de procedimientos resueltos y esquemas TikZ integrados a la sesion 03.
- `Estructura de una secuencia did - PFM02.pdf`: organizacion en cinco fases: antecedente, introduccion/explicacion, practica, evaluacion y retroalimentacion.
- `Los criterios de evaluacion - PFM02.pdf`: ponderacion general del curso: asistencia, actividades diarias, exposicion diaria, escrito reflexivo y exposicion final.
- Presentacion de la sesion 01: referencia de estilo visual, orden pedagogico y uso de procedimientos explicitos.
- Retroalimentacion de la sesion 02: se uso como evidencia para regresar a la sesion 01 y fortalecer evaluacion, retroalimentacion y estructura de secuencia.
- Ajustes posteriores de tabla en los tres reportes: se consolidaron criterios de legibilidad, ancho controlado, encabezados claros y compilacion estable.

## Lineamientos generales

- Conservar la plantilla institucional, sus datos base y sus comentarios de trabajo cuando el archivo los incluya.
- Ocultar del producto final las instrucciones internas de edicion, dejando visible solo el documento terminado.
- Alinear tema, contenido, PDA, aprendizaje esperado, ejercicios, situaciones y autoevaluacion.
- Evitar enlaces a imagenes externas como soporte central; reconstruir esquemas con LaTeX/TikZ cuando sea viable.
- Explicar cada procedimiento con cuatro piezas: estrategia, desarrollo, resultado y verificacion.
- No presentar tablas de respuestas como unico producto: cada bloque debe incluir por lo menos una ruta de solucion.
- Usar problemas contextualizados para evaluar comprension, no solo repeticion del algoritmo.

## Lineamientos para el reporte

- Abrir con una introduccion que explique el problema didactico: operar fracciones exige trabajar partes comparables.
- Incluir los datos institucionales de la secuencia: contenido, PDA y aprendizaje.
- Incorporar una tabla que traduzca los criterios de evaluacion y la estructura didactica a decisiones concretas del producto.
- Organizar el desarrollo con las cinco fases de la secuencia didactica.
- Resolver ejercicios de practica en tablas claras, con simplificacion y conversion cuando sea necesario.
- Resolver situaciones en contexto indicando operacion, procedimiento y respuesta interpretada.
- Incluir esquemas TikZ para representar situaciones visuales importantes.
- Cerrar con conclusion que explique que se comprendio y por que el procedimiento es transferible.
- Cuando una sesion previa se mejore con aprendizajes de una sesion posterior, registrar la mejora como retroalimentacion del proceso, no como correccion aislada.

## Lineamientos para tablas en reportes

- Todas las tablas deben mantenerse dentro del ancho de texto y evitar columnas que dependan de texto sin ajuste.
- Para tablas largas de contenido, usar `longtable` con columnas `p{...}` y ancho proporcional a `\linewidth`.
- Para tablas de autoevaluacion, usar `table[H]` con `tabularx`, una columna flexible `X` para indicadores y columnas `p{...}` centradas para niveles de logro.
- Usar `makecell` cuando los encabezados necesiten dos lineas, por ejemplo `Logrado (3)`, `En proceso (2)` y `No logrado (1)`.
- Aplicar un ajuste comun de tablas en el preambulo: `\LTcapwidth` igual a `\textwidth`, menor `\tabcolsep`, `\arraystretch` mayor a 1 y filas alternadas con `\rowcolors`.
- Conservar `booktabs` para `\toprule`, `\midrule` y `\bottomrule`; no sobrecargar las tablas con lineas verticales.
- Evitar tablas que solo sean bancos de respuestas. Si una tabla resume ejercicios, debe estar acompanada por una ruta visual, ejemplo desarrollado o criterio de verificacion.
- Las tablas institucionales deben traducir la fuente a decisiones del producto: que se recupera, como se aplica y que evidencia genera.
- Las tablas de situaciones deben incluir planteamiento, operacion o procedimiento, y respuesta interpretada con unidad o contexto.
- Antes de entregar, compilar y revisar que no existan errores de LaTeX, `Overfull \hbox`, `Overfull \vbox` ni avisos de referencias pendientes.

## Lineamientos para la presentacion

- Mantener la identidad visual de la presentacion anterior: portada institucional, paleta IIIEPE, bloques y barra inferior.
- Evitar diapositivas repetidas de division de seccion; usar secciones para navegacion, no como relleno.
- Presentar primero la ficha de la sesion y los criterios institucionales incorporados.
- Usar una ruta pedagogica breve: recuperar, igualar, operar, simplificar y verificar.
- Mostrar procedimientos en diapositivas separadas para no saturar texto.
- Resolver ejercicios representativos antes del banco de respuestas.
- Usar tablas solo cuando permitan lectura rapida; si un problema requiere razonamiento, usar procedimiento guiado.
- Sustituir imagenes del PDF por esquemas TikZ editables.
- Cerrar con autoevaluacion, retroalimentacion y conclusiones didacticas.
- Mantener una diapositiva de retroalimentacion con errores frecuentes y preguntas de revision cuando el tema tenga algoritmos sensibles a pasos ocultos.

## Criterios matematicos aplicados en la sesion 01

- Una fraccion decimal se convierte por valor posicional: el numero de ceros del denominador indica la posicion decimal.
- Una fraccion no decimal se convierte dividiendo numerador entre denominador.
- Si el residuo de la division llega a cero, el decimal es finito; si los residuos se repiten, el decimal es periodico.
- Un decimal finito se escribe como fraccion con denominador potencia de 10 y despues se simplifica.
- Un decimal periodico se convierte mediante ecuaciones: se multiplica por potencias de 10 para alinear el periodo, se resta y se despeja.
- La respuesta debe comprobarse convirtiendo de regreso o revisando que conserve la misma cantidad.
- En situaciones en contexto, el resultado debe interpretarse como medida, porcentaje, edad, distancia o cantidad.

## Criterios matematicos aplicados en la sesion 02

- En fracciones con el mismo denominador, se suman o restan numeradores y se conserva el denominador.
- En fracciones con distinto denominador, primero se construye un denominador comun.
- El minimo comun multiplo se prefiere como explicacion pedagogica porque reduce calculos.
- El producto cruzado se presenta como atajo derivado del denominador comun, no como regla sin sentido.
- Las fracciones mixtas se convierten a impropias antes de operar.
- Todo resultado debe simplificarse cuando sea posible.
- En situaciones en contexto, la respuesta debe incluir unidad o interpretacion.

## Criterios matematicos aplicados en la sesion 03

- La multiplicacion de fracciones se interpreta como tomar una parte de otra parte; no siempre aumenta la cantidad.
- Para multiplicar fracciones se multiplican numeradores entre si y denominadores entre si; despues se simplifica.
- Los enteros se expresan como fracciones con denominador 1 cuando participan en productos o cocientes.
- Las fracciones mixtas se convierten a impropias antes de operar para evitar separar indebidamente entero y fraccion.
- La division entre fracciones se interpreta como identificar cuantos grupos de cierto tamano caben en una cantidad.
- Dividir entre una fraccion equivale a multiplicar por su reciproco; solo se invierte el divisor.
- En problemas contextualizados, se debe decidir si la situacion pide parte de una cantidad, reparto por capacidad, medida faltante, area o proceso encadenado.
- La respuesta final debe incluir simplificacion, signo correcto y unidad: litros, metros, hectareas, botellas, vasos, bolsas, dinero o area.

## Criterios de revision antes de entregar

- El tema corresponde a la sesion activa, no a una sesion anterior.
- No quedan referencias visibles a contenido de conversion decimal cuando la actividad trata suma y resta.
- No quedan referencias visibles a suma y resta cuando la actividad trata conversion de fracciones y decimales.
- No quedan referencias visibles a suma y resta cuando la actividad trata multiplicacion y division con fracciones.
- Los ejercicios resueltos muestran procedimiento, no solo resultado.
- Las situaciones en contexto tienen planteamiento, operacion y respuesta interpretada.
- En el reporte, evitar `\div` si el template carga `wasysym`; usar un macro propio para que la division se vea como simbolo de division convencional y no como simbolo triangular.
- Las tablas compilan sin desbordes, conservan encabezados legibles y mantienen el contenido dentro del margen.
- Cuando el nombre del archivo contiene espacios o acentos, compilar con un `-jobname` ASCII y copiar el PDF verificado al nombre final.
- Ejecutar al menos dos pasadas de `pdflatex` cuando se hayan cambiado tablas, indices, etiquetas o referencias.
- La evaluacion mide seleccion de estrategia, procedimiento, simplificacion, comprobacion e interpretacion.
- La conclusion recupera estructura didactica, criterios de evaluacion y aprendizaje matematico.
- La retroalimentacion incluye errores frecuentes y preguntas de revision para guiar una mejora posterior.
