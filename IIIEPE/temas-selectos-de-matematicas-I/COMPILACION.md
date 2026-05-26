# Compilacion - Temas Selectos de Matematicas I

Ejecutar siempre desde la raiz del proyecto:

```powershell
.\scripts\latexmk-build.ps1 .\IIIEPE\temas-selectos-de-matematicas-I\reporte-temas-selectos-de-matematicas-I.tex
.\scripts\latexmk-build.ps1 .\IIIEPE\temas-selectos-de-matematicas-I\reporte-temas-selectos-de-matematicas-I-Actividad-1.tex
.\scripts\latexmk-build.ps1 .\IIIEPE\temas-selectos-de-matematicas-I\presentacion-temas-selectos-de-matematicas.tex
```

Para actividades 2 y 3, cambia solo el numero en el nombre del archivo.

## Contrato de compilacion

- El unico argumento obligatorio del script es la ruta del `.tex`.
- El `\input{template}` no se pasa como argumento. MiKTeX lo busca con `TEXINPUTS`, definido en `.latexmkrc`.
- En reportes, `\input{template}` debe resolver a `base/Plantilla-Informe/template.tex`.
- El `.bib` no se pasa al script. El reporte maestro declara `\bibliography{temas-selectos-de-matematicas-I,bibliografia-unadm}`.
- BibTeX busca `temas-selectos-de-matematicas-I.bib` en esta carpeta y `bibliografia-unadm.bib` en `UnADM/`.
- El estilo `natnumurl.bst` se resuelve con `BSTINPUTS`.
- El PDF final queda en esta misma carpeta, junto al `.tex`.
- Los auxiliares quedan en `.build/latex` y `.build/latex/aux`.

## Checklist del `.tex`

- Mantener el formato del reporte de la materia al crear nuevas actividades.
- Toda clave citada debe existir en `temas-selectos-de-matematicas-I.bib` o `UnADM/bibliografia-unadm.bib`.
- No declarar bibliografias inexistentes como `IIIEPE`.
