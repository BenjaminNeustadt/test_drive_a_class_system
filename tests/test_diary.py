from lib.diary import *
from lib.diary_entry import *

def test_diary_exist():
    diary = Diary()

def test_add_diary_entry_to_diary_entries_list():
    diary = Diary()
    diary_entry = DiaryEntry("Book title number 2", "this is four words")
    diary.add(diary_entry)
    actual = diary.entries_list
    expected = [diary_entry]
    assert actual == expected

def test_add_diary_entry_to_diary_entries_list():
    diary = Diary()
    diary_entry_1 = DiaryEntry("Book title number 1", "this is four words")
    diary_entry_2 = DiaryEntry("Book title number 2", "this is not four words")
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    actual = diary.all()
    expected = diary.entries_list
    assert actual == expected

def test_add_diary_entry_count_words_for_one_entry():
    diary = Diary()
    diary_entry_1 = DiaryEntry("Book title number 1", "this is four words")
    diary.add(diary_entry_1)
    actual = diary.count_words()
    expected = 4
    assert actual == expected

def test_add_diary_entry_count_words_for_one_two_entries():
    diary = Diary()
    diary_entry_1 = DiaryEntry("Book title number 1", "this is four words")
    diary_entry_2 = DiaryEntry("Book title number 6", "this is more like six words")
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    actual = diary.count_words()
    expected = 10
    assert actual == expected

def test_add_diary_entry_count_words_for_one_three_entries():
    # here the '...' isn't really a word, but we choose to leaveit for now and consider the logic later
    diary = Diary()
    diary_entry_1 = DiaryEntry("Book title number 1", "this is four words")
    diary_entry_2 = DiaryEntry("Book title number 6", "this is more like six words")
    diary_entry_3 = DiaryEntry("Book title number 6", "this is … ")
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    diary.add(diary_entry_3)
    actual = diary.count_words()
    expected = 13
    assert actual == expected
