from setuptools import setup

setup(name='genlatex',
      version='0.10',
      description='A simple template based doc generator',
      url='https://github.com/sspickle/genlatex',
      author='Steve Spicklemire',
      author_email='steve@spvi.com',
      license='MIT',
      packages=['genlatex'],
      install_requires=[
          'Jinja2',
      ],
      zip_safe=False,
      entry_points = {
          'console_scripts': ['genlatex=genlatex.genLatex:main'],
      },
)
