# Flujo de actividades academicas

## Flujo recomendado

1. Identificar materia, institucion y tipo de entrega.
2. Buscar una plantilla base en `plantillas/latex/`.
3. Copiar la plantilla, no editar el original.
4. Guardar la copia en `trabajos/` dentro de la materia correspondiente.
5. Crear o actualizar referencias en `referencias/`.
6. Compilar mediante los scripts del proyecto, LaTeX Workshop o TeXstudio.
7. Revisar el PDF final en `salidas/pdf`.
8. Registrar cambios relevantes en esta bitacora si afectan el flujo general.

## Ejemplo: Etica y Moral juridica

Una actividad nueva podria vivir asi:

```text
trabajos/materias/etica-moral-juridica/actividades/actividad-01/
  main.tex
  README.md
```

Sus referencias podrian vivir asi:

```text
referencias/materias/etica-moral-juridica/
  bibliografia.bib
  documentos/
  marco-conceptual/
```

El archivo `main.tex` de la actividad seria una copia adaptada de una plantilla,
no la plantilla original.

## Cuando una actividad combina informe y presentacion

Para materias como Temas Selectos de Matematicas I, donde se trabaja informe y
presentacion juntos, conviene separar productos pero mantener recursos comunes:

```text
trabajos/materias/temas-selectos-matematicas-1/
  informes/
  presentaciones/
  recursos/
```

Las fuentes compartidas, graficas, datos o diagramas pueden vivir en `recursos/`
si alimentan mas de un producto.
