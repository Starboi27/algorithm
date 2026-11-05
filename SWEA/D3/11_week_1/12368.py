import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D3\input.txt", "r")

t = int(input())

for tc in range(1, t + 1):

    n, m = map(int, input().split())
    result = n + m

    if result >= 24:
        result = (n + m) % 24

    print(f"#{tc} {result}")
