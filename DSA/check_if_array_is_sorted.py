# Given an array nums of n integers, return true if the array nums is sorted in non-decreasing order or else false.


# Examples:
# Input : nums = [1, 2, 3, 4, 5]

# Output : true

# Explanation : For all i (1 <= i <= 4) it holds nums[i] <= nums[i+1], hence it is sorted and we return true.

# Input : nums = [1, 2, 1, 4, 5]

# Output : false

# Explanation : For i == 2 it does not hold nums[i] <= nums[i+1], hence it is not sorted and we return false.

def find_if_sorted(nums):
    for i in range(1,len(nums)):
        if (nums[i-1] <= nums[i]):
            continue
        else:
            print("not sorted")
            break
    else:
        print("Sorted")
find_if_sorted([1,2,1,4,5,6])