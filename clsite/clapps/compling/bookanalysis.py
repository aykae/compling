import os, re, random

class Book:

    filename = ""
    rawBook = ""

    bookLines = []
    chapters = []
    wordFreqCount = {}
    sentences = []

    def __init__(self, filename):
        self.filename = filename
        self.loadFile()

    def loadFile(self):
        currDir = os.path.dirname(__file__)
        filepath = os.path.join(currDir, "data/catch22/" + self.filename)

        with open(filepath, "r") as f:
            self.bookLines = f.readlines()[3:]

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
                cleanedWords.append(word.lower().strip("\"\'.,?!()\n"))

        for word in cleanedWords:
            if word in self.wordFreqCount.keys():
                self.wordFreqCount[word] += 1
            else:
                self.wordFreqCount[word] = 1

        #sorting the dictionary by descending frequency (value)
        self.wordFreqCount = dict(sorted(self.wordFreqCount.items(), key=lambda x:x[1], reverse=True))

        print(self.wordFreqCount)

    def sentenceDump(self):
        for i in range(50):
            wordsplit = self.bookLines[i].split()
            for w in range(len(wordsplit)): 
                wordsplit[w] = wordsplit[w].strip("\"\'.?!,")
            print(wordsplit)

    def parseSentences(self):
        bookstr = ""
        #for i in range(50):
        #for i in range(len(self.bookLines)):
        for line in self.bookLines:
            if line[0].isnumeric():
                continue

            bookstr += line.strip()
            bookstr += " "

        self.sentences = re.split(r"(?<=\.|\?|!)\s+", bookstr)
        #TODO: add split case between
            # -> dialogue quotes e.g. abc\' \'xyz

        #TODO: strip sentences of quotations marks and parentheses

        currDir = os.path.dirname(__file__)
        filepath = os.path.join(currDir, "data/catch22/" + "c22-sentences.txt")
        with open(filepath, "w") as out:
            out.writelines([sent + "\n" for sent in self.sentences])

    def randomSentence(self):
        currDir = os.path.dirname(__file__)
        filepath = os.path.join(currDir, "data/catch22/" + "c22-sentences.txt")
        with open(filepath, "r") as file:
            self.sentences = file.readlines()

        if len(self.sentences) > 0:
            return random.choice(self.sentences)
        else:
            return "ERROR: sentences need to be parsed."