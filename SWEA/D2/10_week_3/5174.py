# DFS로 탐색해 노드 개수 구하기


# 1 : 6
# 2 : 1 5
# 3 : 0
# 4 : 0
# 5 : 3
# 6 : 4
def dfs(here):
    visited[here] = True
    count = 1
    for next in MyMap[here]:

        if not visited[next]:
            count += dfs(next)

    return count


t = int(input())

for tc in range(1, t + 1):
    Edgenum, NodeNum = map(int, input().split())
    MyMap = [[] for i in range(Edgenum + 2)]
    visited = [False] * (len(MyMap) + 2)

    edges = list(map(int, input().split()))

    for i in range(0, len(edges), 2):
        start = edges[i]
        stop = edges[i + 1]

        MyMap[start].append(stop)

    print(f"#{tc} {dfs(NodeNum)}")
