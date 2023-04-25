from lib.greet import *

def test_if_given_name_returns_greeting():
    result = greet("cedric")
    assert result == "Hello, cedric!"