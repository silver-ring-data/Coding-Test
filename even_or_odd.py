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
    elif num % 2 == 1 :
        answer = "Odd"
    else :
        return 
    return print(answer)

"""
🛠️ 틀린 부분 찾아보기 (디버깅)

1. return print(answer)의 함정
**print()**는 모니터에 글자를 보여주는 '출력' 기능일 뿐이야.

**return**은 함수가 계산한 최종 결과를 '반환'해서 컴퓨터에게 돌려주는 거야.

파이썬에서 print() 함수 자체는 아무것도 돌려주지 않아서(None), return print(answer)라고 쓰면 함수는 결국 None을 반환하게 돼. 프로그래머스는 채점할 때 이 반환값을 보거든!

2. else: return의 문제
정수는 2로 나누면 나머지가 0 아니면 1밖에 없지? 그래서 사실 else까지 갈 일이 거의 없어.

하지만 만약 else에 걸려서 return만 하고 아무 값도 안 써주면, 이때도 함수는 None을 돌려줘서 오답 처리가 된단다.
"""

