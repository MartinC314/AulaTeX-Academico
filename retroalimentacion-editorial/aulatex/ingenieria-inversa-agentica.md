# Ingeniería inversa agentica de AulaTeX

## 1. Propósito

Diseñar el enfoque agentico de AulaTeX mediante ingeniería inversa o recursiva: partir del resultado esperado —una actividad académica terminada, trazable, compilable y evaluada— y retroceder para identificar qué componentes, ciclos, memorias y herramientas deben existir para producirla de manera agentica.

La meta no es solamente generar texto. La meta es que una actividad pueda emerger de un flujo cíclico verificable:

```text
extractor -> realizador de actividad -> evaluador -> memoria -> extractor
```

Cada etapa debe poder ejecutar su propio bucle de refuerzo, conservar memoria local y entregar un estado verificable a la siguiente etapa.

## 2. Resultado esperado como punto de partida

El resultado esperado actual para una actividad de AulaTeX es:

```text
actividad final = TEX + PDF + bibliografía válida + trazabilidad + memoria actualizada + evaluación aprobada
```

Para Filosofía del Derecho, ese resultado se observa en archivos como:

```text
UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/
  reporte-filosofia-del-derecho-Actividad-1.tex
  reporte-filosofia-del-derecho-Actividad-1.pdf
  filosofia-del-derecho.bib
  referencias-filosofia-del-derecho/
  planeaciones-filosofia-del-derecho/
  .memoria-filosofia-del-derecho-lde/
```

Desde ingeniería inversa, cada actividad terminada se descompone en preguntas:

1. ¿Qué consigna o planeación la originó?
2. ¿Qué conceptos eran necesarios?
3. ¿Qué fuentes sostienen esos conceptos?
4. ¿Qué estructura textual produjo el entregable?
5. ¿Qué citas y claves BibTeX fueron usadas?
6. ¿Qué errores se corrigieron antes de compilar?
7. ¿Qué criterios permitieron declararla finalizada?
8. ¿Qué aprendizaje debe pasar a memoria?

## 3. Componentes existentes

### 3.1 Extractor

Existe parcialmente.

Módulo principal:

```text
scripts/aulatex/extractor_adapter.py
```

Motor adaptado:

```text
scripts/extractor-conceptos-ideas/run.py
```

Capacidades actuales:

- resuelve scope editorial;
- infiere fuentes;
- infiere planeación;
- ejecuta extractor;
- registra manifest, stdout y stderr;
- valida artefactos nucleares.

Artefactos esperados:

```text
fichas_conceptos.json
conceptos_detectados.json
ideas_detectadas.json
trazabilidad_fuentes.json
resumen_planeacion.json
```

Brecha:

- aún no existe un bucle propio del extractor que reintente extracción si la cobertura conceptual es baja;
- aún no compara automáticamente fichas contra rúbrica de actividad;
- aún no decide cuándo reutilizar salidas previas por semana.

### 3.2 Realizador de actividad

Existe parcialmente.

Módulo principal:

```text
scripts/aulatex/agent.py
```

Capacidades actuales:

- ejecuta roles LLM;
- integra memoria editorial persistente;
- puede invocar `ExtractorAdapter`;
- compila objetivos TeX;
- registra workflow y manifest;
- soporta `--cycle-mode stages` y `--cycle-mode full`.

Brecha:

- todavía no materializa automáticamente cambios en el `.tex` final;
- no tiene una política determinista de edición por secciones;
- no produce un `estado-agente.json` por actividad con decisión y siguiente acción;
- no distingue entre redactar desde cero, reparar una actividad existente o mejorar una actividad ya finalizada.

### 3.3 Evaluador

Existe parcialmente.

Componentes:

```text
EditorialConsensusEngine
workspace.compile_tex
manifest.json
workflow-trace.md
```

Capacidades actuales:

- evalúa cobertura textual por criterios generales;
- registra consenso multirol;
- compila TeX cuando se solicita;
- captura logs.

Brecha:

