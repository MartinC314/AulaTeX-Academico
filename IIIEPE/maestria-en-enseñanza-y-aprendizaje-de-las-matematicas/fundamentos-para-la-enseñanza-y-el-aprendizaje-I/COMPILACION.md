# Compilacion - Fundamentos para la Enseñanza y el Aprendizaje I

Ejecutar siempre desde la raiz del proyecto:

```powershell
.\scripts\latexmk-build.ps1 .\IIIEPE\fundamentos-para-la-enseñanza-y-el-aprendizaje-I\reporte-fundamentos-para-la-enseñanza-y-el-aprendizaje-I.tex
.\scripts\latexmk-build.ps1 .\IIIEPE\fundamentos-para-la-enseñanza-y-el-aprendizaje-I\reporte-fundamentos-para-la-enseñanza-y-el-aprendizaje-I-Actividad-1.tex
.\scripts\latexmk-build.ps1 .\IIIEPE\fundamentos-para-la-enseñanza-y-el-aprendizaje-I\presentacion-fundamentos-para-la-enseñanza-y-el-aprendizaje.tex
```

## Contrato de compilacion

- El unico argumento obligatorio del script es la ruta del `.tex`.
- El `\input{template}` no se pasa como argumento. MiKTeX lo busca con `TEXINPUTS`, definido en `.latexmkrc`.
- En reportes, `\input{template}` debe resolver a `base/Plantilla-Informe/template.tex`.
- El `.bib` no se pasa al script. Los reportes deben declarar `\bibliography{fundamentos-para-la-enseñanza-y-el-aprendizaje-I}`.
- BibTeX busca `fundamentos-para-la-enseñanza-y-el-aprendizaje-I.bib` con `BIBINPUTS`.
- El estilo `natnumurl.bst` se resuelve con `BSTINPUTS`.
- El PDF final queda en esta misma carpeta, junto al `.tex`.
- Los auxiliares quedan en `.build/latex` y `.build/latex/aux`.

## Checklist del `.tex`

- Mantener el formato del reporte de la materia al crear nuevas actividades.
- Toda clave citada debe existir en `fundamentos-para-la-enseñanza-y-el-aprendizaje-I.bib`.
