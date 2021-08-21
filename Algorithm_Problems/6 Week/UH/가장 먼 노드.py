"""
테스트 1 〉	통과 (0.02ms, 10.4MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.05ms, 10.2MB)
테스트 4 〉	통과 (0.79ms, 10.3MB)
테스트 5 〉	통과 (1.54ms, 10.6MB)
테스트 6 〉	통과 (5.49ms, 11.2MB)
테스트 7 〉	통과 (54.77ms, 19.5MB)
테스트 8 〉	통과 (49.99ms, 21.6MB)
테스트 9 〉	통과 (92.54ms, 23.3MB)
"""

from collections import defaultdict
from heapq import heappop, heappush
def solution(n, edge):
    answer = 0
    graph = defaultdict(list)
    for v1, v2 in edge:
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    Q =[(0,1)] # (distance, node)
    route = defaultdict(int) # int : distance
    while Q and len(route) < n:
        dist, node = heappop(Q)
        if node not in route :
            route[node] = dist
            for next_node in graph[node]:
                if next_node not in route:
                    heappush(Q, (dist+1, next_node))
                    
    max_val = max(route.values())
    return list(route.values()).count(max_val)
  
