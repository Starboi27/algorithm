import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D2\10_week_5\input.txt", "r")

T = int(input())

for TC in range(1, T + 1):
    code = input().split()
    stack = []

    for token in code:
        if token.isdigit():
            stack.append(int(token))
        elif token in ("+", "-", "/", "*"):
            if len(stack) < 2:
                print(f"#{TC} error")

                break

            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "/":
                if b == 0:
                    break
                stack.append(a // b)
            elif token == "*":
                stack.append(a * b)

        elif token == ".":
            if len(stack) == 1:
                print(f"#{TC} {stack.pop()}")
            else:
                print(f"#{TC} error")
