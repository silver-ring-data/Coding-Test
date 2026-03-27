def function(N,K) :
  
  people = [num+1 for num in range(N)]
  result = []
  current_index = 0

  while people:
    
    current_index = (current_index + K-1) % len(people) # 출발 인덱스 바꾸기
    result.append(people.pop(current_index))


  return result

function(7,3)