t = int(input())

for tc in range(1, t + 1):

    n = int(input())

    odd, even = 0, 0

    for number in range(1, n + 1):
        if number % 2 == 0:
            even -= number
        else:
            odd += number

        result = odd + even

    print(f"#{tc} {result}")

# 복습
