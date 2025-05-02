
from lexer import *
from AST import *

class Parser:
    def __init__(self):
        self.tokens = []
        self.pos = 0

    def feed(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current_token(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def current(self, type):
        token = self.current_token()
        return token and token[0] == type


    def advance(self):
        token = self.current_token()
        self.pos += 1
        return token

    def parse_expr(self):
        node = self.parse_term()
        token = self.current_token()
        while self.current(TokenType.ADD) or self.current(TokenType.SUB):
            op = self.advance()[1]
            right = self.parse_term()
            node = Operation(node, op, right)
        return node


    def parse_term(self):
        node = self.parse_factor()
        while self.current(TokenType.MUL) or  self.current(TokenType.DIV) or  self.current(TokenType.PWR):
            op = self.advance()[1]
            right = self.parse_factor()
            node = Operation(node, op, right)
        return node



    def parse_factor(self):
        token = self.current_token()

        if token[0] == TokenType.NUMBER:
            self.advance()
            node = Number(token[1])
            return node
        elif token[0] == TokenType.COS or token[0] ==  TokenType.SIN:
            func = self.advance()[1]
            self.advance()
            argument = self.parse_expr()
            self.advance()
            node = Function(func, argument)
            return node

        elif token[0] == TokenType.LPAR:
            self.advance()
            expr = self.parse_expr()
            self.advance() ##ending RPAR
            return expr




