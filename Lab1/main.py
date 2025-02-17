from grammar import Grammar

grammar = Grammar()
valid_strings = []
for i in range(5):
    valid_strings.append(grammar.generate_string())

for string in valid_strings:
    print(string)

finite_automaton = grammar.to_finite_automaton()
# print(finite_automaton.delta)
# print(finite_automaton.f)

for string in valid_strings:
    print(finite_automaton.string_belongs_to_fa(string))

