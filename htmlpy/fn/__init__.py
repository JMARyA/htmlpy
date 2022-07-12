
def attribute(name, val):
    if isinstance(val, bool):
        if val:
            return f"{name} "
        else:
            return ""
    if val != None:
        return f"{name}=\"{val}\" "
    return ""

def to_code(el):
    code = ""
    if isinstance(el, list):
        for e in el:
                code += f"{to_code(e)}\n"
    elif isinstance(el, str):
        code += el
    elif el == None:
        return ""
    else:
        code += f"{el.to_code()}"

    return code

def clean_format(c):
    code = c.replace("  ", " ")
    code = code.replace(" >", ">")
    return code