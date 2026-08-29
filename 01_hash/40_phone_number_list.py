def solution(phone_book):
    phone_book.sort()
    for index in range(len(phone_book)-1):
        if phone_book[index+1].startswith(phone_book[index]):
            return False
    answer = True
    return answer

# --------------------------------------------------------------------------
# 풀이 메모 — gist 코멘트에서 옮겨온 기록이다 (2026-08-29 이관).
# 문제를 풀며 남긴 시행착오이므로 당시 문장을 그대로 둔다.
# 원본: https://gist.github.com/silver-ring-data/6b27eda34414f01c86efa98d361471bd
#
# [2026-04-27]
# 작성하다보니, 번호를 일일이 다 비교하는건 비효율적이라고 생각이 들었음 -> sort 사용
# startswitch는 앞부분만 딱 비교하고 끝나기 때문에 find보다 효율적
# --------------------------------------------------------------------------
