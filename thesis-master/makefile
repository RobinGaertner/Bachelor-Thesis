PDFLATEX=pdflatex
BIBTEX=bibtex

OUTDIR=out
SHELL=/bin/bash

HASHopt=--recursive .tex .cls .py .bib
HASHlength=8
HASHexe=python2 sbin/texhash.py

CUSTOMPDFBUILDER=python2 sbin/custompdflatex.py
PDFLATEXopts=-synctex=1 -interaction=nonstopmode -shell-escape -output-directory=$(OUTDIR)

MAINFILE=Thesis.tex

.PHONY: default
default: withHash


.PHONY: withHash
withHash: calcHash
	$(eval JOBNAME := $(shell echo thesis_$(HASH)))
	$(CUSTOMPDFBUILDER) "texhash=$(HASH)" -- $(PDFLATEXopts) -jobname=$(JOBNAME) ?? $(MAINFILE)
	$(BIBTEX) $(OUTDIR)/$(JOBNAME).aux
	$(CUSTOMPDFBUILDER) "texhash=$(HASH)" -- $(PDFLATEXopts) -jobname=$(JOBNAME) ?? $(MAINFILE)

.PHONY: woHash
woHash:
	$(PDFLATEX) $(PDFLATEXopts) $(MAINFILE)	
	$(BIBTEX) $(OUTDIR)/$(patsubst %.tex,%.aux,$(MAINFILE))
	$(PDFLATEX) $(PDFLATEXopts) $(MAINFILE)
	$(PDFLATEX) $(PDFLATEXopts) $(MAINFILE)
	$(PDFLATEX) $(PDFLATEXopts) $(MAINFILE)



.PHONY: calcHash
calcHash:
	$(eval HASH := $(shell $(HASHexe) $(HASHopt) | cut -c1-$(HASHlength)))
	echo "$(HASH)"


.PHONY: clean
clean:	
	find $(OUTDIR) -type f ! -name '*.pdf' -delete

.PHONY: wipe
wipe:
	rm $(OUTDIR)/*

.PHONY: tidy
tidy: clean
	cd $(OUTDIR);\
	ls -t | tail -n +2 | xargs rm --
	
%.tex:
	$(eval MAINFILE := $(shell echo "$@")
	default
