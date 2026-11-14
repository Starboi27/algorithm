t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    result = 0

    if n >= 3:
        result = n // 3

    print(f"#{tc} {result}")
