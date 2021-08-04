"""
테스트 1 〉	통과 (0.10ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
"""

def solution(tickets):
    answer = []
    
    air_table = {}
    for _from, _to in tickets :
        if _from in air_table:
            air_table[_from].append(_to)
        else :
            air_table[_from] = [_to]
            
    for _from in air_table.keys():
        air_table[_from].sort()

    def dfs(key, footprint):
        if len(footprint) == len(tickets) + 1:
            return footprint
        elif key not in air_table:
            return False

        for idx, country in enumerate(air_table[key]):
            air_table[key].pop(idx)

            fp = footprint[:] # deepcopy
            fp.append(country)

            ret = dfs(country, fp)
            if ret: return ret # 모든 티켓을 사용해 통과한 경우

            air_table[key].insert(idx, country) # 통과 못했으면 티켓 반환
            
    # 응용 https://wwlee94.github.io/category/algorithm/bfs-dfs/travel-route/
    # 좋은 아이디어 -> 만일 모든 조건이 아닐 경우 "다시 티켓 반환" 이 아이디어가 필요했음...
    # 다시 티켓 반환을 구현하지 못하여 계속 백트래킹이 안되었음
    # 블로그를 통해 확인 후 일부 로직 수정하여 개선
    # 추가로 카피와 딥카피를 리스트, 딕트에 대하여 다시 확인 필요
            
    answer = dfs('ICN', ['ICN'])
    return answer
