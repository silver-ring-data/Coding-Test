# y값으로 부모-자식 판별
# x값으로 왼쪽-오른쪽 판별
    #새 노드의 x < 현재 노드의 x:
        # 왼쪽 자식이 비어있으면? 자리찾기 완료
        # 있다면? 
import sys
sys.setrecursionlimit(10**6)
from dataclasses import dataclass

@dataclass
class Node:
    id: int      # 노드 번호 (결과 출력용)
    x: int
    y: int
    left: 'Node' = None
    right: 'Node' = None

def solution(nodeinfo):
    # 1. 노드 번호를 포함한 리스트 생성 (id는 1부터 시작)
    # Clean Code: enumerate를 사용해 인덱스와 값을 동시에 깔끔하게 가져오기
    nodes = []
    for i, (x, y) in enumerate(nodeinfo):
        nodes.append(Node(id=i + 1, x=x, y=y))
    
    # 2. y는 내림차순, x는 오름차순으로 정렬
    # 람다(lambda)를 쓰면 한 줄로 우아하게 정렬할 수 있어
    nodes.sort(key=lambda n: (-n.y, n.x))
    
    # 3. 루트 노드 설정 및 트리 구성
    root = nodes[0]
    for i in range(1, len(nodes)):
        insert_node(root, nodes[i])
        
    pre_result = []
    post_result = []
    
    # 4. 순회 결과 담기 (이제 순회 함수만 만들면 끝!)
    pre_order(root,pre_result)
    post_order(root,post_result)
    
    return [pre_result, post_result]
# 전위 순회: 부모 -> 왼쪽 -> 오른쪽
def pre_order(node, result):
    if node is None:
        return
    # 1. 나(부모)를 먼저 기록
    result.append(node.id)
    # 2. 왼쪽으로 가고
    pre_order(node.left, result)
    # 3. 오른쪽으로 가고
    pre_order(node.right, result)
    return result
    
# 후위 순회: 부모 -> 왼쪽 -> 오른쪽
def post_order(node, result):
    if node is None:
        return
    post_order(node.left, result)
    post_order(node.right, result)
    result.append(node.id)
    return result

def insert_node(parent: Node, new_node: Node):
    if new_node.x < parent.x:
        if parent.left is None:
            parent.left = new_node
        else:
            insert_node(parent.left, new_node)
    else: # new_node.x > parent.x
        if parent.right is None:
            parent.right = new_node
        else:
            insert_node(parent.right, new_node)
    