# Templating with LaTex and Python

This year I'm trying to generate quizzes automatically to the degree possible.

I've cooked up a templating scheme using [jijna2](https://jinja.palletsprojects.com/en/2.11.x/)

This [article](http://eosrei.net/articles/2015/11/latex-templates-python-and-jinja2-generate-pdfs) was very helpful.

To get started create a virtual environment:

    python -m venv venv

    source venv/bin/activate  # mac/linux
    ./venv/Scripts/activate.bat # windows

    pip install -r requirements.txt

Once you have that, you can run getLatex using:

    python genLatex.py [ options ] path/to/python/file.py

For example to create 10 versions of tlo-1v2 you'd say:

    python genLatex.py -n 10 tlo-2v1/tlo2v1Data.py

Then check in the tlo-2v1 folder for your .tex files!

To convert to pdf en-masse, with bash:

    find tlo-2v1/*.tex |  xargs -n 1 pdflatex -output-directory tlo-2v1

To export to a .zip for import into an assessment first copy the pdf files to 
a staging directory for zipping.

    cp tlo-2v1/*.pdf export/output/attachment/genlatex/quizzes/contents/
    
Next cd into export and run the `buildZip.sh` script.

    cd export
    sh buildZip.sh
    
There should be an 'export.zip' file in the 'export' directory.

I'm no longer keeping quiz sources in this repo, for obvious reasons!

Students are smart. ;-)




