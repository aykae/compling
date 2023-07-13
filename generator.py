import random, json
from tree import PSTree, PSNode, Word

class English:

    def __init__(self):
        self.grammar = {}
        self.lexicon = {}

        self.initGrammar()
   
    ###
    #Grammar is defined as a dictionary that maps a string to a string.
    #Grammar based on UCLA Prof. Hayes Introductory Linguistics Text, (Figure 116) Phrase Structure Rules V1
    #The string will closely reflect the syntax of the phrase structure rules
    #Ignoring inflectional morphology at the moment
    ###

    def initGrammar(self):
        #Phrase Structure Rules
            #Non-terminals are represented as whitespace-separated strings
        self.grammar["S"] = ["NP (Aux) VP"]
        self.grammar["NP"] = ["(Art) (AP) N"]
        self.grammar["NP"].append("Pro")
        self.grammar["VP"] = ["V (NP)"]
        self.grammar["AP"] = ["Adj"]

        #Terminal Symbol Definitions
            #Terminals are designated by a tuple of values
            #Lexical categories suffixed with comment denoting dataset PoS code

        ptwDict = {}
        with open("data/pos_to_word.json", "r") as f:
            ptwDict = json.load(f)
            
        self.lexicon["N"] = tuple(ptwDict["NN"])
        self.lexicon["V"] = tuple(ptwDict["VB"])
        self.lexicon["Adj"] = tuple(ptwDict["JJ"])

        self.lexicon["Art"] = tuple(ptwDict["DT"])
        self.lexicon["Aux"] = tuple(ptwDict["MD"])
        self.lexicon["Pro"] = ("i", "you", "he", "she", "it", "we", "they") #N/A


class Sentence:

    def __init__(self):
        self.sentStr = ""
        self.tree = PSTree()

class Generator:

    def __init__(self, language):
        self.lang = language

    def generateSentence(self):
        sentence = Sentence()
        root = PSNode()
        root.data = "S"
        sentence.tree.root = root
        sentence.tree.size += 1
        
        sentence.sentStr = self.recurseGrammar(sentence, sentence.tree.root, 1)
        return sentence

    def recurseGrammar(self, sentence, currNode, depth):  
        if currNode.data in self.lang.grammar.keys():
            exprVal = self.lang.grammar[currNode.data] #data should be non-terminal symbol
        else:
            exprVal = self.lang.lexicon[currNode.data]
        
        if isinstance(exprVal, tuple): #we have reached a terminal symbol
            tempStr = random.choice(exprVal) + " "

            #Add leaf node with word data
            newNode = PSNode()
            newWord = Word(tempStr)
            newNode.data = tempStr
            newNode.isLeaf = True
            currNode.children.append(newNode)
            sentence.tree.size += 1
            
            #Set tree depth
            if (depth + 1) > sentence.tree.height:
                sentence.tree.height = depth + 1

            return tempStr
        elif isinstance(exprVal, list): #Recurse to the next non-terminal symbol
            expr = random.choice(exprVal)
            tempStr = sentence.sentStr
            for sym in expr.split(" "):
                if sym[0] == "(": #Remove optional parentheses
                    sym = sym[1:-1]
                    if random.randint(1,10) > 5: #Randomly insert optional symbol
                        newNode = PSNode()
                        newNode.data = sym
                        currNode.children.append(newNode)
                        sentence.tree.size += 1

                        tempStr += self.recurseGrammar(sentence, newNode, depth + 1)
                else:
                    newNode = PSNode()
                    newNode.data = sym
                    currNode.children.append(newNode)
                    sentence.tree.size += 1

                    tempStr += self.recurseGrammar(sentence, newNode, depth + 1)
            return tempStr


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

