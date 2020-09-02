echo removing log, and aux files plus the __pycache__ directory

find . \( -name "*.log" -o -name "*.aux"  \) -exec rm {} \; -print

find . -name __pycache__ -exec rm -r {} \; -prune
