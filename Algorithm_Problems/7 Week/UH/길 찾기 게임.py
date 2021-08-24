"""
테스트 1 〉	통과 (0.08ms, 10.2MB)
테스트 2 〉	통과 (0.10ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (186.74ms, 16.7MB)
테스트 7 〉	통과 (189.88ms, 16.8MB)
테스트 8 〉	통과 (474.20ms, 15MB)
테스트 9 〉	통과 (3060.51ms, 28.4MB)
테스트 10 〉	통과 (110.34ms, 11.8MB)
테스트 11 〉	통과 (2917.46ms, 26.2MB)
테스트 12 〉	통과 (3035.78ms, 27.8MB)
테스트 13 〉	통과 (4.23ms, 10.2MB)
테스트 14 〉	통과 (40.34ms, 10.9MB)
테스트 15 〉	통과 (672.23ms, 13.6MB)
테스트 16 〉	통과 (2565.11ms, 17.4MB)
테스트 17 〉	통과 (58.64ms, 10.9MB)
테스트 18 〉	통과 (2427.64ms, 17.5MB)
테스트 19 〉	통과 (106.24ms, 11.5MB)
테스트 20 〉	통과 (565.13ms, 13.2MB)
테스트 21 〉	통과 (916.44ms, 14.5MB)
테스트 22 〉	통과 (2318.62ms, 17.3MB)
테스트 23 〉	통과 (2581.77ms, 17.6MB)
테스트 24 〉	통과 (0.04ms, 10.3MB)
테스트 25 〉	통과 (0.05ms, 10.3MB)
테스트 26 〉	통과 (377.66ms, 19.5MB)
테스트 27 〉	통과 (0.08ms, 10.3MB)
테스트 28 〉	통과 (0.11ms, 10.2MB)
테스트 29 〉	통과 (0.02ms, 10.3MB)
"""
from collections import deque
import sys
sys.setrecursionlimit(10**6)

class Tree:
    def __init__(self,datas):
        self.data = max(datas, key=lambda x : x[1])
        self.leftList = list(filter(lambda x: x[0] < self.data[0], datas))
        self.rightList = list(filter(lambda x: x[0] > self.data[0], datas))
        
        self.left = self.check_subtree(self.leftList)
        self.right = self.check_subtree(self.rightList)
            
    def check_subtree(self, subList: list):
        if subList == []:
            return None
        else :
            return Tree(subList)
    
def preorder(root):
    
    stack = deque([root])
    route = []
    
    while stack:
        node = stack.pop()
        route.append(node.data)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return route

def postorder(root):
    stack = deque([root])
    route = []
    
    while stack:
        node = stack.pop()
        route.append(node.data)
        if node.left:
            stack.append(node.left)
            
        if node.right:
            stack.append(node.right)
    return route[::-1]

def solution(nodeinfo):
    answer = []
    root = Tree(nodeinfo)
    preorder_view = list(map(lambda x : nodeinfo.index(x)+1, preorder(root)))
    answer.append(preorder_view)
    
    postorder_view = list(map(lambda x : nodeinfo.index(x)+1, postorder(root)))
    answer.append(postorder_view)
    
    return answer
