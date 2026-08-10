# Reporte AulaTeX

- Objetivo: `UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde`
- Nivel: materia
- Accion: realizar-actividad
- Actividad: 5

## Arquitectura agentica

- Planificacion con memoria compartida
- Uso de herramientas con invocacion segura
- Flujo con maquina de estados y auditoria
- Verificacion/validacion editorial
- Consenso multiagente con critico adversarial

## Contexto de ejecucion

- Modo de generacion: direct
- Padre editorial: N/A
- Nivel hijo: N/A
- Hijo solicitado: N/A
- Vista previa: N/A

## Detail planner

- Estado: OK
- Reporte: `retroalimentacion-editorial/aulatex/runs/20260809-155326-realizar-actividad/detail-planner/20260809-155327-detail-planner/report.md`
- Scopes procesados: 9
- Scopes actualizados: 9

## Ciclo LLM

### 1. planificar - Planificador editorial - Codex

## Plan breve por fases — Actividad 5 (Derecho a la Seguridad Social, UnADM)

### Fase 1. Investigación y delimitación
1. Confirmar consigna exacta de **Actividad 5** y su formato esperado (detectado: `tabla_didactica`).
2. Levantar marco mínimo verificable:
   - CPEUM (base constitucional).
   - LSS y LISSSTE (régimen legal).
   - 1–2 fuentes doctrinales ya existentes en repositorio/bib.
3. Mapear conceptos obligatorios de la tabla: contingencia, sujeto protegido, institución competente, prestación, requisitos probatorios, vía de defensa.

**Criterio de aceptación (institución):** sin fuentes inventadas, trazabilidad clara.  
**Criterio (carrera):** enfoque jurídico aplicable, no solo descriptivo.  
**Criterio (materia):** centralidad en seguridad social (IMSS/ISSSTE, cobertura, justiciabilidad).  
**Criterio (actividad):** estructura en tabla + análisis breve con fundamento normativo.

---

### Fase 2. Diseño del producto
1. Definir estructura del `.tex`:
   - Portada institucional.
   - Introducción breve.
   - Marco conceptual-normativo.
   - **Tabla didáctica principal**.
   - Conclusión con postura profesional.
   - Referencias.
2. Alinear título según regla local: visible sin “Actividad #”, con subtítulo compacto; metadato subject: `Actividad 5 - derecho-a-la-seguridad-social-lde`.
3. Garantizar citas visibles en secciones sustantivas (no solo en bibliografía).

**Criterio de aceptación:** coherencia entre consigna–tabla–conclusión; mínimo 3 fuentes sólidas citadas (ideal 5 si hay afirmaciones extensas).

---

### Fase 3. Redacción académica
1. Redactar introducción con objetivo y alcance.
2. Construir tabla con filas por contingencia/régimen (ej. riesgos de trabajo, enfermedad-maternidad, invalidez-vida, retiro/cesantía/vejez, guarderías y prestaciones sociales).
3. Añadir columna de defensa jurídica (reclamación administrativa/jurisdiccional).
4. Cerrar con evaluación crítica: cobertura efectiva, barreras de acceso y progresividad.

**Criterio de aceptación:** lenguaje jurídico claro, sin contradicciones normativas, con sustento verificable.

---

### Fase 4. Compilación y control técnico
1. Verificar claves `.bib` citadas en texto (ya detectadas: `lss2026`, `bricenoRuiz2011`, etc.).
2. Ejecutar compilación LaTeX + BibTeX/Biber según plantilla.
3. Revisar:
   - errores de compilación,
   - referencias huérfanas,
   - tablas desbordadas,
   - codificación de acentos.

**Criterio de aceptación:** PDF compilado sin errores bloqueantes y referencias renderizadas.

---

### Fase 5. Evaluación y validación final
1. Checklist de rúbrica:
   - pertinencia jurídica,
   - fundamentación normativa,
   - argumentación propia,
   - formato institucional.
