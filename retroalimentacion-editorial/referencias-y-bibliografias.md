# Referencias y bibliografias

## Funcion

`referencias/` guarda los materiales que sostienen el trabajo academico:
documentos base, libros, articulos, rubricas, consignas, contexto institucional
y archivos `.bib`.

## Organizacion recomendada

```text
referencias/
  00-general/
  instituciones/
  materias/
  proyectos/
```

Dentro de cada materia, puede existir una estructura como:

```text
referencias/materias/nombre-de-la-materia/
  bibliografia.bib
  documentos/
  marco-conceptual/
  consignas/
```

## Criterio para archivos `.bib`

- Si una bibliografia sirve a toda la materia, se guarda en la carpeta de la
  materia.
- Si sirve solo a una actividad, puede guardarse en una subcarpeta de esa
  actividad dentro de `referencias/`.
- Si es transversal, debe ir a `referencias/00-general/`.

## Relacion con trabajos

Los trabajos deben citar referencias de forma explicita, pero no necesitan
copiar documentos base dentro de cada actividad. La carpeta `referencias/`
funciona como memoria conceptual y bibliografica.
