import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D3\input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    char = list(map(int, input().split()))

    arr = []
    for i in char:
        total = 0
        for j in str(i):
            total += int(j)
        arr.append(total)

    print(arr)

    print(f"#{tc} {max(arr)} {min(arr)}")

# 최소값 선언 하는 방법 복습
