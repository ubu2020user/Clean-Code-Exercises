# Exercise 9: Testing

## Objective
The goal of this exercise is to test the functionality of the `Student` class while ensuring flexibility for future development.

---

## Tasks

### Test the Student Class
Your task is to write tests for the [Student](./exercises/student.py) class.

To proceed:
1. **Understand the Student Class**:
  - Review the implementation of the `Student` class and its methods.
  - Identify the key functionalities that need to be tested.

2. **Write Unit Tests**:
  - Use a testing framework like `unittest` or `pytest` to write unit tests for the `Student` class.
    - The command to test with pytest and see your coverage is:
      ```bash
      pytest --cov test_student.py
      ```    
  - Ensure that all methods are covered, including edge cases.

3. **Mock Dependencies**:
  - If the `Student` class would interact with external systems or dependencies, you could create mock objects to simulate their behavior.
  - Use mocking libraries like `unittest.mock` or `pytest-mock` or `mockito` to create these mocks.

4. **Ensure Code Coverage**:
  - Aim for high code coverage by testing all branches and conditions in the `Student` class.

---

## Goals
By the end of this exercise, you should:
- Understand how to write effective unit tests.
- Optional: Be able to use mocking techniques for testing dependencies.
- Develop skills in creating robust and maintainable test suites.

Good luck!
