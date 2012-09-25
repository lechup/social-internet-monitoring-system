# makefile for pdflatex
# run to make praca.pdf
# requirements:
# pdflatex
# bibtex

all: praca

praca: praca.tex
	pdflatex praca.tex
	bibtex praca.aux
	pdflatex praca.tex
	pdflatex praca.tex

clean:
	rm -rf *.aux
	rm -rf *.toc
	rm -rf *.log
	rm -rf *.bbl
	rm -rf *.blg

watch:
	@echo "\n${HR}"
	@echo "Watching directory ./"
	@echo "${HR}"
	@echo "\n"
	@watchmedo shell-command -c "make" -p "*.tex" ./
