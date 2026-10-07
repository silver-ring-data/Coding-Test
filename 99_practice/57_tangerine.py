# 2026-10-07 (10/06 몫)
# 귤 고르기 (Lv.2)
# https://school.programmers.co.kr/learn/courses/30/lessons/138476


# --------------------------------------------------------------------------
# 1. 나의 풀이
# --------------------------------------------------------------------------
def solution(k, tangerine):
    orange = {}
    count = 0
    answer = 0
    
    for size in tangerine:
        orange[size] = orange.get(size,0)+1
    orange_counts = sorted(orange.values(),reverse=True)
    for orange_count in orange_counts:
        if count < k:
            count += orange_count
            answer += 1
            if count >= k:
                return answer
        elif count >= k:
            return answer


# --- 피드백 과정 ---
#
# 접근: "같은 크기가 많은 것부터 담기" 는 본인이 바로 냄.
# 막힌 지점 ①: dict 를 리스트처럼 생각해 "key 가 얼마까지 있는지" 미리 정하려 함.
#   dict 는 나온 key 만 생긴다 → `orange.get(size, 0) + 1` 은 본인이 씀.
# 막힌 지점 ②: 종료 조건을 "합이 k 가 되면" (==) 으로 잡음.
#   반례 k=5, 묶음 [2,2,2] → 합이 4→6 으로 건너뛰어 5 가 없다.
#   "일부만 담으면 된다" 를 본인이 짚고 >= 로 고침.
# 막힌 지점 ③: `reversed=True` 오타 (옵션은 reverse, reversed() 는 별개 함수).
# 막힌 지점 ④: 확인을 "다음 바퀴" 에서 함 → 마지막 묶음에서 k 를 채우면 None.
#   반례 k=2, [1,1]. **예시 3개는 통과해서 처음엔 맞다고 봄** (가장 큰 수와 같은 패턴).
#   더한 직후 확인으로 고침. 바깥 if/elif 가 필요 없다는 것도 본인이 판단.
# 결과: 통과.


# --------------------------------------------------------------------------
# 2. 최적화된 버전
# --------------------------------------------------------------------------
from collections import Counter


def solution(k, tangerine):
    """k개를 담을 때 크기 종류 수의 최솟값을 반환한다.

    크기별 개수를 세어 많은 묶음부터 담고, k개 이상이 되는 순간의 종류 수가 답.
    """
    count = 0
    for kind, n in enumerate(sorted(Counter(tangerine).values(), reverse=True), 1):
        count += n
        if count >= k:
            return kind


# --- 설명 ---
#
# 고친 이유
# - 바깥 if/elif 삭제: >= k 면 바로 return 하므로 루프 시작 때 count 는 항상 k 미만.
# - Counter: dict 로 세는 것과 같은 일을 한 줄로.
# - enumerate(..., 1): answer 를 따로 세지 않고 순번이 곧 종류 수.
# 복잡도: 시간 O(n log n) (정렬), 공간 O(n).
# 짧지만 안 되는 대안: len(set(tangerine))
#   전부 담았을 때의 종류 수라 k 가 작으면 답보다 커진다.
#
# 다시 만나면: "합이 k 가 되면" 은 == 말고 >=, 확인은 더한 직후에.
