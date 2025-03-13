# Given that:
# AF = (Q,∑,δ,q0,F)

# Variant 29
# Q = {q0,q1,q2},
# ∑ = {a,b},
# F = {q2},
# δ(q0,a) = q1,
# δ(q0,a) = q0,
# δ(q1,b) = q1,
# δ(q1,a) = q2,
# δ(q2,b) = q2,
# δ(q2,a) = q0.


from Lab2.grammar import Grammar

class FiniteAutomaton:
    def __init__(self, q, sigma, delta, q0, f):
        self.q = q #states
        self.sigma = sigma #alphabet
        self.delta = delta #transition functions
        self.q0 = q0 #initial states
        self.f = f #final states

    def fa_to_grammar(self):
        V_n = self.q
        V_t = self.sigma
        S = self.q0
        P = {}

        for state in self.q:
            P[state] = []

        for (start,char), result in self.delta.items():
            for next_state in result:
                P[start].append(f"{char}{next_state}")

                if next_state in self.f:
                    P[start].append(f"{char}")
        grammar = Grammar(V_n, V_t, S, P)
        return grammar

    def is_nfa(self):
        for (start, char), result in self.delta.items():
            if len(result) > 1:
                return True
        return False

    def nfa_to_dfa(self):
        dfa_q0 = {self.q0}
        dfa_sigma = self.sigma
        dfa_delta = {}
        dfa_f = set() #done
        dfa_q = [dfa_q0] #done
        unprocessed_states = [dfa_q0]

        while unprocessed_states:
            current = unprocessed_states.pop(0)

            for letter in dfa_sigma:
                next = set()

                for state in current:
                    if (state, letter) in self.delta:
                        next.update(self.delta[(state, letter)])
                if next and next not in dfa_q:
                    unprocessed_states.append(next)
                    dfa_q.append(next)
                dfa_delta[(tuple(current), letter)] = next

        for q in dfa_q:
            for state in q:
                if state in self.f:
                    dfa_f.add(tuple(q))

        dfa = FiniteAutomaton(dfa_q, dfa_sigma, dfa_delta,dfa_q0, dfa_f)
        return dfa

    def print_fa(self):
        print("FA:")
        print("Q: ", self.q)
        print("∑ : ", self.sigma)
        print("F: ", self.f)
        print("q0:", self.q0)
        print("δ (Transitions):")
        for (start, char), results in self.delta.items():
            print(f"  δ({start}, {char}) → {results}")  # Prints each transition on a new line

