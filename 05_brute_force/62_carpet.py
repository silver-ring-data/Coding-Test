# 2026-10-16
# 카펫 (Lv.2)
# https://school.programmers.co.kr/learn/courses/30/lessons/42842


# --------------------------------------------------------------------------
# 1. 나의 풀이
# --------------------------------------------------------------------------
def solution(brown, yellow):
    total = brown + yellow
    h = 3
    while h < total:
        w, is_w_int = total//h, total%h
        if (w >= h) & (is_w_int == 0):
            yellow_calc = (w-2) * (h-2)
            if yellow_calc == yellow:
                return [w,h]
            else:
                h += 1
                continue
        else:
            h += 1
            continue


# --- 피드백 과정 ---
#
# 접근: 처음엔 감이 안 와서 힌트 요청.
#   "전체 칸 수?" → 12 = 4*3 을 본인이 짚음 (가로*세로 = brown+yellow).
#   12 의 약수 쌍 중 세로 2 이하는 "안쪽이 없어진다" 고 본인이 탈락시킴.
#   안쪽 = (4-2)*(3-2) 를 본인이 써서 멈춤 조건 (w-2)*(h-2) == yellow 완성.
#   "약수를 다 구해야 하나?" → 세로 h 하나만 돌리면 w 는 자동으로 정해진다.
# 코드 1판 버그 넷:
#   ① while h == total — 조건 반대, 루프에 한 번도 안 들어감 (while 조건 반대 패턴 또 나옴)
#   ② w == total/h — 대입 대신 비교
#   ③ / 는 항상 float → isinstance(w, int) 가 늘 False. 나누어떨어짐은 % 로
#   ④ true → True
#   brown=10, yellow=2 를 따라가며 질문으로 짚었고, 넷 다 본인이 고침.
#   // 와 % 를 한 줄에 같이 구한 건 좋았다.
# 반례: 정사각형(brown=8, yellow=1 → [3,3]) 은 w >= h 의 = 덕분에 통과.
# 결과: 통과.


# --------------------------------------------------------------------------
# 2. 최적화된 버전
# --------------------------------------------------------------------------
def solution(brown, yellow):
    """카펫의 [가로, 세로]를 반환한다.

    세로 h 를 3부터 올리며 total 의 약수인지 보고,
    테두리를 벗긴 안쪽 넓이가 yellow 와 같으면 답.
    """
    total = brown + yellow
    for h in range(3, int(total ** 0.5) + 1):
        if total % h == 0:
            w = total // h
            if (w - 2) * (h - 2) == yellow:
                return [w, h]


# --- 설명 ---
#
# 고친 이유
# - while + 수동 h += 1 + continue 를 for range 로. 증가를 빠뜨릴 일이 없다.
# - else: continue 는 루프 끝이라 필요 없다.
# - & 는 비트 연산자. 조건 결합은 and (단락 평가도 된다).
# - h <= w 이므로 h 는 √total 까지만 보면 된다. 그래서 w >= h 검사도 빠진다.
# 복잡도: O(√(brown+yellow)).
# 짧지만 안 되는 대안
# - w > h: 정사각형(8, 1 → [3,3]) 에서 None.
# - w = total / h + isinstance(w, int): / 는 항상 float 라 늘 False.
# - h 를 1부터: 세로 1·2 는 안쪽이 0 이라 yellow ≥ 1 이면 어차피 안 맞지만, 3부터가 의미상 맞다.
# - 수식 풀이: w+h = (brown+4)/2, w*h = total 이라 이차방정식으로 바로 나온다. 짧지만 완전탐색 연습 취지와 다름.
#
# 다시 만나면: 두 값이 곱으로 묶여 있으면 하나만 돌리고 나머지는 나눗셈으로.
