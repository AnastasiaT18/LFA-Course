import unittest
from Lab3_LexerScanner.lexer import *

class TestLexer(unittest.TestCase):
    def test_lexer(self):
        test = "cos(0.9) + sin(30) - 5"
        print(test)
        self.assertEqual(tokenize(test), [('COS', 'cos'), ('LPAR', '('), ('NUMBER', '0.9'), ('RPAR', ')'), ('ADD', '+'),  ('SIN', 'sin'), ('LPAR', '('), ('NUMBER', '30'), ('RPAR', ')'), ('SUB', '-'), ('NUMBER', '5')])
        print(tokenize(test))

        test = "8 - 3 * 2"
        self.assertEqual(tokenize(test), [('NUMBER', '8'), ('SUB', '-'),  ('NUMBER', '3'),  ('MUL', '*'), ('NUMBER', '2')])

        test = "(3^4 + 5) / 2"
        self.assertEqual(tokenize(test), [('LPAR', '('), ('NUMBER', '3'),('PWR', '^'), ('NUMBER', '4'), ('ADD', '+'), ('NUMBER', '5'), ('RPAR', ')'), ('DIV', '/'), ('NUMBER', '2')])

        test = "cos(30)"
        self.assertEqual(tokenize(test), [('COS', 'cos'), ('LPAR', '('), ('NUMBER', '30'), ('RPAR', ')')])

        test = "-3.14 + +2.718"
        print(test)
        self.assertEqual(tokenize(test), [('NUMBER', '-3.14'), ('ADD', '+'), ('NUMBER', '+2.718')])
        print(tokenize(test))

        test = "2.00 + 5"
        self.assertEqual(tokenize(test), [('NUMBER', '2.00'), ('ADD', '+'), ('NUMBER', '5')])

        test = "cos(30 + sin(45) * 2) / 5"
        print(test)
        self.assertEqual(tokenize(test), [('COS', 'cos'), ('LPAR', '('), ('NUMBER', '30'), ('ADD', '+'), ('SIN', 'sin'),
        ('LPAR', '('), ('NUMBER', '45'), ('RPAR', ')'), ('MUL', '*'), ('NUMBER', '2'),
        ('RPAR', ')'), ('DIV', '/'), ('NUMBER', '5')])
        print(tokenize(test))
