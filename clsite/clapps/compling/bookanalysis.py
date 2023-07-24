import os

class Book:

    filename = ""
    rawBook = ""

    bookLines = []
    chapters = []
    wordFreqCount = {}

    def __init__(self, filename):
        self.filename = filename
        self.loadFile()

    def loadFile(self):
        currDir = os.path.dirname(__file__)
        filepath = os.path.join(currDir, "data/" + self.filename)

        with open(filepath, "r") as f:
            self.bookLines = f.readlines()

    def parseChapters(self):
        self.chapters = []
        for line in self.bookLines:
            if line[0].isnumeric():
                self.chapters.append(line.strip())
        print(self.chapters)

    def computeWordFreqCount(self):
        self.wordFreqCount = {}
        cleanedWords = []

        for line in self.bookLines:
            for word in line.split():
                cleanedWords.append(word.lower().strip("\"\'.,?!\n"))

        for word in cleanedWords:
            if word in self.wordFreqCount.keys():
                self.wordFreqCount[word] += 1
            else:
                self.wordFreqCount[word] = 1

        self.wordFreqCount = dict(sorted(self.wordFreqCount.items(), key=lambda x:x[1], reverse=True))

        print(self.wordFreqCount)

    def sentenceDump(self):
        for i in range(50):
            wordsplit = self.bookLines[i].split()
            for w in range(len(wordsplit)): 
                wordsplit[w] = wordsplit[w].strip("\"\'.?!,")
            print(wordsplit)

