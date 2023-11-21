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
