class TeXData:
    """
    Class to keep a set of data for rendering a LaTeX template

    name: the name of the dataset
    fileNameTemplate: a template to generate the filename for the LaTeX file.  Needs a slot for the file number (a string)
    templateData: a dictionary with template data. Each key should have a list of dicts with data

    templateData = {'data':[{'a':3, 'b':2}, {'a':9, 'b':12}, ...], 'answers':[{'c':5}, {'c':21}, ...}]}
    """

    def __init__(self, name, fileNameTemplate, templateData):
        self.name = name
        self.fileNameTemplate = fileNameTemplate
        self.templateData = templateData

    def getSize(self):
        """
        take a stab at determining the size of the template data.
        assume each key has a list of the same length. It must!
        """
        keys = list(self.templateData.keys())
        result = 0
        if keys:
            result = len(self.templateData[keys[0]])
        return result

