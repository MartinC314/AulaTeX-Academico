# Referencias bibliograficas y documentales

Esta carpeta concentra materiales de apoyo para actividades, materias, instituciones y proyectos. La idea es separar el trabajo academico de los archivos de compilacion de LaTeX.

## Criterio general

- `bib`: archivos `.bib` usados por actividades, reportes o presentaciones.
- `libros`: libros completos, capitulos o transcripciones extensas.
- `articulos`: papers, articulos academicos, notas tecnicas o publicaciones breves.
- `documentos-base`: lineamientos, consignas, rubricas, guias institucionales y materiales fuente.
- `marco-conceptual`: textos que ayudan a construir categorias, definiciones y autores base.
- `contexto`: paginas guardadas, documentos institucionales, antecedentes y materiales situacionales.
- `notas`: apuntes propios, planeaciones, esquemas y borradores de analisis.

## Organizacion principal

- `00-general`: referencias transversales para varias materias o plantillas.
- `materias`: referencias organizadas por asignatura o tema academico.
- `instituciones`: documentos propios de IIIEPE, UnADM, FIME u otras instituciones.
- `proyectos`: materiales de proyectos especificos, como PFM01 o PFM02.

## Uso con LaTeX

Por ahora se copiaron los `.bib` existentes a sus carpetas tematicas, pero se dejaron los originales en la raiz para no romper compilaciones previas.

Cuando una actividad ya este lista para usar esta estructura, se puede actualizar su ruta bibliografica. En BibTeX normalmente se referencia sin extension:

```tex
\bibliography{referencias/materias/filosofia-derecho/bib/FilosofiaDerechoAct3}
```

Conviene hacer esa migracion actividad por actividad, compilando despues de cada cambio.
