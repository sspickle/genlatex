# Templating with LaTex and Python

This year I'm trying to generate quizzes automatically to the degree possible.

I've cooked up a templating scheme using [jijna2](https://jinja.palletsprojects.com/en/2.11.x/) that works with LaTeX templates.

This [article](http://eosrei.net/articles/2015/11/latex-templates-python-and-jinja2-generate-pdfs) was very helpful.

Now that this has been published to pypi you can simply:

pip install genlatex

Once you have that, you can 'cd' to the directory with your template and data generator file and run getlatex using:

    genlatex [ options ] dataGeneratorFile.py

For example to create 10 versions of the example you could:

    cd example

    genlatex -n 10 tlo-EX-Data.py

Then check in the folder for your .tex files!

To convert to pdf en-masse, with bash:

    find *.tex |  xargs -n 1 pdflatex

If your dataGeneratorFile needs to import any modules you should add '.' to the PYTHONPATH, e.g.,

    PYTHONPATH=. genlatex -n 10 tlo-EX-Data.py

There is a shell script "buildZip.sh" that creates an importable .zip file that can be used to import quizzes into Sakai. It may also work for other LMS variations. Untested!

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

    v 0.14: add units to latex_float and latex_vec, add some doc tests.

    v 0.15: Changed the path handling to make it more Windows friendly.
