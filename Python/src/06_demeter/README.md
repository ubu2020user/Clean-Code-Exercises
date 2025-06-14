# Exercise 6: Understanding Objects and the Law of Demeter

## Objective
The goal of this exercise is to explore the principles of object-oriented design, specifically focusing on the Law of Demeter, to improve code modularity and maintainability.

---

## Tasks

### Exercise 1: Refactor Code to Adhere to the Law of Demeter
- Open the files in [exercises](./exercises/).
- Identify sections of code that violate the Law of Demeter (e.g., excessive method chaining or direct access to internal objects).
- Refactor the code to ensure:
  - Objects interact only with their immediate collaborators.
  - Encapsulation is maintained by reducing dependencies between objects.
  - Methods are designed to minimize coupling and maximize cohesion.
- Hint: Look in the classes [employee_service.py](./exercises/services/employee_service.py) and [employee.py](./exercises/entities/employee.py) for potential violations.

## Goals
By the end of this exercise, you should:
- Understand the principles of the Law of Demeter and its importance in object-oriented design.
- Be able to identify and refactor code that violates these principles.
- Develop skills in designing modular and maintainable object-oriented systems.

Good luck!
