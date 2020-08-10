
import mendeleev
import random
import vpython as vp

allElements = mendeleev.elements.get_all_elements()

data = []

qe = 1.6e-19
oofpez = 9e9

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
        xValNuc = random.choice([6,5,4])
        yValNuc = random.choice([1,2,3])
        zValNuc = random.choice([-2,-3,-4])
        
        xValFP = random.choice([7,6,5])
        yValFP = random.choice([1,2,3])
        zValFP = random.choice([3,4,5])
        
        qVal = random.choice([-12,-15,+7,9,12,15])
        
        posVec = vp.vec(xValNuc, yValNuc, zValNuc)
        fpVec = vp.vec(xValFP, yValFP, zValFP)

        newData = {
            'vnum':str(seeds[i]).zfill(2),
            'name':element.name,
            'protons':element.atomic_number,
            'neutrons':element.neutrons,
            'mNum':element.mass_number,
            'mass':element.mass_number*1e-3/6e23,
            'qStr1':str(qVal),
            'qStr2':latex_float(qVal*1e-9),
            'posStr':f'{xValNuc}, {yValNuc}, {zValNuc}',
            'fpStr':f'{xValFP}, {yValFP}, {zValFP}',
        }
        data.append(newData)

    answers = []

    def returnDict(**kwargs):
        return kwargs
        
    return returnDict(data = data,
                      answers = answers,
                      templateFile = 'TLO-2v2-template.txt',
                      quizFilenameTemplate = 'TLO-2v2-{:}.tex',
                      quizSolnFilenameTemplate = 'TLO-2v2-soln-{:}.tex')

