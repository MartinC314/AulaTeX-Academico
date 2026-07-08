# Compilacion - Aulatex Academico

Comandos desde la raiz del repositorio:

```powershell
.\scripts\latexmk-build.ps1 .\UnADM\licenciatura-en-derecho-unadm\AulaTeX-Academico\reporte-AulaTeX-Academico.tex
.\scripts\latexmk-build.ps1 .\UnADM\licenciatura-en-derecho-unadm\AulaTeX-Academico\reporte-AulaTeX-Academico-Actividad-1.tex
.\scripts\latexmk-build.ps1 .\UnADM\licenciatura-en-derecho-unadm\AulaTeX-Academico\presentacion-AulaTeX-Academico.tex
```

Validaciones:

- `\input{template}` debe resolver a la plantilla compartida.
- El archivo `.bib` local debe contener toda fuente citada.
- La salida final debe conservar portada institucional UnADM, desarrollo,
  producto solicitado, conclusion y bibliografia.
