import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D2\11_week_1\input.txt", "r")


def BFS(S):
    visited[S] = True
    distance[S] = 0
    Queue.append(S)

    while Queue:
        here = Queue.pop(0)

        for next in node[here]:
            if not visited[next]:
                visited[next] = True
                distance[next] = 1 + distance[here]
                Queue.append(next)

    if distance[G] >= 1:
        return 1
    else:
        return 0


t = int(input())

for tc in range(1, t + 1):
    V, E = map(int, input().split())
    node = [[] for _ in range(V + 1)]
    Queue = []
    distance = [-1] * (V + 1)
    visited = [False] * (V + 1)

    for i in range(E):
        start, end = map(int, input().split())
        node[start].append(end)

    S, G = map(int, input().split())

    result = BFS(S)

    print(f"#{tc} {result}")

# 복습
