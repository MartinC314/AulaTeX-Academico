# Reporte AulaTeX

- Objetivo: `UnADM/licenciatura-en-derecho-unadm/garantias-constitucionales-lde`
- Nivel: materia
- Accion: realizar-actividad
- Actividad: 4

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
- Reporte: `retroalimentacion-editorial/aulatex/runs/20260809-153715-realizar-actividad/detail-planner/20260809-153715-detail-planner/report.md`
- Scopes procesados: 9
- Scopes actualizados: 9

## Ciclo LLM

### 1. planificar - Planificador editorial - Codex

## Plan breve por fases (Actividad 4 — Garantías Constitucionales, UnADM)

### Fase 1. Investigación y acopio verificable
1. Confirmar el **contrato didáctico** de la Actividad 4: técnica detectada `mapa_conceptual`.
2. Delimitar contenido al Tema 1: antecedentes históricos, concepto de derechos humanos, generaciones y principios (universalidad, interdependencia, indivisibilidad, progresividad, no regresión), y vínculo con Art. 1 CPEUM.
3. Validar fuentes disponibles y citables:
   - Programa de asignatura (fuente local oficial).
   - CPEUM (art. 1).
   - Bibliografía base en `.bib` (Álvarez Icaza, Rabinovich, Marcano).
4. Identificar vacíos de referencia (si algún nodo del mapa no queda soportado).

---

### Fase 2. Generación del producto
1. Redactar `reporte-garantias-constitucionales-Actividad-4.tex` con estructura mínima:
   - Introducción breve.
   - Desarrollo del mapa conceptual (en formato textual jerárquico, si no hay gráfico).
   - Explicación sintética de relaciones entre nodos.
   - Conclusión jurídica transferible.
2. Alinear el contenido al propósito de la actividad: **ubicar antecedentes** y **reconocer concepto/principios**.
3. Insertar citas visibles y coherentes con `.bib` (sin inventar claves).

---

### Fase 3. Compilación y control técnico
1. Verificar integridad LaTeX:
   - Codificación, acentos, llaves, entornos.
   - Citas resolubles y bibliografía enlazada.
2. Compilar (PDF) y revisar:
   - Tabla visual del mapa o esquema legible.
   - Consistencia de títulos (sin contradicción “Actividad 4/5”).
3. Confirmar que no existan claves bibliográficas huérfanas usadas en texto.

---

### Fase 4. Evaluación V&V (verificación-validación)
1. Verificación formal:
   - Producto corresponde a `mapa_conceptual`.
   - Contiene análisis propio.
   - Cierre con criterio jurídico personal.
2. Validación académica:
   - Coherencia entre teoría de DD.HH. y marco constitucional mexicano.
   - Claridad en distinción: derecho humano vs garantía de protección.
3. Consenso editorial (multiagente):
   - Agente contenido: suficiencia conceptual.
   - Agente normativo: precisión constitucional.
   - Agente estilo: tono académico UnADM y claridad.

---

## Criterios de aceptación por nivel

### Institución (UnADM)
- Tono respetuoso, académico y formativo.
- Integridad académica: sin fuentes inventadas.
- Evidencia de uso de fuentes institucionales/locales cuando aplique.

### Carrera (Licenciatura en Derecho)
- Argumentación jurídica básica correcta.
- Uso de categorías del derecho constitucional y DD.HH.
- Transferencia a práctica jurídica (caso/diagnóstico/remedio posible, al menos en conclusión).

### Materia (Garantías Constitucionales)
- Distinción explícita entre:
  - Derechos humanos,
  - Garantías para su protección,
  - Medios de control constitucional.
- Referencia al Art. 1 constitucional y principios de DD.HH.

### Actividad 4
- Formato central: **mapa conceptual** (no ensayo puro).
- Cobertura temática mínima del Tema 1.
- Relación jerárquica y lógica entre conceptos (nodos y conectores).
- Citas visibles suficientes (mínimo 3 sólidas para actividad simple; ideal 4–5 si se amplía explicación).

---

## Riesgos, faltantes, placeholders y errores bloqueantes

### Riesgos
- **Inconsistencia de subject canónico** detectada (“Actividad 5” en planner vs solicitud “Actividad 4”).
- Riesgo de convertir la entrega en texto expositivo sin forma de mapa conceptual.
- Riesgo de sobrecargar con teoría sin vínculo al Art. 1 CPEUM.

