class Grammar:
    def __init__(self, V_n, V_t, S, P):
        self.V_n = V_n
        self.V_t = V_t
        self.S = S
        self.P = P

    def printGrammar(self):
        print("Grammar:")
        print("V_n: ",self.V_n)
        print("V_t: ",self.V_t )
        print("S: ",self.S)
        print("P:",self.P)