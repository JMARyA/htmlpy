from htmlpy import GlobalAttributes
from htmlpy import EventAttributes
from htmlpy.fn import attribute, to_code, clean_format
from enum import Enum

class Form:

    def __init__(self,
                 destination,
                 inner,
                 name=None,
                 method="post",
                 autocomplete=False,
                 global_attr=GlobalAttributes(),
                 event_attr=EventAttributes()):
        self.global_attr = global_attr
        self.event_attr = event_attr
        self.action = destination
        self.inner = inner
        self.name = name
        self.method = method
        self.autocomplete = autocomplete

    def to_code(self) -> str:
        code = f"<form "
        code += attribute("action", self.action)
        code += attribute("name", self.name)
        code += attribute("method", self.method)
        if self.autocomplete:
            code += "autocomplete=\"on\""
        else:
            code += "autocomplete=\"off\""
        code += self.global_attr._attributes()
        code += self.event_attr._attributes()
        code += ">"
        code = clean_format(code)

        code += to_code(self.inner)

        code += "</form>"
        return code


class Label:

    def __init__(self,
                 for_id,
                 inner,
                 form=None,
                 global_attr=GlobalAttributes(),
                 event_attr=EventAttributes()):
        self.global_attr = global_attr
        self.event_attr = event_attr
        self.for_id = for_id
        self.form = form
        self.inner = inner

    def to_code(self) -> str:
        code = f"<label "
        code += attribute("for", self.for_id)
        code += attribute("form", self.form)
        code += self.global_attr._attributes()
        code += self.event_attr._attributes()
        code += ">"
        code = clean_format(code)

        code += to_code(self.inner)

        code += "</label>"
        return code


class OptionGroup:

    def __init__(self,
                 label,
                 inner,
                 disabled=False,
                 global_attr=GlobalAttributes(),
                 event_attr=EventAttributes()):
        self.global_attr = global_attr
        self.event_attr = event_attr
        self.label = label
        self.disabled = disabled
        self.inner = inner

    def to_code(self) -> str:
        code = f"<optgroup "
        code += attribute("label", self.label)
        code += attribute("disabled", self.disabled)
        code += self.global_attr._attributes()
        code += self.event_attr._attributes()
        code += ">"
        code = clean_format(code)

        code += to_code(self.inner)

        code += "</optgroup>"
        return code

        return code


class Option:

    def __init__(self,
                 value,
                 inner,
                 label=None,
                 selected=False,
                 disabled=False,
                 global_attr=GlobalAttributes(),
                 event_attr=EventAttributes()):
        self.global_attr = global_attr
        self.event_attr = event_attr
        self.label = label
        self.value = value
        self.selected = selected
        self.disabled = disabled
        self.inner = inner

    def to_code(self) -> str:
        code = f"<option "
        code += attribute("label", self.label)
        code += attribute("value", self.value)
        code += attribute("selected", self.selected)
        code += attribute("disabled", self.disabled)
        code += self.global_attr._attributes()
        code += self.event_attr._attributes()
        code += ">"
        code = clean_format(code)

        code += to_code(self.inner)

        code += "</option>"
        return code

        return code


class Selection:

    def __init__(self,
                 inner,
                 name,
                 form=None,
                 required=True,
                 multiple=False,
                 disabled=False,
                 autofocus=False,
                 global_attr=GlobalAttributes(),
                 event_attr=EventAttributes()):
        self.global_attr = global_attr
        self.event_attr = event_attr
        self.inner = inner
        self.name = name
        self.form = form
        self.required = required
        self.multiple = multiple
        self.disabled = disabled
        self.autofocus = autofocus

    def to_code(self) -> str:
        code = f"<select "
        code += attribute("name", self.name)
        code += attribute("form", self.form)
        code += attribute("required", self.required)
        code += attribute("multiple", self.multiple)
        code += attribute("disabled", self.disabled)
        code += attribute("autofocus", self.autofocus)
        code += self.global_attr._attributes()
        code += self.event_attr._attributes()
        code += ">"
        code = clean_format(code)

        code += to_code(self.inner)

        code += "</select>"
        return code

        return code


class TextArea:

    def __init__(self,
                 inner,
                 placeholder=None,
                 readonly=False,
                 required=True,
                 name=None,
                 maxlength=None,
                 form=None,
                 cols=10,
                 rows=10,
                 disabled=False,
                 autofocus=False,
                 global_attr=GlobalAttributes(),
                 event_attr=EventAttributes()):
        self.global_attr = global_attr
        self.event_attr = event_attr
        self.inner = inner
        self.placeholder = placeholder
        self.readonly = readonly
        self.required = required
        self.name = name
        self.maxlength = maxlength
        self.form = form
        self.cols = cols
        self.rows = rows
        self.disabled = disabled
        self.autofocus = autofocus

    def to_code(self) -> str:
        code = f"<textarea "
        code += attribute("placeholder", self.placeholder)
        code += attribute("readonly", self.readonly)
        code += attribute("required", self.required)
        code += attribute("name", self.name)
        code += attribute("maxlength", self.maxlength)
        code += attribute("form", self.form)
        code += attribute("cols", self.cols)
        code += attribute("rows", self.rows)
        code += attribute("disabled", self.disabled)
        code += attribute("autofocus", self.autofocus)
        code += self.global_attr._attributes()
        code += self.event_attr._attributes()
        code += ">"
        code = clean_format(code)

        code += to_code(self.inner)

        code += "</textarea>"
        return code

        return code


class InputType(Enum):
    Button = "button"
    Checkbox = "checkbox"
    Color = "color"
    Date = "date"
    Email = "email"
    File = "file"
    Hidden = "hidden"
    Image = "image"
    Month = "month"
    Number = "number"
    Password = "password"
    Radio = "radio"
    Range = "range"
    Reset = "reset"
    Search = "search"
    Submit = "submit"
    Telephone = "tel"
    Text = "text"
    Time = "time"
    URL = "url"
    Week = "week"


class Input:

    def __init__(self,
                 value,
                 type=InputType.Text,
                 readonly=False,
                 required=True,
                 name=None,
                 minNumber=None,
                 maxNumber=None,
                 minlength=None,
                 maxlength=None,
                 form=None,
                 disabled=False,
                 autofocus=False,
                 global_attr=GlobalAttributes(),
                 event_attr=EventAttributes()):
        self.global_attr = global_attr
        self.event_attr = event_attr
        self.value = value
        self.type = type
        self.readonly = readonly
        self.required = required
        self.name = name
        self.minNum = minNumber
        self.maxNum = maxNumber
        self.minlength = minlength
        self.maxlength = maxlength
        self.form = form
        self.disabled = disabled
        self.autofocus = autofocus

    def to_code(self) -> str:
        code = f"<input "
        code += attribute("value", self.value)
        code += attribute("type", self.type.value)
        code += attribute("readonly", self.readonly)
        code += attribute("required", self.required)
        code += attribute("name", self.name)
        code += attribute("min", self.minNum)
        code += attribute("max", self.maxNum)
        code += attribute("minlength", self.minlength)
        code += attribute("maxlength", self.maxlength)
        code += attribute("form", self.form)
        code += attribute("disabled", self.disabled)
        code += attribute("autofocus", self.autofocus)
        code += self.global_attr._attributes()
        code += self.event_attr._attributes()
        code += ">"
        code = clean_format(code)
        return code

        return code
