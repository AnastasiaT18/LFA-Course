from Lab2_FiniteAutomata import grammar
from itertools import combinations


class CNFConverter:

    def eliminate_eps_transitions(self, grammar):
        new_P = {key: values[:] for key, values in grammar.P.items()}

        exist_nullables = True

        while exist_nullables:
            N = []
            exist_nullables = False
            for key, values in grammar.P.items():
                for value in values:
                   if value == "" and key != "S":
                       N.append(key)
                       exist_nullables = True

            if not N:
                # if "" in new_P[grammar.S]:
                #     grammar.V_n.append("S0")
                #     new_P["S0"] = [f"{grammar.S}"]
                #     grammar.S = "S0"
                break

            for nullable in N:
                for key, values in grammar.P.items():
                    for value in values:
                        if value.count(nullable) > 0:
                            indexes = self.get_indexes(value, nullable)
                            new_prod = set()

                            for i in range(1, len(indexes) + 1):
                                combos = combinations(indexes, i)
                                for combo in combos:
                                    chars = list(value)
                                    for index in combo:
                                        chars[index] = ''
                                    new = ''.join(chars)
                                    if new not in grammar.P[key]:
                                        new_prod.add(new)
                            new_prod = list(new_prod)
                            for elem in new_prod:
                                new_P[key].append(elem)

            new_P[nullable].remove("")
            exist_nullables = True
            grammar.P = {key: values[:] for key, values in new_P.items()}

        grammar.P = new_P

        return grammar

    def get_indexes(self, word, eps):
        indexes = []
        i = word.find(eps)
        while i != -1:
            indexes.append(i)
            i = word.find(eps, i + 1)
        return indexes

    def eliminate_renaming(self, grammar):

        new_P = {key: values[:] for key, values in grammar.P.items()}

        exist_unit_productions = True

        while exist_unit_productions:
            exist_unit_productions = False
            for key, values in grammar.P.items():
                for value in values:
                    if len(value) == 1 and value in grammar.V_n:
                        new = grammar.P[value]
                        for elem in new:
                            if elem not in new_P[key]:
                                new_P[key].append(elem)
                        new_P[key].remove(value)
                        exist_unit_productions = True

            grammar.P = {key: values[:] for key, values in new_P.items()}

        return grammar

    def eliminate_nonprod(self, grammar):

        nonproductive_symbols = self.find_nonproductive_symbols(grammar)
        new_P = {key: values[:] for key, values in grammar.P.items()}

        if len(nonproductive_symbols) > 0:
            for symbol in nonproductive_symbols:
                grammar.V_n.remove(symbol)
                new_P.pop(symbol) #remove productions from those nonprods
                for key, values in new_P.items():
                    for value in values:
                        if symbol in value:
                            values.remove(value)
            grammar.P = new_P

        return grammar

    def find_nonproductive_symbols(self, grammar):
        productive_symbols = []
        for key, values in grammar.P.items():
            if key in productive_symbols:
                continue
            for value in values:
                if all(char in grammar.V_t or char in productive_symbols for char in value):
                    if key not in productive_symbols:
                        productive_symbols.append(key)
                        break

        nonprod = []
        for nonterminal in grammar.V_n:
            if nonterminal not in productive_symbols:
                nonprod.append(nonterminal)
        return nonprod

    def eliminate_inaccessible(self, grammar):
        new_P = {key: values[:] for key, values in grammar.P.items()}

        inaccessible_symbols = self.find_inaccessible_symbols(grammar)

        if len(inaccessible_symbols) > 0:
            for symbol in inaccessible_symbols:
                grammar.V_n.remove(symbol)
                new_P.pop(symbol)
                for key, values in new_P.items():
                    for value in values:
                        if symbol in value:
                            values.remove(value)
            grammar.P = new_P

        return grammar

    def find_inaccessible_symbols(self, grammar):
        accessible_symbols = [grammar.S]
        inaccessible_symbols = []

        for key, values in grammar.P.items():
            for value in values:
                for elem in value:
                    if elem not in accessible_symbols:
                        accessible_symbols.append(elem)

        for nonterminal in grammar.V_n:
            if nonterminal not in accessible_symbols:
                inaccessible_symbols.append(nonterminal)
        return inaccessible_symbols

    def obtain_chomsky(self, grammar):

        new_P = {key: values[:] for key, values in grammar.P.items()}
        counter = [1]
        new_nonterminals = grammar.V_n
        terminal_to_var = {}

        for key,values in grammar.P.items():
            for i, value in enumerate(values):
                value = list(value)

                if len(value) > 1:
                    new_P[key][i] = self.break_into_binary(grammar, value, new_P, counter, new_nonterminals, terminal_to_var)

        grammar.P = new_P
        grammar.V_n = new_nonterminals
        return grammar

    def break_into_binary(self, grammar, value, new_P, counter, new_nonterminals, terminal_to_var):

        if len(value) == 2:
            if all(elem in grammar.V_n for elem in value):
                return ''.join(value)
            else:
                for i, elem in enumerate(value):
                    if elem in grammar.V_t:
                        if elem not in terminal_to_var.keys():
                            var = f"X{counter[0]}"
                            counter[0] += 1
                            terminal_to_var[elem] = var
                            new_P[var] = [elem]
                            new_nonterminals.append(var)
                        value[i] = terminal_to_var[elem]
                return ''.join(value)


        first= value[0]
        rest = value[1:]

        if first in grammar.V_t:
            if first not in terminal_to_var.keys():
                v = f"X{counter[0]}"
                counter[0] += 1
                terminal_to_var[first] = v
                new_P[v] = [first]
                new_nonterminals.append(v)
            first = terminal_to_var[first]

        var = self.break_into_binary(grammar, rest, new_P, counter, new_nonterminals, terminal_to_var)

        if var not in terminal_to_var.keys():
            v = f"X{counter[0]}"
            counter[0] += 1
            terminal_to_var[var] = v
            new_P[v] = [var]
            new_nonterminals.append(v)
        rest = terminal_to_var[var]
        return ''.join(first + rest)



    def convert_to_cnf(self, grammar):
        grammar = self.eliminate_eps_transitions(grammar)
        print("Grammar after removing eps transitions:")
        grammar.printGrammar()

        grammar = self.eliminate_renaming(grammar)
        print("Grammar after removing unit productions:")
        grammar.printGrammar()

        grammar = self.eliminate_nonprod(grammar)
        print("Grammar after removing non-productive symbols:")
        grammar.printGrammar()

        grammar = self.eliminate_inaccessible(grammar)
        print("Grammar after removing inaccessible symbols:")
        grammar.printGrammar()

        grammar = self.obtain_chomsky(grammar)
        print("Chomsky Normal Form:")
        grammar.printGrammar()


        return grammar