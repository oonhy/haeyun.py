#2476
'''틀렸다는데 오ㅐ 틀렸는지 모름 ㅠㅠㅠ'''

N=int(input())
Max=[]

for i in range(N):
    a,b,c=map(int,input().split())

    if a==b==c:
        money=10000+(a*1000)
       
    elif a==b or a==c:
        money=10000+(a*100)
        
    elif b==c:
        money=10000+(b*100)
        
    elif c==a:
        money=10000+(c*100)
        
    elif a!=b and b!=c:
        money=100*max(a,b,c)

    Max.append(money)
    
print(max(Max))
