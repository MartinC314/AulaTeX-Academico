{
  "summary": [
    "Memoria local canonizada con preservacion total y deduplicacion lossless.",
    "Se mantiene identidad UnADM y contexto curricular verificable de Filosofia del Derecho.",
    "Se mantiene regla de normalizacion estructurada obligatoria antes de propagar.",
    "Se conserva ADN editorial: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se preserva TEX reconstruible del nodo con fuente primaria de Actividad 1."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Citar malla-curricular-derecho-unadm.pdf como fuente de ubicacion curricular.",
    "Marcar como supuesto cualquier dato no visible en la consigna de actividad.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Verificar que el producto corresponda a la consigna de Actividad 1.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir que fuentes de semanas posteriores corresponden a Actividad 1."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna de Actividad 1."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anomalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: archivo .bib canonico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de la actividad en el .bib de la asignatura.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No inventar referencias; usar solo obras realmente consultables.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "No asumir que filosofia-del-derecho-clean.bib corresponde a Actividad 1.",
    "Supuesto: filosofia-del-derecho-clean.bib esta orientado a Semana 7 (interpretacion juridica)."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Propagar solo reglas generales cuando falte consigna textual.",
    "Aplicar normalizacion manual si se detecta salida no estructurada en nodos vecinos.",
    "Evitar regresiones respecto de reglas utiles previas."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 1; confirmar producto exacto solicitado.",
    "Confirmar si la actividad requiere reporte, presentacion u otro formato principal.",
    "Confirmar rubrica de evaluacion especifica.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar nombre canonico final del archivo .bib de la asignatura.",
    "Confirmar si Actividad 1 reutiliza bibliografia existente o requiere .bib propio."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica y citas verificables.",
        "Carpeta de asignatura como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Filosofia del Derecho."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas y doctrina pertinentes.",
      "Evidencia verificable.",
      "Analisis propio del estudiante.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir la planeacion semanal en productos academicos evaluables.",
      "Asegurar fundamento juridico con evidencia.",
      "Formar criterio argumentativo profesional temprano."
    ],
    "style_markers": [
      "Objetivo puntual al inicio.",
      "Secciones funcionales y trazables.",
      "Supuestos marcados cuando falte dato.",
      "Cierre con implicacion practica juridica."
    ],
    "argumentative_patterns": [
      "Del problema al marco conceptual.",
      "Del marco normativo a la postura propia.",
      "De la evidencia a la conclusion juridica aplicada."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofia del Derecho",
        "Objeto de estudio",
        "Principios y normas juridicas",
        "Justicia",
        "Fundamentos del derecho",
        "Analisis critico del fenomeno juridico",
        "Evolucion historica: antiguedad, edad media y moderna, contemporaneidad",
        "Derecho y moral",
        "Constitucion y Ley General de Victimas"
      ],
      "citations": [
        "finnis_estudios_2017",
        "lovon_manual_2020",
        "ruiz_rodriguez_filosofia_derecho_2009",
        "noauthor_constitucion_nodate",
        "generales_ley_2021",
        "de_victimas_ley_2013",
        "franzoni_acevedo_ley_2017",
        "rojas_gonzalez_filosofia_derecho_2018",
        "gandara_ley_2015"
      ],
      "relations": [
        {
          "source": "Problema juridico o social",
          "target": "Conceptos y marco normativo",
          "kind": "depends_on",
          "justification": "El analisis parte de delimitar el problema y luego seleccionar categorias y normas pertinentes."
        },
        {
          "source": "Conceptos y marco normativo",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura estudiantil requiere base doctrinal y juridica verificable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion valida surge de argumentacion y evidencia, no de resumen."
        }
      ],
      "evidence": [
        "README.md de asignatura con ubicacion curricular.",
        "programa-analitico-filosofia-del-derecho.md con ejes de trabajo.",
        "reporte-filosofia-del-derecho-Actividad-1.tex como TEX primario reconstruible.",
        "Conjunto de claves citadas en tex_primary.all_cited_keys."
      ]
    },
    "reinforcement_log": [
      "Se elimino duplicidad textual en reglas sin perdida semantica.",
      "Se preservaron supuestos existentes y se mantuvieron explicitos.",
      "Se mantuvo la traza entre identidad institucional, estructura y control de calidad.",
      "Se reforzo la cadena argumentativa problema->evidencia->postura->conclusion.",
      "Se mantuvo compatibilidad con propagacion recursiva segura."
    ]
  }
}