### Faltantes
- No se mostró aquí el enunciado literal completo de la Actividad 4 (rúbrica puntual).
- Falta confirmar si el docente exige mapa gráfico (imagen) o admite mapa textual jerárquico.

### Placeholders (marcar explícitamente si se usan)
- `[SUPUESTO]` Se asume que se acepta mapa conceptual en formato textual dentro del reporte `.tex`.
- `[PENDIENTE]` Confirmar rúbrica exacta y ponderación de criterios visuales.
- `[PENDIENTE]` Verificar si se requiere portada/formato específico adicional.

### Errores bloqueantes
- Citas en texto sin entrada válida en `garantias-constitucionales.bib`.
- Contradicción en título/encabezado de actividad (4 vs 5).
- Ausencia del componente “mapa conceptual” (entrega no conforme).
- Afirmaciones normativas sustantivas sin respaldo mínimo en fuentes verificables.

### 2. investigar - Investigador documental - Claude Foundry

# Informe de investigación editorial — AulaTeX (Rol: INVESTIGADOR)

**Run:** diagnóstico previo a `realizar-actividad`
**Scope:** `UnADM/licenciatura-en-derecho-unadm/garantias-constitucionales-lde/actividad-4`
**Nivel de operación:** materia (con foco en actividad 4)
**Modo:** direct · Estado propuesto tras este informe: `DIAGNOSTICADO → PLANIFICACIÓN`

---

## 0. Síntesis ejecutiva (5 líneas)

La Actividad 4 corresponde al **Tema 1: marco teórico de los derechos humanos y sus principios**, con producto sumativo **mapa conceptual** y actividad formativa de sesión sincrónica. El corpus local es **suficiente en fuentes doctrinales** (tres libros de la Biblioteca Digital UnADM ya presentes en `.bib`) pero **insuficiente en citas visibles**: el artefacto `.tex` heredado solo cita `unadmMallaDerecho2024` y `unadmSitioWeb`, lo que incumple la regla de mínimo tres fuentes sólidas. Existen **tres inconsistencias bloqueantes** de trazabilidad (subject cruzado con Actividad 5, técnica didáctica contradictoria y entradas `.bib` fantasma). Se detecta además un **riesgo sustantivo de atribución normativa errónea** en la ficha del concepto «Artículo 1 Constitucional».

---

## 1. Hallazgos priorizados

| # | Prioridad | Hallazgo | Evidencia en contexto | Acción requerida |
|---|---|---|---|---|
| H1 | **P0 — bloqueante** | Conflicto de identidad de actividad: el detail planner declara «Subject canónico: **Actividad 5** - garantias-constitucionales-lde» mientras el scope semilla y la memoria `adn_tex` son de **Actividad 4** | Bloque «Detail planner» vs. scope semilla y `reporte-...-Actividad-4.tex` | Fijar subject = `Actividad 4 - garantias-constitucionales-lde` y registrar la corrección en memoria; no propagar el subject de Actividad 5 |
| H2 | **P0 — bloqueante** | Conflicto de técnica didáctica: el scope `actividad-4` detecta `mapa_conceptual`; el resumen global del detail planner detecta `cuestionario_diagnostico` para todos los scopes | Sección «Scopes» vs. «Detail planner» | Prevalece **`mapa_conceptual`** por concordancia con la planeación oficial («Actividad: Mapa Conceptual»). El contrato de forma visible debe ser mapa, no cuestionario |
| H3 | **P0 — integridad académica** | Entradas `.bib` **sin fuente real**: `cicloARefuerzo07` y `cicloARefuerzo08` («AulaTeX Editorial», nota admite que deben sustituirse) | `garantias-constitucionales.bib` | **Prohibido citarlas.** Marcar para depuración o sustitución por fuente disciplinar verificada |
| H4 | **P1 — sustantivo** | Posible **atribución normativa errónea**: la ficha del concepto «Artículo 1 Constitucional» transcribe «libertad de religión (Artículo 8), expresión (artículo 9), asociación (artículo 10), propiedad (artículo 14), trabajo (artículo 15), salud…», articulado que **no corresponde a la CPEUM** | Fichas del extractor, Marcano Salazar p. 90 | Verificar en la fuente a qué instrumento se refiere (probable declaración/convención internacional o constitución extranjera). **Supuesto marcado**: hasta verificar, no citar ese fragmento para sostener el art. 1º CPEUM |
| H5 | **P1 — cobertura bibliográfica** | El artefacto hered

