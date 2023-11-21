# File: lib/diary_entry.py

class DiaryEntry:
#
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.chunk = []
        self.remaining_chunk_start = 0

    def count_words(self):
        list_of_contents_words = self.contents.split()
        return len(list_of_contents_words)

    def reading_time(self, wpm):
        list_of_words = self.contents.split()
        number_of_words = len(list_of_words)
        return number_of_words / wpm

    def reading_chunk(self, wpm, minutes):
        max_words = wpm * minutes
        list_of_words = (self.contents).split()
        remaining_chunk = list_of_words[self.remaining_chunk_start:self.remaining_chunk_start + max_words]
        self.remaining_chunk_start += len(remaining_chunk)
        report_chunk = ' '.join(remaining_chunk)
        return report_chunk
