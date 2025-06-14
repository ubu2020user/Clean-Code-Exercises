class Department:
    """
    Represents a company department.
    
    Attributes:
        name (str): Department name
        code (str): Department code
        location (str): Department's physical location
    """
    
    def __init__(self, name, code, location):
        self.name = name
        self.code = code
        self.location = location
        
    def get_full_name(self):
        """Returns the formatted department name with code."""
        return f"{self.name} ({self.code})"