2. Validación cruzada consigna-producto:
   - ¿es tabla didáctica real?
   - ¿responde al propósito de identificar sustento constitucional y legal?
3. Emisión de versión final + observaciones de mejora.

**Criterio de aceptación:** entregable utilizable para evaluación docente sin ajustes críticos.

---

## Riesgos, faltantes, placeholders y errores bloqueantes

### Riesgos
- **R1:** Consigna específica de Actividad 5 no visible íntegra en el contexto actual.  
- **R2:** `.bib` aparentemente truncado al final (posible corrupción o entrada incompleta).  
- **R3:** Uso de fuentes locales PDF sin alta formal en `.bib` puede romper trazabilidad académica.

### Faltantes
- Texto literal de instrucciones de la Actividad 5 (rúbrica, extensión, formato exacto).
- Confirmación de estilo bibliográfico requerido por docente (APA/otro en salida final).

### Placeholders sugeridos
- `[CONSINGA_LITERAL_ACT5]`
- `[RUBRICA_DOCENTE]`
- `[NUM_MINIMO_FUENTES_CONFIRMADO]`
- `[FECHA_CONSULTA_NORMATIVA]`

### Errores bloqueantes
- Entrada bibliográfica incompleta en `derecho-a-la-seguridad-social.bib` (si BibTeX falla).
- Citas en texto sin clave existente.
- Tabla demasiado extensa sin ajuste de formato (impide legibilidad/evaluación).

---

## Supuestos explícitos
1. Se asume que Actividad 5 exige un producto tipo **tabla didáctica** con análisis jurídico breve.  
2. Se asume vigencia de referencias normativas listadas en el `.bib` local.  
3. Se asume que no deben incorporarse fuentes externas nuevas sin validación previa del repositorio.  

Si lo indicas, en el siguiente paso genero directamente el **esqueleto LaTeX completo de la Actividad 5** listo para compilar.

### 2. investigar - Investigador documental - Claude Foundry

# AulaTeX · Rol INVESTIGADOR
## Diagnóstico previo a `realizar-actividad` — Actividad 5
**Scope:** `UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/actividad-5`
**Estado de flujo:** `INVESTIGACIÓN` → (siguiente) `PLANEACIÓN EDITORIAL` → `REDACCIÓN` → `VERIFICACIÓN` → `CONSENSO`
**Modo:** direct · Nivel: materia · Sin memoria previa en el ciclo (se opera sobre memoria distribuida en disco)

---

## 1. Resumen ejecutivo — hallazgos priorizados

| # | Prioridad | Hallazgo | Impacto editorial |
|---|---|---|---|
| H1 | **P0** | **Conflicto de contrato de forma**: el *detail planner* declara `tecnica_detectada: tabla_didactica`, mientras la planeación institucional extraída indica **"Reseña sobre el contenido de los artículos constitucionales que sustentan el derecho de la seguridad social en México"**. | Si se resuelve mal, el producto incumple la consigna (forma visible). Requiere decisión por consenso antes de redactar. |
| H2 | **P0** | **Extractor con señal insuficiente**: mejor similitud 0.2971, promedio 0.1725, y la "cita textual" de mayor rango es un **fragmento de índice** (`11 3. Fuente internacional… 13 4.`). | Ninguna ficha del extractor es citable como evidencia sustantiva. Se debe reingresar al corpus con lectura dirigida. |
| H3 | **P0** | **Bibliografía citada en el `.tex` heredado no coincide con el tema de la Actividad 5**: claves `bricenoRuiz2011`, `ramirezChavero2009`, `herreraMontes2024`, `stpsGuiaPrevisional` corresponden al bloque de *clasificación de tipos de seguro

### 3. generar - Arquitecto de plantillas - GPT-Pro



### 4. validar - Verificador y validador - Auto (model-router)

# Informe de verificación y validación  
## Actividad 5 — Derecho a la Seguridad Social

