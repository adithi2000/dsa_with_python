def count_anagrams(patt,s):
    k=len(patt)
    n=len(s)
    if k > n:
        return 0
    else:
        count = 0
        patt_count = [0] * 26
        s_count = [0] * 26

        i =0
        j =0

        for p in range(k):
            patt_count[ord(patt[p])-ord('a')] += 1
        while j < n:
            if j - i + 1 < k:
                s_count[ord(s[j]) - ord('a')] += 1
                j += 1
            elif j - i + 1 == k:
                s_count[ord(s[j]) - ord('a')] += 1
                if patt_count == s_count:
                    count += 1
                s_count[ord(s[i]) - ord('a')] -= 1
                i += 1
                j += 1
        return count

#example usage
if __name__ == "__main__":
    patt = "abc"
    s = "cbabcacab"
    print(count_anagrams(patt, s)) # Output: 4
# Output: 4
# Example usage
# Output: 4
# This code counts the number of anagrams of a pattern in a given string using the sliding window technique.
    i = "for"
    j = "foroxxorfoxrfoor"
    print(count_anagrams(i,j))
# This code counts the number of anagrams of a pattern in a given string using the sliding window technique.
