from Lab2 import grammar
from itertools import combinations


class Converter:

    def eliminate_eps_transitions(self, grammar):

        N = []
        new_P = {key: values[:] for key, values in grammar.P.items()}

        for key, values in grammar.P.items():
            for value in values:
               if value == "":
                   N.append(key)

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
                                if new and new != "":
                                    new_prod.add(new)
                        new_prod = list(new_prod)
                        for elem in new_prod:
                            new_P[key].append(elem)

        for key, values in new_P.items():
            if "" in values:
                values.remove("")

        grammar.P = new_P

        return grammar

    def get_indexes(self, word, eps):
        indexes = []
        i = word.find(eps)
        while i != -1:
            indexes.append(i)
            i = word.find(eps, i + 1)
        return indexes

    def eliminate_nonprod(self, grammar):
        pass

    def eliminate_inaccessible(self, grammar):
        pass

    def eliminate_renaming(self, grammar):
        pass

    def obtain_chomsky(self, grammar):
        pass

    def convert_to_cnf(self, grammar):
        grammar = self.eliminate_eps_transitions(grammar)
        grammar = self.eliminate_nonprod(grammar)
        grammar = self.eliminate_inaccessible(grammar)
        grammar = self.eliminate_renaming(grammar)
        grammar = self.obtain_chomsky(grammar)
        return grammar