def bin_search(arr,key):
    start=0
    end=len(arr)-1
    ans = -1
    diff = -1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid]==key:
            return mid
        elif arr[mid] < key:
            sub = key - arr[mid]
            if diff == -1 or sub < diff:
                diff = sub
                ans = mid
            start = mid + 1
        else:
            sub = arr[mid] - key
            if diff == -1 or sub < diff:
                diff = sub
                ans = mid
            end = mid - 1
    return ans
arr=[1,2,3,6,7,10,12]
key=8
print(bin_search(arr,key))
