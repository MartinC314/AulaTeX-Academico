# AulaTeX stage

- Etapa: criticar
- Rol: Critico adversarial
- Mision: encontrar fallas antes de aplicar cambios
- Motor: Codex
- Estado: ok

**ROL CRÍTICO ADVERSARIAL — Informe de bloqueo y criterios de corrección (Actividad 1)**  
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
   - Persisten `Actividad X`, `Semana X`, `\pendiente{}` y “Nombre de la figura docente”.  
   - **Riesgo:** incumplimiento formal institucional y evidencia de borrador no final.

4. **Posible problema de compilación en Beamer (archivo truncado).**  
   - El contenido de `presentacion-...tex` queda cortado en `\se...`  
   - **Riesgo:** compilación fallida si se usa esa vía de entrega.

5. **Metadatos temporales potencialmente no reales.**  
   - En bib: `year = {2026}` y consulta `2026-06-18` (debe corresponder a consulta real del estudiante).  
   - **Riesgo:** inconsistencia de integridad académica si no coincide con fecha efectiva.

---

## 2) Omisiones institucionales detectadas

- Falta **alineación explícita a criterios de evaluación** (no disponibles).
- No se declara **unidad/tema semanal** de la asignatura.
- Falta **producto concreto** exigido (ensayo, cuadro, línea del tiempo, mapa conceptual, etc.).
- No hay **delimitación histórica-jurídica** (periodo, institución, norma, actor, conflicto).
- Falta **criterio de originalidad** y porcentaje de citas/paráfrasis según política de la materia (no provista).

---

## 3) Alucinaciones a evitar en el siguiente ciclo

No se debe inventar:

- Tema exacto de Actividad 1.
- Rúbrica, puntajes o formato exacto.
- Número de páginas/palabras.
- Nombre de docente o fechas.
- Fuentes bibliográficas no verificadas localmente sin marcar que son propuestas por validar.

---

## 4) Verificación técnica mínima previa (checklist duro)

- [ ] Confirmar consigna oficial (captura o transcripción literal).  
- [ ] Definir tipo de entrega: `reporte` o `presentacion`.  
- [ ] Sustituir todos los placeholders (`Actividad X`, `Semana X`, `\pendiente{}`...).  
- [ ] Validar compilación LaTeX limpia (sin errores fatales).  
- [ ] Incorporar bibliografía temática real y verificable en `.bib`.  
- [ ] Cotejar que portada/datos institucionales estén completos y verdaderos.

---

## 5) Criterios obligatorios para el siguiente ciclo (consenso multiagente)

1. **Primero encuadre, luego redacción:** no generar contenido final sin consigna.  
2. **Supuestos explícitos:** si falta dato, marcar `[SUPUESTO]` y solicitar confirmación.  
3. **Fuentes verificables:** toda afirmación histórica relevante debe poder citarse.  
4. **Integridad editorial UnADM:** identidad institucional + conclusión jurídica propia.  
5. **Cierre validado:** revisión cruzada (académica, técnica y formal) antes de entregar.

---

## 6) Solicitud mínima de insumos (para destrabar)

Comparte, por favor:

1. Texto o captura de la **Actividad 1 oficial**.  
2. **Formato requerido** (reporte/presentación/otro).  
3. **Fecha de entrega** y, si existe, **rúbrica**.  
4. Nombre de la **figura docente** (si debe ir en portada).  

Con eso paso a estado `DISEÑO_ACADEMICO` y te genero la actividad sin inventar datos.
