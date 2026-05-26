# Estructura del proyecto

`AulaTeX-Academico` usa una estructura institucional. La raiz conserva solo los
puntos de entrada generales y las carpetas de soporte; el trabajo academico
queda agrupado por institucion.

## Raiz

- `base/`: plantillas, motor LaTeX y copias originales de Pizarror.
- `UnADM/`: reportes, actividades y bibliografias de UnADM.
- `UCNL/`: espacio canonico preparado para materias de UCNL.
- `IIIEPE/`: reportes, presentaciones y bibliografias de IIIEPE.
- `docs/`: decisiones, estructura y compilacion.
- `scripts/`: comandos reutilizables para compilar y exportar.
- `salidas/`: PDFs, TikZ y verificaciones generadas.
- `trabajos/` y `referencias/`: legado historico que todavia no se ha
  eliminado para evitar perdida de informacion.

## Base

- `base/Plantilla-Informe/`: motor compartido. Sustituye al antiguo `engine/`.
- `base/latex/`: wrappers, entradas editables y adaptaciones institucionales.
- `base/Template-*` y `base/Templates-Informe/`: copias historicas/originales para comparacion.
- `base/cwl-docs/` y `base/Export-Subtemmplate/`: herramientas auxiliares.

## Instituciones

- `UnADM/bibliografia-unadm.bib`: bibliografia general.
- `UnADM/<materia>/`: un reporte general, bibliografia de materia y actividades.
- `IIIEPE/<materia>/`: reportes, presentaciones y bibliografia por materia.
- `UCNL/`: estructura preparada con plantillas de reporte, presentacion y
  bibliografia por materia.

## Convencion de nombres

- Reporte general: `reporte-<materia>.tex`.
- Actividades: `reporte-<materia>-Actividad-N.tex`.
- Presentaciones: `presentacion-<materia>.tex`.
- Bibliografia local: `<materia>.bib`.

## Material legado

No se borro `trabajos/` ni `referencias/` porque aun contienen planeaciones,
PDFs fuente, notas, duplicados y materiales pendientes de clasificar. La regla
actual es migrar primero al arbol canonico, validar compilacion y solo despues
limpiar el legado con un commit separado.
