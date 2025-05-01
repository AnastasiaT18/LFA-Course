import unittest

from Lab2_FiniteAutomata import grammar
from Lab5_ChomskyNormalForm import cnf_converter


class TestAddFunction(unittest.TestCase):

    def test_V10(self): #V10
        converter = cnf_converter.CNFConverter()

        V_n = ["S", "A", "B", "D"]
        V_t = ["a", "b", "d"]
        S = "S"
        P = {"S": ["dB", "AB"],
             "A": ["d", "dS", "aAaAb", ""],
             "B": ["a", "aS", "A"],
             "D": ["Aba"]
             }
        g = grammar.Grammar(V_n, V_t, S, P)
        g.printGrammar()

        g = converter.convert_to_cnf(g)

    def test_V14(self):  # V10
        converter = cnf_converter.CNFConverter()

        V_n = ["S", "A", "B","C", "D"]
        V_t = ["a", "b"]
        S = "S"
        P = {"S": ["aB", "A"],
             "A": ["bAa", "aS", "a"],
             "B": ["AbB", "BS", "a", ""],
             "C":["BA"],
             "D": ["a"]
             }
        g = grammar.Grammar(V_n, V_t, S, P)
        g.printGrammar()

        g = converter.convert_to_cnf(g)





