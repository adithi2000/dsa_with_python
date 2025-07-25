# Given an array of integers nums, return the second-largest element in the array. If the second-largest element does not exist, return -1.


# Examples:
# Input: nums = [8, 8, 7, 6, 5]

# Output: 7

# Explanation: The largest value in nums is 8, the second largest is 7

# Input: nums = [10, 10, 10, 10, 10]

# Output: -1

# Explanation: The only value in nums is 10, so there is no second largest value, thus -1 is returned

def second_largest(nums):
    l1 = -1  # this is the mistake, we shouldn't assign nums[0] since comparision doesn't take place
    l2= -1
    for i in nums:
        if (i > l1):
            l2=l1
            l1=i
        elif (i < l1) and (i > l2):
            l2=i
    print(l2)

# second_largest([8, 8, 7, 6, 5])
# second_largest([10, 10, 10, 10, 10])


