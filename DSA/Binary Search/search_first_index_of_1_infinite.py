def BinarySearch(arr,start,end):
    ans = -1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid]==1:
            ans=mid
            end = mid-1
        elif arr[mid] == 0:
            start = mid + 1
    return ans
def search_key_in_infinite_sorted_array(arr):
    l=0
    h=1
    while(arr[h]==0):
        l=h+1
        h=h*2
    return BinarySearch(arr,l,h)

arr=[0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
print(search_key_in_infinite_sorted_array(arr))