#1874
count=1
temp=True
stack=[]
op=[]


n=int(input())

for i in range(n):
    a=int(input())

    while count<=a:
        stack.append(count)
        op.append('+')
        count+=1

    if stack[-1]==a:
        stack.pop()
        op.append('-')

    else:
        temp=False
        break

if temp==False:
    print('No')
else:
    for k in op:
        print(k)



    



