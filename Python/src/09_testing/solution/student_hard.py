import requests


class StudentHard:
    def __init__(self, name: str, student_id: str, grades: list[float]):
        self._name = name
        self._student_id = student_id
        self._grades = grades

    def fetch_student_data_from_api(self, api_url: str) -> dict:
        """Fetch student data from an external API."""
        response = requests.get(f"{api_url}/{self._student_id}")
        if response.status_code != 200:
            raise ConnectionError(f"Failed to fetch data from API. Status code: {response.status_code}")
        return response.json()

    def send_grade_to_external_service(self, grade: float, service_url: str) -> bool:
        """Send a grade to an external service."""
        payload = {"student_id": self._student_id, "grade": grade}
        response = requests.post(service_url, json=payload)
        if response.status_code == 200:
            return True
        else:
            raise ConnectionError(f"Failed to send grade to external service. Status code: {response.status_code}")
