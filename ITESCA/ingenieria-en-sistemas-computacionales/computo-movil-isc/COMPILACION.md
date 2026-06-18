# Compilacion - Computo Movil

Ejecutar desde la raiz del repositorio que contiene la carpeta ITESCA:

```powershell
.\\scripts\\latexmk-build.ps1 .\\ITESCA\\ingenieria-en-sistemas-computacionales\\computo-movil-isc\\reporte-computo-movil-isc.tex
.\\scripts\\latexmk-build.ps1 .\\ITESCA\\ingenieria-en-sistemas-computacionales\\computo-movil-isc\\presentacion-computo-movil-isc.tex
```

## Contrato de compilacion

- El unico argumento obligatorio del script es la ruta del archivo .tex.
- El PDF final queda en la misma carpeta del archivo fuente.
- La bibliografia local de la materia vive en computo-movil.bib.
- Esta carpeta corresponde a la categoria tronco comun ISC.
- La identidad institucional se hereda desde ITESCA/_shared/ y usa los assets oficiales descargados en ITESCA/assets-itesca/web/.
