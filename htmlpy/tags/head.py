from fn.fn import to_code, clean_format, attribute
from attributes.global_attributes import GlobalAttributes
from attributes.event_attributes import EventAttributes

class Title:

    def __init__(self,
                 title,
                 global_attr=GlobalAttributes(),
                 event_attr=EventAttributes()):
        self.global_attr = global_attr
        self.event_attr = event_attr
        self.title = title

    def to_code(self) -> str:
        code = f"<title {self.global_attr._attributes()} {self.event_attr._attributes()}>"
        code = clean_format(code)
        code += self.title
        code += "</title>"
        return code


class Meta:

    def __init__(self,
                 name,
                 content,
                 global_attr=GlobalAttributes(),
                 event_attr=EventAttributes()):
        self.global_attr = global_attr
        self.event_attr = event_attr
        self.name = name
        self.content = content

    def to_code(self) -> str:
        code = f"<meta {self.global_attr._attributes()} {self.event_attr._attributes()} "
        code += attribute("name", self.name)
        code += attribute("content", self.content)
        code += ">"
        code = clean_format(code)
        return code


class Reference:

    def __init__(self,
                 destination,
                 rel,
                 global_attr=GlobalAttributes(),
                 event_attr=EventAttributes()):
        self.global_attr = global_attr
        self.event_attr = event_attr
        self.destination = destination
        self.rel = rel

    def to_code(self) -> str:
        code = f"<link {self.global_attr._attributes()} {self.event_attr._attributes()} "
        code += attribute("href", self.destination)
        code += attribute("rel", self.rel)
        code += ">"
        code = clean_format(code)
        return code


class Head:

    def __init__(self,
                 inner=[Title("Page")],
                 global_attr=GlobalAttributes(),
                 event_attr=EventAttributes()):
        self.global_attr = global_attr
        self.event_attr = event_attr
        self.inner = inner

    def to_code(self) -> str:
        code = f"<head {self.global_attr._attributes()} {self.event_attr._attributes()}>"
        code += to_code(self.inner)
        code += "</head>"
        return code