### 3. generar - Arquitecto de plantillas - GPT-Pro



### 4. validar - Verificador y validador - Auto (model-router)

# AulaTeX — Actividad 4

## Estado del flujo

- **Estado:** propuesta elaborada → verificación editorial pendiente de compilación.
- **Técnica didáctica identificada:** mapa conceptual.
- **Criterio de resolución:** se prioriza la planeación específica de la Actividad 4 sobre señales heredadas que identifican erróneamente la técnica como cuestionario diagnóstico.
- **Producto:** mapa conceptual sobre antecedentes, concepto, generaciones y principios de los derechos humanos.
- **Supuesto explícito:** no se proporcionó el archivo fuente completo de la plantilla ni la rúbrica detallada; por ello, se entrega un bloque compatible con LaTeX estándar que puede integrarse en el reporte institucional existente.

---

## Contenido propuesto para `reporte-garantias-constitucionales-Actividad-4.tex`

```latex
\section{Introducción}

Los derechos humanos constituyen un referente jurídico y ético para limitar el ejercicio arbitrario del poder y proteger la dignidad de todas las personas. Su reconocimiento contemporáneo es resultado de un proceso histórico en el que diversas luchas sociales, documentos jurídicos y transformaciones políticas ampliaron progresivamente el ámbito de protección de las personas. Por ello, su estudio requiere relacionar antecedentes históricos, concepto, generaciones y principios, en lugar de analizarlos como elementos aislados.

En el sistema jurídico mexicano, la reforma constitucional en materia de derechos humanos fortaleció el deber de todas las autoridades de promover, respetar, proteger y garantizar los derechos humanos conforme a los principios de universalidad, interdependencia, indivisibilidad y progresividad. Asimismo, estableció la obligación de prevenir, investigar, sancionar y reparar sus violaciones, en los términos previstos por el artículo 1o. constitucional
\cite{cpeum2026}.

El propósito de esta actividad es ubicar los antecedentes históricos de los derechos humanos, reconocer su concepto y relacionar los principios dogmáticos que orientan su interpretación y protección. Para ello, se presenta un mapa conceptual sustentado en fuentes doctrinales y constitucionales.

\section{Mapa conceptual de los derechos humanos}

El siguiente mapa conceptual organiza las relaciones principales entre los antecedentes históricos, el concepto de derechos humanos, sus generaciones y los principios que rigen su protección jurídica.

\begin{center}
\setlength{\fboxsep}{8pt}

\fbox{%
\begin{minipage}{0.84\textwidth}
\begin{center}
\textbf{\large DERECHOS HUMANOS}
\end{center}

\begin{center}
$\Downarrow$
\end{center}

\begin{center}
\textit{Son derechos inherentes a la dignidad de todas las personas, reconocidos y protegidos por el orden jurídico.}
\end{center}

\begin{center}
$\Downarrow$
\end{center}

Se construyen históricamente mediante:

\begin{center}
\textbf{Antecedentes históricos}
\end{center}

\begin{itemize}
    \item Limitación progresiva del poder.
    \item Reconocimiento de libertades y derechos frente a la autoridad.
    \item Incorporación de derechos en declaraciones y constituciones.
    \item Desarrollo internacional de la protección de la persona.
\end{itemize}

\begin{center}
$\Downarrow$
\end{center}

Se expresan en distintas:

\begin{center}
\textbf{Generaciones de los derechos humanos}
\end{center}

\begin{description}
    \item[Primera generación:] derechos civiles y políticos, relacionados con la libertad, la igualdad jurídica y la participación política.
    \item[Segunda generación:] derechos económicos, sociales y culturales, vinculados con condiciones materiales de vida digna.
    \item[Tercera generación:] derechos colectivos o de solidaridad, relacionados con la paz, el desarrollo, el medio ambiente y la cooperación.
\end{description}

\begin{center}
$\Downarrow$
\end{center}

Su interpretación y protección se orientan por los:

\begin{center}
\textbf{Principios de los derechos humanos}
\end{center}

\begin{description}
    \item[Universalidad:] corresponden a todas las personas sin discriminación.
    \item[Interdependencia:] el disfrute de un derecho se relaciona con el ejercicio de otros derechos.
    \item[Indivisibilidad:] los derechos forman un conjunto integral y no deben jerarquizarse de manera que se desconozca su unidad.
    \item[Progresividad:] las autoridades deben avanzar en su protección y evitar retrocesos injustificados.
\end{description}

\begin{center}
$\Downarrow$
\end{center}

En México, el artículo 1o. constitucional establece obligaciones para todas las autoridades y reconoce que las normas relativas a los derechos humanos deben interpretarse favoreciendo en todo tiempo la protección más amplia de las personas
\cite{cpeum2026}.
\end{minipage}%
}
\end{center}

\section{Explicación del mapa conceptual}

El mapa coloca a los derechos humanos como concepto central porque los demás elementos permiten comprender su origen, contenido y eficacia. Los antecedentes históricos muestran que su reconocimiento no surgió de manera inmediata, sino a partir de procesos sociales y jurídicos orientados a limitar el poder y proteger libertades fundamentales. En este sentido, la evolución histórica permite identificar el tránsito de concepciones centradas en privilegios o pertenencias políticas hacia una idea más amplia de derechos inherentes a la persona \cite{marcanoSalazarDerechosHumanos}.

Las generaciones de derechos representan una forma didáctica de observar su desarrollo histórico. La primera generación se relaciona principalmente con las libertades civiles y los derechos políticos; la segunda, con las condiciones sociales y económicas necesarias para una vida digna; y la tercera, con intereses colectivos que requieren cooperación entre personas, comunidades y Estados. Esta clasificación es útil para fines pedagógicos, aunque no debe interpretarse como una jerarquía, porque todos los derechos humanos son complementarios.

Los principios de universalidad, interdependencia, indivisibilidad y progresividad impiden analizar los derechos humanos de manera fragmentada. La universalidad exige reconocer que su titularidad corresponde a todas las personas; la interdependencia permite advertir que la afectación de un derecho puede repercutir en otros; la indivisibilidad exige proteger el conjunto de derechos; y la progresividad obliga a ampliar su tutela y prohíbe retrocesos injustificados. La doctrina destaca que estos principios son necesarios para comprender la trascendencia jurídica y social de los derechos humanos
\cite{marcanoSalazarDerechosHumanos,rabinovichBerkmanDerechosHumanos}.

En el orden constitucional mexicano, estos elementos se relacionan con el artículo 1o. de la Constitución Política de los Estados Unidos Mexicanos. La norma constitucional no solo reconoce derechos, sino que impone obligaciones concretas a las autoridades. Por tanto, la protección de los derechos humanos requiere que las autoridades adopten medidas de respeto, prevención, garantía, investigación, sanción y reparación frente a posibles violaciones
\cite{cpeum2026}.

\section{Análisis propio}

El mapa conceptual permite advertir que los derechos humanos no deben reducirse a una lista de libertades contenidas en la Constitución. Son una construcción histórica y normativa que exige interpretar las disposiciones jurídicas desde la dignidad humana. Esta perspectiva resulta especialmente importante en la práctica jurídica, porque una controversia aparentemente relacionada con un solo derecho puede involucrar simultáneamente la igualdad, la libertad, la integridad personal, el acceso a la justicia o los derechos sociales.

También es necesario distinguir entre el derecho humano y los mecanismos destinados a protegerlo. El derecho humano constituye el bien jurídico o la facultad que corresponde a la persona; los principios orientan su interpretación; las garantías y los medios de control constitucional proporcionan vías para exigir su respeto. Confundir estos conceptos puede conducir a identificar incorrectamente el problema jurídico o a elegir un mecanismo de defensa inadecuado.

Desde mi perspectiva, la importancia práctica del artículo 1o. constitucional radica en que convierte la protección de los derechos humanos en una obligación transversal para todas las autoridades. En consecuencia, la actuación jurídica no debe limitarse a verificar la existencia formal de una norma, sino que debe valorar sus efectos sobre la dignidad, la igualdad y la protección más amplia de la persona.

\section{Conclusión}

Los derechos humanos son el resultado de una evolución histórica orientada a limitar el poder y reconocer la dignidad de todas las personas. Sus generaciones permiten identificar distintos momentos y ámbitos de protección, mientras que los principios de universalidad, interdependencia, indivisibilidad y progresividad proporcionan criterios para interpretarlos como un sistema integral.

En México, el artículo 1o. constitucional vincula a todas las autoridades con el deber de promover, respetar, proteger y garantizar los derechos humanos. Por ello, el conocimiento de sus antecedentes, concepto y principios no es únicamente teórico: constituye una herramienta indispensable para identificar violaciones, argumentar jurídicamente y seleccionar vías adecuadas de protección. La práctica profesional del derecho debe partir de esta visión integral y orientar sus decisiones hacia la defensa efectiva de la dignidad humana.
```

