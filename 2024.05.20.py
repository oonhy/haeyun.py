total=0
for i in range(1,6):
    score=int(input())
    if score<40:
        score=40
    total += score
average=int(total/5)
print(average)




