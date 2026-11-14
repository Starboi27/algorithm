import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D2\input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    str_ = input()
    stack = [0]

    for str_val in str_:
        if str_val == stack[-1]:
            stack.pop()
        else:
            stack.append(str_val)

    print(f"#{tc} {len(stack) - 1}")

# for stack and str_val == stack[-1]: 로 쓰는게 효율적
