
from .texData import TeXData

def ConvertOldStyleDataGenerator( templateValues ):
    # old style data generator
    data = templateValues['data']
    answers = templateValues['answers']
    templateFile = templateValues['templateFile']
    quizFilenameTemplate = templateValues['quizFilenameTemplate']
    quizSolnFilenameTemplate = templateValues['quizSolnFilenameTemplate']
    
    promptData = {'data': data }
    promptDataSet = TeXData('prompt', quizFilenameTemplate, promptData)
    answerData = {'data': data, 'ans': answers}
    answerDataSet = TeXData('answers', quizSolnFilenameTemplate, answerData)

    return templateFile, [promptDataSet, answerDataSet]
