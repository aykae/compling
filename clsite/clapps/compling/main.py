from .generator import *
from .bookanalysis import *

def main():
    '''
    b = Book("catch22.txt")
    b.parseSentences()
    b.loadSentencesFromFile("c22-sentences-new.txt")
    for sent in b.sentences[:50]:
        print(sent)

    '''
    b = Book("catch22.txt")
    b.parseSentences()
    b.loadSentencesFromFile("c22-sentences-new.txt")
    #c22RandSent()
    c22LongestSentences(b)


def c22LongestSentences(b):
    sortedSents = b.sortSentencesByLength()
    for i in range(10):
        print(sortedSents[i])

def c22RandSent():
    b = Book("catch22.txt")
    b.loadSentencesFromFile("c22-sentences-new.txt")
    print(b.randomSentence())

def c22SentList():
    b = Book("catch22.txt")
    b.parseSentences()

def c22FreqCount():
    b = Book("catch22.txt")
    b.computeWordFreqCount()

def generateSentence():
    eng = English()
    eng.initGrammar()
    
    gen = Generator(eng)

    print("Sentence: ")
    sent = gen.generateSentence()
    print(sent.sentStr)
    sent.tree.displayTree()
    print("Tree size: ", end="")
    print(sent.tree.size)
    print("Tree height: ", end="")
    print(sent.tree.height)