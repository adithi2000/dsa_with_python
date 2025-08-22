def first_negative(arr,k):
    n= len(arr)
    i = 0
    j = 0
    while ( j < n):
        if j - i + 1 < k:
            j += 1
        elif j - i + 1 == k:
            p = i
            while p <= j:
                if arr[p]  < 0:
                    print(arr[p], end=' ')
                    break
                p += 1
            if p > j:
                print(0, end=' ')
            j += 1
        else:
            i += 1      
first_negative([12, -1, -7, 8, -15, 30, 16, 28], 3)  # Example usage
