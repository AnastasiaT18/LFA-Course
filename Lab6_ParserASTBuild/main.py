from lexer import *
from parser import *
from AST import *

if __name__ == '__main__':
    test = "(3^4 + 5) / 2"
    print(tokenize(test))
    tokens = tokenize(test)
    parser = Parser(tokens)
    tree = parser.parse_expr()
    print_ast(tree)