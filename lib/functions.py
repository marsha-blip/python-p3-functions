#!/usr/bin/env python3
# lib/functions.py

def greet_programmer():
    """Prints a generic greeting to the programmer."""
    print("Hello, programmer!")

def greet(name):
    """Prints a greeting to the given name."""
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    """
    Prints a greeting using the provided name.
    If no name is passed, defaults to "programmer".
    """
    print(f"Hello, {name}!")

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def halve(number):
    """Returns half of the provided number."""
    return number / 2

