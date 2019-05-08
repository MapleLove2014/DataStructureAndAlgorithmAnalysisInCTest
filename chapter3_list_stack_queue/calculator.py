import re
from stack import MyStack
from reverse_polish import infix2postfix

num_pat = re.compile(r'\d+')

def pop2(numbers):
    return numbers.pop(), numbers.pop()

def eva(expression):
    postfix = infix2postfix(expression)
    numbers = MyStack()
    
    for ele in postfix:
        if num_pat.match(str(ele)):
            numbers.push(int(ele))
        elif ele == '+':
            num1 ,num2 = pop2(numbers)
            numbers.push(num1 + num2)
        elif ele == '*':
            num1 ,num2 = pop2(numbers)
            numbers.push(num1 * num2)
        else:
            raise Exception('Not support operator:{}'.format(ele))
    result = numbers.pop()
    print('evaluation result is : {}'.format(result))
    return result

if __name__ == "__main__":
    eva('32+5*(2+6*3)+2')