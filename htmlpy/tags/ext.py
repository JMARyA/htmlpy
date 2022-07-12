from attributes.global_attributes import GlobalAttributes
from attributes.event_attributes import EventAttributes
from fn.fn import to_code, attribute, clean_format

class Source:

    def __init__(self,
                 src,
                 type=None,
                 global_attr=GlobalAttributes(),
                 event_attr=EventAttributes()):
        self.global_attr = global_attr
        self.event_attr = event_attr
        self.src = src
        self.type = type

    def to_code(self) -> str:
        code = f"<source {self.global_attr._attributes()} {self.event_attr._attributes()}"
        code += attribute("src", self.src)
        code += attribute("type", self.type)
        code += ">"
        code = clean_format(code)
        return code


class Style:

    def __init__(self, inner, global_attr=GlobalAttributes()):
        self.global_attr = global_attr
        self.inner = inner

    def to_code(self) -> str:
        code = f"<style {self.global_attr._attributes()}>"
        code = clean_format(code)
        code += self.inner
        code += "</style>"
        return code

class Script:

    def __init__(self, src=None, inner=None, global_attr=GlobalAttributes()):
        self.global_attr = global_attr
        self.src = src
        self.inner = inner

    def to_code(self) -> str:
        code = f"<script {self.global_attr._attributes()} "
        code += attribute("src", self.src)
        code += ">"
        code = clean_format(code)
        code += to_code(self.inner)
        code += "</script>"
        return code
