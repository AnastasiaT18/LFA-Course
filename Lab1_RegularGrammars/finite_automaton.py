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
                else:
                    return False

            current_states = next_states

        if any(state in self.f for state in current_states):
            return True
        else:
            return False