- no existe aún un evaluador estructurado de actividad;
- falta validar citas activas contra `.bib`;
- falta detectar placeholders activos;
- falta comparar actividad contra planeación;
- falta evaluar cobertura de extractor.

### 3.4 Memoria

Existe con fuerza.

Componentes:

```text
scripts/aulatex/editorial_memory.py
retroalimentacion-editorial/aulatex/editorial-memory/
.memoria-*/
```

Capacidades actuales:

- memoria por materia y actividad;
- propagación ascendente, lateral, descendente y recursiva;
- deduplicación sin regresión;
- memoria heredada por scope.

Brecha:

- la memoria es principalmente editorial, no todavía operativa;
- no registra con precisión decisiones de herramienta por ciclo;
- no separa suficientemente memoria estable, memoria de evidencia y memoria de ejecución;
- no cierra automáticamente el bucle `evaluador -> memoria -> extractor`.

### 3.5 Constructor de nodos

Existe.

Módulo:

```text
scripts/aulatex/construction.py
```

Capacidades:

- crea o refuerza nodos;
- genera memoria fundacional;
- genera plan;
- deja contrato futuro de agente.

Brecha:

- sirve para preparar el terreno, no para realizar una actividad completa;
- debe conectarse al supervisor recursivo como fase previa si una actividad aún no existe.

## 4. Método de ingeniería inversa

El método propuesto se llama:

```text
RDA: Resultado -> Descomposición -> Agentes
```

### 4.1 Resultado

Se define el producto final deseado:

```json
{
  "producto": "actividad-academica",
  "formatos": ["tex", "pdf"],
  "calidad": ["compila", "citas-validas", "sin-pendientes", "responde-planeacion"],
  "memoria": ["decisiones", "errores", "reglas-reutilizables"]
}
```

### 4.2 Descomposición

Se descompone el resultado en evidencias necesarias:

```text
actividad final
├─ planeación resuelta
├─ conceptos e ideas extraídos
├─ bibliografía válida
├─ redacción estructurada
├─ compilación exitosa
├─ evaluación aprobada
└─ memoria actualizada
```

### 4.3 Agentes

Cada evidencia se asigna a un agente especializado:

| Evidencia requerida | Agente responsable |
| --- | --- |
| Planeación resuelta | Agente de planeación/extractor |
| Conceptos e ideas | Agente extractor |
| Bibliografía válida | Agente bibliográfico |
| Redacción estructurada | Agente realizador |
| PDF compilado | Agente compilador |
| Criterios aprobados | Agente evaluador |
| Aprendizaje persistente | Agente de memoria |

## 5. Flujo recursivo base

El flujo central debe ser circular, pero controlado:

```mermaid
flowchart LR
    E[Extractor] --> R[Realizador de actividad]
    R --> V[Evaluador]
    V --> M[Memoria]
    M --> E
```

La clave es que cada etapa no sea una llamada única. Cada etapa puede tener su propio bucle interno:

```text
Extractor:
  observar planeación -> extraer -> medir cobertura -> reforzar búsqueda -> cerrar

Realizador:
  leer fichas -> redactar sección -> verificar citas -> corregir -> cerrar

Evaluador:
  revisar TEX/PDF -> detectar fallas -> emitir dictamen -> cerrar

Memoria:
  recibir dictamen -> separar reglas estables/evidencias/errores -> actualizar -> cerrar
```

## 6. Bucles por etapa

### 6.1 Bucle del extractor

Objetivo:

```text
obtener conceptos, ideas y trazabilidad suficientes para redactar
```

Entrada:

- planeación;
- carpeta de fuentes;
- `.bib`;
- memoria de actividad/materia.

Ciclo:

```text
1. leer planeación
2. detectar conceptos esperados
3. buscar en fuentes
4. generar fichas
5. medir cobertura
6. si cobertura baja, ampliar búsqueda o depurar conceptos
7. cerrar cuando haya trazabilidad suficiente
```

Criterios de cierre:

