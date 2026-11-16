import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D3\input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    char = input()
    stack = []

    for i in char:
        if i not in "aeiou":  # in을 쓰면 해당 문자가 문자열에 있는지 보는거
            stack.append(i)

    result = "".join(stack)

    print(f"#{tc} {result}")

# join 함수 사용법 복습
