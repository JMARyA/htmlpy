from htmlpy import GlobalAttributes
from htmlpy import EventAttributes
from htmlpy.fn import to_code, clean_format

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

class Header:

    def __init__(self,
                 inner,
                 global_attr=GlobalAttributes(),
                 event_attr=EventAttributes()):
        self.global_attr = global_attr
        self.event_attr = event_attr
        self.inner = inner

    def to_code(self) -> str:
        code = f"<header {self.global_attr._attributes()} {self.event_attr._attributes()}>"
        code = clean_format(code)
        code += to_code(self.inner)
        code += "</header>"
        return code

class Footer:

    def __init__(self,
                 inner,
                 global_attr=GlobalAttributes(),
                 event_attr=EventAttributes()):
        self.global_attr = global_attr
        self.event_attr = event_attr
        self.inner = inner

    def to_code(self) -> str:
        code = f"<footer {self.global_attr._attributes()} {self.event_attr._attributes()}>"
        code = clean_format(code)
        code += to_code(self.inner)
        code += "</footer>"
        return code