import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D2\input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    n = list(input().strip())

    result = 0
    for i in range(1, len(n)):
        if n[:i] == n[i : i * 2]:
            result = i
            break

    print(f"#{tc} {result}")
