"""
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
"""

import collections
import heapq

def solution(N, road, K):

    # draw map
    graph = collections.defaultdict(list)
    for vil1, vil2, time in road:
        graph[vil1].append((vil2, time))
        graph[vil2].append((vil1, time))
        
    # fild available vil
    Q = [(0, 1)]
    dist = collections.defaultdict(int)
    
    
    # BFS
    while Q :
        print(Q)
        w, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = w
            for v, time in graph[node] :
                alt = time + w
                if alt <= K:
                    heapq.heappush(Q, (alt, v))


    return len(dist)
