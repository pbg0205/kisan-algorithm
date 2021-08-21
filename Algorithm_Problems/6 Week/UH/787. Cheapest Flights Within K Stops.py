"""
Time Limit Exceeded
"""

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # make graph
        graph = collections.defaultdict(list)
        for _from, _to, _price in flights:
            graph[_from].append((_to, _price))
        
        # 다익스트라
        Q = [(0,src,k)]

        while Q :
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            if k>=0 :
                for v, w in graph[node]:
                    alt = price + w
                    heapq.heappush(Q, (alt, v, k-1))
        
        return -1
