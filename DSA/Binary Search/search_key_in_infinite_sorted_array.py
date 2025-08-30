def BinarySearch(arr, key,start,end):
    while key > arr[end]:
        new_start = end + 1
        end = end + (end - start + 1) * 2
        start = new_start

    while start <= end:
        mid = (start + end) // 2
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1
def search_key_in_infinite_sorted_array(arr,key):
    l=0
    h=1
    while(key > arr[h]):
        l=h+1
        h=h*2
    return BinarySearch(arr,key,l,h)

arr=[3,5,7,9,10,90,100,130,140,160,170,100,1000,2500,3400,12000,15500,24555]
key=10
print(search_key_in_infinite_sorted_array(arr,key))