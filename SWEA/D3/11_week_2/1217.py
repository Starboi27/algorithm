def recursive(result, time):
    if time == M:
        return result

    return recursive(result * N, time + 1)


t = 10

for tc in range(1, t + 1):
    n = int(input())
    N, M = map(int, input().split())

    result = recursive(N, 1)

    print(f"#{tc} {result}")

# N을 M번 곱함,
