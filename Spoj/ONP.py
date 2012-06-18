'''
Created on Jun 11, 2012

@author: utkarsh
'''

def processExpression(expr):
    stack = []
    ret = ""
    
    for i in range(len(expr)):
        char = expr[i:i+1]
        if char in ['+', '-', '/', '*', '^']:
            stack.append(char)
        elif char==')':
            ret += stack.pop()
        elif char!='(':
            ret += char
            
    while len(stack)>0:
        ret+=stack.pop()
            
    print(ret)

n = int(input())
for i in range(n):
    exp = input()
    processExpression(exp)

if __name__ == '__main__':
    pass