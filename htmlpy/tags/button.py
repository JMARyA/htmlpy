from htmlpy import GlobalAttributes
from htmlpy import EventAttributes
from htmlpy.fn import attribute, to_code, clean_format

class Button:

    def __init__(self,
                 inner,
                 name=None,
                 value=None,
                 autofocus=False,
                 disabled=False,
                 form=None,
                 global_attr=GlobalAttributes(),
                 event_attr=EventAttributes()):
        self.global_attr = global_attr
        self.event_attr = event_attr
        self.inner = inner
        self.name = name
        self.value = value
        self.autofocus = autofocus
        self.disabled = disabled
        self.form = form

    def to_code(self) -> str:
        code = f"<button "
        code += self.global_attr._attributes()
        code += self.event_attr._attributes()
        code += attribute("name", self.name)
        code += attribute("value", self.value)
        code += attribute("autofocus", self.autofocus)
        code += attribute("disabled", self.disabled)
        code += attribute("form", self.form)
        code += ">"
        code = clean_format(code)

        code += to_code(self.inner)

        code += "</button>"
        return code
