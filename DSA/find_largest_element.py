def largestElement(nums):
    lar=nums[0]
    for i in nums:
        if i > lar:
            lar=i
        
    print(lar)

#Given an array of integers nums, return the value of the largest element in the array


# Examples:
# Input: nums = [3, 3, 6, 1]

# Output: 6

# Explanation: The largest element in array is 6

# Input: nums = [3, 3, 0, 99, -40]

# Output: 99

# Explanation: The largest element in array is 99

largestElement([3, 3, 6, 1])  # Output: 6
largestElement([3, 3, 0, 99, -40])  # Output: 99
