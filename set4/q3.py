def solution(N, S, A):
    res = 0
    
    print(take_sub_str(S), get_max_point("bbb", A))
    
    
    return res

def take_sub_str(str):
    i, j = 0, 0
    #abbbac
    upper, lower = 0, 0
    max_ele = -99999999
    
    while j < len(str):
        if str[i] != str[j]:
            if max_ele < abs(i - j):
                max_ele = abs(i - j)
                upper = i
                lower = j - 1
            i = j
            j += 1
        else:
            j += 1    

    return upper, lower

def get_max_point(S, A):
    max_points = A[0] # 5
    # b b b b b
    # 2 5 7 9 11
    for i in range(1, len(S)):
        max_points = max(max_points + A[0], A[i])
    
    print(max_points)
    return max_points




N = 6
S = "abbbac"
A = [2,5,3,7,8,10]

print(solution(N, S, A))