from lib.diary_entry import *

def test_diary_entry_exists():
    diary_entry = DiaryEntry("Book title", "some stuff")

def test_diary_entry_count_words_example_1():
    diary_entry = DiaryEntry("Book title", "some stuff")
    actual = diary_entry.count_words()
    expected = 2
    assert actual == expected

def test_diary_entry_count_words_example_2():
    diary_entry = DiaryEntry("Book title number 2", "this is four words")
    actual = diary_entry.count_words()
    expected = 4
    assert actual == expected

one_hundred_words =  "one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one one"

def test_diary_entry_reading_time():
    diary_entry = DiaryEntry("One hundred words", one_hundred_words)
    # wpm = 100 words per minute
    actual = diary_entry.reading_time(100)
    expected = 1 # this is one minute
    assert actual == expected
