def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True
n=int(input())
arr=list(map(int,input().split()))
if is_sorted(arr):
    print("true")
else:
    print("false")
