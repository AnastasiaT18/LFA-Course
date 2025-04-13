#Variant 29
from Lab2 import grammar
from ChomskyNormalForm import cnf_converter

if __name__ == '__main__':
    V_n = ["S", "A", "B", "C", "D"]
    V_t = ["a", "b"]
    S = "S"
    P = {"S":["aB", "DA", "ab"],
         "A":["a", "BD", "aDADB"],
         "B": ["b", "ASB"],
         "D": ["", "BA"],
         "C": ["BA"]

         }
    my_grammar = grammar.Grammar(V_n, V_t, S, P)

    my_grammar.printGrammar()

    converter = cnf_converter.CNFConverter()

    my_grammar = converter.convert_to_cnf(my_grammar)





