import re
from random import choice, randint
from unittest import case


def generate_string(tokens):
    result = ""
    i = 0

    while i<len(tokens):
        if tokens[i].isalnum():
            result += tokens[i]
            i += 1
        elif tokens[i] == "(": ## get the block of parantheses
            substring = []
            start = i
            j = start + 1

            while j < len(tokens) and tokens[j] != ")":
                substring.append(tokens[j])
                j += 1
            result1 = generate_string(substring)
            i = j + 1

            if i < len(tokens) and (tokens[i] in {"*", "+", "?"} or tokens[i].startswith("{")):
                result += repeat(result1, tokens[i])
                i += 1
            else:
                result += result1

        elif tokens[i] == "|":
            options = [result]
            if tokens[i+1] == "(":
                substring = []
                start = i
                j = start + 1
                while j < len(tokens) and tokens[j] != ")":
                    substring.append(tokens[j])
                    j += 1
                options.append(generate_string(substring))
            else:
                options.append(tokens[i+1])
            result = choice(options)
            i += 2

        elif tokens[i] in {"*", "+", "?"} or tokens[i].startswith("{"):
            last = result[-1]
            result = result[:-1] + repeat(last, tokens[i])
            i += 1


    return result



def repeat(string, symbol):
    match symbol:
        case "*":
            return string * randint(0, 5)
        case "+":
            return string * randint(1, 5)
        case "?":
            return string * randint(0,1)
        case _:
            if symbol.startswith("{"):
                times = int(symbol[1:-1])
                return string * times


def divide(pattern):
    tokens = re.findall(r'\(|\)|\||\*|\+|\?|\{.*?\}|\w+', pattern)
    return tokens

