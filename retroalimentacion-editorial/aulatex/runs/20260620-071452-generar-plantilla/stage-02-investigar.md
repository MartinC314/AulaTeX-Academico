# AulaTeX stage

- Etapa: investigar
- Rol: Investigador documental
- Mision: detectar fuentes, contexto curricular y faltantes editoriales
- Motor: Codex
- Estado: ok

### Diagnóstico editorial (Rol Investigador) — **Derecho a la seguridad social (LDE-S2B1, UnADM)**

## 1) Hallazgos prioritarios (alto impacto)

1. **Identidad institucional bien anclada**
   - Se confirma adscripción a **UnADM**, **Licenciatura en Derecho**, **Semestre 2 / Bloque 1**, **Obligatoria**, **8 créditos** (README + malla referida).
   - Código de curso consistente en plantillas: **LDE-S2B1**.

2. **Programa analítico editorial claro y reutilizable**
   - Ejes definidos: problema jurídico/social, conceptos/fuentes, producto, análisis propio, conclusión transferible.
   - Enfoque metodológico compatible con entregables académicos de reporte y presentación.

3. **Plantillas LaTeX base ya funcionales**
   - Existe `reporte-...tex` con portada institucional, checklist editorial, estructura sugerida y bibliografía.
   - Existe `presentacion-...tex` (beamer) con paleta, metadatos y estructura visual institucional.

4. **Riesgo de trazabilidad de fuentes (crítico)**
   - `.bib` local contiene solo 2 entradas institucionales (sitio UnADM + malla curricular).
   - Para actividades reales faltarán **normas, jurisprudencia, doctrina y fuentes temáticas** de seguridad social.
   - Si no se amplía el `.bib`, habrá debilidad de verificabilidad académica.

---

## 2) Identidad institucional: estado

**Fortalezas**
- Consistencia nominal: asignatura, programa, universidad.
- Pauta editorial explícita: integridad académica, citas verificables, conclusión jurídica propia.
- Uso de marca visual UnADM (logos/watermark).

**Riesgos**
- Campos aún genéricos: “Actividad X”, “Semana X”, “Nombre por definir”.
- Ubicación “Roma Norte, Ciudad de México” podría ser decorativa; **supuesto**: no necesariamente dato institucional obligatorio en todas las entregas.

---

## 3) Programa analítico: alineación operativa

**Cobertura adecuada**
- El programa sirve como “marco maestro” para convertir consignas semanales en productos.
- La plantilla de reporte replica esa lógica (introducción-desarrollo-producto-postura-conclusión).

**Brecha detectada**
- Actividad 1 no trae consigna específica en el insumo actual.  
  **Supuesto explícito válido:** generar plantilla base editable alineada al programa analítico.

---

## 4) Bibliografía y control de evidencia

**Estado actual**
- Archivo: `derecho-a-la-seguridad-social.bib`.
- Entradas mínimas institucionales correctas, pero insuficientes para análisis jurídico sustantivo.

**Riesgos de trazabilidad**
- Posible texto argumentativo sin respaldo especializado.
- Dificultad para auditoría de citas si no se normaliza captura de metadatos (autor, año, fuente, URL/DOI, fecha de consulta).

**Prioridad recomendada**
- Crear bloque inicial de referencias canónicas de seguridad social (leyes, reglamentos, criterios jurisdiccionales, organismos).

---

## 5) Estructura local y activos visuales

**Estructura**
- Carpeta contiene los artefactos esperados: README, programa analítico, reporte, presentación, `.bib`, carpeta de referencias.
- Diseño modular adecuado para flujo editorial por actividad.

**Activos visuales**
- Referencias a `img/departamentos/UnADM.pdf` y `departamentos/UnADM`.
- **Riesgo técnico**: rutas relativas podrían fallar si se compila desde otro directorio o en CI.

---

## 6) Riesgos técnicos y editoriales (priorizados)

1. **(Alto)** Bibliografía temática insuficiente.
2. **(Alto)** Marcadores pendientes no resueltos (docente, actividad, semana, conclusión).
3. **(Medio)** Posibles errores de compilación por rutas de imagen/plantilla (`template`, logos).
4. **(Medio)** Inconsistencias menores visibles en listado de estructura del README (saltos/ruido tipográfico).
5. **(Bajo-Medio)** Año fijo en fuente web (2026) requerirá mantenimiento periódico.

---

## 7) Veredicto de diagnóstico

La base editorial está **bien encaminada y coherente con UnADM**, pero para trazabilidad académica robusta en la Actividad 1 se debe cerrar, como mínimo:
- metadatos pendientes de la entrega,
- ampliación del `.bib` con fuentes específicas de seguridad social,
- validación de rutas de activos para compilación reproducible.

Si quieres, en el siguiente paso te devuelvo una **plantilla Actividad 1 ya “lista para llenar”** (reporte + diapositivas) con campos de control, checklist de evidencias y bloque BibTeX mínimo sugerido.
