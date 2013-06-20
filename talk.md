<!-- -*- mode: markdown; mode: flyspell; mode: auto-fill -*- -->

# Introduction

## Who am I?

* MSc from National University of Colombia

* Heavy Mathematica user and developer for 6 years

* C++ programmer for 3 years

* Python user since 2006

* Spyder contributor since 2010


## The Spyder IDE

\newcommand{\spyLogo}{\includegraphics[width=2.3cm]{images/spy_logo.png}}
\newcommand{\Pierre}{\includegraphics[width=2.3cm]{images/Pierre.png}}

\centering{\spyLogo \qquad \qquad \Pierre}

* Created by **Pierre Raybaut**

* Started in **2009**

* **30000** LOC

* Multiplatform
    
    - Developed with **Qt**
    - **Native** Mac App
    - Great support on **Windows**: Python(x,y) / WinPython

* Next version (2.3) will have support for **Python 3**


## Why a scientific IDE?

\centering\includegraphics[width=2cm]{images/ipython-console.png}

<!-- IPython has been the **traditional** entry point to the Python Scientific
    Stack -->

* IPython is **great**!

    \pause

* A great way to **evaluate** and **document** your code

    \pause

* **Nicer** if it would be:
    
    - Less dependent on the **command-line**
    - **Easier** to configure
    - More **integrated** with other tools
      
    \pause
     
* Spyder tries to do that!

    - By **embedding** and **complementing** it

<!-- ----------------------------------------------- -->

# Easing IPython

## Configuration

\newcommand{\spyPrefs}{\includegraphics[width=5cm]{images/spy_prefs.png}}
\newcommand{\ipyPrefs}{\includegraphics[width=5cm]{images/ipy_prefs.png}}

+---------------------------------------+---------------------------------------+
|                                       |                                       |
|  \centering{\ipyPrefs}                |  \centering{\spyPrefs}                |
|                                       |                                       |
|  - **Need** `ipython create profile`  |  - Set trough our **GUI**             |
|  - **Lots** of options                |  - **Fewer** but more relevant options|
|  - Only apply on **restart**          |  - Apply on **new** consoles          |
|                                       |                                       |
+---------------------------------------+---------------------------------------+


## Sympy

\newcommand{\sympy}{\includegraphics[width=5cm]{images/spy_sympy.png}}

+---------------------------------------+---------------------------------------+
|  **IPython**                          |  **Spyder**                           |
|                                       |                                       |
|  - `ipython create profile sympy`     |  \vspace{0.2cm}                       |
|  - `ipython qtconsole --profile sympy`|  \centering{\sympy}                   |
|                                       |                                       |
+---------------------------------------+---------------------------------------+


## Connection to external kernels

\newcommand{\kernels}{\includegraphics[width=5cm]{images/spy_ext_kernels.png}}

+---------------------------------------+---------------------------------------+
|  **IPython**                          |  **Spyder**                           |
|                                       |                                       |
|  - `ipython --existing`               |  \vspace{0.2cm}                       |
|  - `%qtconsole`                       |  \centering{\kernels}                 |
|  - No notebooks to external kernels   |                                       |
|                                       |                                       |
+---------------------------------------+---------------------------------------+


<!-- ----------------------------------------------- -->

# Complementing IPython (now)

## An integrated Editor

\centering{\includegraphics[height=3.8cm]{images/editor.png}}

* Great code completion (on imports too) $\Longrightarrow$ \keystroke{Ctrl}+ \keystroke{Space}

* Flags errors and warnings

* Connected to IPython consoles

* Quick access to docs  $\Longrightarrow$ \keystroke{Ctrl}+ \keystroke{I}

* Go to definition $\Longrightarrow$ \keystroke{Ctrl}+ \keystroke{Left click}+ `name`


## Variable Explorer

\newcommand{\varExp}{\includegraphics[height=4.0cm]{images/variable_explorer.png}}
\newcommand{\arrayEd}{\includegraphics[height=4.0cm]{images/array_editor.png}}

------- --------
\varExp \arrayEd
------- --------

* Easily inspect variables defined in each console

* Edit them graphically

* Plot them


## Interactive help

\centering{\includegraphics[height=4.8cm]{images/object_inspector.png}}

* Docstrings in rich text (with Sphinx)

* Easily copy/paste doctests

* Render Latex (through MathJax)


## Debugging

\newcommand{\dbToolbar}{\includegraphics[height=2.0cm]{images/db_toolbar.png}}
\newcommand{\bpsPlugin}{\includegraphics[width=5.2cm]{images/bps_plugin.png}}

+---------------------------------------+---------------------------------------+
|                                       |                                       |
|  \vspace{-2.3cm}                      |  \bpsPlugin                           |
|  \centering{\dbToolbar}               |                                       |
|                                       |                                       |
+---------------------------------------+---------------------------------------+

* Debug toolbar

* Connected to the Editor

* Check all your breakpoints


<!-- ----------------------------------------------- -->

# Complementing IPython (in the future)

## Better Help / Documentation Center

mma-doccenter-img

* Add docs for the language keywords (`if`, `for`, `yield`, etc)

* Add important tutorials/intros, like SciPy lectures

* Auto-linking to `docs.python.org`

* Search in docstrings (with `Whoosh`)

* Show Matplotlib plots

* Automatic translation to French, Spanish, etc.


## Notebook plugin

nb-img

* A real desktop application

* Connected to our other plugins

* We have a **prototype**, waiting for multi-directory support (IPEP 16)


## Package Manager

stallion-img

* `conda` for scientific packages

* `stallion` for everything else


## Thank You

\begin{center}
\LARGE{Questions?}
\end{center}



<!--  LocalWords:  Raybaut LocalWords Spyder IPython Multiplatform IDE LOC png
-->
<!--  LocalWords:  Mathematica WinPython Matlab ipython includegraphics Sympy
 -->

<!-- Local IspellDict: english -->
<!--  LocalWords:  newcommand spyLogo
 -->
