import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D2\10_week_5\input.txt", "r")


def BFS(S, G):
    Queue.append(S)
    visited[S] = True
    distance[S] = 0

    while Queue:
        here = Queue.pop(0)

        for next in node[here]:
            if not visited[next]:
                visited[next] = True
                distance[next] = 1 + distance[here]
                Queue.append(next)
    if distance[G] == -1:
        return 0
    return distance[G]


t = int(input())

for tc in range(1, t + 1):
    V, E = map(int, input().split())
    node = [[] for _ in range(V + 1)]
    visited = [False] * (V + 1)
    Queue = []
    distance = [-1] * (V + 1)
    for i in range(E):
        start, end = map(int, input().split())

        node[start].append(end)
        node[end].append(start)

    S, G = map(int, input().split())

    result = BFS(S, G)

    print(f"#{tc} {result}")
