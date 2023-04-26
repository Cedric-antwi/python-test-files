class DiaryEntry():
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents

    def format(self):
        return f"{self.title}, {self.contents}"
    
    def count_words(self):
        titleResult = self.title.split(' ')
        contentResult = self.contents.split(' ')
        finalCount = len(titleResult) + len(contentResult)
        return finalCount
    
    def reading_time(self, wpm):
        result = self.count_words()
        self.wpm = wpm
        wpm = int(result/wpm)
        response = f"This will take approx {wpm} minutes to read"
        return response
    
    def reading_chunk(self, wpm, minutes):
        reading_chunk = ""
        text = self.format()
        splitText = text.split(" ")
        reading_capacity = wpm - minutes
        result = splitText[:reading_capacity + 1]
        for word in result:
            if word == result[-1]:
                reading_chunk += word
            else:
                reading_chunk += word + " "
        return reading_chunk



# diaryEntry = DiaryEntry("Dear Diary", "Good moRNING")
# diaryEntry.reading_chunk(4, 3)
#print(diaryEntry.rea)
