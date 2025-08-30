def near_right(arr):
    stack = []
    result = []
    for i in range(0,len(arr)):
        if not stack:
            stack.append(arr[i])
            result.append(-1)
        elif stack[-1] < arr[i]:
            result.append(stack[-1])
            stack.append(arr[i])
        else:
            while(stack and stack[-1] > arr[i]):
                stack.pop()
            if not stack:
                result.append(-1)
            elif(stack[-1] < arr[i]):
                result.append(stack[-1])
            stack.append(arr[i])
        print(stack)

    return result

print(near_right([1,3,2,4]))