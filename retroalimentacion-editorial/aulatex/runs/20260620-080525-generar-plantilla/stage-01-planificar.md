# AulaTeX stage

- Etapa: planificar
- Rol: Planificador editorial
- Mision: descomponer el objetivo en plan ejecutable y criterios de aceptacion
- Motor: Codex
- Estado: ok

## Plan breve por fases (Actividad 1 — Derecho a la Seguridad Social, UnADM)

### Fase 1. Delimitación e investigación
**Objetivo:** traducir la consigna real de la Actividad 1 a un problema jurídico concreto.  
**Acciones:**
1. Recuperar la consigna oficial (aula virtual) y el criterio de evaluación del docente.
2. Delimitar tema, pregunta jurídica y alcance (constitucional, legal, institucional, jurisprudencial).
3. Levantar fuentes verificables primarias:
   - CPEUM (art. 1º, 4º, 123 y correlativos).
   - LSS, LISSSTE.
   - Fuentes institucionales UnADM y, si aplica, SCJN/TCC.
4. Registrar citas en `.bib` sin inventar referencias.

**Salida esperada:** matriz breve de investigación (problema, normas, criterios, evidencia).

---

### Fase 2. Generación del borrador en plantilla
**Objetivo:** llenar `reporte-derecho-a-la-seguridad-social-Actividad-1.tex` con contenido académico evaluable.  
**Acciones:**
1. Sustituir todos los `\pendiente{}` por redacción propia.
2. Mantener estructura: introducción → marco jurídico → análisis → conclusión.
3. Integrar postura jurídica argumentada (no solo resumen normativo).
4. Citar en estilo `natbib` y vincular con `derecho-a-la-seguridad-social.bib`.

**Salida esperada:** versión 0.9 completa, sin marcadores pendientes.

---

### Fase 3. Compilación técnica
**Objetivo:** generar PDF limpio y trazable.  
**Acciones:**
1. Verificar cierre correcto del archivo (en contexto, aparece truncado en `\bibliog...`).
2. Completar bloque bibliográfico:
   - `\bibliography{derecho-a-la-seguridad-social}`  
3. Compilar (pdflatex + bibtex + pdflatex + pdflatex).
4. Corregir errores de rutas (logo, imágenes, `.bib`).

**Salida esperada:** PDF final sin errores de compilación ni referencias rotas.

---

### Fase 4. Evaluación de calidad y ajuste final
**Objetivo:** asegurar cumplimiento institucional y académico antes de entrega.  
**Acciones:**
1. Revisión contra rúbrica del docente.
2. Revisión jurídica (coherencia normativa + argumentación).
3. Revisión editorial (redacción formal, ortografía, formato UnADM).
4. Lista de verificación final (fuentes, citas, conclusiones aplicables).

**Salida esperada:** versión 1.0 entregable.

---

## Criterios de aceptación

### 1) Institución (UnADM)
- Formato académico formal y orden lógico.
- Evidencia de trabajo original y trazable.
- Entrega en tiempo y forma con bibliografía verificable.

### 2) Carrera (Lic. en Derecho)
- Problema jurídico claro.
- Fundamentación normativa correcta (jerarquía y vigencia).
- Argumentación jurídica propia, no descriptiva únicamente.

### 3) Materia (Derecho a la Seguridad Social)
- Cobertura de ejes mínimos: marco constitucional, IMSS/ISSSTE, principios (universalidad/progresividad/igualdad), y reto de justiciabilidad.
- Uso de fuentes legales vigentes.
- Conclusión vinculada al derecho a la seguridad social en México.

### 4) Actividad 1
- Responde exactamente a la consigna específica (faltante actual).
- Producto solicitado completo (ensayo/informe/cuadro/caso, según indique aula).
- Cumple extensión, estructura y criterios de evaluación del docente.

---

## Riesgos, faltantes, placeholders y errores bloqueantes

### Riesgos
- **R1:** desarrollar contenido sin la consigna exacta de Actividad 1.
- **R2:** análisis excesivamente descriptivo (sin postura jurídica).
- **R3:** desactualización normativa/jurisprudencial al momento de entrega.

### Faltantes de información
- No se proporcionó la **consigna oficial** ni **rúbrica específica** de Actividad 1.
- “Figura docente: Nombre por definir” pendiente de completar.
- No se confirmó extensión mínima/máxima requerida.

### Placeholders detectados
- `\pendiente{...}` en Introducción, Desarrollo, Análisis propio y Conclusión.
- Datos administrativos incompletos (figura docente).

### Errores bloqueantes
- El `.tex` mostrado está **incompleto al final** (`\bibliog...` truncado), lo que impide compilación.
- Posible error de ruta del logo: `img/departamentos/UnADM.pdf` (verificar existencia real).

---

## Supuestos explícitos
1. Se asume que la Actividad 1 exige un producto escrito tipo informe/ensayo jurídico.
2. Se asume uso de la bibliografía local como base mínima obligatoria.
3. Se asume que el entregable final es PDF compilado desde LaTeX.  

Si compartes la consigna exacta de la Actividad 1, te devuelvo el plan ajustado a rúbrica y una versión lista para llenar sección por sección.
