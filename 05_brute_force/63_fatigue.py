# [2026-10-20] (10/19 몫)
# 피로도 (Lv.2)
# https://school.programmers.co.kr/learn/courses/30/lessons/87946


# --------------------------------------------------------------------------
# 1. 나의 풀이
# --------------------------------------------------------------------------
from itertools import permutations
def solution(k, dungeons):
    counts = []
    count = 0
    current_fatigue = k
    for dungeon in permutations(dungeons):
        for min_fatigue, use_fatigue in dungeon:
            if current_fatigue < min_fatigue:
                counts.append(count)
                count = 0
                current_fatigue = k
                continue
            else:
                current_fatigue -= use_fatigue
                count += 1 
        counts.append(count)
        count = 0
        current_fatigue = k
        
    answer = max(counts)
    return answer


# --- 피드백 과정 ---
#
# 첫 접근: 최소 필요 피로도 순으로 정렬. 오름차순은 예시에서 2가 나와 탈락.
#   내림차순 반례: k=10, [[10,10],[6,1],[6,1]] → 내림차순 1, 6→6→10 은 2.
#   정렬 규칙 하나로는 안 풀린다 → 던전 ≤ 8 이니 순서 전부(8! = 40320) 시도.
# "트리인가?" 를 본인이 떠올림. 순열 = 트리, DFS 백트래킹도 가능.
# permutations 를 몰라서 combinations(뽑기) vs permutations(줄 세우기)로 소개받음.
# 1판 버그: 피로도·count 초기화가 함수 맨 위에 한 번뿐 → 순서끼리 상태가 섞임.
#   막힘 없이 끝까지 간 순서는 append 가 안 됨 (예시 정답 3이 바로 그 경우).
# 2판: 막혔을 때만 리셋 → 다 돈 순서의 3이 다음 순서로 넘어가
#   남의 순서에서 막힐 때 대신 append. 예시는 우연히 맞을 뻔.
# 3판: 순서 끝에도 append + 리셋 → 통과.
#   막힘 블록의 continue + 리셋은 남아 있는데, 리셋 뒤 남은 구간도
#   실제 가능한 경로라 답은 안 틀린다. 그래도 불필요한 일.
# 핵심: 리셋·기록은 "막혔을 때"가 아니라 "순서 하나" 단위.


# --------------------------------------------------------------------------
# 2. 최적화된 버전
# --------------------------------------------------------------------------
from itertools import permutations

def solution(k, dungeons):
    """모든 방문 순서를 시뮬레이션해 최대 탐험 수를 고른다."""
    answer = 0
    for order in permutations(dungeons):
        fatigue, count = k, 0              # 순서마다 새로 시작
        for need, cost in order:
            if fatigue < need:
                break                      # 막히면 이 순서는 끝
            fatigue -= cost
            count += 1
        answer = max(answer, count)        # 순서 끝날 때 한 번만 기록
    return answer


# --- 설명 ---
#
# break: 막힘·완주 둘 다 for 아래 한 곳으로 모여 기록·리셋이 한 번만.
# 초기화를 바깥 for 첫 줄로: "순서마다 새로 시작"이 코드에 보인다.
# counts 리스트 대신 max 변수: 40320개를 모을 필요 없음.
# 복잡도: O(N! · N), N ≤ 8 이라 약 32만 번.
# 짧지만 안 되는 대안: 최소 필요치·소모량 기준 정렬 그리디 → 위 반례로 깨짐.
# 다른 방법: DFS + visited 백트래킹. 못 들어가는 가지는 안 내려가서 더 빠름.
#
# 다시 만나면: N 이 작고 순서가 결과를 바꾸면 permutations, 상태는 순서마다 리셋.
