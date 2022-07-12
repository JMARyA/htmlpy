from fn.fn import attribute

class EventAttributes:
    def __init__(self, 
    # Window Events
    onload=None, onresize=None, 
    # Form Events
    onblur=None, onchange=None, onfocus=None, oninput=None, oninvalid=None, onsearch=None, onselect=None, onsubmit=None,
    # Mouse Events
    onclick=None, onmouseover=None
        ):
        self.onload = onload
        self.onresize = onresize

        self.onblur = onblur
        self.onchange = onchange
        self.onfocus = onfocus
        self.oninput = oninput
        self.oninvalid = oninvalid
        self.onsearch = onsearch
        self.onselect = onselect
        self.onsubmit = onsubmit

        self.onclick = onclick
        self.onmouseover = onmouseover

    def _attributes(self):
        attr = ""
        attr += attribute("onload", self.onload)
        attr += attribute("onresize", self.onresize)

        attr += attribute("onblur", self.onblur)
        attr += attribute("onchange", self.onchange)
        attr += attribute("onfocus", self.onfocus)
        attr += attribute("oninput", self.oninput)
        attr += attribute("oninvalid", self.oninvalid)
        attr += attribute("onsearch", self.onsearch)
        attr += attribute("onselect", self.onselect)
        attr += attribute("onsubmit", self.onsubmit)

        attr += attribute("onclick", self.onclick)
        attr += attribute("onmouseover", self.onmouseover)
        return attr