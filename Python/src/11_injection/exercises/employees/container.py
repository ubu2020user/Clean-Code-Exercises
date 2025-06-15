from dependency_injector import containers, providers
import logging.config

import sys
from pathlib import Path

# Add the exercises directory to the path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from email_service import EmailService
from employee_repo import EmployeeRepo


class Container(containers.DeclarativeContainer):
    employee_repo = providers.Factory(EmployeeRepo)
    email_service = providers.Factory(EmailService, employee_repo=employee_repo)

