# Retroalimentacion Editorial de AulaTeX

Esta carpeta funciona como metabitacora del proyecto. No guarda entregas,
plantillas de trabajo ni bibliografia: guarda decisiones, propuestas,
lineamientos y registro historico de la evolucion de AulaTeX.

La idea es que cada cambio importante deje una huella: que se propuso, por que
se propuso, que se hizo, que quedo pendiente y como deberia evolucionar el
proyecto.

## Como usar esta bitacora

- Si el usuario propone una mejora, se registra en `propuestas-de-evolucion.md`.
- Si la mejora se implementa, se resume en un registro fechado.
- Si una decision se vuelve criterio estable, pasa a `lineamientos-del-proyecto.md`.
- Si afecta carpetas, plantillas, referencias o compilacion, se documenta tambien
  en el archivo tematico correspondiente.
- Si llega material nuevo a `Revision`, primero se analiza y despues se decide si
  pertenece a `trabajos`, `plantillas`, `referencias`, `herramientas` o `salidas`.

## Temas

- [Registro inicial 2026-05-12](registro-2026-05-12.md)
- [Decisiones de estructura](decisiones-de-estructura.md)
- [Lineamientos del proyecto](lineamientos-del-proyecto.md)
- [Flujo de actividades academicas](flujo-de-actividades.md)
- [Plantillas e integraciones](plantillas-e-integraciones.md)
- [Fuente editorial Template-Latex](fuentes-template-latex.md)
- [Referencias y bibliografias](referencias-y-bibliografias.md)
- [Compilacion, salidas y TikZ](compilacion-y-tikz.md)
- [Propuestas de evolucion](propuestas-de-evolucion.md)

## Fuentes integradas

- [Fuentes editoriales integradas](fuentes/README.md)
- [Sitio Template-Latex Web](fuentes/template-latex-web/README.md)

## Estados sugeridos

- `Propuesto`: idea planteada, todavia no integrada.
- `En revision`: idea aceptada, falta definir ubicacion o alcance.
- `Implementado`: cambio hecho y registrado.
- `Ajustar`: existe una version funcional, pero requiere mejora.
- `Archivado`: idea descartada o sustituida por otra decision.

## Plantilla breve de entrada

```markdown
## AAAA-MM-DD - Tema

- Origen: Usuario / Codex / ambos.
- Estado: Propuesto / En revision / Implementado / Ajustar / Archivado.
- Cambio o propuesta:
- Motivo:
- Decision tomada:
- Archivos o carpetas afectadas:
- Pendiente:
```
