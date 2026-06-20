# Compilacion - Derecho a la Seguridad Social

Comandos desde la raiz del repositorio:

```powershell
.\scripts\latexmk-build.ps1 .\UnADM\licenciatura-en-derecho-unadm\derecho-a-la-seguridad-social-lde\reporte-derecho-a-la-seguridad-social.tex
.\scripts\latexmk-build.ps1 .\UnADM\licenciatura-en-derecho-unadm\derecho-a-la-seguridad-social-lde\reporte-derecho-a-la-seguridad-social-Actividad-1.tex
.\scripts\latexmk-build.ps1 .\UnADM\licenciatura-en-derecho-unadm\derecho-a-la-seguridad-social-lde\presentacion-derecho-a-la-seguridad-social.tex
```

Validaciones:

- `\input{template}` debe resolver a la plantilla compartida.
- El archivo `.bib` local debe contener toda fuente citada.
- La salida final debe conservar portada institucional UnADM, desarrollo,
  producto solicitado, conclusion y bibliografia.
