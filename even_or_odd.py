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
    if num % 2 = 0
        return answer = "Even"
    elif num % 2 = 1
        return answer = "Odd"
    else
        return 
    print(answer)

"""
🛠️ 틀린 부분 찾아보기 (디버깅)
1. 비교 연산자 (== vs =):

파이썬에서 =는 "변수에 값을 넣을 때(대입)" 쓰고, ==는 "값이 같은지 물어볼 때(비교)" 써.

num % 2 == 0이라고 써야 해!

2. 콜론 (:) 생략:

if, elif, else 문 끝에는 "이제 아래 내용을 실행해!"라는 의미로 반드시 :를 붙여줘야 해.

return의 위치:

3. return answer = "Even"은 문법에 맞지 않아. 값을 바로 돌려주려면 return "Even"이라고 하거나, 변수에 먼저 담고 나중에 돌려줘야 해.

도달할 수 없는 코드:

4. return을 만나면 함수는 그 즉시 끝나버려. 그래서 맨 밑에 있는 print(answer)는 실행되지 않는단다.
"""

