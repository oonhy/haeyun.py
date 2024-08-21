def func(arr, init):
    n=len(arr)
    ret=init
    for i in range(n):
        ret += arr[i]
    return ret

arr= [1,2,3,4,5]
result= func(arr,10)
print(result)