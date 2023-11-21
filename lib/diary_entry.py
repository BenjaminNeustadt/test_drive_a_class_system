# File: lib/diary_entry.py

class DiaryEntry:
#    # Public Properties:
#    #   title: a string
#    #   contents: a string
#
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents

    def count_words(self):
        list_of_contents_words = self.contents.split()
        return len(list_of_contents_words)

    def reading_time(self, wpm):
        list_of_words = self.contents.split()
        number_of_words = len(list_of_words)
        return number_of_words / wpm

#
#    def reading_chunk(self, wpm, minutes):
#        # Parameters:
#        #   wpm: an integer representing the number of words the user can read
#        #        per minute
#        #   minutes: an integer representing the number of minutes the user has
#        #            to read
#        # Returns:
#        #   A string representing a chunk of the contents that the user could
#        #   read in the given number of minutes.
#        # If called again, `reading_chunk` should return the next chunk,
#        # skipping what has already been read, until the contents is fully read.
#        # The next call after that it should restart from the beginning.
#        pass
