from .generator import *
from .bookanalysis import *

def main():
    b = Book("catch22.txt")
    b.loadSentencesFromFile("c22-sentences-new.txt")
    for sent in b.sentences[:50]:
        print(sent)
    #generateSentence()
    #c22SentList()
    #c22RandSent()


def c22RandSent():
    b = Book("catch22.txt")
    print(b.randomSentence("c22-sentences-new.txt"))

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