def solution(arr):
    """ 정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수
        조건 : 빈 배열을 리턴하는 경우 배열에 -1을 채워 리턴
        
        1. 
        Args : 
            arr : 입력 받은 정수로 구성된 배열
            
        Returns : 
            answer : 결과로 나오는 배열
    """
    if len(arr) <= 1: return [-1]
    
    arr.remove(min(arr))
            
    return arr
"""
로직 심플하게 만들기 : min() 사용
가드 절(Guard Clauses) 활용 : 어차피 원소가 1개이면 바로 -1를 리턴하면 됨.
    
"""
