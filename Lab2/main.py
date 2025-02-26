import re

class Grammar:
    def __init__(self):
        self.V_n = ["S", "A", "B", "C"]
        self.V_t = ["a", "b", "c"]  #mistake, there was c missing
        self.P = {"S": ["bA"],
                  "A": ["b", "aB", "bA"],
                  "B":["bC", "aB"],
                  "C": ["cA"]}


def classify_by_chomsky(grammar):

    type3 = {"left":'[A-Z]{1}', "right":['[A-Z]?[a-z]*', '[a-z]*[A-Z]?']}
    #type3_left = '[A-Z]?[a-z]*'
    #type3_right = '[a-z]*[A-Z]?'
    #type2 = '[a-zA-Z]*'
    type2 = r'^[^\s]*[A-Z]*[^\s]*$'
    type1 = {"left":'[a-z]*[A-Z]+[a-z]*', "right":'[a-zA-Z]*'} #lenght of left and right matters??

    if all(re.fullmatch(type3["left"], left) for left in grammar.P.keys()):
        if all(re.fullmatch(type3["right"][0], rule) for rules in grammar.P.values() for rule in rules):
            return 3
        elif all(re.fullmatch(type3["right"][1], rule) for rules in grammar.P.values() for rule in rules):
            return 3
        elif all(re.fullmatch(type2, rule) for rules in grammar.P.values() for rule in rules):
            return 2
        else:
            return -1
    elif all(re.fullmatch(type1["left"],left) for left in grammar.P.keys()):
        if all(re.fullmatch(type1["right"], rule) for rules in grammar.P.values() for rule in rules):
            if all(len(left) <= len(rule) for left, right in grammar.P.items() for rule in right):
                return 1
            else:
                return 0



if __name__ == "__main__":
    grammar = Grammar()
    print("Grammar is of type ", classify_by_chomsky(grammar))

