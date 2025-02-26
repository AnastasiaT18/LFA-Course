from Lab2.task2 import *

class Grammar:
    def __init__(self):
        self.V_n = ["S", "A", "B", "C"]
        self.V_t = ["a", "b", "c"]  #mistake, there was c missing
        self.P = {"S": ["bA"],
                  "A": ["b", "aB", "bA"],
                  "B":["bC", "aB"],
                  "C": ["cA"]}


if __name__ == "__main__":
    grammar = Grammar()
    print("Grammar is of type ", classify_by_chomsky(grammar))

