import unittest
from Lab2.main import classify_by_chomsky

class Grammar3:
    def __init__(self):
        self.V_n = ["S", "A", "B", "C"]
        self.V_t = ["a", "b", "c"]  #mistake, there was c missing
        self.P = {"S": ["bA"],
                  "A": ["b", "aB", "bA"],
                  "B":["bC", "aB"],
                  "C": ["cA"]}

class Grammar2:
    def __init__(self):
        self.V_n = ["S"]
        self.V_t = ["0","1"]
        self.P = {
            "S": ["0S1", ""]
        }

class Grammar21:
    def __init__(self):
        self.V_n = ["S", "A"]
        self.V_t = ["0","1"]
        self.P = {
            "S": ["1S", "0A0S", ""],
            "A": ["1A", ""]
        }


class Grammar1:
    def __init__(self):
        self.V_n = ["S", "A", "B", "C"]
        self.V_t = ["a", "b"]
        self.P = {
            "S": ["ACA"],
            "AC": ["AACA", "ABa", "AaB"],
            "B": ["AB", "A"],
            "A": ["a", "b"]
        }

class Grammar0:
    def __init__(self):
        self.V_n = ["S", "B", "C"]
        self.V_t = ["a", "b"]
        self.P = {
            "S": ["aSBC"],
            "BC": ["B"],
            "B": ["b"],
            "C": ["a"]
        }



class TestAddFunction(unittest.TestCase):

    def test_chomsky_3(self):
        grammar = Grammar3()
        self.assertEqual(classify_by_chomsky(grammar), 3)

    def test_chomsky_2(self):
        grammar = Grammar21()
        self.assertEqual(classify_by_chomsky(grammar), 2)

    def test_chomsky_1(self):
        grammar = Grammar1()
        self.assertEqual(classify_by_chomsky(grammar), 1)

    def test_chomsky_0(self):
        grammar = Grammar0()
        self.assertEqual(classify_by_chomsky(grammar), 0)