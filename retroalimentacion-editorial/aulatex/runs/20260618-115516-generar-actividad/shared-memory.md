# Memoria compartida AulaTeX

Propuestas:
- Claro. **Rol Planificador activado**.  
A continuación presento un **plan breve por fases** para la actividad solicitada (*Acción: generar-actividad, Actividad 1*) en:

**UnADM / Licenciatura en Derecho / Historia del Derecho en México (LDE-S1B1)**.

---

## Plan por fases (flujo con estados)

### Fase 1. Investigación y encuadre (Estado: `RECOLECCION`)
**Objetivo:** delimitar qué pide la Actividad 1 y qué evidencia académica debe entregarse.

Tareas:
1. Revisar consigna oficial de Actividad 1 (si no está disponible, marcar supuesto).
2. Extraer propósito, formato, extensión, criterios de evaluación y fecha.
3. Definir problema jurídico-histórico central alineado con la materia.
4. Identificar fuentes verificables (institucionales y académicas) para `.bib`.

Salida esperada:
- Ficha de requisitos de la actividad.
- Lista inicial de fuentes reales y citables.

---

### Fase 2. Diseño acad

Riesgos:
- # ROL INVESTIGADOR — Diagnóstico de trazabilidad y activos

**Materia:** Historia del Derecho en México (LDE-S1B1)
**Acción:** generar-actividad · **Actividad:** 1
**Estado del flujo:** `RECOLECCION`

---

## 1. Hallazgos prioritarios (orden por riesgo)

| # | Severidad | Hallazgo | Evidencia local | Implicación |
|---|-----------|----------|------------------|-------------|
| H1 | **ALTA** | **No existe consigna oficial de la Actividad 1.** El repositorio solo contiene plantillas base (`reporte-...tex`, `presentacion-...tex`) con marcadores `Actividad X` y `\pendiente{}`. | `reporte-...tex` (`\documentsubtitle {Actividad X...}`), README, programa analítico | No se puede generar la actividad sin inventar propósito, formato ni rúbrica. **Bloqueante metodológico.** |
| H2 | **ALTA** | **Bibliografía local insuficiente.** Solo 2 entradas (`unadmSitioWeb`, `unadmMallaDerecho2024`), ambas ins
- **ROL CRÍTICO ADVERSARIAL — Informe de bloqueo y criterios de corrección (Actividad 1)**  
**Estado del flujo:** `VALIDACION_CRITICA`  
**Materia:** Historia del Derecho en México (LDE-S1B1)  
**Acción:** generar-actividad

---

## 1) Errores bloqueantes (deben resolverse antes de “generar-actividad”)

1. **Consigna oficial inexistente (bloqueante mayor).**  
   - No hay instrucciones de “Actividad 1” (objetivo, producto, rúbrica, extensión, fecha).  
   - **Riesgo:** cualquier entrega sería inferida y puede no alinearse a evaluación real.

2. **Trazabilidad académica insuficiente.**  
   - La `.bib` solo tiene 2 fuentes institucionales generales; no hay fuentes temáticas de historia jurídica mexicana.  
   - **Riesgo:** análisis sin sustento disciplinar verificable.

3. **Plantilla en estado placeholder.**  
   - Persisten `Actividad X`, `Semana X`, `\pendiente{}` y “Nombre de la figura