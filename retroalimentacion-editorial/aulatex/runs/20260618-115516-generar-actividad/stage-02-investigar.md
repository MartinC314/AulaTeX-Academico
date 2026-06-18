# AulaTeX stage

- Etapa: investigar
- Rol: Investigador documental
- Mision: detectar fuentes, contexto curricular y faltantes editoriales
- Motor: Claude Foundry
- Estado: ok

# ROL INVESTIGADOR — Diagnóstico de trazabilidad y activos

**Materia:** Historia del Derecho en México (LDE-S1B1)
**Acción:** generar-actividad · **Actividad:** 1
**Estado del flujo:** `RECOLECCION`

---

## 1. Hallazgos prioritarios (orden por riesgo)

| # | Severidad | Hallazgo | Evidencia local | Implicación |
|---|-----------|----------|------------------|-------------|
| H1 | **ALTA** | **No existe consigna oficial de la Actividad 1.** El repositorio solo contiene plantillas base (`reporte-...tex`, `presentacion-...tex`) con marcadores `Actividad X` y `\pendiente{}`. | `reporte-...tex` (`\documentsubtitle {Actividad X...}`), README, programa analítico | No se puede generar la actividad sin inventar propósito, formato ni rúbrica. **Bloqueante metodológico.** |
| H2 | **ALTA** | **Bibliografía local insuficiente.** Solo 2 entradas (`unadmSitioWeb`, `unadmMallaDerecho2024`), ambas institucionales genéricas. No hay fuentes de historia del derecho. | `historia-del-derecho-en-mexico.bib` | Cualquier contenido sustantivo carecerá de respaldo citable. Riesgo de fabricación de fuentes. |
| H3 | **MEDIA** | **Corrupción de plantillas de ruta/variables.** Aparecen literales sin expandir: `$(@{Name=...}.Slug).bib`, y nombres truncados (`\teporte-`, `\eferencias-`). | README, programa analítico | Riesgo de trazabilidad: el nombre canónico del `.bib` y de la carpeta de referencias no es legible con certeza. **Supuesto requerido.** |
| H4 | **MEDIA** | **Fragmento de plan en memoria compartida truncado** ("Fase 2. Diseño acad…") y con metadato divergente: menciona bloque `LDE-S1B1` pero la propuesta cita "Bloque 1" sin cerrar fases. | Memoria compartida (Propuestas) | Continuidad del flujo incompleta; se debe reconstruir la fase faltante. |
| H5 | **BAJA** | **`presentacion-...tex` truncado** en el preámbulo (`\se`). No afecta al reporte, pero invalida la rama de entregable visual hasta completar. | `presentacion-...tex` | Si la Actividad 1 exige presentación, falta infraestructura. |

---

## 2. Identidad institucional (verificada en local)

| Campo | Valor confirmado | Fuente |
|-------|------------------|--------|
| Institución | Universidad Abierta y a Distancia de México (UnADM) | README, `.tex`, `.bib` |
| Programa | Licenciatura en Derecho | README, `.tex` |
| Asignatura | Historia del Derecho en México | README |
| Código | LDE-S1B1 | `reporte-...tex` (`\coursecode`) |
| Ubicación curricular | Semestre 1 · Bloque 1 · Obligatoria · 8 créditos | README, programa analítico |
| Alumno / Matrícula | Martin Jonathan de la Cruz / ES2611202040 | `\authortable`, presentación |
| Figura docente | **Sin definir** ("Nombre por definir") | `\authortable` |
| Localización | Roma Norte, Ciudad de México | `\universitylocation` |

**Consistencia:** identidad UnADM íntegra y coherente entre reporte y presentación. ✔

---

## 3. Programa analítico (ejes editoriales)

El programa fija **5 ejes** que toda entrega debe articular:
1. Problema jurídico/social que activa la asignatura.
2. Conceptos, normas, doctrina o datos pertinentes.
3. Producto solicitado por la planeación.
4. Análisis propio y postura académica.
5. Conclusión transferible a la práctica jurídica.

➡ La estructura del `reporte-...tex` (Introducción → Desarrollo → Producto visual → Postura → Conclusión) **mapea correctamente** estos ejes. Reutilizable.

---

## 4. Activos visuales

| Activo | Estado | Nota |
|--------|--------|------|
| Marca de agua portada | Definido | `img/departamentos/UnADM.pdf`, opacidad 0.16 |
| Logo departamental (beamer) | Referenciado
