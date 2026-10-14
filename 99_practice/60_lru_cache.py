# 2026-10-14
# [1차] 캐시 (Lv.2)
# https://school.programmers.co.kr/learn/courses/30/lessons/17680


# --------------------------------------------------------------------------
# 1. 나의 풀이
# --------------------------------------------------------------------------
def solution(cacheSize, cities):
    '''
    일괄 대문자/소문자로 변경후
    cities에 검색 
        -> cache hit일 경우 result +1
            -> 해당 위치를 마지막으로 갱신
        -> cache miss 일 경우 result +5
            -> 목록갯수가 cachesize미만일경우 그냥 추가
            -> 목록갯수가 cachesize이상일 경우 처음 제거 후 마지막에추가
    '''
    cacheMiss = 5
    cacheHit = 1
    
    if cacheSize == 0:
        return cacheMiss*len(cities)
    
    cities_lowers = [city.lower() for city in cities]
    caches = []
    answer = 0
        
    for city in cities_lowers:
        if city in caches:
            answer += cacheHit
            caches.remove(city)
            caches.append(city)
        else:
            answer += cacheMiss
            if len(caches) < cacheSize:
                caches.append(city)
            else: 
                del caches[0]
                caches.append(city)
    return answer


# --- 피드백 과정 ---
#
# 접근(첫 판): 소문자 통일 → sorted → hit +1 / miss +5 → 5개 미만이면 추가, 이상이면 마지막 제거.
#   걸린 곳 셋: ① sorted 가 사용 순서를 지움 ② 캐시 크기를 miss 비용 5 와 혼동
#   ③ hit 때 아무것도 안 함 → LRU 가 아니라 FIFO.
# ①② 는 질문 하나로 본인이 고치고, 빼는 쪽을 "앞에서 빼고 뒤에 넣기" 로 방향도 정리함.
# ③ 반례: cacheSize=2, [A, B, A, C] 를 표로 따라가게 하니
#   [B, A] 를 적다가 "최신으로 갱신되는 로직이 없군" 을 본인이 찾음.
# 코드 1판: cities.lower() (리스트에 lower) · < 5 가 다시 돌아옴 → 짚자 바로 고침.
# cacheSize=0: 빈 리스트 del 에러를 elif len==0 → append 로 막음.
#   에러는 사라졌지만 크기 0 캐시에 도시가 담겨 [A, A] 가 6 (답 10).
#   문제 예시는 도시가 전부 달라 그대로 통과 → 예시 통과 ≠ 정답, 또 나온 패턴.
#   본인이 맨 위 early return 으로 바꾸고, 남은 elif 가 dead code 인 것도 정리.
# 결과: 통과.


# --------------------------------------------------------------------------
# 2. 최적화된 버전
# --------------------------------------------------------------------------
from collections import deque


def solution(cacheSize, cities):
    """LRU 캐시로 도시를 조회할 때의 총 실행시간을 반환한다.

    앞 = 가장 오래 안 쓴 것, 뒤 = 방금 쓴 것.
    hit 면 꺼내서 뒤로, miss 면 뒤에 넣는다 (꽉 차면 deque 가 앞을 밀어냄).
    """
    cache = deque(maxlen=cacheSize)
    answer = 0
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            answer += 1
        else:
            answer += 5
        cache.append(city)
    return answer


# --- 설명 ---
#
# 고친 이유
# - hit·miss 둘 다 마지막에 append → 공통으로 한 번만.
# - deque(maxlen): 꽉 찼을 때 append 하면 앞을 자동으로 버린다.
#   maxlen=0 이면 아무것도 안 담겨 전부 miss → cacheSize 0 예외 처리가 필요 없다.
# 복잡도: O(n · cacheSize). in·remove 가 캐시 길이만큼 돌지만 cacheSize ≤ 30 이라 충분.
# 짧지만 안 되는 대안
# - set 캐시: in 은 빠르지만 순서가 없어 누가 제일 오래됐는지 모른다.
# - hit 때 갱신 생략: FIFO 가 된다. 첫 판이 이것.
#
# 다시 만나면: LRU = "쓸 때마다 맨 뒤로". 크기 0 은 손으로 [A, A] 넣어 본다.
