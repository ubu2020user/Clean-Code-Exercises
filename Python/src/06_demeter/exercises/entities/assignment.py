class Assignment:
    """
    Represents an employee's assignment to a project.
    
    Attributes:
        employee (Employee): The assigned employee
        project (Project): The project
        role (str): Employee's role in the project
        hours_allocated (int): Weekly hours allocated to this project
    """
    
    def __init__(self, employee, project, role, hours_allocated):
        self.employee = employee
        self.project = project
        self.role = role
        self.hours_allocated = hours_allocated
        
    def calculate_project_salary_cost(self):
        """Calculate how much of employee's salary is allocated to this project."""
        weekly_salary = self.employee.calculate_monthly_salary() * 12 / 52
        return weekly_salary * self.hours_allocated / 40  # Assuming 40-hour work week