import pytest
from ...exercises.student import Student

class TestStudent:
    def test_init(self):
        """Test proper initialization of a Student object."""
        student = Student("John Doe", "S12345", [85, 90, 78])
        
        assert student.name == "John Doe"
        assert student.student_id == "S12345"
        assert student.grades == [85, 90, 78]
    
    def test_name_setter(self):
        """Test setting a new name."""
        student = Student("John Doe", "S12345", [])
        student.name = "Jane Smith"
        
        assert student.name == "Jane Smith"
    
    def test_student_id_setter(self):
        """Test setting a new student ID."""
        student = Student("John Doe", "S12345", [])
        student.student_id = "S67890"
        
        assert student.student_id == "S67890"
    
    def test_grades_setter(self):
        """Test setting new grades."""
        student = Student("John Doe", "S12345", [85, 90])
        student.grades = [95, 88, 76]
        
        assert student.grades == [95, 88, 76]
    
    def test_calculate_average_normal(self):
        """Test average calculation with normal grades."""
        student = Student("John Doe", "S12345", [85, 90, 75])
        
        assert student.calculate_average() == 83.33333333333333
    
    def test_calculate_average_empty(self):
        """Test average calculation with empty grades list raises error."""
        student = Student("John Doe", "S12345", [])
        
        with pytest.raises(ValueError) as excinfo:
            student.calculate_average()
        
        assert "No grades available" in str(excinfo.value)
    
    def test_add_grade_valid(self):
        """Test adding a valid grade."""
        student = Student("John Doe", "S12345", [85, 90])
        student.add_grade(78)
        
        assert student.grades == [85, 90, 78]
    
    def test_add_grade_too_low(self):
        """Test adding a grade below 0 raises error."""
        student = Student("John Doe", "S12345", [85, 90])
        
        with pytest.raises(ValueError) as excinfo:
            student.add_grade(-5)
        
        assert "Grade must be between" in str(excinfo.value)
        assert student.grades == [85, 90]  # Original grades unchanged
    
    def test_add_grade_too_high(self):
        """Test adding a grade above 100 raises error."""
        student = Student("John Doe", "S12345", [85, 90])
        
        with pytest.raises(ValueError) as excinfo:
            student.add_grade(105)
        
        assert "Grade must be between" in str(excinfo.value)
        assert student.grades == [85, 90]  # Original grades unchanged
    
    def test_get_grade_status_excellent(self):
        """Test grade status is 'Excellent' when average >= 90."""
        student = Student("John Doe", "S12345", [90, 95, 92])
        
        assert student.get_grade_status() == "Excellent"
    
    def test_get_grade_status_good(self):
        """Test grade status is 'Good' when 75 <= average < 90."""
        student = Student("John Doe", "S12345", [75, 85, 80])
        
        assert student.get_grade_status() == "Good"
    
    def test_get_grade_status_pass(self):
        """Test grade status is 'Pass' when 50 <= average < 75."""
        student = Student("John Doe", "S12345", [50, 65, 60])
        
        assert student.get_grade_status() == "Pass"
    
    def test_get_grade_status_fail(self):
        """Test grade status is 'Fail' when average < 50."""
        student = Student("John Doe", "S12345", [30, 45, 40])
        
        assert student.get_grade_status() == "Fail"
    
    def test_throw_error_if_grade_below_threshold_above(self, capsys):
        """Test no error when grade is above threshold."""
        student = Student("John Doe", "S12345", [85])
        
        student.throw_error_if_grade_below_threshold(80, 70)
        
        captured = capsys.readouterr()
        assert "Grade 80 is above the threshold." in captured.out
    
    def test_throw_error_if_grade_below_threshold_below(self):
        """Test error raised when grade is below threshold."""
        student = Student("John Doe", "S12345", [85])
        
        with pytest.raises(ValueError) as excinfo:
            student.throw_error_if_grade_below_threshold(65, 70)
        
        assert "Grade 65 is below the acceptable threshold of 70" in str(excinfo.value)
    
    def test_throw_error_if_grade_below_threshold_equal(self, capsys):
        """Test no error when grade equals threshold."""
        student = Student("John Doe", "S12345", [85])
        
        student.throw_error_if_grade_below_threshold(70, 70)
        
        captured = capsys.readouterr()
        assert "Grade 70 is above the threshold." in captured.out