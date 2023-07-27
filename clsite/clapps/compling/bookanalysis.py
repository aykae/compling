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
        currSent = ""
        sentences = []
        sentCount = 0

        #-> Parse sentences from bookLines
        for line in self.bookLines:

            #Ignore chapter titles
            if line[0].isnumeric():
                continue
            
            line = re.split(r"(?<=\.)\s+", line.strip())
            
            for i in range(len(line)):
                if currSent != "":
                    currSent += " "

                currSent += line[i]
                if line[i][-1] == ".":
                    sentences.append(currSent)
                    currSent = ""

        self.sentences = sentences
        #self.sentences = re.split(r"(?<=\.|\?|!)\s+", bookstr)
        #TODO: add split case between
            # -> dialogue quotes e.g. abc\' \'xyz

        #TODO: strip sentences of quotations marks and parentheses

        #-> Write sentences to file
        currDir = os.path.dirname(__file__)
        filepath = os.path.join(currDir, "data/catch22/" + "c22-sentences-new.txt")
        with open(filepath, "w") as out:
            out.writelines([sent + "\n" for sent in self.sentences])

    def randomSentence(self):
        #load sentences if not already done so
        if len(sentences == 0):
            self.loadSentencesFromFile()

        if len(self.sentences) > 0:
            return random.choice(self.sentences)
        else:
            return "ERROR: sentences need to be parsed."

    def loadSentencesFromFile(self, sentfile = "c22-sentences.txt"):
        currDir = os.path.dirname(__file__)
        filepath = os.path.join(currDir, "data/catch22/" + sentfile)
        with open(filepath, "r") as file:
            self.sentences = file.readlines()
