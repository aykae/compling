import os
import random, json
from .tree import PSTree, PSNode, Word

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
        currDir = os.path.dirname(__file__)
        filepath = os.path.join(currDir, "data/pos_to_word.json")
        with open(filepath, "r") as f:
            ptwDict = json.load(f)
            
        self.lexicon["N"] = tuple(ptwDict["NN"])
        self.lexicon["V"] = tuple(ptwDict["VB"])
        self.lexicon["Adj"] = tuple(ptwDict["JJ"])

        self.lexicon["Art"] = tuple(ptwDict["DT"])
        self.lexicon["Aux"] = tuple(ptwDict["MD"])
        self.lexicon["Pro"] = ("i", "you", "he", "she", "it", "we", "they") #N/A

    #should be compartmentalized (json file, util file) as it supports more cases
    def computePronounInflection(self, pronoun, case):
        if case == "ACC": #accusative case
            if pronoun == "i":
                return "me"
            elif pronoun == "he":
                return "him"
            elif pronoun == "she":
                return "her"
            elif pronoun == "we":
                return "us"
            elif pronoun == "they":
                return "them"


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

            #Inflectional Morphology Computation
            if currNode.pos == "pronoun" and currNode.case == "ACC":
                tempStr = self.lang.computePronounInflection(tempStr, currNode.case)
                print("computed inflectional morphology")
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

                newNode = PSNode()

                if currNode.case: #exchange for transferMorphosyntax() function that generalizes this
                    newNode.case = currNode.case
                
                if sym[0] == "(": #Remove optional parentheses
                    sym = sym[1:-1]
                    if random.randint(1,10) < 5: #Randomly insert optional symbol
                        continue

                newNode.data = sym
                currNode.children.append(newNode)
                sentence.tree.size += 1

                #set noun phrase case
                if currNode.data == "VP" and newNode.data == "NP":
                    newNode.case = "ACC" #set node to accusative case
                if currNode.data == "Pro":
                    newNode.pos = "pronoun"

                tempStr += self.recurseGrammar(sentence, newNode, depth + 1)

            return tempStr