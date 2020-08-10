echo removing pdf files

find . -name output -prune -o -name "*.pdf" -exec rm {} \; -print

echo removing log, aux, and tex files

find . -name "*.log" -o -name "*.aux" -o -name "*.tex" -exec rm {} \; -print

