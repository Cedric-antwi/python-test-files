from lib.task_includes import *

def test_task_returns_False():
    result = task_includes("hello")
    assert result == False

def test_task_includes_hashtag():
    result = task_includes("#hello")
    assert result == False

def test_task_includes_uppercase_todo():
    result = task_includes('TODO')
    assert result == False

def test_task_includes_all():
    result = task_includes('#TODO')
    assert result == True

def test_task_includes_otherwise():
    result = task_includes('#hello')
    assert result == False

def test_task_includes_sentence():
    result = task_includes('#TODO walk the dog')
    assert result == True
