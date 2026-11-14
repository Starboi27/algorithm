import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D2\input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    count = 1
    set_ = set()

    while 1:
        value = str(n * count)

        for i in value:
            set_.add(int(i))

        if len(set_) == 10:
            break

        count += 1

    print(set_, n * count)

# 11.09 다시 복습
