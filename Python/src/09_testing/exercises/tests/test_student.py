import pytest

import sys
from pathlib import Path

# Add the exercises directory to the path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from student import Student


class TestStudent:
    def test_init(self):
        """Test proper initialization of a Student object."""
        # TODO: Implement this test

    def test_name_setter(self):
        """Test setting a new name."""
        # TODO: Implement this test

    def test_student_id_setter(self):
        """Test setting a new student ID."""
        # TODO: Implement this test

    def test_grades_setter(self):
        """Test setting new grades."""
        # TODO: Implement this test

    def test_calculate_average_normal(self):
        """Test average calculation with normal grades."""
        # TODO: Implement this test

    def test_calculate_average_empty(self):
        """Test average calculation with empty grades list raises error."""
        # TODO: Implement this test

    def test_add_grade_valid(self):
        """Test adding a valid grade."""
        # TODO: Implement this test

    def test_add_grade_too_low(self):
        """Test adding a grade below 0 raises error."""
        # TODO: Implement this test

    def test_add_grade_too_high(self):
        """Test adding a grade above 100 raises error."""
        # TODO: Implement this test