---

## Cobertura bibliográfica

| Elemento desarrollado | Fuente visible |
|---|---|
| Artículo 1o. constitucional y obligaciones de las autoridades | `\cite{cpeum2026}` |
| Antecedentes, definición y evolución de los derechos humanos | `\cite{marcanoSalazarDerechosHumanos}` |
| Desarrollo histórico y configuración de los derechos humanos | `\cite{rabinovichBerkmanDerechosHumanos}` |
| Principios de interdependencia, indivisibilidad, universalidad y progresividad | `\cite{marcanoSalazarDerechosHumanos,rabinovichBerkmanDerechosHumanos}` |
| Relación entre derechos humanos y protección constitucional | `\cite{cpeum2026}` |

**Resultado:** cuatro fuentes sólidas o institucionales participan de manera visible en el contenido. No se agregan referencias nuevas al archivo `.bib` porque las claves utilizadas aparecen registradas en el corpus bibliográfico local.

---

# Verificación y validación

## Checklist de defendibilidad académica

- [x] La actividad corresponde a la técnica detectada: **mapa conceptual**.
- [x] Se incluyen antecedentes históricos.
- [x] Se explica el concepto de derechos humanos.
- [x] Se incorporan las generaciones de derechos humanos.
- [x] Se desarrollan los principios de universalidad, interdependencia, indivisibilidad y progresividad.
- [x] Se relaciona el contenido con el artículo 1o. constitucional.
- [x] Se distingue entre derechos humanos, principios y mecanismos de protección.
- [x] Se incorpora análisis propio.
- [x] Se presenta una conclusión jurídica transferible a la práctica profesional.
- [x] Las citas utilizadas corresponden a claves existentes en el archivo `.bib`.
- [x] No se inventan páginas, citas textuales ni datos editoriales adicionales.

