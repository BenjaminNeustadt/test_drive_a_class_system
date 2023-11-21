from lib.diary import *
from lib.diary_entry import *

def test_diary_exist():
    diary = Diary()

def test_diary_exist():
    diary = Diary()
    diary_entry = DiaryEntry("Book title number 2", "this is four words")
    diary.add(diary_entry)
    actual = diary.entries
    expected = [diary_entry]
    assert actual == expected

