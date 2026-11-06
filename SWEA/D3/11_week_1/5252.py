import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D3\input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    A, B = map(int, input().split())
    count = 0
    stack = []

    for _ in range(A):
        answer = input()
        stack.append(answer)
    for _ in range(B):
        answer = input()
        stack.append(answer)

    while stack:
        now = stack.pop()
        if now in stack:
            count += 1

    print(f"#{tc} {count}")
