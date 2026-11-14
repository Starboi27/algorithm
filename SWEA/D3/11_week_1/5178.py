import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D3\input.txt", "r")


def tree(n):
    for i in range(n, 1, -1):
        parent = i // 2
        node[parent] += node[i]


t = int(input())

for tc in range(1, t + 1):
    n, m, l = map(int, input().split())

    node = [0] * (n + 1)

    for i in range(m):
        start, end = map(int, input().split())
        node[start] = end

    tree(n)

    print(f"#{tc} {node[l]}")

# 11.07 복습 다시 복습
