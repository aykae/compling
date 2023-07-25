from .generator import *
from .bookanalysis import *

def main():
    #generateSentence()
    c22SentList()

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