"""
21.07.10
Runtime: 72 ms, faster than 60.93% of Python3 online submissions for Design Circular Deque.
Memory Usage: 14.7 MB, less than 92.90% of Python3 online submissions for Design Circular Deque.
"""
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.deque = collections.deque(maxlen=k)
        self.max_len  = k

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        else :
            self.deque.appendleft(value)
            return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
          
        else :
            self.deque.append(value)
            return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty() :
            return False
        else :
            self.deque.popleft()
            return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """     
        if self.isEmpty() :
            return False
        else :
            self.deque.pop()
            return True
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        else :
            return self.deque[0]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        else :
            return self.deque[-1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return len(self.deque)==0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.max_len == len(self.deque)
