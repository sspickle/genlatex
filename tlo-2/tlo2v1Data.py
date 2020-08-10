
import mendeleev
import random

allElements = mendeleev.elements.get_all_elements()

data = []

qe = 1.6e-19

def latex_float(f):
    float_str = "{0:.2g}".format(f)
    if "e" in float_str:
        base, exponent = float_str.split("e")
        return r"{0} \times 10^{{{1}}}".format(base, int(exponent))
    else:
        return float_str

def getTemplateValues(numSamples, seeds):

    for i in range(numSamples):
    
        random.seed(seeds[i]) # make these reproducable, but randomish

        element = random.choice(allElements)
        aVal = random.choice([2,3,4,5,6,7,8,9])
        direction = random.choice(['right','left'])

        newData = {
            'vnum':str(seeds[i]).zfill(2),
            'name':element.name,
            'protons':element.atomic_number,
            'neutrons':element.neutrons,
            'mNum':element.mass_number,
            'mass':element.mass_number*1e-3/6e23,
            'aVal':aVal,
            'a':aVal*1e13,
            'aDir':direction,
        }
        newData.update({
            'qStr':latex_float(qe*newData['protons']),
            'aStr':latex_float(newData['a']),
            'mStr':latex_float(newData['mass']),
            })
        data.append(newData)

    answers = []

    for d in data:
        eDir = d['aDir']
        m = d['mass']
        a = d['a']
        q = d['protons']*qe
        E = m*a/q
        answers.append({'a':eDir, 'E':f"{E:4.3e}"})

    def returnDict(**kwargs):
        return kwargs
        
    return returnDict(data = data,
                      answers = answers,
                      templateFile = 'TLO-2v1-template.txt',
                      quizFilenameTemplate = 'TLO-2v1-{:}.tex',
                      quizSolnFilenameTemplate = 'TLO-2v1-soln-{:}.tex')

