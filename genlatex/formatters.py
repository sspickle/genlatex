"""
format things for LaTeX
"""

def listish(x):
    """
    Does it smell like a list?
    >>> listish(1)
    False
    >>> listish((1,2,3))
    True
    >>> listish([1,2,3])
    True
    """
    result = True
    try:
        len(x)
    except TypeError:
        result = False
    
    return result

def latex_float(f, fmt="{0:.3g}", units=""):
    r"""
    convert scientific formats to LaTeXish.
    if units are specific, add them in roman font
    
    >>> latex_float(3.2)
    '3.2'
    >>> latex_float(3.2e-12)
    '3.2 \\times 10^{-12}'
    >>> latex_float(3.2e-12,units='km')
    '3.2 \\times 10^{-12}\\,{\\rm km}'
    """
    
    float_str = fmt.format(f)
    if "e" in float_str:
        base, exponent = float_str.split("e")
        result = r"{0} \times 10^{{{1}}}".format(base, int(exponent))
    else:
        result = float_str

    if units:
       result = result + r"\,{\rm " + units + "}"

    return result


def latex_vec(v, fmt="{0:.3g}", units=""):
    r"""
    v could be a vpython vec/vector object, or an iterable
    >>> latex_vec([1,2,3])
    '\\langle1,2,3\\rangle'
    >>> import vpython as vp
    >>> latex_vec(vp.vec(1,2,3))
    '\\langle1,2,3\\rangle'
    >>> latex_vec(vp.vec(1,2,3)*1e-10)
    '\\langle1 \\times 10^{-10},2 \\times 10^{-10},3 \\times 10^{-10}\\rangle'
    >>> latex_vec(vp.vec(1,2,3)*1e-10,units="m")
    '\\langle1 \\times 10^{-10},2 \\times 10^{-10},3 \\times 10^{-10}\\rangle\\,{\\rm m}'
    """
    if not listish(v):
        v = (v.x, v.y, v.z) # it must be a vpython vector, convert to tuple
    v = f"<{latex_float(v[0], fmt)},{latex_float(v[1], fmt)},{latex_float(v[2], fmt)}>"
    v = v.replace('<',r'\langle')
    v = v.replace('>',r'\rangle')
    if units:
        v = v + r"\,{\rm " + units + "}"
    return v

