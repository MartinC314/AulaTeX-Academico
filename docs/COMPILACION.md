# Compilacion en AulaTeX-Academico

El flujo comun usa `latexmk` para que Codex, VS Code LaTeX Workshop y TeXstudio produzcan salidas en las mismas carpetas.

## Carpetas de salida

- `build/latex`: auxiliares de compilacion nuevos.
- `salidas/pdf`: PDF final copiado por el script de compilacion.
- `salidas/tikz/pdf`: copia final de diagramas TikZ en PDF.
- `salidas/tikz/svg`: exportaciones SVG hechas con Inkscape.
- `salidas/tikz/png`: exportaciones PNG hechas con Inkscape.

## Compilar desde terminal o Codex

```powershell
.\scripts\latexmk-build.ps1 .\main.tex
```

El PDF final queda en `salidas/pdf`. El script compila primero en `build/latex`
y despues copia el PDF a la carpeta final; asi evitamos movimientos internos
fragiles de `latexmk`.

## Exportar TikZ

```powershell
.\scripts\tikz-export.ps1 "trabajos\diagramas\tikz\fuentes\Diagramas TikZ.tex" -Format all
```

Esto compila primero y despues genera PDF, SVG y PNG en `salidas/tikz`.

## VS Code LaTeX Workshop

La carpeta `.vscode` ya define dos recetas:

- `AulaTeX: latexmk -> salidas/pdf`
- `AulaTeX: TikZ -> PDF/SVG/PNG`

Abre cualquier `.tex`, elige la receta y compila. La receta ejecuta los scripts desde la raiz del proyecto para que `template.tex`, `src`, `img`, `referencias` y `herramientas/bibtex` esten disponibles.

## TeXstudio

Configura un comando de usuario o el compilador por defecto con:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "<ruta-del-proyecto>\scripts\latexmk-build.ps1" %.tex
```

Para TikZ:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "<ruta-del-proyecto>\scripts\tikz-export.ps1" %.tex -Format all
```

La clave es compilar mediante los scripts o mediante `latexmk` desde la raiz del repositorio. Asi los documentos movidos a `trabajos/` siguen encontrando la plantilla y las bibliografias.

Nota: SyncTeX queda desactivado en la receta del proyecto porque esta instalacion de MiKTeX esta fallando al renombrar archivos `.synctex` dentro del directorio de build. La compilacion y el PDF final no dependen de SyncTeX.
