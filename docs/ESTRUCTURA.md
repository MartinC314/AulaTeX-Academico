# Estructura del proyecto

`AulaTeX-Academico` separa tres cosas que antes convivian en la raiz: fuentes de trabajo, referencias y salidas compiladas.

## Raiz

- `main.tex`: entrada de ejemplo de la plantilla base.
- `template*.tex` y `src/`: nucleo heredado de Template-Informe.
- `.latexmkrc`: regla comun de compilacion.
- `.vscode/`: recetas para LaTeX Workshop.
- `scripts/`: comandos reutilizables para compilar y exportar.

## Trabajo academico

- `trabajos/materias`: documentos por asignatura.
- `trabajos/instituciones`: materiales por institucion.
- `trabajos/proyectos`: reportes y presentaciones por proyecto.
- `trabajos/diagramas/tikz`: fuentes TikZ y beamer orientadas a diagramas.

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