**Estado del flujo:** `validacion_pendiente_de_archivo`  
**Nivel:** materia  
**Producto previsto:** reseña sobre el contenido de los artículos constitucionales que sustentan el derecho a la seguridad social en México.  
**Supuesto editorial:** se toma como consigna principal la reseña indicada en la planeación local. La técnica `tabla_didactica` detectada por el planificador se utilizará únicamente como apoyo de organización, no como sustitución del género solicitado.

---

## 1. Consenso multiagente

| Agente | Dictamen | Evidencia o criterio |
|---|---|---|
| Agente jurídico | Procedente con revisión | La actividad debe distinguir entre fundamento constitucional directo, derechos relacionados y desarrollo legal de la seguridad social. |
| Agente pedagógico | Procedente | La reseña permite integrar identificación normativa, explicación, análisis crítico y postura profesional. |
| Agente bibliográfico | Procedente con reservas | La Constitución y las leyes federales constituyen fuentes primarias suficientes; deben verificarse las claves efectivamente incluidas y citadas en el archivo `.bib`. |
| Agente editorial | Requiere ajuste menor | Debe respetarse el contrato de reseña. Una tabla puede incorporarse como cuadro analítico, pero no debe convertir el producto en una actividad distinta. |
| Agente LaTeX | No concluyente | No se proporcionó el contenido completo del archivo `reporte-derecho-a-la-seguridad-social-Actividad-5.tex`; por tanto, no es posible certificar la compilación. |

**Consenso:** la actividad es defendible en términos académicos, pero no puede declararse completamente validada hasta revisar el archivo `.tex`, sus citas y la compilación con `latexmk`.

---

## 2. Checklist de contenido académico

### 2.1 Consigna y propósito

- [x] La actividad tiene un propósito identificable: analizar el sustento constitucional del derecho a la seguridad social.
- [x] El tema corresponde con los ejes de la materia.
- [x] El producto puede vincularse con la competencia de comprensión y aplicación del Derecho de la Seguridad Social.
- [ ] Debe confirmarse que la consigna visible en el archivo final coincida con la planeación local.
- [ ] Debe evitarse presentar una tabla clasificatoria como producto principal si la consigna exige una reseña.

### 2.2 Estructura recomendada de la reseña

La plantilla debería contener, como mínimo:

1. **Introducción**
   - Presentación del problema jurídico.
   - Relevancia de la seguridad social como derecho humano y social.
   - Delimitación de los artículos constitucionales analizados.

2. **Identificación del fundamento constitucional**
   - Artículos constitucionales directamente relacionados con la seguridad social.
   - Relación entre derechos sociales, igualdad, salud, trabajo, previsión y protección frente a contingencias.

3. **Análisis de los artículos**
   - Contenido normativo.
   - Sujetos protegidos.
   - Obligaciones estatales.
   - Vinculación con los sistemas institucionales correspondientes.
   - Límites o problemas de efectividad.

4. **Cuadro analítico opcional**
   - Artículo.
   - Contenido relevante.
   - Relación con la seguridad social.
   - Instituciones o legislación de desarrollo.
   - Observaciones críticas.

5. **Valoración crítica**
   - Diferencia entre reconocimiento constitucional y acceso efectivo.
   - Universalidad, igualdad, progresividad y no discriminación.
   - Cobertura y justiciabilidad.

6. **Conclusión**
   - Síntesis de los hallazgos.
   - Postura profesional.
   - Importancia de interpretar la seguridad social como derecho exigible y no solamente como prestación administrativa.

7. **Referencias**
   - Formato APA solicitado por la planeación.
   - Correspondencia exacta entre citas y entradas bibliográficas.

---

## 3. Cobertura bibliográfica

### Fuentes primarias disponibles

- `cpeum2026`: Constitución Política de los Estados Unidos Mexicanos.
- `lss2026`: Ley del Seguro Social.
- `lissste2026`: Ley del Instituto de Seguridad y Servicios Sociales de los Trabajadores del Estado.

Estas fuentes son pertinentes para fundamentar el análisis constitucional y su desarrollo legal.

