Debug Demo Files
================

debug_demo.ipynb: The main IPython notebook that describes the problem at hand.
debug_loop.py: The data processing loop, broken out as a small srcipt.

Demo Flow
=========

Launch IPython notebook on debug_demo.ipynb. Run all the cells up to the data processing one.
Switch over to Spyder, and open up an IPtyhon console connected to the notebook kernel.
Either open debug_loop.py in the editor or copy and paste the loop into an empty editor.
Start debugging the loop in the notebook kernel while preserving access the the kernel's
global workspace by running:

	%run -i -d "c:\src\scipy-2013-talk\debug_demo\debug_loop.py"

in the IPython console. Now Spyder's debugging step icons or keyboard shortcuts can 
be used to advance the debugging process. Variables have to be inspected from the
command line since the Variable Explorer is not capable of connecting to an external
kernel workspace. Debug as far as you would like, then quit the debugging session.
Return to the notebook and run the rest of the data processing to completion by
excuting the data processing cell.

