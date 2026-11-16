import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D3\input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())

    contest = [list(map(int, input().split())) for _ in range(n)]

    max_ = 0
    winner = 0

    for i in range(n):
        cnt = 0
        for j in range(m):
            if contest[i][j] == 1:
                cnt += 1

        if max_ == cnt:
            winner += 1
        elif max_ < cnt:
            winner = 1

        max_ = max(max_, cnt)

    print(f"#{tc} {winner} {max_}")

# winner 구하는 방법 복습
