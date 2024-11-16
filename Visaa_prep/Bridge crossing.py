A,B,C=map(int,input().split())
if C>=B:
    max_mangoes=(C-B)//A
else:
    max_mangoes=0
print(max_mangoes)
