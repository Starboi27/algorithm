n = int(input())

for i in range(1, n + 1):
    a, b, n = map(int, input().split())
    count = 0

    while a <= n and b <= n:
        if a < b:
            a = a + b
        else:
            b = b + a
        count += 1
    print(count)

# 걍 존나 이해가 안 됨
# 왜 a랑 b를 왜 따로 비교해서
# whlie 조건을 줘야 하는지 이해가 안되버림
