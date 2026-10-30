# DFS

import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D2\10_week_3\sample_input.txt", "r")


def DFS(here):
    count = 1
    visited[here] = True

    for next in graph[here]:
        if not visited[next]:
            count += DFS(next)

    return count


t = int(input())


for tc in range(1, t + 1):
    E, N = map(int, input().split())
    node = list(map(int, input().split()))
    visited = [False] * (E + 2)

    graph = [[] for _ in range(E + 2)]  # 인덱스를 1부터 쓰기 위해 +2

    for i in range(E):
        start = node[i * 2]
        end = node[i * 2 + 1]

        graph[start].append(end)


    print(f"#{tc} {DFS(N)}")
