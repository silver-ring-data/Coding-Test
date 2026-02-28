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
    
    arr.remove(min_num)
                
    return arr if arr != [] else [-1]
"""
파이썬 리스트의 remove()는 리스트 자체를 **'수정'**하는 일을 하지만, 수정된 리스트를 우리에게 다시 **'전달(return)'**해주지는 않아.
    my_list.remove(2)를 실행하면: my_list라는 변수가 가리키는 실제 데이터 바구니에서 2가 사라짐. (성공!)
    result = my_list.remove(2)라고 쓰면: remove는 아무것도 반환하지 않기 때문에 result에는 None이 들어감. (함정!)
"""
