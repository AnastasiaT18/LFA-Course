import random

class FiniteAutomaton:
    def __init__(self, q, sigma, delta, q0, f):
        self.q = q #states
        self.sigma = sigma #alphabet
        self.delta = delta #transition functions
        self.q0 = q0 #initial states
        self.f = f #final states

    def string_belongs_to_fa(self, string):
        current_states = [self.q0]

        for char in string:
            next_states = []

            for state in current_states:
                if (state, char) in self.delta:
                    next_states.extend(self.delta[(state, char)])
                    # print(next_states)
                else:
                    return False

            current_states = next_states

        if any(state in self.f for state in current_states):
            return True
        else:
            return False



class Grammar:
    def __init__(self):
        self.V_n = ["S", "A", "B", "C"]
        self.V_t = ["a", "b", "c"]  #mistake, there was c missing
        self.P = {"S": ["bA"],
                  "A": ["b", "aB", "bA"],
                  "B":["bC", "aB"],
                  "C": ["cA"]}

    def generate_string(self):
        start = "S"
        valid_string = start
        while any(symbol in self.V_n for symbol in valid_string):
            # print(valid_string)
            for i, symbol in enumerate(valid_string):
                if symbol in self.V_n:
                    symbol = random.choice(self.P[symbol])
                    valid_string = valid_string[:i] + symbol + valid_string[i+1:]
                    break
        return valid_string

    def to_finite_automaton(self):
        delta = {}
        for non_terminal, productions in self.P.items():
            for production in productions:
                for i in range(len(production)):
                    if production[i] in self.V_t:
                        if (non_terminal, production[i]) not in delta:
                            delta[(non_terminal, production[i])] = []
                        next_state = None
                        for non_terminal2 in self.V_n:
                            if non_terminal2 in production:
                                next_state = non_terminal2
                                break
                        if next_state is None:
                            next_state = non_terminal
                            f = non_terminal
                        delta[(non_terminal, production[i])].append(next_state)

        finite_automaton = FiniteAutomaton(self.V_n, self.V_t,delta, "S", f)
        return finite_automaton

grammar = Grammar()
valid_strings = []
for i in range(30):
    valid_strings.append(grammar.generate_string())

for string in valid_strings:
    print(string)

finite_automaton = grammar.to_finite_automaton()
print(finite_automaton.delta)
print(finite_automaton.f)

for string in valid_strings:
    print(finite_automaton.string_belongs_to_fa(string))

# print(finite_automaton.string_belongs_to_fa("bbcbb"))