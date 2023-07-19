import unittest
from generator import Grammar
from clsite.clapps.compling.utils.tree import Word

class TestGrammarParse(unittest.TestCase):
    
    #PLACEHOLDER
    def test_test(self):
        self.assertEqual(2, 2, "Expected: True")

class TestWord(unittest.TestCase):

    def test_third_sg_present_verb_rule(self):
        word = Word(word="write", person=3, number="sg", tense="present", pos="verb")
        self.assertEqual(word.getWord(), "writes", "Expected: True")
    
    def test_past_verb_regular_rule(self):
        word = Word(word="walk", tense="past", pos="verb")
        self.assertEqual(word.getWord(), "walked", "Expected: True")

    def test_past_verb_regular_e_ending_rule(self):
        word = Word(word="code", tense="past", pos="verb")
        self.assertEqual(word.getWord(), "coded", "Expected: True")


if __name__ == '__main__':
    unittest.main()


