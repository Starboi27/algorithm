import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D2\input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    numbers = [2, 3, 5, 7, 11]
    result = []

    while numbers:
        count = 0
        number = numbers.pop(0)

        while n % number == 0:
            n //= number
            count += 1
        result.append(count)

    print(f"#{tc}", *result)
