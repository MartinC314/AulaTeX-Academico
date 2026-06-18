# Memoria compartida AulaTeX

Propuestas:
- ## Plan breve por fases (ROL PLANIFICADOR)

**Supuesto explícito:** falta la consigna específica de la **Actividad 1** (pregunta guía, producto exacto y rúbrica detallada). Se planifica con base en la plantilla y pauta editorial disponibles.

---

### Fase 1. Investigación y encuadre
1. Confirmar datos marco: UnADM, Lic. en Derecho, semestre 1, bloque 1, materia obligatoria de 8 créditos.
2. Identificar en la planeación de semana el tema de Actividad 1 (si no está, marcar pendiente).
3. Delimitar problema jurídico-histórico inicial de la materia.
4. Levantar fuentes mínimas verificables:
   - Institucionales UnADM (sitio y malla).
   - Bibliografía específica de historia del derecho en México (a agregar al `.bib`).

**Salida:** ficha de encuadre + lista de fuentes candidatas.  
**Criterio de aceptación (fase):** no hay afirmaciones sin fuente o sin marca de supuesto.

---

### Fase 2. Ge
- ## Evaluación — Actividad 1 (ROL ARQUITECTO)
**Materia:** Historia del Derecho en México (LDE-S1B1)  
**Acción:** evaluar  
**Estado del repositorio:** **parcialmente listo** (base sólida, requiere cierre técnico-editorial)

---

### 1) Dictamen ejecutivo
La carpeta ya contiene una **estructura canónica correcta** (README, programa analítico, plantilla de reporte, plantilla de presentación, `.bib`).  
Sin embargo, para considerarla “lista para convertir a archivos” faltan ajustes críticos:

1. **Corregir errores de render en README** (rutas con caracteres rotos: `\reporte`, `\eferencias`).
2. **Completar presentación `.tex`** (está truncada en `\se`).
3. **Definir actividad 1 real** (reemplazar “Actividad X/Semana X” por metadatos concretos).
4. **Agregar pautas operativas evaluables** (rúbrica/checklist con criterios medibles).
5. **Fortalecer bibliografía disciplinar** (además de fuent

Riesgos:
- # Evaluación diagnóstica (Actividad 1)  
**Rol: Investigador**  
**Materia:** Historia del Derecho en México (UnADM, LDE-S1B1)  
**Acción:** Evaluar identidad institucional, programa analítico, bibliografía, estructura local, activos visuales y riesgos de trazabilidad.

---

## 1) Estado general (síntesis ejecutiva)

La base editorial está **bien encaminada**: existe README, programa analítico, plantilla de reporte, plantilla de presentación y archivo `.bib` local.  
Sin embargo, hay **riesgos críticos de trazabilidad y compilación** que deben atenderse antes de producir entregables formales.

---

## 2) Hallazgos priorizados

## Prioridad alta (crítico)

1. **Errores de nombres/rutas en README (integridad de estructura).**  
   Se observan entradas corruptas:
   - `eporte-historia-del-derecho-en-mexico.tex` (falta “r”)
   - `eferencias-historia-del-derecho-en-mexico/` (falta “r”)
   - N
- ## Evaluación verificadora (defendible y compilable)

### 1) Checklist de compilabilidad LaTeX (con evidencia)

- [x] **Estructura mínima del reporte está completa**  
  **Evidencia:** `\documentclass...`, `\begin{document}`, `\end{document}`, bibliografía y secciones presentes en `reporte-historia-del-derecho-en-mexico.tex`.

- [x] **Bibliografía enlazada correctamente en el reporte**  
  **Evidencia:** `\bibliography{historia-del-derecho-en-mexico}` coincide con archivo `.bib` existente.

- [x] **Citas forzadas para poblar referencias**  
  **Evidencia:** `\nocite{unadmSitioWeb,unadmMallaDerecho2024}` usa claves existentes en `.bib`.

- [!] **Dependencia crítica externa: `template`**  
  **Evidencia:** `\input{template}`. Si `template.tex` no está en ruta, falla inmediata de compilación.

- [!] **Dependencia crítica de imagen para marca de agua**  
  **Evidencia:** `img/departamentos/U
- ## Evaluación crítica adversarial — Actividad 1 (nivel materia)  
**Estado del flujo:** revisión documental inicial completada  
**Supuesto explícito:** no se recibió la parte final completa de `presentacion-historia-del-derecho-en-mexico.tex` (el contenido quedó truncado en `\se`), por lo que esa evaluación es **parcial**.

---

### 1) Hallazgos bloqueantes (deben corregirse antes del siguiente ciclo)

1. **Error de estructura en `README.md` (nombres de archivo corruptos)**
   - Aparecen rutas con caracteres extraños/salto:  
     - `eporte-historia-del-derecho-en-mexico.tex`  
     - `eferencias-historia-del-derecho-en-mexico/`
   - Impacto: rompe trazabilidad editorial y automatizaciones de indexado.

2. **Placeholder no resuelto en `README.md` y programa analítico**
   - Se muestra literal:  
     - `$(@{Name=Historia del Derecho en Mexico; ...}.Slug).bib`
   - Impacto: inconsistenci