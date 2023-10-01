# def EqualScores(M, N, X, Y, Array):
#     sum_array = [0] * M
#     for i in range(M):
#         for j in range(N):
#             sum_array[i] += Array[i][j]

#     print(sum_array)
#     avg = sum(sum_array) // M

#     # Find the number of arrays with a sum less than the average
#     count_less = 0
#     for i in range(M):
#         if sum_array[i] < avg:
#             count_less += 1

#     # Find the number of arrays with a sum greater than the average
#     count_greater = 0
#     for i in range(M):
#         if sum_array[i] > avg:
#             count_greater += 1

#     # If there are no arrays with a sum less than the average, then we only
#     # need to decrease the elements of the arrays with a sum greater than the
#     # average.
#     if count_less == 0:
#         return count_greater

#     # If there are no arrays with a sum greater than the average, then we only
#     # need to increase the elements of the arrays with a sum less than the
#     # average.
#     if count_greater == 0:
#         return count_less

#     # If there are both arrays with a sum less than the average and arrays with
#     # a sum greater than the average, then we need to perform both decreasing
#     # and increasing operations. The minimum number of operations is the
#     # minimum of count_less and count_greater.
#     return min(count_less, count_greater)

def EqualScores(M, N, X, Y, Array):
    sum_array = [0] * M
    for i in range(M):
        for j in range(N):
            sum_array[i] += Array[i][j]

    avg = sum(sum_array) // M
    min_ele = 9999999999
    target = 0
    print(sum_array, avg)
    for ele in sum_array:
        if min_ele > abs(avg - ele):
            min_ele = abs(avg - ele)
            target = ele
    
    print(target)
    
    #target cal
    avg = target
    # print(sum_array, avg)

    for index, ele in enumerate(Array):
        Array[index] = sorted(ele, reverse=True)
    # print(Array)
    
    total_ops, count = 0, 0

    while True:
        changed = False
        for index, arr in enumerate(Array):
            if sum_array[index] < avg:
                # increase elemets within bounds
                diff = avg - sum_array[index]
                # print(sum_array[index], diff)
                for idx, ele in reversed(list(enumerate(arr))):
                    # if the current element is at upper bound
                    if ele >= Y:
                        continue
                    # if the sum of curr + dff overflows bound
                    if ele + diff > Y:
                        # sum curr ele till upper bound, keep rest to next element
                        incr_value = diff - ((ele + diff) - Y)
                        arr[idx] += incr_value
                        sum_array[index] += incr_value
                        changed = True
                        # print(arr, sum_array)
                        break
                    else:
                        # normal case
                        # ele = ele + diff
                        arr[idx] += diff
                        sum_array[index] += diff
                        changed = True
                        # print(arr, sum_array)
                        break
                
            elif sum_array[index] > avg:
                # decrease elements within bounds
                diff = sum_array[index] - avg
                # print(sum_array[index], diff)
                for idx, ele in enumerate(arr):
                    # if the current element is at lower bound
                    if ele == X:
                        continue
                    # if the sum of curr - dffer underflows bounds
                    if ele - diff < X:
                        # decr curr ele till lower bound, keep rest to next element
                        dcr_value = diff - ((diff - ele) + X)
                        arr[idx] -= dcr_value
                        sum_array[index] -= dcr_value
                        changed = True
                        # print(arr, sum_array, dcr_value)
                        
                        break
                    else:
                        # normal case
                        arr[idx] -= diff
                        sum_array[index] -= diff
                        changed = True
                        # print(arr, sum_array)
                        
                        break
                
            else:
                # no operation elements equalized
                count += 1
                # print(count, arr)
            # print(arr, sum_array)   
        if changed: total_ops += 1
        if count >= M:
            break
        # print("ops: ", total_ops)
    return total_ops


# Input format
M, N, X, Y = 4,3,1,9
arrays = [
    [1,1,2],
    [1,2,3],
    [1,2,4],
    [9,9,9]
]

arrays1 = [
    [4,5,7],
    [1,3,5],
    [7,8,9],
    [6,8,8]
]

M1 = 4
N1 = 3
X1 = 1
Y1 = 9
arrays2 = [[1, 1, 9], [1, 2, 9], [1, 2, 9], [1, 2, 9]]
# for _ in range(M):
#     array = list(map(int, input().split()))
#     arrays.append(array)

# Call the function and print the result
# result = EqualScores(M1, N1, X1, Y1, arrays2)
result = EqualScores(M, N, X, Y, arrays)

print(result)