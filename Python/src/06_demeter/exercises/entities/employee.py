from datetime import date
from dateutil.relativedelta import relativedelta

class Employee:
    """
    Represents an employee in the company.
    
    Attributes:
        employee_id (str): Unique identifier for the employee
        first_name (str): Employee's first name
        last_name (str): Employee's last name
        address (Address): Employee's address
        department (Department): Employee's department
        hire_date (date): Date when employee was hired
        salary (float): Employee's annual salary
    """
    
    def __init__(self, employee_id, first_name, last_name, address, department, hire_date, salary):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.department = department
        self.hire_date = hire_date
        self.salary = salary
        
    def get_full_name(self):
        """Returns employee's full name."""
        return f"{self.first_name} {self.last_name}"
        
    def calculate_years_of_service(self):
        """Calculate how many years employee has been with the company."""
        today = date.today()
        return relativedelta(today, self.hire_date).years
        
    def calculate_monthly_salary(self):
        """Calculate employee's monthly salary."""
        return self.salary / 12