def EqualScores(M, N, X, Y, Array):
    sum_array = [0] * M
    for i in range(M):
        for j in range(N):
            sum_array[i] += Array[i][j]
    
    A = sum_array.index(max(sum_array))
    B = sum_array.index(min(sum_array))
    
    SA = Array[A]
    SB = Array[B]
    
    print(SA, A, SB, B)   
    
    i = 0
    sum_a = sum(SA)
    sum_b = sum(SB)
    
    if sum_a == sum_b or N == 1:
        print(0)
        return
    
    while (sum_b < sum_a):
        sum_b += (Y - SB[i])
        SB[i] = Y
        
        sum_a -= (SA[i] - X)
        SA[i] = X
        i += 1
    
    print(i)


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
result = EqualScores(M, N, X, Y, arrays1)

print(result)