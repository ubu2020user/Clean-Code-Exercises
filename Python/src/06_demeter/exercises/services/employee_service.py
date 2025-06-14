class EmployeeService:
    """
    Service class to manage employee-related operations.
    
    Attributes:
        employees (list): List of all employees
    """
    
    def __init__(self):
        self.employees = []
        
    def add_employee(self, employee):
        """Add an employee to the system."""
        self.employees.append(employee)
        
    def find_employee_by_id(self, employee_id):
        """Find an employee by their ID."""
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee
        return None
        
    def get_employees_by_department(self, department_code):
        """Get all employees in a specific department."""
        return [e for e in self.employees if e.department.code == department_code]
        
    def calculate_total_salary_cost(self):
        """Calculate total salary cost across all employees."""
        return sum(e.salary for e in self.employees)