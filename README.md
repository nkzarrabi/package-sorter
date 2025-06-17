# Package Sorter Coding Exercise

This repository contains a simple setup for the technical screening described below.

## Platform Technical Screen

![Challenge Illustration](https://prod-files-secure.s3.us-west-2.amazonaws.com/1eec7df9-d484-4330-b2c6-8078b2cdeb0e/65e82bd0-dfac-457f-af29-3727fce75c5e/Untitled.png)

### Objective

Imagine you work in Thoughtful’s robotic automation factory. Your objective is to write a function for one of its robotic arms that will dispatch packages to the correct stack according to their volume and mass.

### Rules

A package is **bulky** if its volume (Width x Height x Length) is greater than or equal to `1,000,000 cm³` or when one of its dimensions is greater than or equal to `150 cm`.
A package is **heavy** when its mass is greater than or equal to `20 kg`.

You must dispatch the packages into the following stacks:

- **STANDARD**: packages that are not bulky or heavy.
- **SPECIAL**: packages that are either heavy or bulky.
- **REJECTED**: packages that are **both** heavy and bulky.

### Implementation

Implement the function `sort(width, height, length, mass)` where the units are centimeters for the dimensions and kilograms for the mass. The function should return the name of the stack that the package belongs to as a string.

### Submission Guidance

1. **Time Management**: Allocate no more than 30 minutes to complete this challenge.
2. **Programming Language**: Use any language you are comfortable with. Feel free to demonstrate your skills with a language you know well.
3. **Submission Format**: 
   - Option 1: Provide a public GitHub repository with clear README instructions.
   - Option 2 (preferred): Host your solution on an online IDE such as Repl.it or CodePen for immediate code review. Ensure that the link can be executed directly.
4. **Evaluation Criteria**:
   - Correct sorting logic.
   - Code quality.
   - Handling of edge cases and inputs.
   - Test coverage.

This repository is intentionally minimal. Fork or clone it to begin your implementation.

