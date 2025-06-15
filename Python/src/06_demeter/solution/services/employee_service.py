from warnings import deprecated

import sys
from pathlib import Path

# Add the exercises directory to the path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from entities.employee import Employee

class EmployeeService:
    """
    Service class to manage employee-related operations.

    Attributes:
        employees (list): List of all employees
    """

    def __init__(self):
        self.employees: list[Employee] = []

    def add_employee(self, employee):
        """Add an employee to the system."""
        self.employees.append(employee)

    def find_employee_by_id(self, employee_id):
        """Find an employee by their ID."""
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee
        return None

    @deprecated(
        "get_employees_by_department is deprecated. Use filter_employees_by_department instead."
    )
    def get_employees_by_department_old(self, department_code):
        """
        Get all employees in a specific department.
        """
        return [e for e in self.employees if e.department.code == department_code]

    def calculate_total_salary_cost(self):
        """Calculate total salary cost across all employees."""
        return sum(e.salary for e in self.employees)

    def get_employees_by_department(self, department_code):
        """
        Get all employees in a specific department.
        This method is a replacement for the deprecated get_employees_by_department.
        """
        return [e for e in self.employees if e.is_in_department(department_code)]
