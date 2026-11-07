import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D3\input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    count = 0

    N, M = map(int, input().split())

    dataA = list(map(int, input().split()))
    dataB = list(map(int, input().split()))

    for a in dataA:
        if a in dataB:
            count += 1

    print(f"#{tc} {count}")


# 복습
