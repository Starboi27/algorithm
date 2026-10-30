import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D2\10_week_5\input.txt", "r")


def DFS():
    stack = [(1, 0, visited)]  # [(1, 0, [0, 0, 0, 0])]
    min_sum = float("inf")

    while stack:
        here, total, current_visited = stack.pop()
        # here = 1, total = 0, current_visited = [0, 0, 0, 0]
        if total >= min_sum:
            continue
        if here > N:
            min_sum = total
            continue

        for i in range(1, N + 1):
            if current_visited[i] == 0:
                new_visited = current_visited.copy()
                new_visited[i] = 1

                new_total = total + array[here][i - 1]

                stack.append((here + 1, new_total, new_visited))

    return min_sum


t = int(input())

for tc in range(1, t + 1):
    N = int(input())
    visited = [0] * (N + 1)
    array = [[] for _ in range(N + 1)]

    for i in range(N):
        array[i + 1] = list(map(int, input().split()))

    print(array)

    result = DFS()

    print(f"#{tc} {result}")
