# Fuente editorial Template-Latex

## Origen

El contenido de `Revision/template-latex.github.io/` se integro como fuente
editorial en:

```text
retroalimentacion-editorial/fuentes/template-latex-web/
```

Corresponde a una copia local del sitio `latex.ppizarror.com`, asociado a la
familia Template-Latex de Pablo Pizarro R. Se elimino su `.git` anidado para que
AulaTeX no cargue un repositorio dentro de otro.

## Por que se integra aqui

Estamos trabajando con plantillas de Pizarro, pero AulaTeX no debe tratarlas
solo como archivos sueltos. El sitio contiene contexto editorial: familias,
descripciones, paginas HTML, configuraciones de releases, recursos visuales,
documentos de apoyo y enlaces al ecosistema Template-Latex.

Por eso pertenece a `retroalimentacion-editorial`: ayuda a decidir como adaptar,
clasificar y evolucionar nuestras plantillas.

## Familias reconocidas

- `Template-Articulo`
- `Template-Auxiliares`
- `Template-Controles`
- `Template-Informe`
- `Template-Poster`
- `Template-Presentacion`
- `Template-Reporte`
- `Template-Tesis`
- `Professional-CV`

Todas estas familias tienen espacio legitimo dentro de AulaTeX. El uso actual
no limita su posible uso futuro.

## Material util dentro de la fuente

- `*.html`: paginas publicas de cada familia de plantilla.
- `app/releases/*/config.js`: configuracion editorial y enlaces por plantilla.
- `doc/`: guias PDF sobre Beamer, BibTeX, Mendeley y paquetes LaTeX.
- `res/library.bib`: bibliografia de ejemplo asociada al sitio.
- `res/images/`: capturas, collages y recursos visuales para entender la
  presentacion de cada familia.
- `res/Excel2LaTeX.*`, `res/indent.zip`, `res/es_CL.oxt`: utilidades externas
  referenciadas por el ecosistema.

## Decision tomada

- `Revision` queda limpia como bandeja de entrada.
- La fuente web de Template-Latex queda integrada en la bitacora editorial.
- Las plantillas de trabajo siguen en `plantillas/latex/ppizarror/originales/`.
- Las adaptaciones propias siguen en `plantillas/latex/adaptadas/`.

## Pendientes editoriales

- Crear una ficha por familia de plantilla con: origen, uso recomendado,
  archivos principales, dependencias y estado en AulaTeX.
- Revisar que elementos del sitio pueden convertirse en documentacion interna.
- Evaluar si los recursos visuales pueden ayudar al catalogo de plantillas.