- `conceptos_detectados.json` existe;
- `fichas_conceptos.json` existe;
- `trazabilidad_fuentes.json` existe;
- conceptos mínimos cubiertos;
- citas con fuente y ubicación.

### 6.2 Bucle del realizador

Objetivo:

```text
convertir planeación + fichas + memoria en actividad TEX
```

Entrada:

- `resumen_planeacion.json`;
- `fichas_conceptos.json`;
- `ideas_detectadas.json`;
- `trazabilidad_fuentes.json`;
- `.bib` canónico;
- memoria editorial.

Ciclo:

```text
1. construir esquema de actividad
2. redactar sección por sección
3. insertar citas existentes
4. revisar si cada afirmación fuerte tiene fuente
5. corregir huecos
6. producir TEX candidato
```

Criterios de cierre:

- secciones obligatorias presentes;
- sin `\pendiente{}` activo;
- citas solo con claves reales;
- conclusión jurídica propia;
- no se copia literal de fuentes.

### 6.3 Bucle evaluador

Objetivo:

```text
probar si la actividad es entregable
```

Entrada:

- TEX candidato;
- PDF si existe;
- `.bib`;
- planeación;
- fichas y trazabilidad.

Ciclo:

```text
1. validar claves de cita
2. validar placeholders
3. compilar
4. leer errores
5. comparar contra planeación
6. emitir dictamen
7. si falla, enviar observaciones al realizador o extractor
```

Criterios de cierre:

- compila;
- no hay claves faltantes;
- no hay placeholders;
- responde a la técnica didáctica;
- cumple producto solicitado;
- tiene trazabilidad suficiente.

### 6.4 Bucle de memoria

Objetivo:

```text
convertir ejecución en aprendizaje reutilizable
```

Entrada:

- manifest del extractor;
- cambios del realizador;
- dictamen del evaluador;
- errores corregidos;
- decisiones aceptadas.

Ciclo:

```text
1. separar hechos de opiniones
2. clasificar memoria estable, memoria de actividad y memoria de evidencia
3. registrar errores no repetir
4. actualizar siguiente acción sugerida
5. propagar solo reglas reutilizables
```

Criterios de cierre:

- memoria estable actualizada sin contaminarla con detalles puntuales;
- memoria de actividad actualizada con estado específico;
- evidencia referenciada por rutas;
- siguiente acción clara.

## 7. Estado agentico requerido

Debe existir un estado por actividad:

```json
{
  "schema_version": 1,
  "scope_key": "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-01",
  "activity_number": 1,
  "target_tex": "reporte-filosofia-del-derecho-Actividad-1.tex",
  "expected_result": {
    "tex": true,
    "pdf": true,
    "bibliography_valid": true,
    "extractor_traceability": true,
    "evaluation_passed": true
  },
  "stage_state": {
    "extractor": "pending",
    "realizador": "pending",
    "evaluador": "pending",
    "memoria": "pending"
  },
  "next_stage": "extractor",
  "cycle_policy": {
    "extractor_cycles": 2,
    "realizador_cycles": 3,
    "evaluador_cycles": 2,
    "memoria_cycles": 1,
    "max_total_cycles": 100
  }
}
```

## 8. Componentes que deben modificarse

### 8.1 Crear `activity_agent_state.py`

Responsabilidad:

- leer estado de actividad;
- guardar `estado-agente.json`;
- registrar etapa actual;
- registrar decisiones y evidencias.

### 8.2 Crear `activity_observer.py`

Responsabilidad:

- detectar TEX existente;
- detectar PDF;
- contar citas;
- comparar `.bib`;
- detectar planeación;
- detectar salida del extractor;
- detectar pendientes.

### 8.3 Crear `activity_evaluator.py`

Responsabilidad:

- producir `evaluacion.json`;
- emitir `pass`, `warn`, `fail` por dimensión;
- decidir si vuelve a extractor, realizador o memoria.

### 8.4 Extender `ExtractorAdapter`

Cambios:

