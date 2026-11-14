import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D3\input.txt", "r")


def is_palindrome(i):
    char = str(i)
    if char == char[::-1]:
        return True


t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    cnt = 0
    for i in range(n, m + 1):
        if is_palindrome(i):
            root = int(i**0.5)
            if root * root == i and is_palindrome(root):
                cnt += 1

    print(f"#{tc} {cnt}")

# 복습 피료
