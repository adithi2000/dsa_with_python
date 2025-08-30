def near_right(arr):
    stack = []
    result = []
    for i in range(len(arr)-1,-1,-1):
        if not stack:
            result.append(-1)
        elif stack[-1] < arr[i]:
            result.append(stack[-1])
        else:
            while(stack and stack[-1] >= arr[i]):
                stack.pop()
            if not stack:
                result.append(-1)
            elif(stack[-1] < arr[i]):
                result.append(stack[-1])
        stack.append(arr[i])

    return result[::-1]
print(near_right([1,3,2,4]))