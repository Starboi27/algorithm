import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D3\input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    n = list(map(int, input().strip()))
    cnt = 0
    stack = []

    for number in n:
        if number not in stack:  # stack에 특정 idx를 확인하는 게 아님
            cnt += 1
            stack.append(number)

    print(f"#{tc} {cnt}")

# 복습 필요
