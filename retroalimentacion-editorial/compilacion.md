# Compilacion en AulaTeX-Academico

El flujo comun usa `latexmk` desde la raiz del repositorio. La configuracion
`.latexmkrc` agrega a las rutas de busqueda `base/Plantilla-Informe/`,
`base/latex/`, `UnADM/`, `UCNL/`, `IIIEPE/`, `trabajos/` y `referencias/`.

## Carpetas de salida

- `build/latex`: auxiliares de compilacion.
- `salidas/pdf`: PDF final copiado por el script.
- `salidas/tikz/pdf`: diagramas TikZ en PDF.
- `salidas/tikz/svg`: exportaciones SVG.
- `salidas/tikz/png`: exportaciones PNG.

## Compilar desde terminal o Codex

```powershell
.\scripts\latexmk-build.ps1 .\base\latex\main.tex
```

```powershell
.\scripts\latexmk-build.ps1 .\UnADM\filosofia-del-derecho\reporte-filosofia-del-derecho-Actividad-5.tex
```

```powershell
.\scripts\latexmk-build.ps1 .\IIIEPE\temas-selectos-de-matematicas-I\reporte-temas-selectos-de-matematicas-I.tex
```

El PDF final queda en `salidas/pdf`. El script compila primero en `build/latex`
y despues copia el PDF final, evitando movimientos fragiles de `latexmk`.

## Exportar TikZ

```powershell
.\scripts\tikz-export.ps1 "trabajos\diagramas\tikz\fuentes\Diagramas TikZ.tex" -Format all
```

## VS Code LaTeX Workshop

La carpeta `.vscode` define dos recetas:

- `AulaTeX: latexmk -> salidas/pdf`
- `AulaTeX: TikZ -> PDF/SVG/PNG`

Abre cualquier `.tex`, elige la receta y compila. La receta ejecuta los scripts
desde la raiz del proyecto para que plantillas, bibliografias e imagenes se
resuelvan con las mismas rutas en todos los editores.

## TeXstudio

Configura un comando de usuario con:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "<ruta-del-proyecto>\scripts\latexmk-build.ps1" %.tex
```

Para TikZ:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "<ruta-del-proyecto>\scripts\tikz-export.ps1" %.tex -Format all
```
