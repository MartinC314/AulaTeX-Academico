# AulaTeX stage

- Etapa: criticar
- Rol: Critico adversarial
- Mision: encontrar fallas antes de aplicar cambios
- Motor: Codex
- Estado: ok

```latex
% =========================================================
% ARCHIVO: reporte-derecho-a-la-seguridad-social-act1.tex
% Actividad 1 | LDE-S2B1 | UnADM
% Modo: generacion directa
% Supuesto explicito: no se proporciono consigna tematica especifica de la Actividad 1.
% Se entrega plantilla base editable alineada al programa analitico local.
% =========================================================
\documentclass[spanish,letterpaper,oneside]{article}

% ---------- Metadatos editables ----------
\def\documenttitle{Actividad 1 - Derecho a la seguridad social}
\def\documentsubtitle{Plantilla editorial base}
\def\documentsubject{Licenciatura en Derecho}
\def\documentauthor{[Tu nombre completo]}
\def\coursename{Derecho a la seguridad social}
\def\coursecode{LDE-S2B1}

\def\universityname{Universidad Abierta y a Distancia de Mexico}
\def\universityfaculty{Licenciatura en Derecho}
\def\universitydepartment{Derecho a la seguridad social}
\def\universitydepartmentimage{departamentos/UnADM}
\def\universitydepartmentimagecfg{height=1.57cm}
\def\universitylocation{Ciudad de Mexico}

\def\authortable{
  \begin{tabular}{ll}
    \textbf{Alumno:} & \documentauthor \\
    Matricula: & [Tu matricula] \\
    Figura docente: & [Nombre de la figura docente] \\
    Semestre/Bloque: & 2 / 1 \\
    Tipo/Creditos: & Obligatoria / 8 \\
    Fecha de entrega: & \today \\
    Sede referencial: & \universitylocation
  \end{tabular}
}

% ---------- Carga de plantilla institucional ----------
\input{template}

% ---------- Paquetes de apoyo ----------
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[spanish,es-tabla]{babel}
\usepackage{helvet}
\renewcommand{\familydefault}{\sfdefault}
\usepackage{array}
\usepackage{longtable}
\usepackage{booktabs}
\usepackage{enumitem}
\usepackage{xcolor}
\usepackage{csquotes}
\setcitestyle{authoryear,open={(},close={)}}

% ---------- Utilidad de pendientes ----------
\newcommand{\pendiente}[1]{\textcolor{red}{[PENDIENTE: #1]}}

\begin{document}

\templatePortrait
\templatePagecfg
\onehalfspacing

\begin{abstractd}
Esta Actividad 1 se presenta en la asignatura \textit{Derecho a la seguridad social}
(LDE-S2B1), correspondiente al semestre 2, bloque 1, de la Licenciatura en Derecho
de la UnADM. \textbf{Supuesto metodologico:} al no contar con consigna tematica
especifica en el insumo recibido, se estructura una base editable centrada en:
problema juridico/social, fundamentos conceptuales y normativos, analisis propio,
y conclusion con criterio profesional transferible.
\end{abstractd}

\templateIndex
\templateFinalcfg

\section{Datos de encuadre de la actividad}
\begin{itemize}[leftmargin=1.2cm]
  \item \textbf{Asignatura:} Derecho a la seguridad social.
  \item \textbf{Clave:} LDE-S2B1.
  \item \textbf{Ubicacion curricular:} Semestre 2, Bloque 1.
  \item \textbf{Naturaleza:} Obligatoria, 8 creditos.
  \item \textbf{Institucion:} Universidad Abierta y a Distancia de Mexico (UnADM).
\end{itemize}

\section{Planteamiento del problema juridico o social}
\pendiente{Delimitar el problema central de la Actividad 1 en 1-2 parrafos, con contexto, sujetos involucrados y relevancia juridica.}

\subsection{Pregunta rectora}
\pendiente{Formular una pregunta de investigacion juridica clara, verificable y acotada.}

\subsection{Objetivo}
\pendiente{Redactar un objetivo general en infinitivo alineado con la consigna real de la semana.}

\section{Marco conceptual y normativo}
\pendiente{Incorporar conceptos clave de seguridad social y su sustento normativo/doctrinal, con citas verificables.}

\subsection{Conceptos operativos minimos}
\begin{itemize}
  \item Seguridad social.
  \item Derecho humano a la proteccion social.
  \item Sujetos de aseguramiento y cobertura.
  \item Prestaciones (salud, riesgos, invalidez, retiro, etc.).
\end{itemize}

\subsection{Fuentes a integrar}
\begin{enumerate}
  \item Fuentes institucionales de la UnADM.
  \item Normativa aplicable (segun consigna concreta).
  \item Doctrina o jurisprudencia pertinente (si la actividad lo exige).
\end{enumerate}

\section{Desarrollo y analisis propio}
\pendiente{Desarrollar argumentacion: describir, contrastar y valorar implicaciones juridicas del tema. Evitar resumen descriptivo sin postura.}

\subsection{Evidencia o producto solicitado}
\pendiente{Insertar aqui cuadro, matriz, mapa conceptual, linea de tiempo o analisis de caso, segun la actividad real.}

\section{Conclusion}
\pendiente{Cerrar con postura academica propia: hallazgo principal, consecuencia juridica y posible aplicacion practica/profesional.}

\section{Checklist de verificacion academica}
\begin{itemize}
  \item El texto responde a la consigna real de Actividad 1.
  \item Existe coherencia entre problema, objetivo, desarrollo y conclusion.
  \item Todas las afirmaciones relevantes tienen respaldo en fuente citada.
  \item No hay fuentes inventadas ni referencias sin rastro verificable.
  \item La bibliografia citada aparece en el archivo \texttt{derecho-a-la-seguridad-social.bib}.
  \item Se conserva identidad institucional UnADM en forma y fondo.
\end{itemize}

\clearpage
% Citas base verificables del contexto local:
\nocite{unadmSitioWeb,unadmMallaDerecho2024}
\bibliography{derecho-a-la-seguridad-social}

\end{document}
```

### Verificacion adversarial (bloqueantes y siguiente ciclo)

1. **Bloqueante potencial de compilacion:** `\input{template}` exige que exista `template.tex` compatible en la ruta del proyecto.  
2. **Bloqueante de evaluacion academica:** faltan datos reales de estudiante, matricula, figura docente y consigna exacta de Actividad 1 (marcados como supuestos/pendientes).  
3. **Integridad de fuentes:** no se inventaron referencias; solo se usan las dos entradas `.bib` locales disponibles.  
4. **Siguiente ciclo recomendado:** compartir la consigna textual de Actividad 1 para convertir esta base en version final (con problema juridico concreto, marco normativo especifico y producto solicitado).
