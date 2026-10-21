# [2026-10-21]
# 소수 찾기 (Lv.2)
# https://school.programmers.co.kr/learn/courses/30/lessons/42839


# --------------------------------------------------------------------------
# 1. 나의 풀이
# --------------------------------------------------------------------------
import itertools

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    count = []
    
    for length in range(1,len(numbers)+1):
        for arr_number in itertools.permutations(numbers, length):
            int_number = int("".join(arr_number))
            if is_prime(int_number):
                count.append(int_number)
    answer = len(list(set(count)))
    return answer


# --- 피드백 과정 ---
#
# 접근은 본인이 바로 냄: 순열(permutations)로 다 만들고, 소수는 √n 까지 나눠 판별.
# 카드를 1장만 쓰는 경우("17" 의 7)도 세야 함 → 길이 1 ~ len(numbers) 반복은 본인이 짚음.
#   range(1, len(numbers)+1) 경계는 이번엔 안 꼬였다.
# 1판: count += len(number) → 튜플 ('1','7') 의 글자 수(카드 장수)를 셈.
# 2판: count += len(list(permutations(...))) → 순열 총 개수. "17" 이면 4 (정답 3, 1 이 섞임).
#   예시와 1 차이라 맞는 것처럼 보이기 쉬움. "011" 이면 15 (정답 2).
#   → 튜플 → 숫자 → 중복 제거 → 소수만 세기, 세 단계로 나눔.
# 3판 통과: "".join → int 로 "011" 과 "11" 을 같은 11 로 만들고 set 으로 중복 제거.
#   is_prime 의 n < 2 와 int(n**0.5) + 1 경계도 본인이 맞게 씀.


# --------------------------------------------------------------------------
# 2. 최적화된 버전
# --------------------------------------------------------------------------
from itertools import permutations

def is_prime(n):
    return n >= 2 and all(n % i for i in range(2, int(n**0.5) + 1))

def solution(numbers):
    """모든 길이의 순열을 숫자로 바꿔 set 에 모은 뒤 소수만 센다."""
    nums = {int(''.join(p))
            for k in range(1, len(numbers) + 1)
            for p in permutations(numbers, k)}
    return sum(is_prime(n) for n in nums)


# --- 설명 ---
#
# 중복을 먼저 set 으로 없애고 소수 판별 → 같은 수를 여러 번 판별하지 않는다.
# list 에 모았다가 set 으로 바꿔도 되지만, 처음부터 set 컴프리헨션이면 한 줄.
# len(list(set(count))) 의 list() 는 불필요 — set 도 len 이 된다.
# all(n % i ...) 은 "나누어떨어지는 i 가 하나도 없다" = 소수.
# 복잡도: 순열 수 최대 7! + ... ≈ 13,699 개 × 판별 O(√n) (n < 10^7).
# 다른 방법: 가장 큰 수(내림차순으로 이은 수)까지 에라토스테네스의 체로 소수표를 만들어 두기.
# 짧지만 안 되는 대안:
#   - set 없이 소수를 바로 세기 → "11" 이 두 번, "011" 도 11 로 또 셈.
#   - 문자열 그대로 set 에 넣기 → "011" 과 "11" 이 다른 값으로 남는다. int 로 바꾼 뒤 모아야 함.
#   - permutations(numbers) 만 쓰기 → 카드를 전부 쓴 순서만 나와서 7 같은 한 장짜리가 빠진다.
#
# 다시 만나면: 카드 조합 = 길이별 permutations, 같은 수 판별은 int 로 바꾼 뒤 set.
