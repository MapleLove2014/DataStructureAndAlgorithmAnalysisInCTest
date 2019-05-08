import re

from stack import MyStack

num_pat = re.compile(r'\d')

operator_priority = {
    '+' : 1,
    '-' : 1,
    '*' : 2,
    '(' : -1
}

def pop_all_not_lower(bit, operators, postfix):
    while operators.get_size() > 0:
        ope = operators.pop()
        if operator_priority[ope] < operator_priority[bit]:
            operators.push(ope)
            break
        else:
            postfix.append(ope)

def pop_all_operators(operators, postfix):
    while operators.get_size() > 0:
        postfix.append(operators.pop())

def pop_all(bit, operators, postfix, stop):
    while operators.get_size() > 0:
        ope = operators.pop()
        if ope == stop:
            break
        else:
            postfix.append(ope)

def check_operator(bit, operators, postfix):
    bit = str(bit)
    if operators.get_size() == 0:
        operators.push(bit)
    else:
        if bit == '+' or bit == '-' or bit == '*':
            pop_all_not_lower(bit, operators, postfix)
            operators.push(bit)
        elif bit == '(':
            operators.push(bit)
        elif bit == ')':
            pop_all(bit, operators, postfix, '(')
        else:
            raise Exception('invalid operator:{}'.format(bit))


def infix2postfix(infix):
    postfix = []
    operators = MyStack()
    
    base = 10
    number = None
    for bit in infix:
        if num_pat.match(bit):
            if number is None:
                number = 0
            number = number * base + int(bit)
        else:
            if number is not None:
                postfix.append(number)
                number = None
            check_operator(bit, operators, postfix)
    if number is not None:
        postfix.append(number)
    pop_all_operators(operators, postfix)
    print(' '.join(map(str, postfix)))
    return postfix

if __name__ == "__main__":
    infix2postfix('32+5*(2+6*3)+2')

