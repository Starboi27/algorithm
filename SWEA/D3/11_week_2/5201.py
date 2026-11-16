import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D3\input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    container.sort(reverse=1)
    truck.sort(reverse=1)

    result = []

    for i in range(m):
        for j in range(len(container)):
            if truck[i] >= container[j]:
                result.append(container[j])
                container.pop(j)
                break

    print(f"#{tc} {sum(result)}")

# 그리디 알고리즘 복습