- permitir salida por actividad: `extractor-aulatex/actividad-01/`;
- detectar si ya existe salida reutilizable;
- evaluar cobertura conceptual;
- permitir ciclos de refuerzo propios.

### 8.5 Extender `AulaTeXAgent`

Cambios:

- separar rol LLM de flujo de etapa;
- permitir que el realizador use artefactos del extractor;
- producir TEX candidato o parche;
- registrar salida estructurada por ciclo.

### 8.6 Extender `EditorialMemoryStore`

Cambios:

- distinguir memoria estable vs memoria operativa;
- registrar decisiones de agente;
- registrar errores no repetir;
- propagar solo patrones reutilizables.

## 9. Flujo para Actividad 1 como prueba inicial

Actividad 1 es la mejor prueba porque tiene un resultado ya existente y un fallo verificable: claves bibliográficas antiguas.

### Resultado esperado

```text
reporte-filosofia-del-derecho-Actividad-1.tex
reporte-filosofia-del-derecho-Actividad-1.pdf
citas alineadas con filosofia-del-derecho.bib
memoria actualizada
```

### Ingeniería inversa

1. Observar actividad final existente.
2. Detectar citas activas.
3. Comparar contra `.bib` canónico.
4. Detectar claves antiguas.
5. Proponer equivalencias.
6. Reparar TEX o `.bib`.
7. Compilar.
8. Evaluar.
9. Registrar en memoria: “Actividad 1 migrada de claves antiguas a canon actual”.

### Bucle recomendado

```text
Evaluador bibliográfico -> Realizador/Reparador -> Compilador -> Memoria -> Evaluador
```

No debe empezar con redacción nueva. Debe empezar por ingeniería inversa del documento existente.

## 10. Expansión por niveles

### Nivel actividad

Unidad mínima. Produce o repara un entregable.

### Nivel materia

Coordina patrones entre actividades. Detecta bibliografía canónica y reglas comunes.

### Nivel carrera

Transfiere patrones de escritura jurídica entre materias sin copiar contenido temático.

### Nivel institución

Estabiliza identidad, portada, lineamientos y criterios institucionales.

### Nivel workspace

Coordina convenciones globales de AulaTeX: plantillas, salidas, memoria, referencias y compilación.

## 11. Validación del enfoque

La validación debe hacerse por etapas:

### Prueba 1: ingeniería inversa sin modificar archivos

- observar Actividad 1;
- generar `estado-agente.json`;
- generar `evaluacion.json`;
- listar acciones recomendadas.

### Prueba 2: reparación controlada

- reparar claves de Actividad 1;
- compilar;
- evaluar.

### Prueba 3: extractor controlado

- ejecutar extractor para una actividad sin fichas;
- validar cobertura;
- no redactar todavía.

### Prueba 4: realización completa

- usar extractor + memoria + realizador;
- generar o revisar actividad;
- compilar;
- actualizar memoria.

### Prueba 5: expansión a materia

- correr diagnóstico sobre Actividades 1 a 6;
- producir tablero de estado por actividad;
- decidir siguiente acción por actividad.

## 12. Prototipo cerrado recomendado

La especificación accionable para aterrizar este enfoque vive en:

```text
retroalimentacion-editorial/aulatex/prototipo-actividad-1-agentica.md
```

Ese documento convierte el enfoque general en cinco piezas validables:

1. contrato objetivo de Actividad 1;
2. mapa de componentes por reutilización real;
3. flujo secuencial con bucles acotados;
4. memoria útil para corrección;
5. matriz de validación y puerta de escalamiento.

## 13. Principio rector

El agente no debe empezar preguntando “qué redacto”.

Debe empezar preguntando:

```text
¿Qué resultado final quiero reproducir o mejorar, y qué evidencias necesito para llegar ahí?
```

Esto convierte AulaTeX en un sistema de ingeniería inversa editorial: observa entregables, deduce insumos, ejecuta herramientas, evalúa resultados y actualiza memoria para que la siguiente actividad nazca con menos incertidumbre.
