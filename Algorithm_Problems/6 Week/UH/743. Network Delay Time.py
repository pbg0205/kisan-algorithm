"""
Runtime: 484 ms, faster than 48.44% of Python3 online submissions for Network Delay Time.
Memory Usage: 16.3 MB, less than 24.99% of Python3 online submissions for Network Delay Time.
"""

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Make graph
        graph = collections.defaultdict(list)
        for u,v,w in times :
            graph[u].append((v,w))
            
        Q = [(0,k)]
        dist = collections.defaultdict(int)
        
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist :
                dist[node] = time
                for v, w in graph[node]:
                    alt = time+w
                    heapq.heappush(Q, (alt, v))
        
        if len(dist) == n :
            return max(dist.values())
        else :
            return -1


