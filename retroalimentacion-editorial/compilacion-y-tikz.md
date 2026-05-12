# Compilacion, salidas y TikZ

## Flujo actual

El proyecto usa `latexmk` mediante scripts para que Codex, VS Code LaTeX
Workshop y TeXstudio puedan producir salidas de forma consistente.

```powershell
.\scripts\latexmk-build.ps1 .\main.tex
```

Los auxiliares nuevos quedan en:

```text
build/latex/
```

Los PDFs finales quedan en:

```text
salidas/pdf/
```

## TikZ

El flujo TikZ busca compilar una fuente y exportarla a varios formatos:

```powershell
.\scripts\tikz-export.ps1 "trabajos\diagramas\tikz\fuentes\Diagramas TikZ.tex" -Format all
```

Las salidas se separan por formato:

```text
salidas/tikz/pdf/
salidas/tikz/svg/
salidas/tikz/png/
```

## Lineamiento

Una compilacion no debe ensuciar la raiz del proyecto. Si aparece un auxiliar o
un PDF fuera de `build/` o `salidas/`, el flujo debe ajustarse.

## Mejora futura

Conviene evolucionar este flujo hacia perfiles de conversion:

- `tikz-pdf`: solo PDF.
- `tikz-svg`: PDF y SVG.
- `tikz-png`: PDF y PNG.
- `tikz-all`: PDF, SVG y PNG.

Tambien seria util registrar ejemplos minimos de TikZ y Beamer para reutilizar
diagramas entre informes, presentaciones y materiales de clase.
