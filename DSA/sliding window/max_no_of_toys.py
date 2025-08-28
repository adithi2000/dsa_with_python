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
print(max_len(2,"aabacbebebe")) # should return 5
