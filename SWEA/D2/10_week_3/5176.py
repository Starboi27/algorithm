import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D2\10_week_3\sample_input.txt", "r")


def BST(node):

    global idx

    if node >= len(tree):
        return
    BST(2 * node)
    tree[node] = Node[idx]
    idx += 1
    BST(node * 2 + 1)


t = int(input())

for tc in range(1, t + 1):
    N = int(input())
    Node = [i for i in range(1, N + 1)]
    tree = [0] * (N + 1)
    idx = 0

    BST(1)

    print(f"#{tc} {tree[1]} {tree[N // 2]}")
