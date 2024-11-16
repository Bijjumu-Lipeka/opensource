A,B,C=map(int,input().split())
if A+B<=C:
    print(2)
elif A<=C:
    print(1)
else:
    print(0)
