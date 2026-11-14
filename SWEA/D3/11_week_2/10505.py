import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D3\input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    data = list(map(int, input().split()))
    avg = sum(data) // len(data)
    cnt = 0

    for now in data:
        if now <= avg:
            cnt += 1

    print(f"#{tc} {cnt}")

# 코드 최적화 복습
