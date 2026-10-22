# 2026-10-22
# 연속 부분 수열 합의 개수 (Lv.2)
# https://school.programmers.co.kr/learn/courses/30/lessons/131701


# --------------------------------------------------------------------------
# 1. 나의 풀이
# --------------------------------------------------------------------------
import itertools
def solution(elements):
    sequence = elements
    sum_list = []
    for i in range(1, len(elements)+1):
        for j in range(1, len(elements)+1):
            sum_list.append(sum(sequence[0:j]))
        sequence = sequence[1:] + sequence[:1]
    answer = len(set(sum_list))
    return answer


# --- 피드백 과정 ---
#
# 접근: 앞자리를 뒤로 보내며 n번 회전 → 원형을 일반 배열로 바꾼다. 본인이 바로 냄.
#   회전마다 "맨 앞에서 시작하는 것만" 보면 된다(중간 시작은 다음 회전이 해 줌)도 본인이 짚음.
# 1판: itertools.permutations(elements, j) — 소수 찾기 때 손에 익은 걸 그대로 가져옴.
#   순서를 섞어 (7, 1)·(9, 7) 처럼 연속이 아닌 조합이 섞이고, 합 대신 튜플을 append,
#   회전한 sequence 대신 elements 를 씀 → 셋 다 계획과 코드가 어긋난 것.
# 2판: for element in sequence → element 가 int 라 sum(7) 에러. 길이 j 를 안 씀.
#   "맨 앞에서 길이 j" 를 sequence[?] 빈칸으로 주니
# 3판: sequence[1:j] — 맨 앞이 인덱스 0 인 걸 놓침 (j=1 이면 빈 슬라이스 → 0).
# 4판: sequence[0:j] 로 통과. 다만 시간이 오래 걸림 (매번 처음부터 다시 더함).
# 반례 [1, 1] → {1, 2} 로 2개, 손으로 확인.


# --------------------------------------------------------------------------
# 2. 최적화된 버전
# --------------------------------------------------------------------------
def solution(elements):
    """원형 수열의 연속 부분 수열 합으로 나올 수 있는 서로 다른 값의 개수.

    두 번 이어 붙이면 회전 없이 끝을 넘는 구간을 그대로 슬라이스할 수 있다.
    시작점마다 길이를 하나씩 늘리며 직전 합에 한 칸만 더한다.
    """
    n = len(elements)
    circular = elements * 2
    sums = set()
    for start in range(n):
        total = 0
        for length in range(n):
            total += circular[start + length]
            sums.add(total)
    return len(sums)


# --- 설명 ---
#
# 고친 이유
# - sum(sequence[0:j]) 는 j 가 늘 때마다 앞부분을 다시 더함 → 누적합 변수 하나로.
#   길이 j 의 합 = 길이 j-1 의 합 + 한 칸. total 은 시작점이 바뀔 때 0 으로.
# - 회전(slice + concat)도 매번 새 리스트를 만든다 → elements * 2 로 한 번만.
# - 리스트에 모았다 set 으로 바꾸지 않고 처음부터 set 에 add.
# 복잡도: O(n²). 나의 풀이는 합을 매번 새로 구해 O(n³) — n=1000 이면 약 5억 번.
# 짧지만 안 되는 대안
# - permutations: 순서를 섞어 연속이 아닌 조합이 섞이고, 개수도 폭발한다. 1판이 이것.
# - set 없이 리스트 길이: 같은 합이 여러 번 세진다.
#
# 다시 만나면: 원형 배열은 두 번 이어 붙인다. 구간 길이를 늘려 가며 합을 구하면 직전 합에 한 칸만 더한다.
