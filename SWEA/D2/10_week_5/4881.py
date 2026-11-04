import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D2\10_week_5\input.txt", "r")


def DFS():
    stack.append((0, 0, [False] * N))
    min_sum = float("inf")

    while stack:
        row, total, visited = stack.pop()

        if total >= min_sum:
            continue

        if row == N:
            min_sum = total
            continue

        for col in range(N):
            if not visited[col]:
                new_visited = visited.copy()
                new_visited[col] = True

                new_total = total + data[row][col]

                stack.append((row + 1, new_total, new_visited))

    return min_sum


t = int(input())

for tc in range(1, t + 1):
    N = int(input())

    stack = []
    data = [[] for _ in range(N)]

    for TN in range(N):
        number = list(map(int, input().split()))
        data[TN].extend(number)

    result = DFS()

print(data, result)
