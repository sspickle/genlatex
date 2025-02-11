#
# Assume everything is in src
#

find src/ -name "*.tex" | xargs -n 1 pdflatex -output-directory src/.

