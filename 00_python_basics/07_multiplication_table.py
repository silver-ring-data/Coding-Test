def function(start_num : int, end_num : int) :
  for n in range(start_num,end_num+1) :
    if not n % 2 :
      for m in range(1,10) :
        if not m % 3 :
          continue
        else : 
          print(f'{n} * {m} = {n*m:>2}')


function(2,9)

# --------------------------------------------------------------------------
# 풀이 메모 — gist 코멘트에서 옮겨온 기록이다 (2026-08-29 이관).
# 문제를 풀며 남긴 시행착오이므로 당시 문장을 그대로 둔다.
# 원본: https://gist.github.com/silver-ring-data/b34e29e168f9461282e5a76d3650b5de
#
# [2026-03-04]
# [initial] : 구현 성공. 최적화 필요
#
# [2026-03-04]
# [refactor] :  if not n % 2 : 의 위치를 바꿈으로써 코드 최적화 적용
# --------------------------------------------------------------------------
