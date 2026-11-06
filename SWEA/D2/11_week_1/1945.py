import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D2\input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    queue = [2, 3, 5, 7, 11]
    result = []
    n = int(input())

    while queue:
        count = 0
        num = queue.pop(0)

        while n % num == 0:
            n = n // num
            count += 1
        result.append(count)

    print(f"#{tc}", *result)

# 소인수분해: 자연수를 소수들의 곱으로 나타내는 것
