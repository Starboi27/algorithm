import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D2\10_week_5\input.txt", "r")


def DFS():
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while stack:
        row, col = stack.pop()

        if data[row][col] == 3:
            return 1

        for dr, dc in direction:
            next_row = dr + row
            next_col = dc + col

            if 0 <= next_row < N and 0 <= next_col < N:
                if data[next_row][next_col] != 1 and not visited[next_row][next_col]:
                    visited[next_row][next_col] = True
                    stack.append((next_row, next_col))

    return 0


t = int(input())

for tc in range(1, t + 1):
    N = int(input())
    stack = []
    visited = [[False] * N for _ in range(N)]
    data = [[] for _ in range(N)]

    for i in range(N):
        data[i] = list(map(int, input()))

    for row in range(N):
        for col in range(N):
            if data[row][col] == 2:
                start_row = row
                start_col = col
                stack.append((start_row, start_col))
                visited[start_row][start_col] = True

    result = DFS()
    print(f"#{tc} {result}")
