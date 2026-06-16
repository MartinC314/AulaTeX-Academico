# ITESCA

Estructura institucional para ITESCA.

La identidad visual institucional se centraliza en:

- `ITESCA/_shared/itesca-report-template.tex`
- `ITESCA/_shared/itesca-presentation-template.tex`
- `ITESCA/_shared/itesca-profile-isc.tex`
- `ITESCA/_shared/itesca-profile-isc-primer-ingreso.tex`
- `ITESCA/_shared/itesca-profile-mga.tex`
- `ITESCA/_shared/itesca-profile-mga-primer-ingreso.tex`
- `ITESCA/assets/web/logo-itesca-contorno.png`
- `ITESCA/assets/itesca-monograma.png`
- `ITESCA/bibliografia-itesca.bib`

Esta carpeta introduce un nivel nuevo en el repositorio:

- institucion -> carrera -> materia

Cada carrera replica el patron que hoy usan UCNL, UnADM o IIIEPE en su nivel
principal:

- bibliografia compartida de carrera
- punto de entrada canonico para reporte
- punto de entrada canonico para presentacion
- carpeta de referencias de apoyo
- carpetas por materia

Carreras iniciales:

- ingenieria-en-sistemas-computacionales
- maestria-en-gestion-administrativa

Materia semilla en ambas carreras:

- primer-ingreso

Todos los `.tex` ejecutables dentro de `ITESCA/` heredan desde los templates
compartidos y, ahora, desde perfiles editoriales por programa. Eso convierte a
`_shared/` en el nucleo real de uniformidad ITESCA: identidad visual,
metadatos institucionales y criterio editorial viven en un solo lugar.

La carpeta `_shared/` no esta de mas. Su funcion es evitar que la rama ITESCA
se fragmente en wrappers con metadatos repetidos o reglas editoriales copiadas
por carrera o materia. Si cambia el enfoque institucional, el ajuste debe vivir
ahi y no dispersarse en cada `.tex`.

## Control editorial

La rama ITESCA queda alineada con el nivel de profundidad editorial de UnADM e
IIIEPE mediante una capa comun de revision:

- ficha editorial de actividad
- nivel cognitivo minimo
- matriz de cumplimiento
- producto visible y evidencia interpretada
- vinculacion con carrera, materia y contexto profesional
- cierre con postura, aprendizaje y consecuencia transferible

El objetivo no es que los documentos solo tengan identidad visual, sino que
mantengan identidad institucional en la argumentacion: claridad tecnica,
pertinencia academica, evidencia verificable y aplicacion profesional.

## Uniformidad por perfiles

Los wrappers canonicos y de materias en `ITESCA/` deben limitarse a declarar
el documento concreto que producen: titulo, actividad, bloque, producto y
archivo de bibliografia especifico cuando aplique.

La informacion repetible se concentra en perfiles compartidos:

- programa y nivel academico
- nombre corto del estudiante y codigos institucionales
- enfoque profesional y contexto de transferencia
- ubicacion institucional y rutas bibliograficas comunes

Con esto, el enfoque editorial se refuerza porque cada documento parte de una
misma base institucional antes de describir su actividad particular.