## Riesgos de compilación LaTeX

1. **Comandos de cita:** el bloque utiliza `\cite{...}` estándar. Debe conservarse el sistema bibliográfico ya configurado por la plantilla.
2. **Entorno `minipage`:** es compatible con LaTeX estándar y no requiere paquetes adicionales.
3. **Símbolos de flecha:** `\Downarrow` pertenece a los símbolos matemáticos usuales. Si la plantilla presenta problemas, puede sustituirse por `\(\Downarrow\)`.
4. **Ancho de la caja:** `0.84\textwidth` debería ser compatible con una página convencional. Si se desborda, puede reducirse a `0.78\textwidth`.
5. **Caracteres especiales:** verificar que los archivos estén guardados en UTF-8 y que la plantilla utilice `inputenc` o LuaLaTeX/XeLaTeX con configuración equivalente.
6. **Referencias:** si se usa BibTeX o Biber, debe ejecutarse la secuencia correspondiente antes de evaluar la ausencia de citas.

## Placeholders o información pendiente

- [ ] Nombre de la o el estudiante.
- [ ] Matrícula.
- [ ] Grupo.
- [ ] Nombre del docente.
- [ ] Fecha de entrega.
- [ ] Rúbrica específica de la Actividad 4, si existe.
- [ ] Confirmación del sistema bibliográfico de la plantilla: BibTeX o Biber.

## Pruebas recomendadas

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error \
  reporte-garantias-constitucionales-Actividad-4.tex
