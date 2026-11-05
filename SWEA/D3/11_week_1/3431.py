import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D3\input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    L, U, X = map(int, input().split())
    solve = 0
    if X < L:
        solve = L - X
    elif X > L and X > U:
        solve = -1
    print(f"#{tc} {solve}")
