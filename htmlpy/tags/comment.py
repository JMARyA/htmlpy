class Comment:
    def __init__(self, msg):
        self.msg = msg

    def to_code(self) -> str:
        return f"<!-- {self.msg} -->"