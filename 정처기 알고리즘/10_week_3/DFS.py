# DFS(Depeth-First-Search) : 한 경로로 최대한 깊이 들어갔다 막히면 돌아오는 탐색 방법

NodeNum, Edgenum = map(int, input().split())
MyMap = [[] for _ in range(NodeNum + 1)]
visited = [False] * (NodeNum + 1)

for _ in range(Edgenum):
    start, stop = map(int, input().split())

    MyMap[start].append(stop)
    MyMap[stop].append(start)
    # 양방향의미

# 7 8
# 1 2
# 1 3
# 1 4
# 1 5
# 2 6
# 2 7
# 5 6
# 6 7


def dfs(here):
    stack = []
    order = []
    visited[here] = True

    order.append(here)
    while here:
        next = None

        for i in MyMap[here]:
            if not visited[i]:
                next = i
                break

        if next:
            order.append(next)
            stack.append(here)
            here = next
            visited[here] = True
        elif stack:
            here = stack.pop()
        else:
            break

    return order


result = dfs(1)
print(result)
