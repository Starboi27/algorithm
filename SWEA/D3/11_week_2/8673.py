import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D3\input.txt", "r")


def tournament(players):
    global solve
    queue = []

    if len(players) == 1:
        return solve

    for idx in range(0, len(players), 2):
        left = players[idx]
        right = players[idx + 1]

        if left > right:
            solve += left - right
            queue.append(left)
        else:
            solve += right - left
            queue.append(right)

    return tournament(queue)


t = int(input())

for tc in range(1, t + 1):
    k = int(input())
    case = list(map(int, input().split()))
    solve = 0

    result = tournament(case)

    print(f"#{tc} {result}")

# 재귀 사용법 복습
