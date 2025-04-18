from generator import *

if __name__ == '__main__':
    input1 = r"(a|b)(c|d)E+G?"
    input2 = r"P(Q|R|S)T(UV|W|X)*Z+"
    input3 = r"1(0|1)*2(3|4){5}36"

    inputs = [input1, input2, input3]

    for input in inputs:
        strings = [generate_string(divide(input)) for i in range(5)]
        print("Generated strings for ", input, "is: ", strings)

