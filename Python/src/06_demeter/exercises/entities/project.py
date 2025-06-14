from datetime import date

class Project:
    """
    Represents a company project.
    
    Attributes:
        project_id (str): Unique identifier for the project
        name (str): Project name
        start_date (date): Project start date
        end_date (date): Expected project completion date
        budget (float): Project budget
    """
    
    def __init__(self, project_id, name, start_date, end_date, budget):
        self.project_id = project_id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.budget = budget
        
    def is_active(self):
        """Check if project is currently active."""
        today = date.today()
        return self.start_date <= today <= self.end_date
        
    def calculate_duration_days(self):
        """Calculate total project duration in days."""
        return (self.end_date - self.start_date).days