#https://school.programmers.co.kr/learn/courses/30/lessons/12937?language=python3

def solution(num):
    """문제 : 정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.

    1. num을 입력받는다.
    2. num % 2 = 0 이면 "Even"을 출력하고, num % 2 = 1 이면 "Odd"를 출력한다. 예외 처리도 추가해준다.

    Args:
        num: 입력받는 수.

    Returns:
        num의 짝수/홀수 여부 문자열.
    """
    if num % 2 == 0 :
        answer = "Even"
    else :
        answer = "Odd"
    return answer

"""
"""

