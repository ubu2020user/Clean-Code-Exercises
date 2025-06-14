from ..entities.assignment import Assignment

class ProjectService:
    """
    Service class to manage project-related operations.
    
    Attributes:
        projects (list): List of all projects
        assignments (list): List of all project assignments
    """
    
    def __init__(self):
        self.projects = []
        self.assignments = []
        
    def add_project(self, project):
        """Add a project to the system."""
        self.projects.append(project)
        
    def assign_employee_to_project(self, employee, project, role, hours):
        """Create a new assignment of an employee to a project."""
        assignment = Assignment(employee, project, role, hours)
        self.assignments.append(assignment)
        return assignment
        
    def get_project_team(self, project_id):
        """Get all employees assigned to a specific project."""
        return [a.employee for a in self.assignments 
                if a.project.project_id == project_id]
        
    def calculate_project_resource_allocation(self, project_id):
        """Calculate total weekly hours allocated to a project."""
        project_assignments = [a for a in self.assignments 
                              if a.project.project_id == project_id]
        return sum(a.hours_allocated for a in project_assignments)