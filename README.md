# Templating with LaTex and Python

This year I'm trying to generate quizzes automatically to the degree possible.

I've cooked up a templating scheme using [jijna2](https://jinja.palletsprojects.com/en/2.11.x/)

This [article](http://eosrei.net/articles/2015/11/latex-templates-python-and-jinja2-generate-pdfs) was very helpful.

To get started clone this repository, and create a virtual environment:

    git clone https://github.com/sspickle/genlatex.git

    cd genlatex

    python -m venv venv

    source venv/bin/activate  # mac/linux
    ./venv/Scripts/activate.bat # windows

    pip install -r requirements.txt

    pip install .

Once you have that, you can 'cd' to the directory with your template and data generator file and run getlatex using:

    genlatex [ options ] dataGeneratorFile.py

For example to create 10 versions of the example you could:

    cd example

    genlatex -n 10 tlo-EX-Data.py

Then check in the example folder for your .tex files!

To convert to pdf en-masse, with bash:

    find *.tex |  xargs -n 1 pdflatex

To export to a .zip for import into an assessment first copy the pdf files to 
a staging directory for zipping.

    cp tlo-2v1/*.pdf ../export/output/attachment/genlatex/quizzes/contents/
    
Next cd into export and run the `buildZip.sh` script.

    cd ../export
    sh buildZip.sh
    
There should be an 'export.zip' file in the 'export' directory.

I'm no longer keeping quiz sources in this repo, for obvious reasons!

Students are smart. ;-)

Update: Now you can run the full docker (Dockerfile-w-latex) version:

    docker run --rm -it -v `pwd`:/work/src genlatex-full doExport.sh -n 10 tlo-EX-Data.py

Or the mini-docker (Dockerfile)

    docker run --rm -it -v `pwd`:/work/src genlatex buildTeXs.sh -n 10 tlo-EX-Data.py

to build the mini-docker (without a full LaTeX install ~1.4GB)

    docker build -t genlatex .

to build the full docker build (with a full LaTeX install ~7GB)

    docker build -f Dockerfile-w-latex -t genlatex-full .

CHANGES:

	v 0.12: Added units to formatters (e.g., latex_float(2.31, units="m"))
	