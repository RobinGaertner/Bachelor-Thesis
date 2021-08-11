Thesis Template
===================

1) BUILD INSTRCUTIONS
---------------------

This template supports two build modes:
    a) with a hash (default)
    b) without a hash
For both modes can be build using `make`.
The default can be changed in the makefile

  a) The mode with the hash adds a small version string to the document (on the second page) and to the output filename as well (so that you will not overwrite earlier builds).
     This mode is meant to keep track of possibly lots of different versions of the document.
     One should be aware, that not overwriting the existing output files can result large disk usage.
     This can be avoided by setting the `JOBNAME` in the makefile to a static value or by cleaning (e.g. `make clean`) the output directory regularly.
     NOTE that the version/hash vill only regard files, which match the file ending specified in `HASHopt`(see makefile). If you want other filetypes to be regarded add the fileending here.
     NOTE: The produced version string has (for usability reasons) a very limited length and can therefore not be seen as a cryptographic hash function i.e. might produce collisions.

  b) Building the document without the hash/version string can be done using `make woHash`.
     This will just run `pdflatex` once, then `bibtex` and to finish it `pdflatex` 3 more times.

For both mode the output files should be produced in the `OUTDIR` (default out/).
There are some latex packages, that depend on the output files of pdflatex. For these it might be necessary to configure the output director


1.1 Custom Latex Editor
-----------------------

For the use for any sort of latex editor make sure to set Thesis.tex to be the main file and to set the output directory to your liking.
Be aware, that unless you set the build command the produced document will not include the version string.


 
2) Files and Directories
------------------------

  - Missing Packages/
    Legacy directory for some tweeks on latex packages.
    Should not be altered without a deep understanding on latex packages.  

  - out/
    The build directory for the document.
    All produces output files SHOULD end up here
    The output directory can be changed in the makefile (OUTDIR)

  - res/
  | Directory for non-latex resources such as source code or graphics
  |
  | - res/code
  |   Directory for source code, which will be included in the main document
  |
  | - res/Figures
      Directory for graphics.
      In the main latex file `Thesis.tex` this is set to be the `graphicspath` so all paths to graphics are interpreted relative to this directory

  - sbin/
  | Directory for some custom scripts used for building the document
  | 
  | - custompdflatex.py
  |   Python script which allows to define custom tex variables without altering the tex files.
  |   This can for example be useful to generate customized exams, etc.
  |   It is used here to add a hash of all files, used to generate the document, as a version string to the document.
  | 
  | - texhash.py
      Python script which calculates a hash (currently SHA-512) of multiple files which match the specified file endings.

  - src/
  | Main directory for latex code of the document
  | 
  | - Appendices/
  |   Directory to add the latex code for possible appendices
  |
  | - Chapters/
  |   Directoy all main chapters of the document
  |
  | - Presection/
  | | Directory for the presections such as abstract, acknowledgements, declaration, dedication
  | |
  | | - abstract.tex
  | |   Abstract of the thesis
  | |
  | | - acknowledgement.tex
  | |   Acknowledgements of the thesis
  | |
  | | - declaration.tex
  | |   Statement in Lieu of an Oath and Declaration of Consent
  | |
  | | - dedication.tex
  | |   Dedication of the thesis
  |  
  | - Bibligraphy.bib
  |   file for all references of the thesis (see bibtex)
  | 
  | - definitions.tex
  |   File meant to define custom latex commands, that might be used in various parts of the document

  - makefile
    Main makefile for the document
  
  - Thesis.tex
    Main latex file of the document.
    Fill in the general information about the thesis here (e.g. title, author name, ...).
    Also this is the place where presections, chapters, and appecdices are put together.
  
  - Thesis_template.zip
    Content of this directory just as an easy to distribute zip file
    
3) Contact
----------
For questions, problems, and/or suggestions for improvement feel free to write an email to Joshua Steffensky <joshua.steffensky@cispa.saarland>
