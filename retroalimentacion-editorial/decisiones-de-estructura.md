# Decisiones de estructura

## Principio general

AulaTeX separa fuentes, referencias, plantillas, herramientas y salidas. Esa
separacion evita que una entrega academica, una plantilla maestra y un PDF
compilado compitan por el mismo lugar.

## Carpetas principales

- `trabajos/`: documentos vivos de materias, instituciones, proyectos y
  diagramas.
- `referencias/`: bibliografia, archivos `.bib`, libros, documentos de contexto,
  rubricas y marcos conceptuales.
- `plantillas/`: moldes reutilizables; no son entregas.
- `herramientas/`: scripts, utilidades y recursos tecnicos.
- `salidas/`: PDFs finales, exportaciones TikZ y verificaciones.
- `Revision/`: bandeja de entrada para material pendiente de clasificar.
- `retroalimentacion-editorial/`: memoria meta del proyecto, decisiones y
  propuestas de mejora.

## Regla de ubicacion

Un archivo debe ubicarse por su funcion principal:

- Si se entrega o se edita como actividad academica, va en `trabajos/`.
- Si fundamenta, cita o contextualiza, va en `referencias/`.
- Si sirve de molde para crear otros archivos, va en `plantillas/`.
- Si transforma, compila, exporta o automatiza, va en `herramientas/` o
  `scripts/`.
- Si es resultado generado, va en `salidas/`.
- Si todavia no se decide, va en `Revision/`.

## Criterio para materias

Cuando una materia tenga varios tipos de producto, se recomienda separar:

```text
trabajos/materias/nombre-de-la-materia/
  informes/
  presentaciones/
  actividades/
  recursos/
```

La estructura exacta puede adaptarse a cada materia, pero debe permitir que una
actividad concreta se encuentre sin depender del nombre de la plantilla base.

## Criterio para nombres

- Usar nombres descriptivos y estables.
- Preferir minusculas, guiones medios y nombres sin acentos para carpetas
  tecnicas.
- En titulos visibles se pueden usar acentos y nombres completos.
- Evitar que una carpeta dependa del nombre temporal de un archivo como
  `main-informe.tex`.
