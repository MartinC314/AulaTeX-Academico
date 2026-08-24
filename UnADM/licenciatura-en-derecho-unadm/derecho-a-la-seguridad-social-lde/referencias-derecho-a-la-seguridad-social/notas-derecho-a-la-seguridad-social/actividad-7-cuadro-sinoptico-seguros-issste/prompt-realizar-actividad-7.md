# Prompt para `realizar-actividad`: Actividad 7

Realiza la **Actividad 7 de Derecho a la Seguridad Social (UnADM)** y genera el archivo `reporte-derecho-a-la-seguridad-social-Actividad-7.tex`, listo para compilar a PDF. Trabaja desde la raíz de la asignatura y conserva la identidad institucional y el estilo editorial de las actividades previas, especialmente la Actividad 5, sin copiar sus contenidos.

## Fuentes locales obligatorias

Antes de redactar, lee y contrasta:

1. `planeaciones-derecho-a-la-seguridad-social/Planificacion de actividades S7 - Derecho a la seguridad social.pdf`
2. `planeaciones-derecho-a-la-seguridad-social/Prsentacion de clase S7 - Derecho a la seguridad social.pdf`
3. `planeaciones-derecho-a-la-seguridad-social/Contenidos de clase S7 - Derecho a la seguridad social.pdf`
4. `presentacion-derecho-a-la-seguridad-social.tex`
5. `derecho-a-la-seguridad-social.bib`
6. Los PDF pertinentes de `referencias-derecho-a-la-seguridad-social/libros-derecho-a-la-seguridad-social/`, en particular:
   - `Derecho de la seguridad social - Alberto Briceno Ruiz.pdf`
   - `Nociones juridicas de los seguros sociales en Mexico - Ivan Ramirez Chavero.pdf`
   - `El ISSSTE la salud y la seguridad social para los trabajadores al servicio del Estado - Alejandro Carrillo Castro.pdf`
   - `Constitucion Politica de los Es - Camara de Diputados del H. Cong.pdf`
   - `Ley del Instituto de Seguridad - Camara de Diputados del H. Cong.pdf`
   - `El derecho a la seguridad socia - Diana Beatriz Gonzalez Carvallo.pdf`
7. Como referencia de estructura gráfica y metadatos, `reporte-derecho-a-la-seguridad-social-Actividad-5.tex`.

Prioriza como autoridad la **Constitución vigente** y la **Ley del ISSSTE vigente**. Usa la doctrina para explicar y contextualizar, nunca para contradecir la norma. Comprueba cada artículo en la ley local antes de citarlo. No inventes artículos, fechas, páginas, datos bibliográficos ni contenidos.

## Datos de la actividad

- Semana: 7, del 17 al 23 de agosto de 2026.
- Entrega: 23 de agosto de 2026, 23:55, hora de Ciudad de México.
- Docente: Cristian Ortega Barrera.
- Producto: **cuadro sinóptico sobre los seguros del ISSSTE**.
- Propósito: identificar las contingencias que cubren los diversos seguros del régimen obligatorio del ISSSTE.
- Ponderación: 20/100.
- Tiempo estimado: 4 horas.

## Contenido mínimo exigido

El producto debe incluir:

1. Un concepto claro de **seguro o rama en el contexto del seguro social del ISSSTE**, con su naturaleza y contenido.
2. El listado completo y legalmente correcto de los seguros del régimen obligatorio conforme al artículo 3 de la Ley del ISSSTE:
   - Seguro de salud.
   - Seguro de riesgos del trabajo.
   - Seguro de retiro, cesantía en edad avanzada y vejez.
   - Seguro de invalidez y vida.
3. Para **cada seguro**, mostrar jerárquicamente:
   - contingencia o riesgo protegido;
   - cobertura o prestaciones generales;
   - personas protegidas o beneficiarias cuando sea pertinente;
   - sustento legal básico, con artículos verificados de la Ley del ISSSTE.
4. Distinguir expresamente los seguros del artículo 3 de las prestaciones y servicios del artículo 4 (préstamos hipotecarios y personales, servicios sociales y culturales), para no presentarlos erróneamente como seguros.
5. Contexto normativo breve: artículo 123, apartado B, fracción XI, de la Constitución; naturaleza del ISSSTE; régimen obligatorio y voluntario. Este contexto debe apoyar el cuadro, no desplazarlo.
6. Introducción breve, guía de lectura del cuadro, conclusión propia y referencias en APA 7.

No conviertas la actividad en un ensayo extenso ni centres el trabajo en PENSIONISSSTE, pues este corresponde a la Actividad 8. El elemento central y de mayor superficie visual debe ser el cuadro sinóptico.

## Diseño y formato

- Produce un documento LaTeX institucional, legible y profesional.
- Diseña el cuadro sinóptico con TikZ u otra solución LaTeX vectorial; debe verse completo, sin nodos superpuestos, texto cortado, flechas sobre el texto ni desbordamientos.
- Usa orientación horizontal o una página de formato amplio si es necesario para mantener legibilidad.
- Mantén una jerarquía visual inequívoca: régimen obligatorio → cuatro seguros → contingencias/cobertura → fundamento legal.
- Incluye citas autor-año en el texto y una bibliografía final compatible con el `.bib` local.
- Si faltan en el `.bib` las entradas de Ramírez Chavero o Carrillo Castro, agrégalas con metadatos verificables y trazabilidad local; no dupliques claves existentes.
- Declara de manera transparente el apoyo de IA conforme a los lineamientos de la planeación, sin atribuir a la IA autoría de fuentes ni verificación jurídica.
- Evita metadiscurso, afirmaciones no sustentadas y referencias que no se hayan consultado.

## Criterios de aceptación (rúbrica: 20 puntos)

La entrega solo se considera terminada si satisface los cinco rubros de nivel excelente, 4 puntos cada uno:

1. **Concepto de rama:** contempla naturaleza y contenidos.
2. **Ramas:** incluye los cuatro seguros del régimen obligatorio sin confundirlos con prestaciones y servicios.
3. **Contenido de las ramas:** explica de forma general la cobertura de cada seguro.
4. **Sustento:** indica el fundamento legal básico de cada seguro.
5. **Fuentes y escritura:** citas y referencias APA 7, buena redacción y ortografía.

## Validación final obligatoria

1. Compila el `.tex` a PDF con el flujo del workspace.
2. Revisa el log: cero errores, referencias resueltas y sin `Overfull/Underfull` graves.
3. Inspecciona visualmente todas las páginas, especialmente el cuadro sinóptico.
4. Verifica contra los artículos vigentes que los nombres, coberturas y fundamentos sean correctos.
5. Confirma que el PDF sea el producto solicitado, que la bibliografía realmente aparezca y que incluya la declaración de apoyo de IA.
6. Si alguna fuente local no puede leerse o algún dato no puede verificarse, repórtalo como limitación y no lo inventes.
