class PSNode:
    def __init__(self):
        self.isLeaf = True
        self.data = None #instance of Word class
        self.child = [] #list of child nodes
        self.next = None #node that comes next in the resulting phrase of the tree.

class PSTree: #Phrase Structure Tree
    def __init__(self):
        self.root = PSNode()
        self.size = 0
        self.height = 0
         
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
