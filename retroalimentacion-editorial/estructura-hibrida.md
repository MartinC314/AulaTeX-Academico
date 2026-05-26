# Estructura hibrida anterior

Este documento queda como nota historica. La rama `aulaTEX` uso durante un
periodo una estructura hibrida con `engine/`, `plantillas/latex/`, `trabajos/`
y `referencias/`.

La refactorizacion actual migro esa idea a una arquitectura mas cercana al
arbol academico solicitado:

- `engine/` ahora vive como `base/Plantilla-Informe/`.
- `plantillas/` ahora vive como `base/`.
- Los trabajos recuperados se agruparon por institucion en `UnADM/` e `IIIEPE/`.
- `trabajos/` y `referencias/` permanecen como legado hasta terminar la limpieza
  validada.

Consulta la estructura vigente en [ESTRUCTURA.md](ESTRUCTURA.md).
