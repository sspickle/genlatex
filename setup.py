from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(name='genlatex',
      version='0.14',
      description='A simple template based doc generator',
      long_description=long_description,
      long_description_content_type='text/markdown',
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
