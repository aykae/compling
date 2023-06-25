class Grammar:

    def __init__(self):
        self.grammar = {}
    
    #Grammar is defined as a dictionary that maps a string to a string.
    #Grammar based on UCLA Prof. Hayes Introductory Linguistics Text, (Figure 116) Phrase Structure Rules V1
        #The string will closely reflect the syntax of the phrase structure rules
        #Ignoring inflectional morphology at the moment
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
        self.grammar["V"] = ("speaks", "jumps", "learns")
        self.grammar["Adj"] = ("tall", "loud", "big", "expensive")


