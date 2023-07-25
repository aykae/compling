from .generator import *
from .bookanalysis import *

def main():
    #generateSentence()
    c22RandSent()

def c22RandSent():
    b = Book("catch22.txt")
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