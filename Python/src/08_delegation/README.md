# Exercise 8: PaintEngine using Delegation

## Objective
The goal of this exercise is to design a system that delegates the painting process to an external system while ensuring flexibility for future development.

---

## Tasks

### Design and Implement PaintConfigurator
Our client wants to develop a PaintConfigurator application that should initiate a painting process. The actual painting process will be delegated to an external system called "PaintEngine." However, the "PaintEngine" doesn't exist yet, and its interface is unknown. 

2 files are provided in the [`exercises`](./exercises/) directory.

To proceed:
1. **Define an Interface for PaintEngine**:
  - Create an abstract class or interface that outlines the expected methods for the PaintEngine.
  - Ensure the interface can accept an object of the existing `PaintConfiguration` class.

2. **Implement a Mock PaintEngine**:
  - Develop a mock implementation of the PaintEngine interface to simulate the painting process.
  - Use this mock implementation for testing and integration purposes.

3. **Integrate PaintConfigurator**:
  - Ensure the PaintConfigurator can initiate the painting process by delegating it to the PaintEngine.

4. **Prepare for Future Development**:
  - Document the interface and assumptions about the PaintEngine.
  - Throw an exception if the PaintEngine is not implemented when the PaintConfigurator tries to initiate the painting process.

---

## Goals
By the end of this exercise, you should:
- Understand how to design systems with external dependencies.
- Be able to implement mock objects for testing and integration.
- Develop skills in creating flexible and maintainable code structures.

Good luck!
