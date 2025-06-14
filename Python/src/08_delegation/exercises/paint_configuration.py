class PaintConfiguration:
    def __init__(self, canvas_data):
        self._canvas_data = canvas_data

    @property
    def canvas_data(self):
        return self._canvas_data

    @canvas_data.setter
    def canvas_data(self, value):
        self._canvas_data = value