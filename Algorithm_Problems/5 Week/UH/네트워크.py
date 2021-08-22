"""
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.09ms, 10.2MB)
테스트 4 〉	통과 (0.08ms, 10.2MB)
테스트 5 〉	통과 (0.00ms, 10.2MB)
테스트 6 〉	통과 (0.82ms, 10.4MB)
테스트 7 〉	통과 (0.04ms, 10.3MB)
테스트 8 〉	통과 (0.34ms, 10.3MB)
테스트 9 〉	통과 (0.18ms, 10.2MB)
테스트 10 〉	통과 (0.36ms, 10.3MB)
테스트 11 〉	통과 (2.99ms, 10.6MB)
테스트 12 〉	통과 (1.99ms, 10.4MB)
테스트 13 〉	통과 (0.63ms, 10.3MB)
"""

def solution(n, computers):
    answer = 1
    visitied = [0]*n

    def dfs(current_com):
        nonlocal computers, visitied
        visitied[current_com] = 1
        
        for next_com in range(n):
            if computers[current_com][next_com] and next_com != current_com:
                computers[current_com][next_com] = 0
                dfs(next_com)
    dfs(0)
    
    while sum(visitied) < n :
        dfs(visitied.index(0))
        answer+=1
    
    return answer
