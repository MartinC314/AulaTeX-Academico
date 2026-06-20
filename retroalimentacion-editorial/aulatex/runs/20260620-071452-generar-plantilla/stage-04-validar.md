# AulaTeX stage

- Etapa: validar
- Rol: Verificador y validador
- Mision: verificar consistencia, compilacion y evidencias
- Motor: Codex
- Estado: ok

## Verificación editorial-técnica (ROL VERIFICADOR)

### 1) Checklist de defendibilidad académica y alineación institucional

- [x] **Identidad UnADM presente**  
  **Evidencia:** `\universityname`, `\facultyname`, `README.md` (semestre 2, bloque 1, obligatoria, 8 créditos).

- [x] **Alineación con programa analítico**  
  **Evidencia:** secciones en reporte: problema, desarrollo conceptual/normativo, análisis propio, conclusión transferible; coincide con `programa-analitico...md`.

- [x] **Supuesto explícito correctamente declarado**  
  **Evidencia:** comentario inicial “no se proporcionó consigna específica de Actividad 1”.

- [~] **Integridad académica (lista de fuentes verificables)**  
  **Evidencia:** `.bib` local con 2 fuentes institucionales.  
  **Riesgo:** cobertura mínima; faltan fuentes normativas/doctrinales específicas de la actividad real.

---

### 2) Compilabilidad LaTeX (reporte)

- [~] **Compilable condicionado a entorno local**  
  **Evidencia:** estructura estándar `article`, `\bibliography{derecho-a-la-seguridad-social}`, uso consistente de comandos.  
  **Riesgos latexmk:**
  1. Dependencia de archivo externo `template.tex` (`\input{template}`) no mostrado.
  2. Dependencia de recurso gráfico `img/departamentos/UnADM.pdf`.
  3. Uso de comandos no nativos (`abstractd`, `\templatePortrait`, etc.) que deben existir en `template`.
  4. Requiere BibTeX/Biber según plantilla madre (aquí parece BibTeX clásico).
  5. `\setcitestyle` exige paquete de citación compatible (probablemente `natbib` en `template`).

- [x] **Codificación y español**  
  **Evidencia:** clase con opción `spanish`; estilo coherente.

---

### 3) Compilabilidad LaTeX (presentación)

- [~] **Compilabilidad parcial por fragmento incompleto**  
  **Evidencia:** preámbulo beamer correcto hasta donde se ve.  
  **Riesgo crítico:** archivo compartido está truncado (`\setbeamercolor{normal text}{fg...`), por lo que **no se puede garantizar compilación** sin versión completa.

---

### 4) Cobertura bibliográfica

- [x] **Bib local existe y enlaza con reporte**  
  **Evidencia:** `derecho-a-la-seguridad-social.bib`; `\nocite{unadmSitioWeb,unadmMallaDerecho2024}`.

- [~] **Cobertura suficiente para plantilla base, no para entrega final**  
  **Riesgo:** para una Actividad 1 real, normalmente se requieren normas (CPEUM/LSS/LFT/criterios), doctrina y/o datos oficiales.  
  **Supuesto marcado:** al no haber consigna, la cobertura mínima institucional es defendible solo como “plantilla”.

---

### 5) Placeholders y campos pendientes

- [x] **Placeholders visibles y controlados**  
  **Evidencia:** `\pendiente{...}`, “Actividad X”, “Semana X”, “Nombre de la figura docente”.

- [~] **Riesgo de entrega accidental con marcadores**  
  **Acción recomendada:** regla de validación previa: búsqueda de `PENDIENTE`, `X`, `por definir`.

---

## Riesgos latexmk priorizados (semáforo)

- 🔴 **Alto:** `template.tex` faltante/incompatible.  
- 🔴 **Alto:** presentación truncada/incompleta.  
- 🟠 **Medio:** recurso `img/departamentos/UnADM.pdf` no encontrado.  
- 🟠 **Medio:** cadena de bibliografía (BibTeX vs Biber) no alineada al template real.  
- 🟡 **Bajo:** placeholders no sustituidos antes de entrega.

---

## Pruebas recomendadas (mínimas y rápidas)

1. **Smoke test reporte**  
   ```bash
   latexmk -pdf -interaction=nonstopmode -file-line-error reporte-derecho-a-la-seguridad-social.tex
   ```
2. **Smoke test presentación** (cuando esté completa)  
   ```bash
   latexmk -pdf -interaction=nonstopmode -file-line-error presentacion-derecho-a-la-seguridad-social.tex
   ```
3. **Prueba bibliografía**  
   - Verificar que se generen citas/referencias sin warnings “undefined citations”.
4. **Prueba de assets**  
   - Confirmar existencia de `template.tex` y `img/departamentos/UnADM.pdf`.
5. **Control de placeholders**  
   ```bash
   grep -RIn "PENDIENTE\|Actividad X\|Semana X\|por definir" .
   ```

---

## Dictamen del verificador

**Defendible:** Sí, como **plantilla base editable** de Actividad 1 con supuesto explícito.  
**Compilable:** **Parcialmente verificable**; reporte probablemente compila si existen dependencias (`template`, logo, cadena bib). Presentación no verificable hasta contar con archivo íntegro.  
**Recomendación de consenso:** aprobar con observaciones técnicas y ejecutar pruebas de compilación antes de publicar/entregar.
