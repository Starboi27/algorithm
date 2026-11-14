import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D3\input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    a, b = map(int, input().split())
    n = list(map(int, input().split()))
    m = list(map(int, input().split()))
    count = 0

    for value_a in n:  # 1, 2, 3
        if value_a in m:
            count += 1

    print(f"#{tc} {count}")
