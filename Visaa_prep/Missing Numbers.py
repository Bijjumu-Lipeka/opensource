def missingNumbers(arr, brr):
    freq1={}
    freq2={}
    for num in arr:
        freq1[num]=freq1.get(num,0)+1
    for num in brr:
        freq2[num]=freq2.get(num,0)+1
    missing=[]
    for num in freq2:
        if freq2[num]>freq1.get(num,0):
            missing.append(num)
    return sorted(missing)
