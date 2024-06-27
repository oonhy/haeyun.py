T=int(input())

def calc(num,item):
    if item=='@': return num*3
    elif item=='%': return num+5
    elif item=='#': return num-7

for i in range(0,T):
    A=list(input.split(" "))
    num=float(A.pop(0))

    for i in A:
        num=calc(num,i)
    print("%.2f"%num)