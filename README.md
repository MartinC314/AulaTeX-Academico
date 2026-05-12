# AulaTeX-Academico

Entorno personal de trabajo academico en LaTeX, construido sobre `Template-Informe` y adaptado para materias, proyectos, referencias bibliograficas, diagramas TikZ y salidas compiladas ordenadas.

## Flujo principal

- Escribe documentos en `trabajos/`.
- Guarda bibliografia y documentos fuente en `referencias/`.
- Coloca materiales pendientes de integrar en `Revisión/`.
- Compila con `latexmk` mediante los scripts o las recetas de VS Code.
- Recibe PDFs finales en `salidas/pdf`.
- Exporta diagramas TikZ a `salidas/tikz/pdf`, `salidas/tikz/svg` y `salidas/tikz/png`.

## Comandos utiles

```powershell
.\scripts\latexmk-build.ps1 .\main.tex
```

```powershell
.\scripts\tikz-export.ps1 "trabajos\diagramas\tikz\fuentes\Diagramas TikZ.tex" -Format all
```

## Documentacion interna

- [Estructura](docs/ESTRUCTURA.md)
- [Compilacion](docs/COMPILACION.md)
- [Referencias](referencias/README.md)
- [Mapa de bibliografias](referencias/MAPA_BIBLIOGRAFIAS.md)

## Base original

Este proyecto conserva el nucleo de `Template-Informe` de Pablo Pizarro R. como base tecnica de la plantilla. La personalizacion de `AulaTeX-Academico` organiza el flujo local de trabajo, referencias, materias, proyectos y salidas compiladas.

Licencia base: MIT.
