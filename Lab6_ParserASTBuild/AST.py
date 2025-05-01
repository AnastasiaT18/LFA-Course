class ASTNode:
    pass

class Number:
    def __init__(self, value):
        self.value = value

class Operation:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Function:
    def __init__(self, function, argument):
        self.function = function
        self.argument = argument

def print_ast(node, prefix="", is_last=True):
    connector = "└── " if is_last else "├── "
    if isinstance(node, Number):
        print(prefix, connector, node.value)
    elif isinstance(node, Function):
        print(prefix, connector, node.function)
        print_ast(node.argument, prefix + ("    " if is_last else " │   "), True)
    elif isinstance(node, Operation):
        print(prefix, connector, node.op)
        print_ast(node.left, prefix + ("    " if is_last else " │   "), False)
        print_ast(node.right, prefix + ("    " if is_last else " │   "), True)



