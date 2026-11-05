import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D3\input.txt", "r")

t = 10

for tc in range(1, t + 1):
    n = int(input())
    data = list(map(int, input().split()))
    result = 0

    for i in range(2, n - 2):
        highest = max(data[i - 2], data[i - 1], data[i + 1], data[i + 2])
        if highest < data[i]:
            result += data[i] - highest

    print(f"#{tc} {result}")
