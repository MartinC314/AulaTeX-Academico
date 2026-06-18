# AulaTeX-Academico

Entorno academico en LaTeX organizado por institucion, con una base comun de
plantillas Pizarror y puntos de entrada canonicos para reportes, actividades,
presentaciones y bibliografias.

## Flujo Principal

- Plantillas maestras y motor LaTeX: `base/`.
- Trabajos canonicos por institucion: `UnADM/`, `UCNL/`, `IIIEPE/`, `ITESCA/`.
- Material editorial y criterios de revision: `retroalimentacion-editorial/`.
- Automatizacion de compilacion y exportacion: `scripts/`.
- Residuales de compilacion: `.build/`.

## Comandos Utiles

```powershell
.\scripts\latexmk-build.ps1 .\UnADM\reporte-unadm.tex
```

```powershell
.\scripts\latexmk-build.ps1 .\IIIEPE\temas-selectos-de-matematicas-I\reporte-temas-selectos-de-matematicas-I.tex
```

```powershell
.\scripts\latexmk-build.ps1 .\ITESCA\ingenieria-en-sistemas-computacionales\primer-ingreso\reporte-primer-ingreso.tex
```

```powershell
.\scripts\latexmk-build.ps1 .\base\Templates-Informe\main.tex
```

```powershell
.\scripts\aulatex.ps1
```

El PDF final se copia en la misma carpeta del archivo `.tex`.

Cada carpeta de materia tiene un `COMPILACION.md` con el comando exacto, el
`.bib` esperado y el contrato de compilacion. Regla central: al script solo se
le pasa el `.tex`; `\input{template}` se resuelve con `TEXINPUTS` y
`\bibliography{...}` se resuelve con `BIBINPUTS`, ambos definidos en
`.latexmkrc`.

## Estructura Canonica

```text
AulaTeX-Academico/
|-- README.md
|-- base/
|   |-- cwl-docs/
|   |-- Export-Subtemmplate/
|   |-- Plantilla-Informe/
|   |-- latex/
|   |-- Professional-CV/
|   |-- Template-Articulo/
|   |-- Template-Auxiliares/
|   |-- Template-Controles/
|   |-- Templates-Informe/
|   |-- Template-Informe-master/
|   |-- Template-latex.github.io/
|   |-- Template-Poster/
|   |-- Template-Presentacion/
|   |-- Template-Reporte/
|   `-- Template-Tesis/
|-- UnADM/
|   |-- bibliografia-unadm.bib
|   |-- reporte-unadm.tex
|   |-- presentacion-unadm.tex
|   |-- referencias-unadm/
|   |-- redaccion-en-contextos-virtuales/
|   |-- etica-y-moral-juridica/
|   `-- filosofia-del-derecho/
|-- UCNL/
|   |-- bibliografia-ucnl.bib
|   |-- reporte-ucnl.tex
|   |-- presentacion-ucnl.tex
|   |-- referencias-ucnl/
|   |-- administracion-I/
|   |-- contabilidad-I/
|   |-- curso-inductivo/
|   |-- desarrollo-sustentable/
|   |-- ingles-I/
|   |-- matematicas-I/
|   `-- microeconomia/
|-- IIIEPE/
|   |-- temas-selectos-de-matematicas-I/
|   `-- fundamentos-para-la-enseñanza-y-el-aprendizaje-I/
|-- ITESCA/
|   |-- ingenieria-en-sistemas-computacionales/
|   |   |-- bibliografia-itesca-isc.bib
|   |   |-- reporte-itesca-isc.tex
|   |   |-- presentacion-itesca-isc.tex
|   |   |-- referencias-itesca-isc/
|   |   `-- primer-ingreso/
|   `-- maestria-en-gestion-administrativa/
|       |-- bibliografia-itesca-mga.bib
|       |-- reporte-itesca-mga.tex
|       |-- presentacion-itesca-mga.tex
|       |-- referencias-itesca-mga/
|       `-- primer-ingreso/
|-- retroalimentacion-editorial/
`-- scripts/
```

## Convenciones

- Reporte general: `reporte-<materia>.tex`.
- Actividad: `reporte-<materia>-Actividad-N.tex`.
- Presentacion: `presentacion-<materia>.tex`.
- Bibliografia local: `<materia>.bib`.
- Cuando una institucion tiene mas de un programa educativo, el nivel canonico se mueve a `institucion/carrera/materia`.

## Base Original

El proyecto conserva el nucleo tecnico de `Template-Informe` de Pablo Pizarro R.
en `base/Plantilla-Informe/`, junto con copias originales y adaptaciones
institucionales. Licencia base: MIT.
