T=str(input())
num=10

for i in range(1,len(T)):
    if T[i]==T[i-1]:
        num+=5
    else:
        num+=10

print(num)