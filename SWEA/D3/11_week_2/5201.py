import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D3\input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    result = 0

    container.sort(reverse=1)
    truck.sort(reverse=1)

    for capacity in truck:
        for i in range(len(container)):
            if capacity >= container[i]:
                result += container[i]
                container.pop(i)
                break

    print(f"#{tc} {result}")

# 그리디 알고리즘 복습
