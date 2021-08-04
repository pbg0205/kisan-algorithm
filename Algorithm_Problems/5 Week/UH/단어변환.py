"""
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.08ms, 10.3MB)
테스트 3 〉	통과 (0.28ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
"""

def solution(begin, target, words):
    answer = 0
    
    def distance_between_words(word1, word2):
        # same word length
        # if diff over 2 return 
        diff = 0
        for char1, char2 in zip(word1, word2):
            if char1 != char2:
                diff += 1
                if diff >= 2 :
                    break
        return diff
    
    def dfs(before_word, array, path):
        nonlocal answer
        path.append(before_word)
        if before_word == target:
            answer = len(path)-1
            return
        elif answer != 0 and len(path) > answer:
            return
        
        for word in array:
            if distance_between_words(before_word, word) == 1:
                next_array=array.copy()
                next_array.remove(word)
                dfs(word, next_array, path.copy())
    
    dfs(begin, words.copy(), []) 
    return answer
