<!-- -*- mode: markdown; mode: flyspell; mode: auto-fill -*- -->

# Introduction

## Who am I?

* MSc from National University of Colombia

* Heavy Mathematica user and developer for 6 years

* C++ programmer for 3 years

* Python user since 2006

* Spyder contributor since 2010


## The Spyder IDE

* Created by Pierre Raybaut

* Started in 2009

* 30000 LOC

* Multiplatform
    
    - Developed with Qt
    - Native Mac App
    - Great support on Windows: Python(x,y) / WinPython

* Next version (2.3) will have support for Python 3


## Why a scientific IDE?

\centering\includegraphics[width=2cm]{images/ipython-console.png}

<!-- IPython has been the **traditional** entry point to the Python Scientific
    Stack -->

* IPython is **great**!

\pause

* **But** a great way to **evaluate** and **document** your code

* It's too **command-line** oriented

* We need a simpler, more intuitive tool
  
      - To gain **wider adoption**
      - For **teaching**

<!-- ----------------------------------------------- -->

# Complementing IPython

## Configuration

\newcommand{\spyPrefs}{\includegraphics[width=4.0cm]{images/spy_prefs.png}}
\newcommand{\ipyPrefs}{\includegraphics[width=4.0cm]{images/ipy_prefs.png}}

\centering{\spyPrefs \quad \quad \ipyPrefs}

### IPython
  
- **Need** `ipython create profile`
- Lots of options, some repeated
- Only apply on application **restart**

\pause

### Spyder

- Fewer but more relevant options
- Read IPython options too
- Apply on new consoles


## Sympy



## Ease of connection to external kernels


<!-- ----------------------------------------------- -->

# Beyond IPython (now)

## An Integrated Editor

editor-img

* Great code completion (on imports too) $\Longrightarrow$ \keystroke{Ctrl}+ \keystroke{Space}

* Flags errors and warnings

* Connected to IPython consoles

* Quick access to docs  $\Longrightarrow$ \keystroke{Ctrl}+ \keystroke{I}

* Go to definition $\Longrightarrow$ \keystroke{Ctrl}+ \keystroke{Left click}+ `name`


## Variable Explorer

------ ----------------
ve-img array-editor-img
------ ----------------

* Easily inspect variables defined in each console

* Edit them graphically

* Plot them


## Interactive help

oi-img

* Docstrings in rich text (with Sphinx)

* Easily copy/paste doctests

* Render Latex (through MathJax)


## Debugging

-------------- ----------------------
db-toolbar-img breakpoints-plugin-img
-------------- ----------------------

* Debug toolbar

* Connected to the Editor

* Check all your breakpoints


<!-- ----------------------------------------------- -->

# Beyond IPython (in the future)

## Better Help / Documentation Center

mma-doccenter-img

* Add docs for the main language keywords (`if`, `for`, `yield`, etc)

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
