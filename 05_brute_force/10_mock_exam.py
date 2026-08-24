def solution(answers):

    patterns = [[1, 2, 3, 4, 5],[2, 1, 2, 3, 2, 4, 2, 5],[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    
    scores = [0]*len(patterns)

    for answer_index, answer in enumerate(answers) :
        for i, (pattern, score) in enumerate(zip(patterns, scores)):
            if answer == pattern[answer_index % len(pattern)]:
                scores[i] += 1
                
    max_scores = max(scores)
    return [i + 1 for i, s in enumerate(scores) if s == max_scores]