def BST(node):
    global idx

    if node >= len(tree):
        return
    BST(node * 2)  # 왼쪽 자식 방문
    tree[node] = n[idx]  # 현재 노드에 숫자 넣기
    idx += 1
    BST(node * 2 + 1)  # 오른쪽 자식 방문


t = int(input())

for i in range(t):
    n = list(range(1, (int(input())) + 1))
    tree = [0] * (len(n) + 1)
    idx = 0

    BST(1)

    print(f"#{i + 1} {tree[1]} {tree[len(n) // 2]}")
