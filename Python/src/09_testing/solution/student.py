class Student:
    def __init__(self, name: str, student_id: str, grades: list[float]):
        self._name = name
        self._student_id = student_id
        self._grades = grades

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def student_id(self) -> str:
        return self._student_id

    @student_id.setter
    def student_id(self, student_id: str) -> None:
        self._student_id = student_id

    @property
    def grades(self) -> list[float]:
        return self._grades

    @grades.setter
    def grades(self, grades: list[float]) -> None:
        self._grades = grades

    def calculate_average(self) -> float:
        if not self._grades:
            raise ValueError("No grades available to calculate average.")
        return sum(self._grades) / len(self._grades)

    def add_grade(self, grade: float) -> None:
        if grade < 0 or grade > 100:
            raise ValueError("Grade must be between 0 and 100.")
        self._grades.append(grade)

    def get_grade_status(self) -> str:
        average = self.calculate_average()
        if average >= 90:
            return "Excellent"
        elif average >= 75:
            return "Good"
        elif average >= 50:
            return "Pass"
        else:
            return "Fail"

    def throw_error_if_grade_below_threshold(self, grade: float, threshold: float) -> None:
        if grade < threshold:
            raise ValueError(f"Grade {grade} is below the acceptable threshold of {threshold}.")
        else:
            print(f"Grade {grade} is above the threshold.")
