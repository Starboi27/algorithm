# 재귀로 DFS 구현

Data = [
    # 0  1  2  3  4  5  6  7 ← 연결 대상 번호
    [0, 0, 0, 0, 0, 0, 0, 0],  # 0번
    [0, 0, 1, 1, 1, 1, 0, 0],  # 1번
    [0, 1, 0, 0, 0, 0, 1, 1],  # 2번
    [0, 1, 0, 0, 0, 0, 0, 0],  # 3번
    [0, 1, 0, 0, 0, 0, 0, 0],  # 4번
    [0, 1, 0, 0, 0, 0, 1, 0],  # 5번
    [0, 0, 1, 0, 0, 1, 0, 1],  # 6번
    [0, 0, 1, 0, 0, 0, 1, 0],  # 7번
]
visited = [False] * 8

def DFS(here):
    print(here)
    visited[here] = True

    for next in range(8):
        if Data[here][next] and not visited[next]:
            DFS(next)


DFS(1)
