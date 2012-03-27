# makefile for pdflatex
# run to make praca.pdf
# requirements:
# pdflatex
# bibtex

all: sample-userstory

sample-userstory: sample-userstory.tex
	pdflatex sample-userstory.tex
	pdflatex sample-userstory.tex

clean:
	rm -rf *.aux
	rm -rf *.toc
	rm -rf *.pdf
	rm -rf *.log
	rm -rf *.bbl
	rm -rf *.blg
