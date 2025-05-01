import unittest

from Lab2_FiniteAutomata.task3 import FiniteAutomaton

class TestAddFunction(unittest.TestCase):

    def test_fa_to_grammar(self):
        delta = {
            ("q0", "a"): ["q1", "q0"],
            ("q1", "c"): ["q1"],
            ("q1", "b"): ["q2"],
            ("q2", "b"): ["q3"],
            ("q3", "a"): ["q1"],
        }
        fa = FiniteAutomaton(["q0", "q1", "q2", "q3"], ["a","c", "b"], delta, "q0", "q2")
        expected_P = {
            "q0": {"aq0", "aq1"},
            "q1": {"cq1", "bq2", "b"},
            "q2": {"bq3"},
            "q3": {"aq1"}
        }


        #V10
        # delta = {
        #     ("q0", "a"): ["q1"],
        #     ("q1", "b"): ["q2", "q1"],
        #     ("q2", "c"): ["q3"],
        #     ("q3", "a"): ["q1"],
        #     ("q0", "b"): ["q2"],
        # }
        # fa = FiniteAutomaton(["q0", "q1", "q2", "q3"], ["a", "c", "b"], delta, "q0", "q3")
        #
        # expected_P = {
        #     "q0": {"aq1", "bq2"},
        #     "q1": {"bq1", "bq2"},
        #     "q2": {"cq3", "c"},
        #     "q3": {"aq1"}
        # }


        #   V14
        # delta = {
        #     ("q0", "a"): ["q0"],
        #     ("q1", "c"): ["q1", "q2"],
        #     ("q2", "c"): ["q3"],
        #     ("q2", "a"): ["q0"],
        #     ("q1", "a"): ["q1"],
        #     ("q0", "b"): ["q1"],
        # }
        # fa = FiniteAutomaton(["q0", "q1", "q2"], ["a", "c", "b"], delta, "q0", "q2")
        #
        # expected_P = {
        #     "q0": {"aq0", "bq1"},
        #     "q1": {"cq1", "cq2", "aq1", "c"},
        #     "q2": {"cq3", "aq0"}
        # }


        grammar = fa.fa_to_grammar()
        grammar_P_as_sets = {key: set(value) for key, value in grammar.P.items()}
        grammar.printGrammar()

        self.assertEqual(grammar_P_as_sets, expected_P)
        self.assertTrue(fa.is_nfa())

    def test_nfa_to_dfa(self):

        #v10
        # delta = {
        #     ("q0", "a"): ["q1"],
        #     ("q1", "b"): ["q2", "q1"],
        #     ("q2", "c"): ["q3"],
        #     ("q3", "a"): ["q1"],
        #     ("q0", "b"): ["q2"]
        # }
        #
        # fa = FiniteAutomaton(["q0", "q1", "q2", "q3"], ["a", "b", "c"], delta, "q0", "q3")
        #
        # dfa = fa.nfa_to_dfa()
        # dfa.print_fa()

        # #v14
        delta = {
            ("q0", "a"): ["q0"],
            ("q1", "c"): ["q2", "q1"],
            ("q1", "a"): ["q1"],
            ("q2", "a"): ["q0"],
            ("q0", "b"): ["q1"],
        }

        fa = FiniteAutomaton(["q0", "q1", "q2"], ["a", "b", "c"], delta, "q0", "q2")

        dfa = fa.nfa_to_dfa()
        dfa.print_fa()

