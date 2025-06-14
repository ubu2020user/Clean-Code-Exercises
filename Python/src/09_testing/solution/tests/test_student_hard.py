import pytest
import requests
from unittest.mock import patch, Mock
from student_hard import StudentHard

class TestStudentHard:
    
    def setup_method(self):
        """Setup for each test case."""
        self.student = StudentHard("John Doe", "S12345", [85, 90, 75])
        
    @patch('requests.get')
    def test_fetch_student_data_from_api_success(self, mock_get):
        """Test successful API data fetch with mocked response."""
        # Configure mock
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "name": "John Doe",
            "student_id": "S12345",
            "courses": ["Math", "Physics", "Chemistry"],
            "additional_info": {"enrollment_date": "2023-01-15"}
        }
        mock_get.return_value = mock_response
        
        # Call the method to test
        result = self.student.fetch_student_data_from_api("https://example.com/api/students")
        
        # Assertions
        mock_get.assert_called_once_with("https://example.com/api/students/S12345")
        assert "name" in result
        assert result["courses"] == ["Math", "Physics", "Chemistry"]
        assert result["additional_info"]["enrollment_date"] == "2023-01-15"
    
    @patch('requests.get')
    def test_fetch_student_data_from_api_failure(self, mock_get):
        """Test API data fetch failure with mocked response."""
        # Configure mock
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        
        # Call the method and expect exception
        with pytest.raises(ConnectionError) as excinfo:
            self.student.fetch_student_data_from_api("https://example.com/api/students")
        
        # Assertions
        mock_get.assert_called_once_with("https://example.com/api/students/S12345")
        assert "Failed to fetch data from API" in str(excinfo.value)
        assert "404" in str(excinfo.value)
    
    @patch('requests.post')
    def test_send_grade_to_external_service_success(self, mock_post):
        """Test successful grade submission with mocked response."""
        # Configure mock
        mock_response = Mock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response
        
        # Call the method to test
        result = self.student.send_grade_to_external_service(92.5, "https://example.com/api/grades")
        
        # Assertions
        mock_post.assert_called_once_with(
            "https://example.com/api/grades", 
            json={"student_id": "S12345", "grade": 92.5}
        )
        assert result is True
    
    @patch('requests.post')
    def test_send_grade_to_external_service_failure(self, mock_post):
        """Test grade submission failure with mocked response."""
        # Configure mock
        mock_response = Mock()
        mock_response.status_code = 500
        mock_post.return_value = mock_response
        
        # Call the method and expect exception
        with pytest.raises(ConnectionError) as excinfo:
            self.student.send_grade_to_external_service(92.5, "https://example.com/api/grades")
        
        # Assertions
        mock_post.assert_called_once_with(
            "https://example.com/api/grades", 
            json={"student_id": "S12345", "grade": 92.5}
        )
        assert "Failed to send grade to external service" in str(excinfo.value)
        assert "500" in str(excinfo.value)
    
    @patch('requests.get')
    def test_fetch_student_data_network_error(self, mock_get):
        """Test API data fetch with network error."""
        # Configure mock to raise an exception
        mock_get.side_effect = requests.exceptions.RequestException("Network error")
        
        # Call the method and expect exception
        with pytest.raises(requests.exceptions.RequestException) as excinfo:
            self.student.fetch_student_data_from_api("https://example.com/api/students")
        
        # Assertions
        mock_get.assert_called_once()
        assert "Network error" in str(excinfo.value)
    
    @patch('requests.post')
    def test_send_grade_network_error(self, mock_post):
        """Test grade submission with network error."""
        # Configure mock to raise an exception
        mock_post.side_effect = requests.exceptions.RequestException("Network error")
        
        # Call the method and expect exception
        with pytest.raises(requests.exceptions.RequestException) as excinfo:
            self.student.send_grade_to_external_service(92.5, "https://example.com/api/grades")
        
        # Assertions
        mock_post.assert_called_once()
        assert "Network error" in str(excinfo.value)