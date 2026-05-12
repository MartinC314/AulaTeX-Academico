# Estructura del proyecto

`AulaTeX-Academico` separa tres cosas que antes convivian en la raiz: fuentes de trabajo, referencias y salidas compiladas.

## Raiz

- `main.tex`: entrada de ejemplo de la plantilla base.
- `template*.tex` y `src/`: nucleo heredado de Template-Informe.
- `.latexmkrc`: regla comun de compilacion.
- `.vscode/`: recetas para LaTeX Workshop.
- `scripts/`: comandos reutilizables para compilar y exportar.
- `plantillas/latex`: bases originales, adaptaciones institucionales y moldes por materia.
- `Revisión/`: bandeja temporal para proyectos o materiales que todavia no tienen ubicacion definitiva.

## Trabajo academico

- `trabajos/materias`: documentos por asignatura.
- `trabajos/instituciones`: materiales por institucion.
- `trabajos/proyectos`: reportes y presentaciones por proyecto.
- `trabajos/diagramas/tikz`: fuentes TikZ y beamer orientadas a diagramas.
- Si una materia produce mas de un tipo de entrega, usa subcarpetas como `informes`, `presentaciones` y `recursos`.

## Plantillas

- `plantillas/latex/ppizarror/originales`: copias base descargadas de Template-Latex; no se editan directamente.
- `plantillas/latex/adaptadas/instituciones`: plantillas maestras para UnADM, IIIEPE u otra institucion.
- `plantillas/latex/adaptadas/materias`: moldes derivados para una materia especifica.
- `plantillas/entradas`: entradas historicas del template base.

## Revision previa

- `Revisión/`: coloca aqui carpetas nuevas, como proyectos Slidev o materiales externos, antes de integrarlas al flujo principal.
- La regla practica: nada se mueve a `trabajos/`, `referencias/` o `herramientas/` hasta decidir si sera materia, proyecto, recurso transversal o herramienta.
- El contenido de `Revisión/` queda fuera de Git salvo `README.md` e `INVENTARIO.md`.

## Referencias

- `referencias/materias`: bibliografia y documentos base por materia.
- `referencias/instituciones`: lineamientos y contexto institucional.
- `referencias/proyectos`: rubricas, consignas y bibliografias por proyecto.
- `referencias/00-general`: recursos transversales.

## Salidas

- `salidas/pdf`: PDFs finales.
- `salidas/tikz`: exportaciones de diagramas.
- `salidas/verificacion`: capturas y material de revision visual.
- `salidas/auxiliares-antiguos`: auxiliares historicos movidos fuera de la raiz.

Los auxiliares nuevos deben caer en `build/latex` y no en la raiz.
