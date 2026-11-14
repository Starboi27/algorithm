t = int(input())

for tc in range(1, t + 1):
    n = int(input())

    solve = 0

    for i in range(1, n + 1):
        if i % 2 == 0:  # 짝수
            solve -= i
        else:
            solve += i

    print(f"#{tc} {solve}")
