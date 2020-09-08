"""
format things for LaTeX
"""

def listish(x):
    result = True
    try:
        len(x)
    except TypeError:
        result = False
    
    return result

def latex_float(f, fmt="{0:.3g}"):
    """
    convert scientific formats to LaTeXish.
    """
    
    float_str = fmt.format(f)
    if "e" in float_str:
        base, exponent = float_str.split("e")
        return r"{0} \times 10^{{{1}}}".format(base, int(exponent))
    else:
        return float_str
        
def latex_vec(v, fmt="{0:.3g}"):
    """
    v could be a vpython vec/vector object, or an iterable
    """
    if not listish(v):
        v = (v.x, v.y, v.z) # it must be a vpython vector, convert to tuple
    v = f"<{latex_float(v[0], fmt)},{latex_float(v[1], fmt)},{latex_float(v[2], fmt)}>"
    v = v.replace('<',r'\langle')
    v = v.replace('>',r'\rangle')
    return v
