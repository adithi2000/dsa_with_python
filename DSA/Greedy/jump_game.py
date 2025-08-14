jump=[2,3, 1, 0, 4]
i = 0
while i < len(jump)-1:
    j = i+jump[i]+1
    if j >= len(jump):
        j = len(jump)
    ind = jump.index(max(jump[i+1:j]))
    i = ind
    if jump[i] == 0 and i < len(jump)-1:
        print("Not possible to reach the end of the array")
        break
else:
    print("Possible to reach the end of the array")

#TC = O(n^2)
# Output: Possible to reach the end of the array    
# Explanation: The jumps can be made as follows:
# 1st jump: 2 steps to index 2 (value 1)
# 2nd jump: 3 steps to index 4 (value 4)
# The end of the array is reached.

# Greedy approach is used here to find the maximum jump possible at each step, and it continues until the end of the array is reached or it is determined that reaching the end is not possible.
# Explanation: The jumps can be made as follows:
# 1st jump: 2 steps to index 2 (value 1)
# 2nd jump: 3 steps to index 4 (value 4)
# The end of the array is reached.
#   
# The greedy approach is used here to find the maximum jump possible at each step, and it continues until the end of the array is reached or it is determined that reaching the end is not possible.
#         # The greedy approach is used here to find the maximum jump possible at each step, and it continues until the end of the array is reached or it is determined that reaching the end is not possible.
# # The greedy approach is used here to find the maximum jump possible at each step, and it continues until the end of the array is reached or it is determined that reaching the end is not possible.
def greedy_jump_game(jump):
    i = 0
    while i < len(jump) - 1:
        j = i + jump[i] + 1
        if j >= len(jump):
            j = len(jump)
        ind = jump.index(max(jump[i + 1:j]))
        i = ind
        if jump[i] == 0 and i < len(jump) - 1:
            return "Not possible to reach the end of the array"
    return "Possible to reach the end of the array"
