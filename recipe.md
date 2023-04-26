1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.

As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.
check for # & uppercase

2. Design the Function Signature
Include the name of the function, its parameters, return value, and side effects.
- Parameters: (list all parameters and their types)
- Returns: (state the return value and its type)
- Side effects: (state any side effects)

<!-- function name: -->
task_includes()
<!-- parameters -->
- string representing the user's task
<!-- returns -->
Boolean (True if successful) otherwise false 
<!-- side effects -->
Should return Boolean, will not print anything



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
task_includes("#task") -> True (INCLUDES HASHTAG)
task_includes("#TASK) -> TRUE (uppercase)




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
