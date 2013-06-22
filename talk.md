<!-- -*- mode: markdown; mode: flyspell; mode: auto-fill -*- -->

# Introduction

## Who am I?

\centering{\textbf{@ccordoba12}}

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

* Next version will have support for **Python 3**


## Why a scientific IDE?

\centering\includegraphics[width=2cm]{images/ipython-console.png}

<!-- IPython has been the **traditional** entry point to the Python Scientific
    Stack -->

* If IPython is **great**

    \pause

* A great way to **evaluate** and **document** your code

    \pause

* **Nicer** if it'd be:
    
    - Less dependent on the **command-line**
    - **Easier** to configure
    - More **integrated** with other tools
      
    \pause
     
* **Also** to gain **wider adoption**

    - Compete with the big M's: **Matlab** and **Mathematica**

<!-- ----------------------------------------------- -->

# Easing IPython

## Configuration

\newcommand{\spyPrefs}{\includegraphics[width=5cm]{images/spy_prefs.png}}
\newcommand{\ipyPrefs}{\includegraphics[width=5cm]{images/ipy_prefs.png}}

+---------------------------------------+---------------------------------------+
|                                       |                                       |
|  \centering{\ipyPrefs}                |  \centering{\spyPrefs}                |
|                                       |                                       |
|  - Edit **plain-text** files          |  - Set through our **GUI**            |
|  - **Lots** of options                |  - **Fewer** but more relevant options|
|  - Only apply on **restart**          |  - Apply on **new** consoles          |
|                                       |                                       |
+---------------------------------------+---------------------------------------+


## Sympy

\newcommand{\sympy}{\includegraphics[width=5.5cm]{images/spy_sympy.png}}

+---------------------------------------+---------------------------------------+
|  **IPython**                          |  **Spyder**                           |
|                                       |                                       |
|  - `ipython create profile sympy`     |  \vspace{0.2cm}                       |
|  - `ipython qtconsole --profile sympy`|  \centering{\sympy}                   |
|                                       |                                       |
+---------------------------------------+---------------------------------------+


## Connection to external kernels

\newcommand{\kernels}{\includegraphics[width=5.5cm]{images/spy_ext_kernels.png}}

+---------------------------------------+---------------------------------------+
|  **IPython**                          |  **Spyder**                           |
|                                       |                                       |
|  - `ipython --existing`               |  \vspace{0.2cm}                       |
|  - `%qtconsole`                       |  \centering{\kernels}                 |
|                                       |                                       |
+---------------------------------------+---------------------------------------+


<!-- ----------------------------------------------- -->

# Sharing with Matlab

## An integrated Editor

\centering{\includegraphics[height=3.8cm]{images/editor.png}}

* Great **code completion** (on imports too) $\Longrightarrow$
  \keystroke{Ctrl}+ \keystroke{Space}

* Flags **errors** and **warnings**

* **Connected** to IPython **consoles** for **evaluation**
    $\Longrightarrow$ \keystroke{F5} / \keystroke{F9}

* Quick access to **docs**  $\Longrightarrow$ \keystroke{Ctrl}+ \keystroke{I}

* **Go to definition** $\Longrightarrow$ \keystroke{Ctrl}+ \keystroke{Left click}+ `name`


## Variable Explorer

\newcommand{\varExp}{\includegraphics[height=4.5cm]{images/variable_explorer.png}}
\newcommand{\arrayEd}{\includegraphics[height=4.5cm]{images/array_editor.png}}

------- --------
\varExp \arrayEd
------- --------

* **Inspect** variables defined in **each console**

* **Check** and **edit** their contents **graphically**

* **More facilities**: plot, copy, remove variables, etc.


## Interactive help

\centering{\includegraphics[height=4.8cm]{images/object_inspector.png}}

* **Read** docstrings in **rich text** (with `Sphinx`)

* **Copy/paste doctests** to the Editor or Console

* **Show math** (with `MathJax`)


## Debugging

\newcommand{\dbToolbar}{\includegraphics[height=2.0cm]{images/db_toolbar.png}}
\newcommand{\bpsPlugin}{\includegraphics[width=5.5cm]{images/bps_plugin.png}}

+---------------------------------------+---------------------------------------+
|                                       |                                       |
|  \vspace{-2.5cm}                      |  \bpsPlugin                           |
|  \centering{\dbToolbar}               |                                       |
|                                       |                                       |
+---------------------------------------+---------------------------------------+

* **Debug toolbar** with `step over`, `step into`, `continue`, etc

* **Set breakpoints** in the Editor

* **Synced** with the Console

* **Check** all your **current breakpoints**


<!-- ----------------------------------------------- -->

# Getting closer to Mathematica

## Notebook plugin

nb-img

* Provide a **desktop friendly** version

* **Connected** to our other **plugins**

    \pause

* We already have a **prototype**

    - Waiting for multi-directory support to be merged


## Documentation Center

\newcommand{\mma}{\includegraphics[width=6.0cm]{images/mma_doc_center.png}}
\newcommand{\docsMma}{\includegraphics[width=4.4cm]{images/mma_docs.png}}

\mma \quad \docsMma

* Add important **tutorials/intros**, like `SciPy lectures`

* **Guides** to Spyder and IPython

* **Search** in docstrings (with `Whoosh`)

* **Auto-linking** to `docs.python.org`

<!-- * Docs for the **language keywords** (`if`, `for`, `yield`, etc) -->

<!-- * Automatic translation to French, Spanish, etc. -->


## A pretty interface for package managers

stallion-img

* `conda` for scientific packages

* `stallion` for everything else


## Thank You

\begin{center}
\LARGE{Questions?}
\end{center}


<!-- Local IspellDict: english -->


<!--  LocalWords:  Raybaut LocalWords Spyder IPython Multiplatform IDE LOC png
-->
<!--  LocalWords:  Mathematica WinPython Matlab ipython includegraphics Sympy
 -->
<!--  LocalWords:  newcommand spyLogo qquad spyPrefs ipyPrefs ipy prefs sympy
 -->
<!--  LocalWords:  varExp arrayEd qtconsole vspace Longrightarrow Ctrl MathJax
 -->
<!--  LocalWords:  Docstrings doctests dbToolbar bpsPlugin SciPy docstrings
 -->
<!--  LocalWords:  Matplotlib conda textbf ccordoba mma docsMma multi
 -->
