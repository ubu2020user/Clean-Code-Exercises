from paint_configuration import PaintConfiguration

class PaintEngineInterface:
    def paint(self, paint_configuration: PaintConfiguration):
        """Abstract method to be implemented by the PaintEngine."""
        raise NotImplementedError("This method should be implemented by a concrete PaintEngine.")

class PaintConfigurator:
    def __init__(self, paint_engine: PaintEngineInterface):
        self.paint_engine = paint_engine

    def build(self, paint_configuration: PaintConfiguration):
        # Delegate the painting process to the PaintEngine
        self.paint_engine.paint(paint_configuration)
