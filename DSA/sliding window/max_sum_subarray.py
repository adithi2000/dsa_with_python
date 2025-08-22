import sys
def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k or k <=0:
        return "Invalid input: k should be less than or equal to the length of the array and greater than 0."
    else:
        max_sum = -sys.maxsize - 1
        sum = 0
        i = 0
        j = 0
        while j < n:
            if j - i + 1 <= k:
                sum += arr[j]
                j += 1
            else:
                max_sum = max(max_sum, sum)
                sum -= arr[i]
                i += 1
    return max_sum

print(max_sum_subarray([2,5,1,8,2,9,1],3))  # Example usage

