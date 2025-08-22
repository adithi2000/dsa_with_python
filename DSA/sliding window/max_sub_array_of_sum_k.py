def max_subarray(k,arr):
    ws = -1
    i,j=0,0
    sum_ =0
    n = len(arr)
    while(j < n): # // i <= j helps us prevent window shrinking beyond j
        sum_ += arr[j]
        if (sum_ < k):
            j += 1
        elif (sum_ == k):
            print(f"sum found between {i} and {j},and sum is {sum_}")
            ws = max(ws,j-i+1)
            j += 1
        else:
            while( sum_ > k and i <=j): # while loop is used so that we dont add new arr[j] until we have shrunk the window enough
                sum_ -= arr[i] # we do this so that we can shrink or move our overlapping range, we can just move blindly right
                i += 1
            j += 1
    return ws

print(max_subarray(5,[4,1,1,1,2,3,5]))
print(max_subarray(5,[4,1,1,1,2,3,5,1,1,1,1])) # should return 7
# Given an array of positive numbers and a positive number ‘k,’ find the length of the
# longest contiguous subarray whose sum is equal to ‘k’.
# Example 1:
# Input: [2, 1, 5, 2, 3, 2], k=7
# Output: 4