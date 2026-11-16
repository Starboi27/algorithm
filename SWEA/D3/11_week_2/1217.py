def recursive(val, cnt):
    if m == cnt:
        return val

    current = val * n

    return recursive(current, cnt + 1)


t = int(input())

for tc in range(1, t + 1):
    # n를 m번 곱함
    n, m = map(int, input().split())

    result = recursive(n, 1)

    print(f"#{tc} {result}")
