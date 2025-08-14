def candy(ratings):
        # bruteforce
    count = [0]*len(ratings)
    for i in range(len(ratings)):
        if i == 0:
            count[i] = 1
        elif ratings[i] > ratings[i-1]:
            count[i] = count[i-1]+1
        elif ratings[i] < ratings[i-1]:
            count[i]=1
            if count[i-1] > count[i]:
                continue
            else:
                count[i-1] += 1
        else:
            

#  time Complexity = O(n)
        # space Complexity = O(n)
        # 1. Create a list to store the count of candies for each child.
        # 2. Iterate through the ratings and assign candies based on the rules.
        # 3. Sum up the candies to get the total.
        # 4. Return the total count of candies.
        # 5. The algorithm runs in linear time, making it efficient for large inputs.
print(candy([1,0,2]))  # Output: 5
print(candy([1,2,2]))  
# Output: 4
print(candy([1,3,2,2,1]))
# Output: 9
print(candy([1,2,3,4,5]))
# Output: 15
print(candy([5,4,3,2,1]))
# Output: 15
