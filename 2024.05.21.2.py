while True:
    try:
        a,b=map(int,input().split())

        if a>b:
            print('Yes')

        elif a<=0 or b<=0:
            break
        else:
            print('No')
    except:
        break

