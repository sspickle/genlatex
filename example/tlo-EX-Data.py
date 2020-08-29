
import random
import vpython as vp
import numpy as np

data = []

"""
naming convention. 

tlo: this is the prefix to all the templates, and to the .tex outputs

e.g., if you're working on TLO-3 and this is the third quiz you've
given, you might say "tlo = 'TLO-3v3' and then the template would
be 'TLO-3v1-template.txt' and the .tex files would be:

'TLO-3v1-XX.tex' and
'TLO-3v1-soln-XX.tex' 

where 'XX' would be a quiz version number based on the random numbers
used to create the problem/solution pairs.

"""

tlo='TLO-EX'
templateFile = tlo + '-template.txt'
quizFilenameTemplate = tlo + '-{:}.tex'
quizSolnFilenameTemplate = tlo + '-soln-{:}.tex'

qe = 1.6e-19
G = 1.67e-11

#
# --- these functions are for formatting floats and vecs in LaTeX ---
#

def latex_float(f, fmt="{0:.3g}"):
    #
    # convert scientific formats to LaTeXish.
    #
    
    float_str = fmt.format(f)
    if "e" in float_str:
        base, exponent = float_str.split("e")
        return r"{0} \times 10^{{{1}}}".format(base, int(exponent))
    else:
        return float_str
        
def latex_vec(v, fmt="{0:.3g}"):
    #
    # create a nice M&I vector object
    # v should be a vpython vec/vector object.
    #
    
    v = f"<{latex_float(v.x,fmt)},{latex_float(v.y,fmt)},{latex_float(v.z,fmt)}>"
    v = v.replace('<',r'\langle')
    v = v.replace('>',r'\rangle')
    return v

#
# --- this is where the random values are set up --
#

rint = random.randint
uni = random.uniform

def getTemplateValues(numSamples, seeds):
    """
    input:
        numSamples: Integer, number of random Versions to generate.
        seeds: a list of integers to act as random number seeds.
            This allows you to re-create the same values reproducibly.
            If you send in the same integer, you get the same values again.
            
    output:
        A dictionary of data, answers, and the template filenames
        (see below for details)
        
    This example creates a random planet, star mass and position.
    """
    
    data = []
    answers = []

    for i in range(numSamples):
    
        random.seed(seeds[i]) # make these reproducible, but randomish

        Mstar = uni(0.6,1.0)*2e30
        Mplanet = random.randint(2,9)*1e26
        rStar = vp.vec(rint(-8,8),rint(-8,8),rint(-8,8))*1e11
        rPlanet = vp.vec(rint(-8,8),rint(-8,8),rint(-8,8))*1e11
        
        MstarStr = latex_float(Mstar) + r'\,{\rm kg}'
        MplanetStr = latex_float(Mplanet) + r'\,{\rm kg}'
        rStarStr = latex_vec(rStar) + r'\,{\rm m}'
        rPlanetStr = latex_vec(rPlanet) + r'\,{\rm m}'
        
        dt = uni(0.8,1.2)*30*3600*24  # around one month
        dtStr = latex_float(dt) + r'\,{\rm s}'
        
        r = rPlanet - rStar
        rStr = latex_vec(r) + r'\,{\rm m}'
        
        rhat = r.norm()
        rHatStr = latex_vec(rhat)
        
        # let's work out a circular orbit speed
        
        v = np.sqrt(G*Mstar/r.mag)
        vPlanet = r.cross(vp.vec(0,0,1)).norm()*v # pick a good perp. direction
        vPlanetStr = latex_vec(vPlanet) + r'\,{\rm m/s}'

        newData = {}
        newData.update(vnum= str(seeds[i]).zfill(2))
        newData.update(tlo=tlo, dt=dtStr)
        newData.update(Mstar=MstarStr)
        newData.update(Mplanet=MplanetStr)
        newData.update(rStar=rStarStr)
        newData.update(rPlanet=rPlanetStr)
        newData.update(vPlanet=vPlanetStr)

        data.append(newData)
        
        F = -G*Mplanet*Mstar*r.norm()/r.mag**2
        p = Mplanet*vPlanet
        dp = F*dt
        pnew = p + dp
        vnew = pnew/Mplanet
        
        Fstr = latex_vec(F) + r'\,{\rm N}'
        pStr = latex_vec(p) + r'\,{\rm N s}'
        dPstr = latex_vec(dp) + r'\,{\rm N s}'
        vNewStr = latex_vec(vnew) + r'\,{\rm m/s}'
        rNew = rPlanet + vnew*dt
        rNewStr = latex_vec(rNew) + r'\,{\rm m}'
        
        newAnswer = {}
        newAnswer.update(F=Fstr, p=pStr, dp=dPstr)
        newAnswer.update(r=rStr, rhat=rHatStr)
        newAnswer.update(vNew = vNewStr)
        newAnswer.update(rNew = rNewStr)

        answers.append(newAnswer)

    def returnDict(**kwargs):
        return kwargs
        
    return returnDict(data = data,
                      answers = answers,
                      templateFile = templateFile,
                      quizFilenameTemplate = quizFilenameTemplate,
                      quizSolnFilenameTemplate = quizSolnFilenameTemplate)

