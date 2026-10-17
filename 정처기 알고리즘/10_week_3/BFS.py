# 너비 우선 탐색. 시작점에서 가까운 노드부터 탐색

MyMap = [
    # 0  1  2  3  4  5  6  7  8
    [0, 0, 0, 0, 0, 0, 0, 0, 0],  # 0번
    [0, 0, 1, 1, 1, 1, 0, 0, 0],  # 1번
    [0, 1, 0, 0, 0, 0, 1, 1, 0],  # 2번
    [0, 1, 0, 0, 0, 0, 0, 0, 0],  # 3번
    [0, 1, 0, 0, 0, 0, 0, 0, 0],  # 4번
    [0, 1, 0, 0, 0, 0, 1, 0, 0],  # 5번
    [0, 0, 1, 0, 0, 1, 0, 1, 1],  # 6번
    [0, 0, 1, 0, 0, 0, 1, 0, 0],  # 7번
    [0, 0, 0, 0, 0, 0, 1, 0, 0],  # 8번
]

visited = [False] * 9
Queue = []
Distance = [0] * 9
Parent = [-1] * 9


def BFS(here):
    Queue.append(here)
    visited[here] = True

    while Queue:

        here = Queue.pop(0)
        print(here)

        for next in range(9):
            if MyMap[here][next] and not visited[next]:
                visited[next] = True
                Distance[next] = Distance[here] + 1
                Parent[next] = here
                Queue.append(next)

    print(Distance)
    print(Parent)


BFS(1)
