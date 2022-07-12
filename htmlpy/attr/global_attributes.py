from htmlpy.fn import attribute

class GlobalAttributes:
    def __init__(self, css_class=None, hidden=False, id=None, style=None):
        self.css_class = css_class
        self.hidden = hidden
        self.id = id
        self.style = style

    def _attributes(self):
        attr = ""
        attr += attribute("class", self.css_class)
        attr += attribute("hidden", self.hidden)
        attr += attribute("id", self.id)
        attr += attribute("style", self.style)
        return attr