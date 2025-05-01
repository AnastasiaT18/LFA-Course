import unittest
from Lab2_FiniteAutomata.task2 import classify_by_chomsky
from Lab2_FiniteAutomata.grammar import *



class TestAddFunction(unittest.TestCase):

    def test_chomsky_3(self):
        grammar = Grammar(["S", "A", "B", "C"], ["a", "b", "c"], "S", {"S": ["bA"],
                  "A": ["b", "aB", "bA"],
                  "B": ["bC", "aB"],
                  "C": ["cA"]})
        self.assertEqual(classify_by_chomsky(grammar), 3)

    def test_chomsky_2(self):
        grammar = Grammar(["S", "A"], ["0", "1"], "S",{"S": ["1S", "0A0S", ""],"A": ["1A", ""]})
        self.assertEqual(classify_by_chomsky(grammar), 2)
        grammar2 = Grammar(["S"], ["0", "1"], "S", {
            "S": ["0S1", ""]
        } )
        self.assertEqual(classify_by_chomsky(grammar2), 2)



    def test_chomsky_1(self):
        grammar = Grammar(["S", "A", "B", "C"], ["a", "b"], "S", {
            "S": ["ACA"],
            "AC": ["AACA", "ABa", "AaB"],
            "B": ["AB", "A"],
            "A": ["a", "b"]
        })

        self.assertEqual(classify_by_chomsky(grammar), 1)

    def test_chomsky_0(self):
        grammar = Grammar(["S", "B", "C"],["a", "b"],"S", {
            "S": ["aSBC"],
            "BC": ["B"],
            "B": ["b"],
            "C": ["a"]
        } )
        self.assertEqual(classify_by_chomsky(grammar), 0)