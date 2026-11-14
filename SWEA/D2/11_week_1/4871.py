import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D2\input.txt", "r")


def BFS(s, g):
    queue.append(s)
    distance[s] = 0
    visited[s] = True

    while queue:
        here = queue.pop(0)

        for next in node[here]:
            if not visited[next]:
                distance[next] = 1 + distance[here]
                visited[next] = True
                queue.append(next)

    if distance[g] == -1:
        return 0
    return 1


t = int(input())

for tc in range(1, t + 1):
    v, e = map(int, input().split())  # 단방향 노드
    node = [[] for _ in range(v + 1)]
    queue = []
    visited = [False] * (v + 1)
    distance = [-1] * (v + 1)

    for i in range(e):
        idx, val = map(int, input().split())
        node[idx].append(val)

    s, g = map(int, input().split())

    result = BFS(s, g)

    print(f"#{tc} {result}")
