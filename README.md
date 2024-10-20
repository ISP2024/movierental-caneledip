## Movie Rental Refactoring

A classic refactoring problem from Chapter 1 of
_Refactoring: Improving the Design of Existing Code_ by Martin Fowler.  

This repository contains Python code translated from the Java version.

The runnable `main.py` creates a customer and prints a statement.


## Instructions

See [Movie Rental Refactoring, Part 1](https://cpske.github.io/ISP/assignment/movierental/movierental-part1) for description of the code and what to do.

Before and after each refactoring you should **run the unit tests**.

## Resources

See [Resources](https://cpske.github.io/ISP/assignment/movierental/movierental-part1#resources) in the assignment description.

## Rationale
2.1 Coupler, Inappropriate Intimacy

2.2 Use move method, because movie class doesn't need this method and class should know less about each other.

5.2 My choice is Rental module. The reason is made from considering low coupling principle, because you will need a price code when you need to calculate rental price. The other modules don't have specific need for this method. Also as time pass, new movie will turn into a regular, so I think that a method should be in rental module that is used at the time customer rent a movie.