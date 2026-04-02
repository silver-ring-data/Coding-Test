def solution(X, Y):
    # 공통점 찾고
    # 큰순서대로 나열
    
    x_counts = [0] * 10
    y_counts = [0] * 10
    
    for current_x in X :
        x_counts[int(current_x)] += 1
    for current_y in Y :
        y_counts[int(current_y)] += 1
        
    duplicates = []
    number = 0
    for x_count, y_count in zip(x_counts,y_counts) :
        if x_count > 0 and y_count > 0 : # 값이 모두 있는 경우
            dup_count = min(x_count,y_count)
        
            for _ in range(dup_count) :
                duplicates.append(str(number))
        number += 1
    duplicates.reverse()
    
    if not duplicates:
        return "-1"

    if duplicates[0] == "0":
        return "0"
    
    return "".join(duplicates)

   