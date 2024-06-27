#10828 파이썬에서 리스트가 스택의 기능을 하기 때문에/n
#스택을 따로 구현할 필요가 없다

import sys
input=sys.stdin.readline
stack=[]

for i in range(int(input())):
    a=input().rstrip()

    if 'push' in a:
        stack.append(a)
    elif a=='pop':
        print(stack.pop() if stack else -1)
    elif a=='size':
        print(len(stack))
    elif a=='empty':
        print(0 if stack else 1)
    elif a=='top':
        print(stack[-1] if stack else -1)
