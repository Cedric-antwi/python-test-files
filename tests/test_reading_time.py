from lib.reading_time import *

def test_takes_two_paramters_returns_string():
    result = read_time_estimate("Hello there", 1)
    assert result != None

def test_returns_read_time_estimate():
    result = read_time_estimate("Hello there my language is python", 1)
    assert result == "This will take approx 6 minutes to read"

def test_returns_read_time_estimate_for_large_text():
    text = "Given a lowercase word and an uppercase word with an exclamation mark It returns a list with the uppercase word no exclamation mark"
    result = read_time_estimate(text, 1)
    assert result == "This will take approx 23 minutes to read"

def test_returns_error_msg_if_text_is_int():
    result = read_time_estimate(15, 5)
    assert result == "You have not entered any text"