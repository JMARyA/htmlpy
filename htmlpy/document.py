from tags.head import Head
from tags.body import Body

class Document:
    head: Head
    body: Body

    def __init__(self, body, head=Head()):
        self.head = head
        self.body = body

    def to_code(self) -> str:
        code = f"""<!DOCTYPE html>
<html>
{self.head.to_code()}
{self.body.to_code()}
</html>
        """
        return code