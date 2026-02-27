'''
#https://school.programmers.co.kr/learn/courses/30/lessons/12932

[문제정의] : 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

[제한 조건]
n은 10,000,000,000이하인 자연수입니다.

[입출력 예]
n	return
12345	[5,4,3,2,1]
'''

def solution(n : int) -> list:
    """자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴하는 함수

    1. n을 문자열로 변환
    2. 슬라이싱을 이용해 n의 순서를 바꾸어줌
    3. 바꾼 순서를 배열로 다시 변환
    4. 각 요소들을 다시 int로 변환

    Args:
        n : 입력된 자연수

    Returns:
        answer : 숫자를 원소로 가지는 배열
    """
    answer = []
    n_str = str(n)
    list_n_str = list(n_str[::-1])
    for i in range(len(n_str)):
        answer[i] = list_n_str[i]
    
    return answer

'''
피드백

문자를 직접 꺼내오는 방식으로 설계하는 게 좋음
지금처럼 인덱스 에러가 날 확률이 높음
'''
