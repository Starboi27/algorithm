t = int(input())

for tc in range(1, t + 1):
    binary_data = list(map(int, input().strip()))
    result = 0
    current = 0

    while binary_data:
        data = binary_data.pop(0)
        if data != current:
            result += 1
            current = data

    print(f"#{tc} {result}")

# tl발 이해가 안 됨
