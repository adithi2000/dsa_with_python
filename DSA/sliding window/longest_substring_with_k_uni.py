def max_len_1(k,s):
    ws = -1
    i,j=0,0
    sum_ =0
    n = len(s)
    while(j < n): # // i <= j helps us prevent window shrinking beyond j
        uni = len(set(s[i:j+1]))
        if (uni < k):
            j += 1
        elif (uni == k):
            print("found",s[i:j+1])
            ws = max(ws,j-i+1)
            j += 1
        else:
            while( uni > k and i <= j): 
                i += 1
                uni = len(set(s[i:j+1])) # we do this so that we can shrink or move our overlapping range, we can just move blindly right
                
            if uni == k:
                print("found",s[i:j+1])
                ws = max(ws, j - i + 1)
            j += 1
    return ws
def max_len(k,s):
    ws =-1
    i = 0
    freq = {}
    for j in range(len(s)):
        freq[s[j]]=freq.get(s[j],0)+1
        while len(freq) > k:
            freq[s[i]] -= 1
            if freq[s[i]]==0:
                del freq[s[i]]
            i+=1
        if len(freq) == k:
            ws = max(ws, j - i + 1)
    return ws
print(max_len(3,"aabacbebebe")) # should return 5