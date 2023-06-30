import random

class Grammar:

    def __init__(self):
        self.grammar = {}
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
        self.grammar["N"] = ("book", "scientist", "language")
        self.grammar["Art"] = ("the", "a", "that", "this")
        self.grammar["Aux"] = ("have", "should", "must")
        self.grammar["Pro"] = ("he", "she", "it")
        self.grammar["V"] = ("speak", "jump", "learn")
        self.grammar["Adj"] = ("tall", "loud", "big", "expensive")

    def generateSentence(self):
        sentence = ""
        state = "S" 
        
        return self.recurseGrammar(sentence, state)
   
    def recurseGrammar(self, sentence, state):  
        exprVal = self.grammar[state]

        if isinstance(exprVal, tuple): #we have reached a terminal symbol
            tempStr = random.choice(exprVal) + " "
            return tempStr
        elif isinstance(exprVal, list): #recurse to the next non-terminal symbol
            expr = random.choice(exprVal)
            tempStr = sentence
            for sym in expr.split(" "):
                if sym[0] == "(": #Remove optional parentheses
                    sym = sym[1:-1]
                    if random.randint(1,10) > 5: #Randomly insert optional symbol
                        state = sym
                        tempStr += self.recurseGrammar(sentence, state)
                else:
                    state = sym
                    tempStr += self.recurseGrammar(sentence, state)
            return tempStr

if __name__ == '__main__':
    g = Grammar()
    g.initGrammar()
    
    print("Sentence: ")
    print(g.generateSentence())
