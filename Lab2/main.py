from Lab2.task2 import *
from Lab2.task3 import *


class Grammar:
    def __init__(self):
        self.V_n = ["S", "A", "B", "C"]
        self.V_t = ["a", "b", "c"]  #mistake, there was c missing
        self.P = {"S": ["bA"],
                  "A": ["b", "aB", "bA"],
                  "B":["bC", "aB"],
                  "C": ["cA"]}


if __name__ == "__main__":
    #task 2
    grammar = Grammar()
    print("---Task 2---")
    print("Grammar is of type ", classify_by_chomsky(grammar))

    #task3
    print("---Task 3 ---")
    delta = {
        ("q0", "a"): ["q1", "q0"],
        ("q1", "b"): ["q1"],
        ("q1", "a"): ["q2"],
        ("q2", "b"): ["q2"],
        ("q2", "a"): ["q0"],
    }
    fa = FiniteAutomaton(["q0", "q1", "q2"], ["a", "b"], delta, "q0", "q2")

    #convert fa to regular grammar
    grammar = fa.fa_to_grammar()
    grammar.printGrammar()

    # determine if NFA or DFA
    if fa.is_nfa():
        print("Nondeterministic")
    else:
        print("Deterministic")

    # convert ndfa to dfa
    dfa = fa.nfa_to_dfa()
    dfa.print_fa()

