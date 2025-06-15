
import sys
from pathlib import Path

# Add the exercises directory to the path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from employee_repo import EmployeeRepo


class EmailService:
    def __init__(self, employee_repo: EmployeeRepo):
        self._employee_repo = employee_repo
        pass

    def send_email(self, employeeReceiverId: int, subject: str, message: str):
        print(f"Sending email to {employeeReceiverId}")