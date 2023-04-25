1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.
- check if starts with capital (first index)
- check for suitable punctuation (last index)

2. Design the Function Signature
Include the name of the function, its parameters, return value, and side effects.
- Parameters: (list all parameters and their types)
- Returns: (state the return value and its type)
- Side effects: (state any side effects)

<!-- function name: -->
grammer_checker
<!-- parameters -->
grammer_checker(text)
<!-- returns -->
should return True or False for capital and punctuation.
<!-- side effects -->
this function will return a boolean and not print anything.



3. Create Examples as Tests
Make a list of examples of what the function will take and return.
E.g.
This will form your tests
"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
extract_uppercase("hello WORLD") => ["WORLD"]

<!-- example test -->
Given a piece of text, test for capital letter in text
grammer_checker("Hello world") => True

Given a piece of text, test for punctuation in text
grammer_checker("Hello world!") => True

given a number, test should return an error message
grammer_checker(25) => "Enter a string"


4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

End Example
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
