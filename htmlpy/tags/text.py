from htmlpy import GlobalAttributes
from htmlpy import EventAttributes
from htmlpy.fn import to_code, clean_format


class LineBreak:

    def __init__(self,
                 global_attr=GlobalAttributes(),
                 event_attr=EventAttributes()):
        self.global_attr = global_attr
        self.event_attr = event_attr

    def to_code(self) -> str:
        code = f"<br {self.global_attr._attributes()} {self.event_attr._attributes()}>"
        code = clean_format(code)
        return code


class Bold:

    def __init__(self,
                 inner,
                 global_attr=GlobalAttributes(),
                 event_attr=EventAttributes()):
        self.global_attr = global_attr
        self.event_attr = event_attr
        self.inner = inner

    def to_code(self) -> str:
        code = f"<b {self.global_attr._attributes()} {self.event_attr._attributes()}>"
        code = clean_format(code)

        code += to_code(self.inner)

        code += "</b>"
        return code
        
class Span:

    def __init__(self,
                 inner,
                 global_attr=GlobalAttributes(),
                 event_attr=EventAttributes()):
        self.global_attr = global_attr
        self.event_attr = event_attr
        self.inner = inner

    def to_code(self) -> str:
        code = f"<span {self.global_attr._attributes()} {self.event_attr._attributes()}>"
        code = clean_format(code)
        code += to_code(self.inner)
        code += "</span>"
        return code


class Paragraph:

    def __init__(self,
                 inner,
                 global_attr=GlobalAttributes(),
                 event_attr=EventAttributes()):
        self.global_attr = global_attr
        self.event_attr = event_attr
        self.inner = inner

    def to_code(self) -> str:
        code = f"<p {self.global_attr._attributes()} {self.event_attr._attributes()}>"
        code = clean_format(code)

        code += to_code(self.inner)

        code += "</p>"
        return code


class Heading:

    def __init__(self,
                 n,
                 inner,
                 global_attr=GlobalAttributes(),
                 event_attr=EventAttributes()):
        self.global_attr = global_attr
        self.event_attr = event_attr
        if n < 1 or n > 6:
            raise Exception("Heading must be between 1 and 6")
        self.n = n
        self.inner = inner

    def to_code(self) -> str:
        code = f"<h{self.n} {self.global_attr._attributes()} {self.event_attr._attributes()}>"
        code = clean_format(code)

        code += to_code(self.inner)

        code += f"</h{self.n}>"
        return code
