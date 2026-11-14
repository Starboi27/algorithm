import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D3\input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    a = 1
    b = 1

    direction_data = list(map(str, input().strip()))

    solve = []

    for direction in direction_data:
        if direction == "L":
            b = a + b
        else:
            a = a + b

    print(f"#{tc} {a} {b}")

# 분자 분모로 접근해서 풀어보센
