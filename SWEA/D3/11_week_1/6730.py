import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D3\input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    l = int(input())

    block = list(map(int, input().split()))

    up = 0
    down = 0

    for i in range(l - 1):
        now = block[i]
        next = block[i + 1]

        if now < next:
            up = max(up, next - now)
        elif now > next:
            down = max(down, now - next)

    print(f"#{tc} {up} {down}")

# max로 이전 up, down의 값과 현재 값의 최대를 구한다