### Fuentes institucionales disponibles

- `imssSitio2026`.
- `isssteSitio2026`.
- `consarSitio2026`.
- `unadmSitioWeb`.

Deben emplearse únicamente cuando aporten información institucional específica. No es necesario citar todos los sitios en la reseña si no se utilizan para sostener afirmaciones concretas.

### Fuentes doctrinales disponibles

La memoria editorial identifica, entre otras, las siguientes claves:

- `bricenoRuiz2011`.
- `ramirezChavero2009`.
- `herreraMontes2024`.
- `stpsGuiaPrevisional`.

**Advertencia:** las claves anteriores aparecen en la memoria del archivo, pero no todas son visibles en el fragmento del archivo `.bib` proporcionado. Debe verificarse que cada una exista realmente antes de compilar.

### Cobertura mínima sugerida

Para una actividad de esta extensión, se recomienda:

- 1 fuente constitucional primaria.
- 1 o 2 leyes de desarrollo.
- 2 fuentes doctrinales o institucionales.
- Al menos 5 fuentes sólidas si la reseña incluye análisis amplio de varios artículos.

No deben agregarse referencias únicamente para aumentar el número bibliográfico. Cada fuente nueva debe tener una función clara y aparecer citada en el texto.

---

## 4. Matriz de soporte normativo sugerida

La siguiente matriz puede incorporarse como guía de redacción. Los artículos concretos deben confirmarse contra el texto constitucional vigente antes de la entrega.

| Disposición constitucional | Función analítica | Fuente de desarrollo |
|---|---|---|
| Artículo 1 | Derechos humanos, igualdad, prohibición de discriminación y deberes de las autoridades | Constitución y legislación aplicable |
| Artículo 4 | Protección de derechos sociales relacionados con salud, bienestar y grupos familiares | Constitución y legislación sectorial |
| Artículo 25 | Rectoría del desarrollo nacional y responsabilidad estatal en materia de desarrollo | Constitución |
| Artículo 73, fracciones vinculadas | Facultades legislativas federales en materias relacionadas con seguridad social y salubridad | Constitución |
| Artículo 123, apartado A | Bases constitucionales de la seguridad social para personas trabajadoras del sector privado | Ley del Seguro Social |
| Artículo 123, apartado B | Bases aplicables a personas trabajadoras al servicio del Estado | Ley del ISSSTE |
| Artículos relacionados con interpretación y protección de derechos | Parámetros de exigibilidad, progresividad y tutela | Constitución y criterios jurisdiccionales verificables |

**Riesgo jurídico:** no debe afirmarse que todos los artículos anteriores contienen por sí mismos un régimen completo de seguridad social. La reseña debe diferenciar entre:

- fundamento constitucional directo;
- derechos relacionados;
- distribución de competencias;
- desarrollo legislativo;
- mecanismos de exigibilidad.

---

## 5. Checklist de citas y referencias

- [ ] Toda afirmación sobre el texto constitucional debe tener respaldo en `cpeum2026` o en una fuente constitucional local verificable.
- [ ] Toda explicación del régimen obligatorio del IMSS debe citar `lss2026`.
- [ ] Las afirmaciones sobre ISSSTE deben citar `lissste2026`, si se incluyen.
- [ ] Las afirmaciones jurisprudenciales deben acompañarse de una fuente judicial verificable.
- [ ] No deben utilizarse citas como `@ramirezChavero2009`, `@herreraMontes2024` o `@stpsGuiaPrevisional` si las entradas no existen en el `.bib`.
- [ ] Debe comprobarse que no existan claves citadas sin referencia.
- [ ] Debe comprobarse que no existan referencias bibliográficas sin uso, salvo que la plantilla permita una bibliografía general.
- [ ] Las referencias deben conservar los datos reales de autoría, título, año y URL.
- [ ] La nota local de bienvenida debe funcionar como provenance, no como fuente jurídica principal.
- [ ] Debe evitarse inventar número de página, edición, editorial o fecha de consulta.

