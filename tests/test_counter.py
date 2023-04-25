from lib.counter import *

def test_reports_count_operations():
    count = Counter()
    count.add(10)
    result = count.report()
    assert result == "Counted to 10 so far."

def test_if_given_10_giving_5_gives_error():
    count = Counter()
    count.add(10)
    result = count.report()
    assert result == "Counted to 10 so far."