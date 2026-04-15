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