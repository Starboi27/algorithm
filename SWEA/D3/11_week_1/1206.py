import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D3\input.txt", "r")

t = 10

for tc in range(1, t + 1):
    n = int(input())
    billding = list(map(int, input().split()))
    result = 0

    for i in range(2, len(billding) - 2):
        highest = max(
            billding[i - 2], billding[i - 1], billding[i + 1], billding[i + 2]
        )
        if billding[i] > highest:
            result += billding[i] - highest

    print(f"#{tc} {result}")

# 현재 빌딩이 highest보다 커야 조망권이 확보가 됨 ㅇㅋ?
