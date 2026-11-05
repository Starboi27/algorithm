import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D3\input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    solve = 0
    if n >= 3:  # 3명도 포함해야지
        solve = n // 3
    print(f"#{tc} {solve}")
