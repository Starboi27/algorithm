t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    solve = n * m

    if (n >= 10) or (m >= 10):
        solve = -1

    print(f"#{tc} {solve}")
