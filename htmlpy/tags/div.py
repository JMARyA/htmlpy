from htmlpy import GlobalAttributes
from htmlpy import EventAttributes
from htmlpy.fn import to_code, clean_format

class Div:

    def __init__(self,
                 inner,
                 global_attr=GlobalAttributes(),
                 event_attr=EventAttributes()):
        self.global_attr = global_attr
        self.event_attr = event_attr
        self.inner = inner

    def to_code(self) -> str:
        code = f"<div {self.global_attr._attributes()} {self.event_attr._attributes()}>"
        code = clean_format(code)
        code += to_code(self.inner)
        code += "</div>"
        return code