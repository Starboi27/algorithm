import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D3\input.txt", "r")


def tree():
    for i in range(N, 1, -1):
        parent = i // 2
        node[parent] += node[i]


t = int(input())

for tc in range(1, t + 1):
    N, M, L = map(int, input().split())  # 5, 3, 2

    node = [0] * (N + 1)
    stack = []
    visited = [False] * (N + 1)

    for i in range(M):
        idx, val = map(int, input().split())
        node[idx] = val

    tree()

    print(f"#{tc} {node[L]}")

# 복습
