def inorder(node, tree):
    if node == '.': return

    left, right = tree[node]

    inorder(left, tree)
    print(node, end='')
    inorder(right, tree)

def preorder(node, tree):
    if node == '.': return

    left, right = tree[node]

    print(node, end='')
    preorder(left, tree)
    preorder(right, tree)

def postorder(node, tree):
    if node == '.': return

    left, right = tree[node]
    
    postorder(left, tree)
    postorder(right, tree)
    print(node, end='')

def solve_test():
    # 예시 데이터를 아예 넣어버림 (백준 1991번 예제)
    example_input = """7
A B C
B D .
C E F
E . .
F . G
D . .
G . ."""
    
    lines = example_input.split('\n')
    n = int(lines[0])
    tree = {}
    
    for i in range(1, n + 1):
        root, left, right = lines[i].split()
        tree[root] = (left, right)
    
    print("전위 순회:", end=' ')
    preorder('A', tree); print()
    print("중위 순회:", end=' ')
    inorder('A', tree); print()
    print("후위 순회:", end=' ')
    postorder('A', tree); print()

solve_test()

# --------------------------------------------------------------------------
# 풀이 메모 — gist 코멘트에서 옮겨온 기록이다 (2026-08-29 이관).
# 문제를 풀며 남긴 시행착오이므로 당시 문장을 그대로 둔다.
# 원본: https://gist.github.com/silver-ring-data/29cde824f8ed3cb6fb78bb83de815046
#
# [2026-04-15]
# [배운 것]
#
# 트리 순회 방식
# - 전위 순회(Pre-order): 루트 -> 왼쪽 -> 오른쪽
# - 중위 순회(In-order): 왼쪽 -> 루트 -> 오른쪽
# - 후위 순회(Post-order): 왼쪽 -> 오른쪽 -> 루트
#
# 재귀함수 쓰는 것
# --------------------------------------------------------------------------