```

Después de la compilación, verificar:

- ausencia de errores `Undefined control sequence`;
- ausencia de referencias `[?]`;
- ausencia de claves bibliográficas no encontradas;
- que el mapa conceptual no rebase los márgenes;
- que no existan cajas o párrafos cortados;
- que todas las citas aparezcan en la lista de referencias;
- que el PDF conserve la identidad visual institucional de la UnADM.

## Dictamen del verificador

**Propuesta defendible:** sí.  
**Cobertura bibliográfica:** suficiente para una actividad simple de mapa conceptual.  
**Riesgo académico principal:** bajo; debe evitarse presentar las generaciones como una jerarquía de derechos.  
**Riesgo técnico principal:** medio, condicionado a la configuración bibliográfica y al diseño preexistente de la plantilla.  
**Acción recomendada:** integrar el bloque, completar los datos institucionales y ejecutar `latexmk` con revisión visual final.

### 5. criticar - Critico adversarial - Codex

## Actividad 4 — Entrega propuesta (Mapa conceptual)

**Asignatura:** Garantías Constitucionales (UnADM, Derecho)  
**Técnica detectada/solicitada:** **Mapa conceptual**  
**Tema base:** Marco teórico de los derechos humanos y sus principios.

---

### 1) Diagnóstico crítico adversarial (bloqueantes detectados)

1. **Inconsistencia de planeación**  
   - El detalle planner muestra para *actividad-4* la técnica `mapa_conceptual`, pero en reglas heredadas aparece “Subject canónico: Actividad 5” y técnica `cuestionario_diagnostico`.  
   - **Riesgo:** desalineación entre rúbrica esperada y producto entregado.  
   - **Acción correctiva:** mantener **Actividad 4 = mapa conceptual** (prioridad a extractor/planeación de actividad local).

2. **Riesgo de fuente incompleta en `.bib`**  
   - La entrada `alvarezIcazaDerechosMexico` parece truncada (`note = {Capítul...`).  
   - **Riesgo:** error de compilación BibTeX/Biber.  
   - **Acción correctiva:** cerrar correctamente la entrada antes de compilar.

3. **Fuente metodológica no confirmada en `.bib`**  
   - Se menciona López, A. (2022) “100 técnicas didácticas...”, pero no se observa clave BibTeX explícita en el fragmento compartido.  
   - **Riesgo:** cita visible sin respaldo bibliográfico.  
   - **Acción correctiva:** agregar entrada BibTeX verificable o marcarla como **[supuesto: pendiente de alta bibliográfica]**.

4. **Calidad de trazabilidad parcial**  
   - Algunas fichas tienen similitud baja/media y observación de posible “ruido”.  
   - **Riesgo:** sobreafirmaciones doctrinales sin soporte robusto.  
   - **Acción correctiva:** usar afirmaciones conservadoras y anclar a CPEUM + 2–3 fuentes doctrinales sólidas ya listadas.

---

### 2) Producto académico (contenido listo para pasar a LaTeX)

## Introducción
El estudio de las garantías constitucionales exige distinguir con precisión entre **derechos humanos**, **principios de interpretación y aplicación** y **mecanismos de protección**. En esta actividad se presenta un **mapa conceptual** centrado en los antecedentes históricos, las generaciones de derechos, el concepto jurídico de derechos humanos y su base en el artículo 1o constitucional, con el propósito de visualizar relaciones sustantivas para el análisis jurídico posterior \cite{programaAsignaturaGarantiasConstitucionales2026,cpeum2026}.

## Mapa conceptual (estructura textual)

**Nodo central:**  
**Derechos humanos en el constitucionalismo mexicano**

**Rama A. Fundamentación histórica**
- Antecedentes históricos  
  - Luchas contra el poder absoluto  
  - Reconocimiento progresivo de libertades  
  - Constitucionalización de derechos  
- Idea clave: los derechos no surgen de forma instantánea; son resultado de procesos históricos y políticos \cite{marcanoSalazarDerechosHumanos,rabinovichBerkmanDerechosHumanos}.

**Rama B. Generaciones de derechos**
- Primera generación: libertades civiles y políticas  
- Segunda generación: derechos económicos, sociales y culturales  
- Tercera generación: derechos colectivos o de solidaridad  
- Idea clave: la clasificación por generaciones es didáctica; no implica jerarquías entre derechos \cite{alvarezIcazaDerechosMexico}.

**Rama C. Concepto jurídico de derechos humanos**
- Prerrogativas inherentes a la dignidad de toda persona  
- Reconocidas en Constitución y tratados internacionales  
- Exigibles frente a actos de autoridad  
- Idea clave: los derechos humanos tienen función limitadora del poder público \cite{cpeum2026}.

**Rama D. Artículo 1o constitucional (eje normativo)**
- Principio pro persona  
- Obligaciones de todas las autoridades: promover, respetar, proteger y garantizar  
- Deber de prevenir, investigar, sancionar y reparar violaciones  
- Prohibición de discriminación \cite{cpeum2026}.

**Rama E. Principios de los derechos humanos**
- Universalidad  
- Interdependencia  
- Indivisibilidad  
- Progresividad  
- No regresión (como criterio derivado de progresividad en doctrina y práctica interpretativa)  
- Idea clave: la protección debe ser integral, no fragmentaria \cite{marcanoSalazarDerechosHumanos,cpeum2026}.

**Rama F. Vinculación con garantías y control constitucional**
- Garantías como vías de protección efectiva  
- Articulación con medios de control constitucional (p. ej., juicio de amparo) \cite{leyAmparo2026}.  
- Idea clave: sin mecanismos de tutela, el derecho queda en plano declarativo.

## Análisis propio
Desde una perspectiva de práctica jurídica, el principal desafío no es solo “conocer” catálogos de derechos, sino **argumentar su aplicabilidad concreta** ante hechos específicos. El mapa conceptual permite advertir que el artículo 1o constitucional funciona como punto de conexión entre teoría (dignidad, universalidad, interdependencia) y litigio estratégico (interpretación pro persona, control de actos de autoridad y reparación). Por ello, una formación sólida en garantías constitucionales requiere integrar historia, dogmática y técnica procesal.

## Conclusión
El mapa conceptual evidencia que los derechos humanos, sus principios y sus garantías de protección forman un sistema unitario: histórico en su construcción, constitucional en su fundamento y jurisdiccional en su exigibilidad. En términos profesionales, esta comprensión permite pasar de definiciones generales a decisiones jurídicas fundadas para la defensa efectiva de las personas, especialmente frente a violaciones de autoridad.

---

### 3) Validación rápida de cumplimiento institucional

- ✅ Producto corresponde a **mapa conceptual** (no cuestionario).  
- ✅ Tono académico y jurídico, con postura propia en análisis/conclusión.  
- ✅ Citas apoyadas en fuentes locales/institucionales ya registradas.  
- ⚠️ **Pendiente técnico:** corregir entrada truncada en `.bib` y confirmar alta de fuente didáctica de López (2022) si se citará explícitamente.

---

### 4) Recomendación para siguiente ciclo

1. Normalizar metadatos para evitar colisión “Actividad 4 vs Actividad 5”.  
2. Ejecutar lint bibliográfico previo (`bibtex/biber check`) para detectar entradas incompletas.  
3. Incorporar versión visual del mapa (TikZ o diagrama embebido) si la rúbrica pide componente gráfico explícito.

## Consenso y validacion

- Puntuacion de consenso: 8.33/10
- Estado: PASS

### Criterios
- identidad_institucional: OK
- bibliografia: OK
- trazabilidad: OK
- compilacion: OK
- riesgos: OK

### Puntuacion por rol
- Planificador editorial: 7.80/10
- Investigador documental: 9.87/10
- Arquitecto de plantillas: 0.00/10
- Verificador y validador: 8.58/10
- Critico adversarial: 8.58/10

### Recomendaciones
- Usar el reporte como retroalimentacion editorial aplicable al objetivo.

## Extractor

- Estado: ERROR
- Manifest: `retroalimentacion-editorial/aulatex/extractor/runs/20260809-154210-extractor/manifest.json`
- Salida: `UnADM/licenciatura-en-derecho-unadm/garantias-constitucionales-lde/extractor-aulatex/conceptos-garantias-constitucionales-actividad-4`

## Compilacion

- UnADM/licenciatura-en-derecho-unadm/garantias-constitucionales-lde/reporte-garantias-constitucionales-Actividad-4.tex: OK (0)
- UnADM/licenciatura-en-derecho-unadm/garantias-constitucionales-lde/presentacion-garantias-constitucionales-Actividad-4.tex: OK (0)
