def solution(s : str, skip : str, index : int) -> str:
    """문자열을 각각 index번째 뒤의 알파벳으로 바꿔주나, 특정 알파벳은 변환하지 않고 그대로 리턴시키는 함수

    1. s, skip, index에 대한 형태 작성
    2. 문자열 s를 리스트 형태로 변환
    3. s 리스트의 각 문자를 아스키코드로 변환
    4. 조건문 : 
        반복문
        4-1. s 리스트의 문자가 skip 리스트의 문자에 해당되지 않을시
                반복문 : 리스트의 아스키코드들을 각각 index만큼 플러스
                조건문 : 만약 122(z)가 넘어간다면 26을 뺌 (a부터 시작)
        4-2. s 리스트의 문자가 skip 리스트의 문자에 해당될 경우
            pass
    5. 문자열을 아스키코드에서 str로 변경
    6. list(str)에서 str로 변경

    Args:
        s : 변환할 문자열
        skip : 건들지 않을 문자열
        index : 문자 변환 기준

    Returns: 
        answer : 변환한 결과
    """
    s_list = [ord(char) for char in s]
    skip_list = [ord(char) for char in skip]
    answer_list = []
    
    for s_num in s_list :
        for skip_num in skip_list : 
            if s_num == skip_num : 
                answer_list = answer_list + [s_num]
            else :
                s_num = s_num + index
                if s_num > 122 :
                    s_num = s_num - 26
                answer_list = answer_list + [s_num]
                
    answer = str([chr(char) for char in answer_list])
    return answer

"""

"""
