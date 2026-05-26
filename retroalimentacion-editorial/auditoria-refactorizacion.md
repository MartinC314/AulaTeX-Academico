# Auditoria de refactorizacion

Fecha de auditoria: 2026-05-25.

## Historial revisado

- Rama activa: `aulaTEX`.
- Rama local integrada: `codex/probar-plantillas-principales`.
- Rama base: `master`.
- Remotos revisados: `origin/master`, `upstream/master`, `origin/gh-pages`,
  `origin/imgbot`.
- Stash revisado: `stash@{0}`.

## Lectura del historial

- `codex/probar-plantillas-principales` no contiene commits que no esten ya en
  `aulaTEX`; quedo como ancestro historico.
- `master` integro catalogo de plantillas, bitacora editorial y reorganizacion
  inicial.
- `aulaTEX` agrego el motor separado, wrappers funcionales, scripts de
  compilacion y movimientos de archivos sueltos.
- `stash@{0}` contenia tres bibliografias temporales:
  `EticaMoralJuridica.bib`, `FilosofiaDerechoAct4.bib` y
  `RedaccionContextosVirtuales.bib`.

## Recuperacion aplicada

- `plantillas/` se migro a `base/`.
- `engine/` se migro a `base/Plantilla-Informe/`.
- Los wrappers de `base/latex/` y `base/Templates-Informe/` apuntan ahora a
  `base/Plantilla-Informe/`.
- Bibliografias y actividades de UnADM se reagruparon en:
  - `UnADM/redaccion-en-contextos-virtuales/`
  - `UnADM/etica-y-moral-juridica/`
  - `UnADM/filosofia-del-derecho/`
- Material IIIEPE recuperado se reagruparo en:
  - `IIIEPE/temas-selectos-de-matematicas-I/`
  - `IIIEPE/fundamentos-para-la-enseñanza-y-el-aprendizaje-I/`
- Se recuperaron entradas bibliograficas del stash para:
  - `redaccion-en-contextos-virtuales.bib`
  - `filosofia-del-derecho.bib`
  - `etica-y-moral-juridica.bib`

## Pendientes deliberados

- `UCNL/` queda como estructura preparada. No se encontraron archivos historicos
  de UCNL en las ramas revisadas.
- `trabajos/` y `referencias/` aun contienen notas, planeaciones, PDFs y
  duplicados. Se mantienen para no perder material mientras se valida la nueva
  estructura.
- Hay nombres con mojibake y archivos vacios heredados. No se eliminaron en esta
  pasada; conviene limpiarlos en un commit posterior, ya con la estructura
  canonica compilando.

## Criterio de mantenimiento

La fuente canonica debe vivir en las carpetas institucionales. El material nuevo
debe entrar directamente a `UnADM/`, `UCNL/` o `IIIEPE/`, y solo despues copiarse
a `salidas/` si es un PDF final.
