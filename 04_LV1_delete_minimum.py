def solution(arr):
    """ 정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수
        조건 : 빈 배열을 리턴하는 경우 배열에 -1을 채워 리턴
        
        1. 
        Args : 
            arr : 입력 받은 정수로 구성된 배열
            
        Returns : 
            answer : 결과로 나오는 배열
    """
    index = 0
    min_num = 0
    
    for num in arr :
        if index == 0 :
            min_num = num
            
        else :
            if num >= min_num :
                pass
            else :
                min_num = num
        index = index + 1
    
    answer = arr.remove(min_num)
                
    return answer if answer != [] else [-1]
    
