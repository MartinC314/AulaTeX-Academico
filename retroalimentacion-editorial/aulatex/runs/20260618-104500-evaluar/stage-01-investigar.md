# AulaTeX stage

- Motor: Codex
- Estado: ok

## Diagnóstico editorial — Actividad 1 (evaluar)  
**Materia:** Historia del Derecho en México (LDE-S1B1)  
**Target:** `UnADM/licenciatura-en-derecho-unadm/historia-del-derecho-en-mexico-lde`  

---

### 1) Estado general (prioridad alta)
El objetivo **sí tiene base institucional y estructura mínima funcional**, pero está en **estado de plantilla en construcción** (no listo para entrega académica final).  
Fortalezas: identidad UnADM visible, metadatos curriculares, pauta editorial clara, archivos nucleares presentes (`README`, programa analítico, `.tex` reporte/presentación, `.bib`).  
Debilidades críticas: errores de integridad textual en README, presentación truncada, placeholders no resueltos y posibles riesgos de compilación.

---

### 2) Hallazgos priorizados

## A. Críticos (resolver primero)

1. **Presentación `.tex` incompleta/truncada**
   - El archivo `presentacion-historia-del-derecho-en-mexico.tex` termina abruptamente en `\se`.
   - **Riesgo:** compilación imposible.
   - **Acción:** restaurar bloque faltante (tema beamer, portada, secciones, cierre `\begin{document}...\end{document}`).

2. **README con corrupción de rutas/listado**
   - En “Estructura” aparecen entradas rotas: `eporte-...`, `eferencias-...`.
   - **Riesgo:** baja trazabilidad, confusión operativa y errores de automatización.
   - **Acción:** corregir nombres exactos de archivos/carpetas y validar consistencia con árbol real.

3. **Placeholders no resueltos en reporte**
   - “Actividad X”, “Nombre por definir”, secciones `\pendiente{...}` sin desarrollar.
   - **Riesgo:** producto no evaluable académicamente.
   - **Acción:** parametrizar por actividad real (consigna, semana, docente, problema jurídico, conclusión con criterio propio).

---

## B. Importantes (calidad editorial y académica)

4. **Bibliografía insuficiente para la asignatura**
   - `.bib` contiene solo 2 fuentes institucionales (sitio UnADM y malla curricular).
   - **Riesgo:** soporte doctrinal/histórico-jurídico débil para actividades.
   - **Acción:** incorporar fuentes de historia del derecho mexicano (normativas históricas, doctrina, textos académicos verificables).

5. **Inconsistencia potencial de dependencias del template**
   - `\input{template}` presupone archivo externo no mostrado.
   - Uso de comandos dependientes (`\templatePortrait`, `\templateIndex`, etc.).
   - **Riesgo:** compilación fallida si falta `template.tex` o paquetes asociados.
   - **Acción:** verificar existencia del template y su compatibilidad con clase/article.

6. **Ubicación geográfica genérica/no institucional**
   - `Roma Norte, Ciudad de Mexico` en portada.
   - **Riesgo:** posible desalineación institucional (UnADM es modalidad a distancia).
   - **Supuesto:** puede ser dato personal del alumno, no institucional.
   - **Acción:** definir política editorial: ubicación institucional, personal o eliminar si no aplica.

---

## C. Mejora recomendada (madurez editorial)

7. **Trazabilidad de actividad**
   - Falta bloque explícito de: consigna oficial, evidencias, criterios de evaluación/rúbrica.
   - **Acción:** añadir sección fija “Trazabilidad” (fuente de consigna, fecha, versión, cumplimiento por criterio).

8. **Normalización de nombres y metadatos**
   - Hay token no resuelto en README: `$(@{...}.Slug).bib`.
   - **Riesgo:** documentación confusa.
   - **Acción:** reemplazar por nombre final `historia-del-derecho-en-mexico.bib`.

9. **Checklist editorial sólido pero genérico**
   - Buena base, pero puede volverse instrumento de control verificable.
   - **Acción:** convertir checklist a tabla Sí/No + evidencia (página/sección).

---

### 3) Identidad institucional (evaluación puntual)
**Cumplimiento parcial-alto.**  
Hay identidad UnADM en:
- nombre institucional,
- licenciatura,
- ubicación curricular (semestre, bloque, créditos, obligatoriedad),
- marca visual (watermark/logo).  

Pendiente para cumplimiento alto:
- estandarizar redacción institucional,
- eliminar placeholders,
- alinear portada/presentación a formato final de entrega.

---

### 4) Riesgos de compilación (resumen técnico)
- **Seguro:** presentación truncada (`\se`).
- **Probable:** dependencia no garantizada de `template`.
- **Potencial:** ruta de imagen watermark/logo (`img/departamentos/UnADM.pdf`) si no existe.
- **Potencial:** comandos definidos en template que no estén cargados.

---

### 5) Veredicto de estado editorial
**Estado actual:** `En desarrollo (pre-entrega)`  
**Nivel de preparación estimado:** 55/100  
**Condición para pasar a “listo para actividad”:** resolver críticos A1–A3 + fortalecer bibliografía mínima de actividad.

---

Si deseas, en la siguiente acción te entrego un **plan de corrección en 10 pasos con orden de ejecución** y una **plantilla de control de calidad previa a compilación**.
