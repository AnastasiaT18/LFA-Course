import unittest
import re
from generator import *


class testGenerator(unittest.TestCase):
    def test1(self):

        inputs = [
            r"(a|b)(c|d)E+G?",
            r"P(Q|R|S)T(UV|W|X)*Z+",
            r"1(0|1)*2(3|4){5}36",
            r"M?N{2}(O|P){3}Q*R+",
            r"(X|Y|Z){3}8+(9|0){2}",
            r"(H|i)(J|K)L*N",
            r"O(P|Q|R)+2(3|4)",
            r"A*B(C|D|E)F(G|H|i){2}",
            r"J+K(L|M|N)*O?(P|Q){3}",
            r"(S|T)(U|V)W*Y+24",
            r"L(M|N)O{3}P*Q(2|3)",
            r"R*S(T|U|V)W(X|Y|Z){2}"
        ]

        for input in inputs:
            print("Generated string for ", input, "is: ", generate_string(divide(input)))
            assert re.fullmatch(input, generate_string(divide(input))), "Generated string does not match regex!"




