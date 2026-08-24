def solution(n,a,b):
    
    # n번 참가자의 다음 순서 : (n+1)//2 -> 이후 n은 n/2가 됨
    # 만나는 경우 : (n-1)//2가 같을 때
    answer = 1
    
    while not cal_stage(a) == cal_stage(b) :
        a = cal_index(a)
        b = cal_index(b)
        
        n = n/2
        answer += 1

    return answer

def cal_stage(index):
    return (index - 1) // 2

def cal_index(index):
    return (index + 1) // 2
    