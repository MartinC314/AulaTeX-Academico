# Compilacion - Garantias constitucionales

Ejecutar desde la raiz del proyecto:

`powershell
.\scripts\latexmk-build.ps1 .\UnADM\licenciatura-en-derecho-unadm\garantias-constitucionales-lde\reporte-garantias-constitucionales.tex
.\scripts\latexmk-build.ps1 .\UnADM\licenciatura-en-derecho-unadm\garantias-constitucionales-lde\presentacion-garantias-constitucionales.tex
`

## Contrato de compilacion

- El PDF final queda en la misma carpeta del archivo fuente.
- La bibliografia local vive en $(@{Name=Garantias constitucionales; Block=1; Credits=8; Type=Obligatoria; Slug=garantias-constitucionales; Semester=2}.Slug).bib.
- La identidad institucional usa img/departamentos/UnADM.pdf.
- La malla curricular base esta en UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.