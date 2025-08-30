def infi_search(arr,key):
    l = 0
    h = 1
    while arr[h] < key:
        l = h
        h = 2*h # h = h*2 because array is infinite not h *= 3 because it will skip some elements
        while l <= h:
            mid = (l+h)//2
            if(arr[mid] == key):
                return mid
            elif(arr[mid] < key):
                l = mid + 1
            else:
                h = mid - 1
    return -1
# arr = [3,5,7,9,10,90,100,130,140,160,170]
arr = [3,5,7,9,10,90,100,130,140,160,170]
key = 10
print(infi_search(arr,key))
# Time Complexity: O(log n)