from generator import *

if __name__ == '__main__':
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
