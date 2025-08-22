import sys

def max_sub(arr,k):
    maximum = -sys.maxsize-1
    i = 0
    j = 0
    n = len(arr)
    result = []
    while(j < n):
        if ( j-i+1 < k):
            j += 1
        elif (j-i+1 == k):
            maximum = -sys.maxsize-1
            for x  in range(i,j+1):
                maximum = max(maximum,arr[x])
            result.append(maximum)
            j += 1
        else:
            i += 1
    return result

print(max_sub([4,3,-1,-3,5,3,6,7],3))

