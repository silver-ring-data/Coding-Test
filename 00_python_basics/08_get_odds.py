def get_odds(*args : int):
  result = []
  args_list = list(args)

  while args_list:
    arg = args_list.pop(0)
    if arg % 2 :
      result.append(arg)
  
  return result

# --------------------------------------------------------------------------
# 풀이 메모 — gist 코멘트에서 옮겨온 기록이다 (2026-08-29 이관).
# 문제를 풀며 남긴 시행착오이므로 당시 문장을 그대로 둔다.
# 원본: https://gist.github.com/silver-ring-data/61671226cd231fc7b7e619e923debb88
#
# [2026-03-05]
# [bug] : 튜플을 리스트 내부 함수 pop을 쓰는 바람에 오류가 남 -> 튜플을 리스트로 변환해야함.
#
# [2026-03-05]
# [bug] : while args에서 args가 변하지 않으니 무한루프하는 문제
#
# + 인자를 가변처리 안한 문제
# --------------------------------------------------------------------------
