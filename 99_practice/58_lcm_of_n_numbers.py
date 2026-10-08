# 2026-10-08 (10/07 몫)
# N개의 최소공배수 (Lv.2)
# https://school.programmers.co.kr/learn/courses/30/lessons/12953


# --------------------------------------------------------------------------
# 1. 나의 풀이
# --------------------------------------------------------------------------
import math


def func(a, b):
    return (a*b)//math.gcd(a, b)


def solution(arr):

    answer = arr[0]
    length = len(arr)
    if length == 1:
        return answer
    else:
        for index in range(1, len(arr)):
            answer = func(answer, arr[index])
        return answer


# --- 피드백 과정 ---
#
# 첫 시도: math.prod(arr) // math.gcd(arr)
#   ① gcd 에 리스트를 통째로 넣음 → 에러 (숫자를 따로 받는다).
#   ② a*b/gcd 는 "두 수" 공식이라 N개에 그대로 못 쓴다.
#      반례 [2,4,8]: 진짜 답 8, 전체곱/전체gcd = 64/2 = 32.
# 접근: "두 개씩 최소공배수를 반복" 은 본인이 바로 냄.
# 막힌 지점 (둘째 판):
#   ① arr.length() → 다른 언어 문법, len(arr).
#   ② 정의 안 된 변수(calculated_num) 사용 → 갱신 변수 answer.
#   ③ range(0, n) + arr[index+1] → 마지막에 범위 밖, arr[0] 은 이미 시작값.
#      **루프 경계 패턴 또 나옴.** range(1, n) + arr[index] 로 본인이 고침.
# 반례 [5] 를 본인이 떠올려 확인함 (좋아진 점).
#   다만 길이 1 예외처리를 넣었는데 불필요 → range(1, 1) 이 빈 범위라 그대로 arr[0] 반환.
# 결과: 통과.


# --------------------------------------------------------------------------
# 2. 최적화된 버전
# --------------------------------------------------------------------------
from functools import reduce


def solution(arr):
    """arr 전체의 최소공배수를 반환한다. 두 수씩 접어 간다."""
    return reduce(lambda a, b: a * b // math.gcd(a, b), arr)


# --- 설명 ---
#
# 고친 이유
# - reduce: "첫 값을 들고 다음 값과 하나씩 접기" 를 그대로 표현. 원소 하나면 그 값 반환.
# - 길이 1 예외처리 삭제: 빈 range 가 이미 처리한다.
# 복잡도: 시간 O(n log M) (gcd 가 log), 공간 O(1).
# 짧지만 안 되는 대안
# - math.prod(arr) // math.gcd(*arr): 두 수일 때만 맞다 ([2,4,8] → 32).
# - math.lcm(*arr): 파이썬 3.9+ 에서만 동작. 채점 환경 버전에 따라 막힐 수 있다.
#
# 다시 만나면: 두 수 공식을 N개로 늘릴 땐 공식을 키우지 말고 "두 개씩 접기".
