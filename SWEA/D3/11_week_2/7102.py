t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())

    card_a = [i for i in range(1, n + 1)]
    card_b = [i for i in range(1, m + 1)]

    cnt = 0
    total = [0] * (n + m + 1)

    for i in range(n):
        for j in range(m):
            cal = card_a[i] + card_b[j]
            total[cal] += 1

    max_ = max(total)
    result = []

    for i in range(len(total)):
        if total[i] == max_:
            result.append(i)

    print(f"#{tc}", *result)

# 복습
