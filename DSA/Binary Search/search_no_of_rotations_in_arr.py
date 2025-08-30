# no of rotations in a sorted array is the index of the minimum element
def count_rotations(arr):
    n = len(arr)
    l=0
    h=n-1
    while(l <= h):
        # we calculate mid, prev and next in a circular manner due to nature of array
        #nature of array is circularly sorted
        mid = (l+h)//2
        #circulary sorted maens that the next of last elemenent is the first elements
        prev = (mid+n-1)%n # if mid = 0 , prev = n-1
        next = (mid+1)%n # if mid = n-1 , next = 0
        if(arr[mid] <= arr[prev] and arr[mid] <= arr[next]):
            return mid
        elif(arr[mid] <= arr[h]):
            h = mid-1
        elif(arr[mid] >= arr[l]):
            l = mid+1
    return -1
print(count_rotations([15,18,2,3,6,12])) # should return 2
print(count_rotations([7,9,11,12,5])) # should return 4