from lib.grammar_checker import *

def test_grammar__at_first_index():
    result = grammar_checker('hello')
    assert result == False

def test_grammar_punctuation():
    result = grammar_checker('Hello!')
    assert result == True

# def test_Capital_at_first_index():
#     result = grammar_checker('Hello')
#     assert result == True