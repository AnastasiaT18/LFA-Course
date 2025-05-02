import unittest
from parser import *
from lexer import *


class Teser(unittest.TestCase):
    def test1(self):
        tokens = []
        parser = Parser()

        # test = "cos(0.9) + sin(30) - 5"
        # test = "8 - 3 * 2"
        # test = "(3^4 + 5) / 2"
        # test = "cos(30)"
        # test = "-3.14 + +2.718"
        # test = "2.00 + 5"
        # test = "cos(30 + sin(45) * 2) / 5"
        test = "2-(cos(30)- 2^5)"

        parser.feed(tokenize(test))
        tree = parser.parse_expr()
        print_ast(tree)