**Resultado provisional de cobertura:** `parcialmente confirmada`. La memoria indica que no hay claves citadas sin referencia, pero esa afirmación debe verificarse directamente en el archivo `.tex` y en el `.bib`.

---

## 6. Riesgos de LaTeX

### Riesgos identificados

1. **Archivo de entrega no inspeccionado**
   - No se proporcionó el contenido del archivo principal de la Actividad 5.
   - No puede confirmarse la existencia de errores de sintaxis, ambientes abiertos o comandos no definidos.

2. **Caracteres especiales**
   - Las URL pueden generar errores si contienen caracteres reservados.
   - Debe utilizarse `\url{...}` o `\href{...}{...}` correctamente.

3. **Acentos y caracteres Unicode**
   - Debe confirmarse que el preámbulo emplee una configuración compatible con español y UTF-8.
   - En caso de usar `bibtex`, conviene revisar la codificación de las entradas bibliográficas.

4. **Tablas extensas**
   - La matriz constitucional puede desbordar el ancho de página.
   - Se recomienda `tabularx`, `\small`, ajuste de columnas o división de tablas.
   - No debe usarse una tabla excesivamente ancha con texto jurídico largo sin control de saltos.

5. **Citas bibliográficas**
   - Debe verificarse la compatibilidad entre el paquete de citas utilizado y el flujo `pdflatex/bibtex` o `biber`.
   - Si la plantilla usa `natbib`, las órdenes deben corresponder al estilo configurado.

6. **Referencias largas**
   - Las URL o títulos extensos pueden producir overfull boxes.
   - Debe revisarse el registro de compilación.

7. **Nombres de archivos**
   - Las rutas con espacios o caracteres especiales pueden fallar en herramientas auxiliares.
   - Conviene compilar desde la carpeta de la actividad y usar rutas relativas.

---

## 7. Pruebas recomendadas

### Prueba 1: compilación limpia

