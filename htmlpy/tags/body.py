from attributes.global_attributes import GlobalAttributes
from attributes.event_attributes import EventAttributes
from fn.fn import to_code, clean_format

class Body:
    content: list
    global_attr: GlobalAttributes

    def __init__(self,
                 content,
                 global_attr=GlobalAttributes(),
                 event_attr=EventAttributes()):
        self.content = content
        self.event_attr = event_attr
        self.global_attr = global_attr

    def to_code(self) -> str:
        code = f"<body {self.global_attr._attributes()} {self.event_attr._attributes()}>\n"
        code = clean_format(code)
        code += to_code(self.content)
        code += "</body>"
        return code
