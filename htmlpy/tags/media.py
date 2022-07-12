from htmlpy import GlobalAttributes
from htmlpy import EventAttributes
from htmlpy.fn import attribute, to_code, clean_format

class Audio:

    def __init__(self,
                 src,
                 controls=True,
                 muted=False,
                 loop=False,
                 autoplay=False,
                 global_attr=GlobalAttributes(),
                 event_attr=EventAttributes()):
        self.global_attr = global_attr
        self.event_attr = event_attr
        self.src = src
        self.controls = controls
        self.muted = muted
        self.loop = loop
        self.autoplay = autoplay

    def to_code(self) -> str:
        code = f"<audio "
        code += attribute("controls", self.controls)
        code += attribute("muted", self.muted)
        code += attribute("loop", self.loop)
        code += attribute("autoplay", self.autoplay)
        code += self.global_attr._attributes()
        code += self.event_attr._attributes()
        code += ">"
        code = clean_format(code)

        code += to_code(self.src)

        code += "</audio>"
        return code


class Video:

    def __init__(self,
                 src,
                 poster=None,
                 height=None,
                 width=None,
                 controls=True,
                 muted=False,
                 loop=False,
                 autoplay=False,
                 global_attr=GlobalAttributes(),
                 event_attr=EventAttributes()):
        self.global_attr = global_attr
        self.event_attr = event_attr
        self.src = src
        self.poster = poster
        self.height = height
        self.width = width
        self.controls = controls
        self.muted = muted
        self.loop = loop
        self.autoplay = autoplay

    def to_code(self) -> str:
        code = f"<video "
        code += attribute("poster", self.poster)
        code += attribute("height", self.height)
        code += attribute("width", self.width)
        code += attribute("controls", self.controls)
        code += attribute("muted", self.muted)
        code += attribute("loop", self.loop)
        code += attribute("autoplay", self.autoplay)
        code += self.global_attr._attributes()
        code += self.event_attr._attributes()
        code += ">"
        code = clean_format(code)

        code += to_code(self.src)

        code += "</video>"
        return code


class Image:

    def __init__(self,
                 src,
                 height=None,
                 width=None,
                 alt=None,
                 global_attr=GlobalAttributes(),
                 event_attr=EventAttributes()):
        self.global_attr = global_attr
        self.event_attr = event_attr
        self.src = src
        self.height = height
        self.width = width
        self.alt = alt

    def to_code(self) -> str:
        code = f"<img "
        code += attribute("src", self.src)
        code += attribute("height", self.height)
        code += attribute("width", self.width)
        code += attribute("alt", self.alt)
        code += self.global_attr._attributes()
        code += self.event_attr._attributes()
        code += ">"
        code = clean_format(code)
        return code