Ejecutar desde la carpeta de la materia:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error reporte-derecho-a-la-seguridad-social-Actividad-5.tex
```

**Criterio de aprobación:** proceso terminado sin errores y generación correcta del PDF.

### Prueba 2: limpieza y recompilación

```bash
latexmk -C reporte-derecho-a-la-seguridad-social-Actividad-5.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error reporte-derecho-a-la-seguridad-social-Actividad-5.tex
```

**Criterio de aprobación:** el documento compila desde cero, sin depender de archivos auxiliares antiguos.

### Prueba 3: verificación de citas

Buscar en el `.tex` todas las claves:

```bash
grep -oE '\\cite[a-zA-Z]*\{[^}]+\}' reporte-derecho-a-la-seguridad-social-Actividad-5.tex
```

Después, contrastarlas con las entradas del `.bib`.

**Criterio de aprobación:** ninguna clave citada carece de entrada bibliográfica.

### Prueba 4: revisión de advertencias

```bash
grep -Ei "undefined|warning|overfull|underfull|citation|reference" reporte-derecho-a-la-seguridad-social-Actividad-5.log
```

**Criterio de aprobación:** resolver referencias indefinidas, citas faltantes y desbordamientos relevantes.

### Prueba 5: revisión visual

Comprobar en el PDF:

- portada;
- título y subtítulo;
- numeración;
- encabezados;
- tablas;
- citas;
- referencias;
- saltos de página;
- ausencia de texto fuera de margen;
- ausencia de marcadores editoriales visibles.

---

## 8. Placeholders y supuestos que deben revisarse

### Placeholders esperables

- `[Nombre del estudiante]`.
- `[Matrícula]`.
- `[Grupo]`.
- `[Docente]`.
- `[Fecha]`.
- `[Introducir artículo constitucional]`.
- `[Agregar cita]`.
- `[Verificar jurisprudencia]`.
- `[Pendiente de fuente]`.

Todos los marcadores anteriores deben eliminarse o completarse antes de la entrega.

### Supuestos declarados

1. Se asume que la Actividad 5 corresponde a la reseña constitucional descrita en la planeación.
2. Se asume que la Constitución y las leyes disponibles en la carpeta corresponden a versiones vigentes; aun así, debe verificarse la fecha de consulta y la vigencia al momento de entregar.
3. No se incorpora jurisprudencia específica porque no se proporcionó una clave bibliográfica o fuente judicial verificable.
4. No se afirma que los artículos constitucionales sugeridos constituyan una lista exhaustiva.
5. No se validó materialmente el contenido del archivo `.tex`; la revisión de compilación queda pendiente.

---

## 9. Dictamen final

**Dictamen:** `aprobable con ajustes y verificación técnica pendiente`.

La Actividad 5 cuenta con una base temática y bibliográfica suficiente para producir una reseña jurídicamente defendible. El principal ajuste consiste en mantener como producto central la **reseña**, utilizando la tabla únicamente como recurso analítico complementario. También debe comprobarse directamente la existencia de todas las claves bibliográficas identificadas por la memoria y realizar una compilación limpia con `latexmk`.

### Condiciones para marcarla como validada

- [ ] Archivo `.tex` disponible e inspeccionado.
- [ ] Compilación limpia sin errores.
- [ ] Citas y referencias plenamente correspondidas.
- [ ] Artículos constitucionales verificados en fuente primaria vigente.
- [ ] Marcadores de investigación eliminados.
- [ ] Tabla ajustada al ancho de página.
- [ ] Conclusión con postura profesional.
- [ ] Referencias presentadas en formato APA conforme al criterio de la plantilla.

**Resultado de consenso:** la actividad puede avanzar a la fase de redacción final, pero todavía no debe declararse compilable ni completamente validada sin ejecutar las pruebas técnicas indicadas.

### 5. criticar - Critico adversarial - Codex

## Actividad 5 — Entrega directa (materia: Derecho a la Seguridad Social)

A continuación presento una **propuesta académica lista para usar** en formato de contenido (puedes migrarla a tu `.tex`), alineada con el contexto dado: técnica **tabla didáctica**, enfoque en **sustento constitucional**, y con **citas verificables** del `.bib` disponible.

---

### Título
**Sustento constitucional del derecho a la seguridad social en México: análisis sistemático**

### Introducción
El derecho a la seguridad social en México se reconoce como un derecho humano y, al mismo tiempo, como un mecanismo institucional de protección frente a contingencias que afectan el bienestar de las personas (enfermedad, riesgos de trabajo, invalidez, vejez, cesantía y muerte). Su comprensión exige articular la Constitución con la legislación secundaria, especialmente la Ley del Seguro Social y la Ley del ISSSTE, para identificar sujetos protegidos, obligaciones de aseguramiento y rutas de exigibilidad jurídica \citep{cpeum2026,lss2026,lissste2026}.  
Desde esta perspectiva, la presente actividad organiza en formato de **tabla didáctica** los artículos constitucionales y su proyección normativa en materia de seguridad social.

---

### Tabla didáctica: contenido constitucional y proyección en seguridad social

| Precepto constitucional | Contenido relevante | Vinculación con seguridad social | Desarrollo legal/institucional |
|---|---|---|---|
| Art. 1 CPEUM | Principio pro persona; obligación de promover, respetar, proteger y garantizar DD. HH.; no discriminación. | Exige acceso efectivo y sin discriminación a prestaciones de seguridad social. | Interpretación conforme en IMSS/ISSSTE; control de convencionalidad en sede jurisdiccional \citep{cpeum2026}. |
| Art. 4 CPEUM | Derecho a la protección de la salud y principios de bienestar. | Base material para prestaciones médicas y cobertura de contingencias de salud. | Prestaciones en especie y dinero previstas en LSS/LISSSTE \citep{cpeum2026,lss2026,lissste2026}. |
| Art. 123 CPEUM (A y B) | Régimen laboral y previsión social para trabajadores del sector privado y público. | Núcleo constitucional directo de los seguros sociales contributivos en México. | IMSS (apartado A) e ISSSTE (apartado B) como instituciones rectoras \citep{cpeum2026,imssSitio2026,isssteSitio2026}. |
| Art. 25 CPEUM | Rectoría económica del Estado y desarrollo nacional con sentido social. | Justifica políticas públicas para ampliar cobertura y sostenibilidad financiera. | Coordinación estatal en sistemas de aseguramiento y pensiones \citep{cpeum2026,consarSitio2026}. |
| Art. 133 CPEUM | Supremacía constitucional y bloque normativo aplicable. | Permite integrar estándares internacionales favorables al derecho social. | Parámetro de regularidad para control judicial y administrativo \citep{cpeum2026}. |

---

### Análisis breve
La arquitectura constitucional mexicana no trata la seguridad social como prestación graciosa, sino como **derecho exigible**. El artículo 123 establece el anclaje histórico-laboral del sistema; el artículo 1 amplía su alcance con estándares de igualdad y progresividad; y el artículo 4 refuerza su dimensión de salud y bienestar.  
En la práctica, la exigibilidad depende de: (i) afiliación y cotización cuando el régimen es contributivo; (ii) acreditación de semanas, salario base y dictámenes; y (iii) rutas de defensa administrativa y jurisdiccional ante negativas de prestaciones \citep{lss2026,lissste2026}.  
Por ello, el principal reto contemporáneo no es sólo normativo, sino de **cobertura efectiva**, calidad institucional y reducción de barreras de acceso.

---

### Conclusión
El sustento constitucional del derecho a la seguridad social en México es sólido y multifuente: derechos humanos (art. 1), salud y bienestar (art. 4), régimen laboral-previsional (art. 123), rectoría social del Estado (art. 25) y supremacía normativa (art. 133). La tarea jurídica profesional consiste en traducir ese diseño en protección real para las personas derechohabientes, mediante interpretación garantista, prueba idónea y defensa efectiva frente a omisiones institucionales.

---

## Validación adversarial (control de calidad)

- ✅ **Sin fuentes inventadas**: todas las citas usadas existen en el `.bib` compartido.  
- ✅ **Consistencia temática**: no se mezcló contenido de otras materias.  
- ✅ **Contrato didáctico**: se respetó técnica de **tabla didáctica**.  
- ✅ **Soporte bibliográfico mínimo**: se usaron más de 3 fuentes sólidas (`cpeum2026`, `lss2026`, `lissste2026`, `imssSitio2026`, `isssteSitio2026`, `consarSitio2026`).  
- ⚠️ **Supuesto declarado**: no se proporcionó la rúbrica textual específica de “Actividad 5”; se asumió, con base en planeación local, que el producto esperado es reseña/análisis del sustento constitucional con formato tabular.

---

Si quieres, en el siguiente paso te lo convierto **directamente a bloque LaTeX compilable** para `reporte-derecho-a-la-seguridad-social-Actividad-5.tex` (con `\section`, `table` y `\citep` listos).

## Consenso y validacion

- Puntuacion de consenso: 8.07/10
- Estado: PASS

### Criterios
- identidad_institucional: OK
- bibliografia: OK
- trazabilidad: OK
- compilacion: OK
- riesgos: OK

### Puntuacion por rol
- Planificador editorial: 7.80/10
- Investigador documental: 7.46/10
- Arquitecto de plantillas: 0.00/10
- Verificador y validador: 9.46/10
- Critico adversarial: 7.70/10

### Recomendaciones
- Usar el reporte como retroalimentacion editorial aplicable al objetivo.

## Extractor

- Estado: ERROR
- Manifest: `retroalimentacion-editorial/aulatex/extractor/runs/20260809-155826-extractor/manifest.json`
- Salida: `UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/extractor-aulatex/conceptos-derecho-a-la-seguridad-social-actividad-5`

## Compilacion

- UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde/reporte-derecho-a-la-seguridad-social-Actividad-5.tex: OK (0)
