"""
format things for LaTeX
"""

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
    v should be a vpython vec/vector object.
    """
    
    v = f"<{latex_float(v.x, fmt)},{latex_float(v.y, fmt)},{latex_float(v.z, fmt)}>"
    v = v.replace('<',r'\langle')
    v = v.replace('>',r'\rangle')
    return v

