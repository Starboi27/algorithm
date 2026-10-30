import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D2\9_week_3\sample_input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    n = float(input())
    solve = ""

    while n != 0:
        n *= 2
        if n >= 1:
            solve += "1"
            n -= 1
        else:
            solve += "0"

    if len(solve) > 12:
        solve = "overflow"
    # solve의 길이가 12를 넘어가면 overflow
    # while에 넣고 overflow를 쓴 다음 brack를 해주면 됨

    print(f"#{tc} {solve}")
