# AulaTeX stage

- Etapa: generar
- Rol: Arquitecto de plantillas
- Mision: proponer estructura de reporte/presentacion y actividad
- Motor: Codex
- Estado: ok

```latex
% =========================================================
% ARCHIVO 1: reporte-derecho-a-la-seguridad-social-act1.tex
% Actividad 1 | LDE-S2B1 | UnADM
% Supuesto: no se proporciono consigna especifica de Actividad 1.
% Se entrega plantilla base editable alineada al programa analitico.
% =========================================================
\documentclass[spanish,letterpaper,oneside]{article}

\def\documenttitle{Actividad 1 - Derecho a la seguridad social}
\def\documentsubtitle{Plantilla editorial con control academico}
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
    \textbf{Alumno:} & [Tu nombre completo] \\
    Matricula: & [Tu matricula] \\
    Figura docente: & [Nombre de la figura docente] \\
    Semestre/Bloque: & 2 / 1 \\
    Tipo/Creditos: & Obligatoria / 8 \\
    Fecha de realizacion: & \today \\
    Sede de referencia: & \universitylocation
  \end{tabular}
}

\input{template}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{babel}
\usepackage{helvet}
\renewcommand{\familydefault}{\sfdefault}
\usepackage{array,longtable,pdflscape,tikz}
\usetikzlibrary{arrows.meta,positioning,calc,matrix,fit,shapes.geometric,shadows.blur}
\setcitestyle{authoryear,open={(},close={)}}

% Control visual institucional
\def\coverwatermarkenabled{true}
\def\coverwatermarkimage{img/departamentos/UnADM.pdf}
\def\coverwatermarkopacity{0.14}
\def\coverwatermarkwidth{0.70\paperwidth}
\def\coverwatermarkxshift{0cm}
\def\coverwatermarkyshift{-0.30cm}

\newcommand{\insertcoverwatermark}{%
  \ifthenelse{\equal{\coverwatermarkenabled}{true}}{%
    \AddToShipoutPictureBG*{%
      \begin{tikzpicture}[remember picture,overlay]
        \node[opacity=\coverwatermarkopacity,inner sep=0pt,
        xshift=\coverwatermarkxshift,yshift=\coverwatermarkyshift]
        at (current page.center)
        {\includegraphics[width=\coverwatermarkwidth]{\coverwatermarkimage}};
      \end{tikzpicture}
    }
  }{}
}

\newcommand{\pendiente}[1]{\textcolor{red}{[PENDIENTE: #1]}}

\begin{document}
\insertcoverwatermark
\templatePortrait
\templatePagecfg
\onehalfspacing

\begin{abstractd}
Plantilla de la \textbf{Actividad 1} para \textit{Derecho a la seguridad social}
(UnADM, LDE-S2B1). Integra: problema juridico-social, fundamentos,
analisis propio, producto academico y conclusion transferible.
\textbf{Supuesto declarado:} al no contar con consigna puntual, se propone
estructura canonica editable conforme al programa analitico.
\end{abstractd}

\templateIndex
\templateFinalcfg

\section{Datos de la actividad}
\begin{itemize}
  \item Asignatura: Derecho a la seguridad social.
  \item Clave: LDE-S2B1.
  \item Ubicacion curricular: Semestre 2, Bloque 1.
  \item Producto: Reporte academico argumentativo.
  \item Consigna recibida: \pendiente{Pegar literal de aula virtual.}
\end{itemize}

\section{Problema juridico o social}
\pendiente{Formular en 1 parrafo el problema que activa la actividad.}

\section{Objetivo y alcance}
\pendiente{Definir objetivo general y limites del analisis (temporal, normativo y material).}

\section{Desarrollo conceptual y normativo}
\subsection{Conceptos clave}
\pendiente{Definir conceptos doctrinales centrales con cita.}

\subsection{Marco normativo aplicable}
\pendiente{Incorporar normas, principios o criterios relevantes con referencia verificable.}

\subsection{Analisis propio}
\pendiente{Contrastar norma y realidad; exponer postura personal argumentada.}

\section{Producto solicitado / evidencia}
\pendiente{Insertar cuadro, matriz, mapa conceptual o sintesis segun consigna.}

\section{Conclusion transferible}
\pendiente{Cerrar con consecuencia juridica y aplicacion practica profesional.}

\section{Control editorial de calidad (checklist)}
\begin{itemize}
  \item Problema delimitado y congruente con la consigna.
  \item Uso de fuentes verificables y citas consistentes.
  \item Diferencia clara entre descripcion y analisis propio.
  \item Identidad institucional UnADM visible en forma y fondo.
  \item Conclusion con criterio juridico, no solo resumen.
\end{itemize}

\clearpage
\nocite{unadmSitioWeb,unadmMallaDerecho2024}
\bibliography{derecho-a-la-seguridad-social}
\end{document}
```

```latex
% =========================================================
% ARCHIVO 2: presentacion-derecho-a-la-seguridad-social-act1.tex
% =========================================================
\documentclass[spanish,aspectratio=169,xcolor={dvipsnames,table}]{beamer}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[spanish,es-tabla]{babel}
\usepackage[scaled=.96]{helvet}
\renewcommand{\familydefault}{\sfdefault}
\usepackage{graphicx,booktabs,tikz,hyperref}
\usetikzlibrary{calc,positioning,fit,shadows.blur}

\newcommand{\studentname}{[Tu nombre]}
\newcommand{\studentid}{[Tu matricula]}
\newcommand{\universityname}{Universidad Abierta y a Distancia de Mexico}
\newcommand{\facultyname}{Licenciatura en Derecho}
\newcommand{\coursename}{Derecho a la seguridad social}
\newcommand{\coursecode}{LDE-S2B1}
\newcommand{\activitytitle}{Actividad 1 - Plantilla base}
\newcommand{\activitysubtitle}{Problema, fundamento y postura juridica}
\newcommand{\teachingfigure}{[Figura docente]}
\newcommand{\deliverydate}{\today}
\newcommand{\departmentlogo}{img/departamentos/UnADM.pdf}

\definecolor{unadmGreenDark}{HTML}{174A3A}
\
