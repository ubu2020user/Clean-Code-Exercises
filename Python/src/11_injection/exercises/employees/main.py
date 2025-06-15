import sys

from dependency_injector.wiring import Provide, inject


import sys
from pathlib import Path

# Add the exercises directory to the path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from container import Container
from email_service import EmailService
from employee_repo import EmployeeRepo
from employee import Employee


@inject
def main(
    employee_repo: EmployeeRepo = Provide[Container.employee_repo],
    email_service: EmailService = Provide[Container.email_service],
) -> None:
    employee = Employee("Daniel Lukas", "Daniel@github.de")
    employee_repo.save(employee)

    all_employees = employee_repo.find_all()
    first_employee = all_employees[0]
    print(first_employee)

    email_service.send_email(first_employee.id, "Hello Employee", "how are you?")


if __name__ == "__main__":
    container = Container()
    container.init_resources()
    container.wire(modules=[__name__])
    main()
