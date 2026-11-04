import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D2\11_week_1\input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    stack = []
    char = list(input().strip())

    while char:
        now = char.pop(0)
        if stack and now == stack[-1]:
            stack.pop()
        else:
            stack.append(now)

    print(f"#{tc} {len(stack)}")
