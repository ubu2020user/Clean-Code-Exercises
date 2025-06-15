import sys
from pathlib import Path
from dependency_injector.wiring import Provide, inject

sys.path.append(str(Path(__file__).resolve().parent.parent))

from container import Container
from email_service import EmailService
from employee_repo import EmployeeRepo
from employee import Employee

class EmployeeService:
    def __init__(
        self,
        employee_repo: EmployeeRepo = Provide[Container.employee_repo],
        email_service: EmailService = Provide[Container.email_service],
    ) -> None:
        """
        Initializes the EmployeeService with an injected EmployeeRepo instance.
        :param employee_repo: An instance of EmployeeRepo for managing employee data.
        :param email_service: An instance of EmailService for sending emails to employees.
        """
        self.employee_repo = employee_repo
        self.email_service = email_service

    def initialize_employees(self):
        """
        Initializes the employee repository with a default employee.
        This method is called during the service initialization.
        """
        employee = Employee("Daniel Lukas", "Daniel@github.de")
        self.employee_repo.save(employee)

        self.create_departement(
            [
                Employee(name="Alice Smith", email="alice@github.de"),
                Employee(name="Bob Johnson", email="bob@github.de"),
                Employee(name="Charlie Brown", email="charles.xavier@github.de"),
            ]
        )

    def create_departement(self, employees):
        """
        Creates multiple employees in the employee repository.
        :param employees: A list of dictionaries containing employee data.
        """
        for employee_data in employees:
            self.employee_repo.save(employee_data)

    def send_emails_to_all(self):
        """
        Sends an email to all employees in the repository.
        This method retrieves all employees and sends a test email to each.
        """
        all_employees = self.employee_repo.find_all()
        for employee in all_employees:
            self.email_service.send_email(employee.id, "Hello Employee", "how are you?")
            print(f"Email sent to '{employee.name}' at '{employee.email}'")


if __name__ == "__main__":
    container = Container()
    container.init_resources()
    container.wire(modules=[__name__])

    service = EmployeeService()

    service.initialize_employees()
    service.send_emails_to_all()
