import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D2\input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    count = 1
    set_ = set()

    while 1:
        result = n * count

        for number in str(result):
            set_.add(number)

        if len(set_) == 10:
            break

        count += 1

    print(f"#{tc} {result}")

# 집합 쓰면 풀 수 있쓴
