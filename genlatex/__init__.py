"""
The `genlatex` module is for creating LaTeX documents from Jijna2 templates.
"""

version = '0.23'

from .genLatex import main
from .formatters import latex_float, latex_vec, eunits
from .texData import TeXData
