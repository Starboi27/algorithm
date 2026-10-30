import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D2\10_week_5\input.txt", "r")


def BFS(here):
    Queue.append(here)
    visited[here] = True
    Distance[here] = 0

    while Queue:
        here = Queue.pop(0)

        for next in myMap[here]:
            if not visited[next]:
                visited[next] = True
                Distance[next] = Distance[here] + 1
                Queue.append(next)


t = int(input())

for tc in range(1, t + 1):
    V, E = map(int, input().split())

    myMap = [[] for _ in range(V + 1)]
    visited = [False] * (V + 1)
    Queue = []
    Distance = [-1] * (V + 1)

    for i in range(E):
        start, end = map(int, input().split())
        myMap[start].append(end)
        myMap[end].append(start)

    S, G = map(int, input().split())

    BFS(S)
    answer = 0
    if Distance[G] == -1:
        answer = 0
    else:
        answer = Distance[G]
    print(f"#{tc} {answer}")

# BFS 이용