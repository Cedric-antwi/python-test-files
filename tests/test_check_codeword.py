from lib.check_codeword import *

def test_if_given_codeword_returns_correct():
    result = check_codeword("horse")
    assert result == "Correct! Come in."