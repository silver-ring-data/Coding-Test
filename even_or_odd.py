#https://school.programmers.co.kr/learn/courses/30/lessons/12937?language=python3

def solution(num: int) -> str:
    """문제 : 정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.

    1. num을 입력받는다.
    2. num % 2 = 0 이면 "Even"을 출력하고, num % 2 = 1 이면 "Odd"를 출력한다. 예외 처리도 추가해준다.

    Args:
        num: 입력받는 수.

    Returns:
        num의 짝수/홀수 여부 문자열.
    """
    # ✅ 클린 코드: 조건부 표현식 활용
    return "Even" if num % 2 == 0 else "Odd"


"""
1. 왜 이렇게 쓸까? (Clean Code Tip)

- 간결함: answer라는 변수를 만들고 값을 할당하는 과정을 생략할 수 있어. 코드가 짧아지면 읽는 속도도 빨라지지.

- 의도의 명확성: "이 함수는 무조건 이 조건에 따라 이 값을 돌려준다"는 의도가 한눈에 들어와.

- 파이썬다운 방식(Pythonic): 파이썬 개발자들이 가장 즐겨 쓰는 패턴 중 하나야.

2. 타입 힌트(Type Hint) 파헤치기

이 문장은 컴퓨터와 미래의 너에게 보내는 **'메모'**라고 생각하면 돼.

num: int: "이 함수에 들어오는 num이라는 데이터는 **정수(int)**여야 해!"라는 뜻이야.

-> str: "이 함수가 모든 계산을 끝내고 너에게 돌려주는(return) 결과값은 **문자열(str)**이야!"라는 뜻이지.
"""

