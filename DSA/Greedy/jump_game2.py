class Solution:
    def jump(self, nums) :
        maxreach = 0
        jump = 0
        if len(nums) == 1:
            return 0
        for i in range(len(nums)):
            if i > maxreach:
                return -1
            temp = maxreach
            maxreach = max(maxreach,nums[i]+i)
            if maxreach != temp:
                print(f"jump: {jump}, maxreach: {maxreach}, i: {i}")
                jump += 
            if maxreach >= len(nums)-1:
                return jump
arr = [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]
a = Solution()
print(a.jump(arr))  # Output: 2