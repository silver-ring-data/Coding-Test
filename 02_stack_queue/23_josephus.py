def function(N,K) :
  
  people = [num+1 for num in range(N)]
  result = []
  current_index = 0

  while people:
    
    current_index = (current_index + K-1) % len(people) # 출발 인덱스 바꾸기
    result.append(people.pop(current_index))


  return result

function(7,3)

# --------------------------------------------------------------------------
# 풀이 메모 — gist 코멘트에서 옮겨온 기록이다 (2026-08-29 이관).
# 문제를 풀며 남긴 시행착오이므로 당시 문장을 그대로 둔다.
# 원본: https://gist.github.com/silver-ring-data/97369d01905395fe6f2e12b27e78ce44
#
# [2026-03-27]
# question : (current_index + K-1) 이게 왜이렇게 이해가 안될까 ..
# --------------------------------------------------------------------------
