from htmlpy import GlobalAttributes
from htmlpy import EventAttributes
from htmlpy.fn import attribute, to_code, clean_format

class Link:

    def __init__(self,
                 destination,
                 inner,
                 download=False,
                 global_attr=GlobalAttributes(),
                 event_attr=EventAttributes()):
        self.global_attr = global_attr
        self.event_attr = event_attr
        self.href = destination
        self.inner = inner
        self.download = download

    def to_code(self) -> str:
        code = f"<a href=\"{self.href}\" "
        code += attribute("download", self.download)
        code += self.global_attr._attributes()
        code += self.event_attr._attributes()
        code += ">"
        code = clean_format(code)

        code += to_code(self.inner)

        code += "</a>"
        return code
