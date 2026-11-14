import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D3\input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    list_ = list(map(int, input().split()))

    up = 0
    down = 0

    for i in range(n - 1):  
        now = list_[i]
        next = list_[i + 1]

        if now < next:
            up = max(up, next - now)
        elif now > next:
            down = max(down, now - next)

    print(f"#{tc} {up} {down}")

