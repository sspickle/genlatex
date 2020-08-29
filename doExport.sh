
echo python genLatex.py --num 10 --prompt src/$1

python genLatex.py --num 10 --prompt src/$1

find src/ -name "*.tex" | xargs -n 1 pdflatex -output-directory src/.

cp src/*.pdf export/output/attachment/genlatex/quizzes/contents/

cd export && sh buildZip.sh && cd ..

sh clean.sh





