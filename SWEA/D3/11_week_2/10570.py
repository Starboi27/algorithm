import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D3\input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    arr = [val for val in range(n, m + 1)]

    result = []
    for i in arr:
        root = int(i**0.5)

        if str(i) == str(i)[::-1] and root**2 == i:
            result.append(i)

    print(f"#{tc} {len(result)}")

# 복습 피료
