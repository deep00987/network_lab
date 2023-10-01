def compare_code(s1, s2):
    cost = 0
    # 1001
    # 1110
    for e1, e2 in zip(s1, s2):
        if e1 != e2:
            cost += 1
    
    return cost

def solution(M, N, A):
    total_cost = M
    
    hash = set()
    hash.add(A[0])
    
    for i in range(1, N):
        #cost of new Str
        min_cost = M
        for ele in hash:
            curr_cost = compare_code(ele, A[i])
            if  curr_cost < min_cost:
                min_cost = curr_cost
        
        total_cost += min_cost
        hash.add(A[i])
    
    return total_cost
    
A = [
    "011",
    "011",
    "111"
]
        
M, N = 3, 3      

print("cost: " , solution(M, N, A))