"""
format things for LaTeX
"""
from si_prefix import si_format as si

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

def latex_float(f, units="", fmt="{0:.3g}"):
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
    
    if f == 0:
        f = 0  # fix annoying `-0` results.
    float_str = fmt.format(f)
    if "e" in float_str:
        base, exponent = float_str.split("e")
        result = r"{0} \times 10^{{{1}}}".format(base, int(exponent))
    else:
        result = float_str

    if units:
       result = result + r"\,{\rm " + units + "}"

    return result


def latex_vec(v, units="", fmt="{0:.3g}"):
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
    v = f"<{latex_float(v[0], fmt=fmt)},{latex_float(v[1], fmt=fmt)},{latex_float(v[2], fmt=fmt)}>"
    v = v.replace('<',r'\langle')
    v = v.replace('>',r'\rangle')
    if units:
        v = v + r"\,{\rm " + units + "}"
    return v

def eunits(val, units):
    r"""
    v could be a vpython vec/vector object, or an iterable
    >>> eunits(0.003,"A")
    '3.00\\,mA'
    """
    si_val = si(val,precision=4)
    num,pfx=si_val.split(' ')
    ip,fp = num.split('.')
    len_fp = max(3 - len(ip),0)
    if len_fp:
        fp = fp[:len_fp]
        num = '.'.join([ip,fp])
    else:
        num = ip
    pfx = pfx.replace(chr(181),r'\mu ') # take care of micro units
    si_val = r'\,'.join([num,pfx])
    return si_val + units


if __name__=='__main__':
    import doctest
    doctest.testmod()
