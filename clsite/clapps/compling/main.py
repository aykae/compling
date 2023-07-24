from .generator import *
from .bookanalysis import *

def main():
    #generateSentence()
    printBook()

def printBook():
    b = Book("catch22.txt")
    b.parseChapters()


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