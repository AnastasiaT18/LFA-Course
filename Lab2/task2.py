import re

def classify_by_chomsky(grammar):

    type3 = {"left":'[A-Z]{1}', "right":['[A-Z]?[a-z]*', '[a-z]*[A-Z]?']}
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



