# Estructura Híbrida - AulaTeX

## Organización del Proyecto

```
AulaTeX/
├── engine/                      → Motor del template (NO MODIFICAR)
│   ├── template.tex             → Template base
│   ├── template_*.tex           → Variantes (tesis, presentacion, etc.)
│   ├── src/                     → Módulos del sistema
│   ├── img/                     → Imágenes compartidas
│   └── test/                    → Archivos de prueba
│
├── plantillas/latex/            → Plantillas pre-configuradas
│   ├── main.tex                 → Informe (editable)
│   ├── main_tesis.tex           → Tesis (editable)
│   ├── main_presentacion.tex    → Presentación (editable)
│   ├── main_articulo.tex        → Artículo (editable)
│   ├── main_poster.tex          → Póster (editable)
│   ├── main_reporte.tex         → Reporte (editable)
│   ├── _template_wrapper.tex   → Wrapper para informe
│   ├── _template_*_wrapper.tex  → Wrappers para otras variantes
│   ├── library.bib              → Bibliografía de ejemplo
│   └── natnumurl.bst            → Estilo bibliográfico
│
├── trabajos/                    → Documentos del usuario
│   ├── instituciones/           → Por institución
│   ├── materias/                → Por materia
│   ├── proyectos/               → Por proyecto
│   └── diagramas/               → Diagramas TikZ
│
├── referencias/                 → Bibliografías organizadas
│   ├── 00-general/              → Referencias generales
│   ├── materias/                → Por materia
│   ├── instituciones/           → Por institución
│   └── proyectos/               → Por proyecto
│
├── salidas/                     → PDFs generados
│   ├── pdf/                     → PDFs finales
│   └── tikz/                    → Exportaciones TikZ
│
└── scripts/                     → Scripts de compilación
    ├── latexmk-build.ps1        → Compilación con latexmk
    └── tikz-export.ps1          → Exportación de diagramas
```

## Cómo Usar

### 1. Compilar desde plantillas/latex/

```powershell
cd plantillas/latex
latexmk -pdf main.tex
```

### 2. Crear un nuevo documento

1. Copiar plantilla deseada de `plantillas/latex/` a `trabajos/`
2. Editar el archivo copiado
3. Compilar desde el directorio del documento

### 3. Sistema de Wrappers

Los archivos `_template_*_wrapper.tex` resuelven las rutas relativas:

```latex
% Define rutas de búsqueda
\makeatletter
\def\input@path{{../../engine/}{../../engine/src/}{../../engine/img/}}
\makeatother

% Define rutas de imágenes
\graphicspath{{../../engine/img/}}

% Importa el template real
\input{../../engine/template}
```

## Ventajas de esta Estructura

✅ **Separación clara**: Engine (no tocar) vs Plantillas (editables)  
✅ **Rutas relativas funcionales**: Wrappers manejan las rutas automáticamente  
✅ **Organización por contexto**: trabajos/, referencias/, salidas/  
✅ **Fácil actualización**: Solo actualizar engine/ sin afectar documentos  
✅ **Sin duplicación**: Un solo engine para todas las plantillas  

## Resultados de Pruebas

- ✅ `main.tex` (informe): Compila correctamente → PDF 384 KB
- ✅ `main_tesis.tex`: Compila correctamente → PDF 29 KB
- ⚠️ `main_presentacion.tex`: Conflictos con beamer/sectsty (problema conocido del template base)

## Notas Técnicas

- Los wrappers usan `\input@path` y `\graphicspath` para resolver rutas
- Las plantillas en `plantillas/latex/` son puntos de partida editables
- El directorio `engine/` debe permanecer intacto
- Para actualizar el engine, reemplazar todo el directorio `engine/`

## Migración desde Rama Principal

La rama principal mantiene la estructura original (todo en raíz).  
Esta rama (aulaTEX) implementa la estructura híbrida sin afectar la principal.
