class FileContent:
    def __init__(self, name):
        self._name = name
        self._lines = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def lines(self):
        return self._lines

    @lines.setter
    def lines(self, value):
        self._lines = value

    def __str__(self):
        if self._lines is None:
            return f"FileContent{{name='{self._name}', lines: \nNone}}"
        return (
            f"FileContent{{name='{self._name}', lines: \n"
            + "\n".join(self._lines)
            + "}}"
        )
