# Plantillas e integraciones

## Catalogo de plantillas

Las plantillas originales de Template-Latex viven en:

```text
plantillas/latex/ppizarror/originales/
```

Ese espacio incluye familias como articulo, reporte, tesis, presentacion,
poster, controles, auxiliares y CV profesional.

## Plantillas adaptadas

Las adaptaciones viven en:

```text
plantillas/latex/adaptadas/
```

Se organizan por institucion o por materia cuando ya tienen una intencion de uso
mas concreta. Por ejemplo, una plantilla de UnADM o IIIEPE puede servir como
base institucional, mientras que una plantilla de Filosofia del Derecho puede
ser un molde por materia.

## Regla de trabajo

- Original: se conserva.
- Adaptacion: se mejora como molde.
- Actividad concreta: se copia a `trabajos/` y se edita ahi.

Esta regla reduce el riesgo de romper plantillas maestras por resolver una sola
entrega urgente.

## Integracion desde Revision

Cuando llegue una nueva carpeta a `Revision`, se debe decidir si es:

- Plantilla LaTeX original.
- Adaptacion institucional.
- Plantilla por materia.
- Proyecto academico concreto.
- Herramienta tecnica.
- Recurso de referencia.
- Proyecto externo que merece su propia logica, como Slidev.

Hasta que exista esa decision, el material puede permanecer en `Revision` sin
entrar al historial principal de Git.
