t = int(input())


def BFS(here):
    Queue.append(here)
    visited[here] = True

    while Queue:
        here = Queue.pop(0)
        print(here)


for tc in range(t):
    V, E = map(int, input().split())

    MyMap = [[] for _ in range(V + 1)]
    visited = [False] * (V + 1)
    Queue = []
    Distance = [] * (V + 1)
    Parent = [-1] * (V + 1)

    for _ in range(E):
        start, end = map(int, input().split())
        MyMap[start].append(end)
        MyMap[end].append(start)

    print(MyMap)

    BFS(1)

# 그래프 그리는 거 까지 완성
