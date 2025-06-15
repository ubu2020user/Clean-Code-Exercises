
class Employee:
    def __init__(self, name: str, email: str):
        self._id = None
        self._name = name
        self._email = email

    @property
    def name(self) -> str:
        return self._name

    @property
    def email(self) -> str:
        return self._email

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, employee_id: int) -> None:
        self._id = employee_id

    def __str__(self):
        return f"[Employee] ID: {self._id}, Name: '{self._name}', E-Mail: '{self._email}'"