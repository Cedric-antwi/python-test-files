1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.

<!-- As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute. -->
the user wants to be able to see a estimation for how long it would ake to read a piece of text, given that they can read 200 words a minute
200 words per 60 seconds
so a text of 100 words should take 30 seconds to read through
400words in 2 mins aka 120secs (2 * 60)


2. Design the Function Signature
Include the name of the function, its parameters, return value, and side effects.
- Parameters: (list all parameters and their types)
- Returns: (state the return value and its type)
- Side effects: (state any side effects)

<!-- function name: -->
# read_time_estimate
<!-- parameters -->
# should take a piece of text as a string
# should take a known wpm from the user as an integer
e.g. read_time_estimate(text, wpm):
<!-- returns -->
# should return an eestimated reading time in minutes as an integer.
<!-- side effects -->
# the function doest print anything, just returns a value



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
Given a text and wpm
it returns a piece of text

Given a piece of text and a wpm integer
it returns an f"string" as a time estimation
"""
read_time_estimate("This is my piece of text", 1) => This will take 6 minutes to read
"""

Given an integer as text
It returns an error msg
""""
read_time_estimate(15, 2) => "You have not entered any text"



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
