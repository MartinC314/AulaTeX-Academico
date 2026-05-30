# Extractor de conceptos e ideas

Esta carpeta está reservada para alojar la adaptación local del proyecto funcional `proyecto_2_fichador_azure` dentro de `Template-Informe`.

## Propósito

Concentrar en un solo lugar:
- el código del motor de extracción;
- los scripts de ejecución;
- la configuración de rutas para este repositorio;
- la documentación mínima de uso.

## Uso previsto dentro de `Template-Informe`

El flujo esperado es:

1. Tomar una planeación de una materia.
2. Tomar la carpeta de libros o fuentes base de esa materia.
3. Ejecutar el motor para extraer conceptos e ideas.
4. Guardar las fichas resultantes en una carpeta de salida reutilizable.
5. Usar esas fichas como apoyo para redactar actividades, construir esquemas y sostener retroalimentación editorial.

## Estructura sugerida

```text
scripts/extractor-conceptos-ideas/
├─ README.md
├─ src/
├─ config/
├─ runners/
└─ output/
```

## Integración prevista

- `src/`: módulos del motor adaptado.
- `config/`: rutas, parámetros y convenciones.
- `runners/`: scripts de ejecución por materia o por semana.
- `output/`: salidas temporales o de prueba del motor.

La salida estable y reutilizable del proyecto no debe quedarse aquí, sino publicarse en una ruta de trabajo definida por materia y semana dentro del repositorio editorial.
