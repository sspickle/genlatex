
echo python genLatex.py --num 10 --prompt src/$1

/bin/bash buildTeXs.sh

/bin/bash buildPDFs.sh

/bin/bash buildZip.sh

