from lib.diary_entry import *

def test_diary_entry_title():
    diaryEntry = DiaryEntry("Dear Diary", "Good Morning")
    assert diaryEntry.title == "Dear Diary"

def test_diary_returns_format():
    diaryEntry = DiaryEntry("Dear Diary", "Good Morning")
    assert diaryEntry.format() == "Dear Diary, Good Morning"

def test_returns_number_of_words():
    diaryEntry = DiaryEntry("Dear Diary", "Good Morning")
    assert diaryEntry.count_words() == 4

def test_returns_reading_time():
    diaryEntry = DiaryEntry("Dear Diary", "Good Morning")
    assert diaryEntry.reading_time(1) == 'This will take approx 4 minutes to read'

def test_returns_reading_chunk():
    diaryEntry = DiaryEntry("Dear Diary", "Good Morning")
    assert diaryEntry.reading_chunk(1, 3) == "Dear Diary, Good"