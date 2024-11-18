def balance_array(N,A):
    total_sum=sum(A)
    left_weight=0
    B=[]
    for i in range(N):
        right_weight=total_sum-left_weight-A[i]
        B.append(abs(left_weight-right_weight))
        left_weight+=A[i]
    return B

N=int(input())
A=list(map(int,input().split()))
B=balance_array(N,A)
print(" ".join(map(str,B)))
