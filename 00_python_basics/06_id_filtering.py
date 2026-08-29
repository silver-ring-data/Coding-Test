def function(raw_ids : list[str]) -> tuple[int,list[str]]:
  new_ids = set([raw_id.lower() for raw_id in raw_ids])

  return len(new_ids), sorted(list(new_ids))

raw_ids = ["User1", "admin", "USER1", "Guest", "ADMIN"]
print(function(raw_ids))

# --------------------------------------------------------------------------
# 풀이 메모 — gist 코멘트에서 옮겨온 기록이다 (2026-08-29 이관).
# 문제를 풀며 남긴 시행착오이므로 당시 문장을 그대로 둔다.
# 원본: https://gist.github.com/silver-ring-data/70d97eaebe9abd4b21d67f5994e82361
#
# [2026-03-03]
# 타입 힌트 불일치:
#
# 순서 보장(정렬): 아까 우리가 고민했듯이 set은 순서가 제멋대로야. 문제 요구사항인 **'알파벳 순서 정렬'**을 만족하려면 list(new_ids) 대신 **sorted(new_ids)**를 쓰는 게 좋아. sorted()는 결과를 알아서 리스트로 돌려주거든!
# --------------------------------------------------------------------------
