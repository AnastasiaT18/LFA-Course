import re

TOKENS = {
    "NUMBER" : r"[+-]?(\d+(\.\d+)?)",
    "ADD": r"\+" ,
    "SUB": r"\-" ,
    "MUL": r"\*" ,
    "COS": r"cos",
    "SIN": r"sin",
    "MOD": r"%",
    "DIV": r"\/",
    "LPAR": r"\(",
    "RPAR": r"\)",
    "PWR": r"\^",
    "WHITESPACE": r"\s+"
}

TOKEN_REGEX = "|".join(f"(?P<{name}>{pattern})" for name, pattern in TOKENS.items())
TOKEN_PATTERN = re.compile(TOKEN_REGEX)


def tokenize(text):
    tokens = []
    for match in TOKEN_PATTERN.finditer(text):
        type = match.lastgroup
        value = match.group()
        if type != "WHITESPACE":
            tokens.append((type, value))
    return tokens

