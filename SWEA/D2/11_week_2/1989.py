import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D2\input.txt", "r")


def is_palindrom():
    return n == n[::-1]


t = int(input())

for tc in range(1, t + 1):
    n = input()
    result = 0

    if is_palindrom():
        result = 1

    print(f"#{tc} {result}")
