from lib.grammar_stats import *

def test_grammar_stats_is_not_empty():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello! There! Friend!")
    assert result == True

def test_returns_percentage():
    grammar_stats = GrammarStats()
    sentence = grammar_stats.check("Hello! There! Friend!")
    result = grammar_stats.percentage_good()
    assert result == 100

