"""
21.07.10
Runtime: 140 ms, faster than 33.75% of Python3 online submissions for Merge k Sorted Lists.
Memory Usage: 17 MB, less than 99.89% of Python3 online submissions for Merge k Sorted Lists.
"""


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 연결 리스트의 갯수 최대 10,000개
        # 개별 연결 리스트의 원소 갯수 최대 500개
        # 원소 값의 범위 -10,000~10,000
        # 개별 연결 리스트는 오름차순 정렬됨
        # => 결론 힙을 사용(min-heap)
        
        heap = []
        while True :
            none_count = 0
            for idx, node in enumerate(lists):
                if node is None :
                    none_count+=1
                    continue
                else :
                    heapq.heappush(heap, node.val)
                    lists[idx] = node.next
                    
            if len(lists) == none_count:
                break
        
        # heap check 
        if len(heap)==0:
            return None
        
        node_head = ListNode(heapq.heappop(heap))
        current_node = node_head
        while heap:
            current_node.next = ListNode(heapq.heappop(heap))
            current_node = current_node.next
            
        return node_head 
      
