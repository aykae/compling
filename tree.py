class PSNode:
    def __init__(self):
        self.isLeaf = False
        self.data = None #either instance of Word class (leaf) OR string (non-leaf)
        self.children = [] #list of child nodes
        self.next = None #node that comes next in the resulting phrase of the tree. only applies if leaf

class PSTree: #Phrase Structure Tree
    def __init__(self):
        self.root = PSNode()
        self.size = 0
        self.height = 0

    def displayTree(self):
        self.recurseDisplay(self.root, 1)

    def recurseDisplay(self, currNode, depth):
        for _ in range(depth - 1):
            print("\t", end="")
        
        if isinstance(currNode.data, str):
            print(currNode.data)
        elif isinstance(currNode.data, Word):
            print(currNode.data.getWord())

        for ch in currNode.children:
            self.recurseDisplay(ch, depth + 1)
         
class Word:
    def __init__(self, word, pos=None, person=None, number=None, case=None, tense=None):
        self.baseWord = word #str: the word itself, in its base inflectional form
        self.word = word #str: the up to date inflectional form of the word

        #Optionals
        self.pos = pos #Part of Speech: noun, verb, article, preposition, adjective, adverb
        self.person = person #1st, 2nd, or 3rd person
        self.number = number #str: sg for singular, pl for plural
        self.case = case #str: nominative, accusative, genitive, dative, locative, ablative, instrumental
        self.tense = tense #str: past, present, future

    def update(self):
        if self.pos == "verb" and self.tense == "present" and self.person == 3 and self.number == "sg": #3rd pres sing rule
            self.word = self.baseWord + "s"
        if self.pos == "verb" and self.tense == "past": #past regular verb rule
            if self.word[-1] == "e": #accounting for verb-ending-in-e cas
                self.word = self.baseWord + "d"
            else:
                self.word = self.baseWord + "ed"


    def getWord(self): #update word based on inflectional morphology and return it
        self.update()
        return self.word
