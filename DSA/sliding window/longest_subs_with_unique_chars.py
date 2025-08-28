def max_len_1(s):
    ws = -1
    i,j=0,0
    sum_ =0
    n = len(s)
    while(j < n): # // i <= j helps us prevent window shrinking beyond j
        uni = len(set(s[i:j+1]))
        if (uni < j-i+1):
            while( uni < j-i+1 and i <= j): 
                i += 1
                uni = len(set(s[i:j+1])) # we do this so that we can shrink or move our overlapping range, we can just move blindly right
                
            if uni == j-i+1:
                print("found",s[i:j+1])
                ws = max(ws, j - i + 1)
            j += 1
        elif (uni == j-i+1):
            print("found",s[i:j+1])
            ws = max(ws,j-i+1)
            j += 1
        
    return ws



def max_len_2(s):
    ws = -1
    i=0
    j=0
    freq = {}
    for j in range(len(s)):
        freq[s[j]]=freq.get(s[j],0)+1
        while(len(freq)<j-i+1):
            freq[s[i]]-=1
            if freq[s[i]]==0:
                del(freq[s[i]])
            i+=1
        if(len(freq)==j-i+1):
           ws = max(ws,j-i+1)
    return ws

print(max_len_2("abcde"))