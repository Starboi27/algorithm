t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    juice = f"1/{str(n)}"
    result = []

    for i in range(n):
        result.append(juice)

    print(f"#{tc}", *result)

# 문제 해석 복습