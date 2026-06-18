# Compilacion - Derecho a la seguridad social

Ejecutar desde la raiz del proyecto:

`powershell
.\scripts\latexmk-build.ps1 .\UnADM\licenciatura-en-derecho-unadm\derecho-a-la-seguridad-social-lde\reporte-derecho-a-la-seguridad-social.tex
.\scripts\latexmk-build.ps1 .\UnADM\licenciatura-en-derecho-unadm\derecho-a-la-seguridad-social-lde\presentacion-derecho-a-la-seguridad-social.tex
`

## Contrato de compilacion

- El PDF final queda en la misma carpeta del archivo fuente.
- La bibliografia local vive en $(@{Name=Derecho a la seguridad social; Block=1; Credits=8; Type=Obligatoria; Slug=derecho-a-la-seguridad-social; Semester=2}.Slug).bib.
- La identidad institucional usa img/departamentos/UnADM.pdf.
- La malla curricular base esta en UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.