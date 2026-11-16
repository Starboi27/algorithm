import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D3\input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    n = list(map(int, input().strip()))

    result = [0] * (max(n) + 1)

    for i in n:
        result[i] = 1

    print(f"#{tc} {sum(result)}")
# 복습 필요
