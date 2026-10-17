# 이진 탐색 트리
# 왼쪽 값은 루트보다 작음
# 오른쪽 값은 루트보다 큼
# tree는 index 1부터 시작해야 됨


def BST(node):
    global idx
    # 없는 노드면 끝내기
    if node >= len(tree):
        return

    # 왼쪽 자식 처리하기
    BST(node * 2)

    # 현재 노드에 숫자 넣고 다음 숫자 준비하기
    tree[node] = list[idx]

    idx += 1

    # 오른쪽 자식 처리하기
    BST(node * 2 + 1)


list = [1, 2, 3, 4, 5, 6]
tree = [0] * (len(list) + 1)
idx = 0

BST(1)

print(tree)
