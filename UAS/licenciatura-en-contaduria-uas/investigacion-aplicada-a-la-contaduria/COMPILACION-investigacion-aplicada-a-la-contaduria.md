# Compilación — Investigación aplicada a la contaduría

Ejecutar desde la raíz de `AulaTeX-Academico`:

```powershell
.\scripts\latexmk-build.ps1 .\UAS\assets\marca-uas-provisional.tex
.\scripts\latexmk-build.ps1 .\UAS\licenciatura-en-contaduria-uas\investigacion-aplicada-a-la-contaduria\reporte-investigacion-aplicada-a-la-contaduria.tex
.\scripts\latexmk-build.ps1 .\UAS\licenciatura-en-contaduria-uas\investigacion-aplicada-a-la-contaduria\reporte-investigacion-aplicada-a-la-contaduria-Actividad-1.tex
.\scripts\latexmk-build.ps1 .\UAS\licenciatura-en-contaduria-uas\investigacion-aplicada-a-la-contaduria\actividad-investigacion-aplicada-a-la-contaduria.tex
.\scripts\latexmk-build.ps1 .\UAS\licenciatura-en-contaduria-uas\investigacion-aplicada-a-la-contaduria\presentacion-investigacion-aplicada-a-la-contaduria.tex
```

## Contrato

- Al script se entrega únicamente la ruta del `.tex`.
- `\input{template}` se resuelve desde `base/Plantilla-Informe` mediante `TEXINPUTS`.
- La bibliografía se declara como `\bibliography{investigacion-aplicada-a-la-contaduria}` y se resuelve mediante `BIBINPUTS`.
- El PDF final se copia junto al `.tex`; los auxiliares quedan en `.build/latex`.
- La marca provisional debe compilarse antes del reporte y la presentación.
- Antes de entregar, sustituir todos los textos `[POR COMPLETAR]`, confirmar metadatos y comprobar que cada cita tenga una entrada real en el `.bib`.
