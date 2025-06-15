# Exercise 10: Snake Refactored

## Objective
The goal of this exercise is to refactor the `SnakeGame` class into smaller, specialized classes to improve maintainability and readability.

---

## Tasks

### Refactor the SnakeGame Class
Your task is to split the [SnakeGame](./exercises/snake_game_clean.py) class into smaller, more focused classes.

To proceed:
**Analyze the SnakeGame Class**:
  - Review the implementation of the `SnakeGame` class and its methods.
  - Refactor the `SnakeGame` class into smaller classes, such as:
    - `GameBoard`: Handles the game board logic.
    - `Snake`: Manages the snake's position and movement.
    - `Position`: Represents a position on the game board.
    - `Food`: Manages the food's position and spawning.
    - `Game`: Coordinates the game flow and interactions between the other classes.
  - Ensure each class has a clear responsibility and minimal code (duplication).

In case the code is not working after the refactoring, You made the experience, how important unit tests are for refactoring. 😉

## Goals
By the end of this exercise, you should:
- Understand how to refactor large classes into smaller, specialized classes.
- Improve the design and maintainability of the code.
- Develop skills in creating modular and reusable components.

Good luck!
