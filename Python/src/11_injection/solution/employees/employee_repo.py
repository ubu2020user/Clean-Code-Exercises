from typing import Dict, Optional, List

import sys
from pathlib import Path

# Add the exercises directory to the path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from employee import Employee


class EmployeeRepo:
    def __init__(self):
        self._employee_dict: Dict[int, Employee] = {}
        self._nextId: int = 1

    def save(self, employee: Employee) -> Employee:
        if not employee.id:
            employee.id = self._nextId
            self._nextId += 1

        self._employee_dict[employee.id] = employee

        return employee

    def find_by_id(self, employee_id: int) -> Optional[Employee]:
        return self._employee_dict.get(employee_id)

    def find_all(self) -> List[Employee]:
        return list(self._employee_dict.values())
